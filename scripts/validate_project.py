"""Validate static flexible-joint project assets without running MATLAB.

Run from any directory: python scripts/validate_project.py
"""
from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile, BadZipFile
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'matlab/modeling/Equation_Solve.m',
    'matlab/lead/Matrix_Lead.m',
    'matlab/lead/Lead.slx',
    'matlab/lag/Matrix_Lag.m',
    'matlab/lag/Lag.slx',
    'matlab/lead_lag/Matrix_Lead.m',
    'matlab/state_feedback/M8.m',
    'matlab/state_feedback/simulin8.slx',
    'reports/report_05_lead.pdf',
    'reports/report_06_lag.pdf',
    'reports/report_07_lead_lag.pdf',
    'reports/report_08_state_feedback.pdf',
]


def check() -> dict:
    missing = [x for x in REQUIRED if not (ROOT / x).is_file()]
    if missing:
        raise ValueError(f'Missing required project assets: {missing}')
    models = sorted(ROOT.rglob('*.slx'))
    if len(models) != 3:
        raise ValueError(f'Expected exactly 3 Simulink models; found {len(models)}')
    for model in models:
        try:
            with ZipFile(model) as archive:
                error = archive.testzip()
                if error:
                    raise ValueError(f'Invalid model member: {error}')
                if 'simulink/blockdiagram.xml' not in archive.namelist():
                    raise ValueError('No Simulink blockdiagram.xml')
        except BadZipFile as exc:
            raise ValueError(f'Corrupt Simulink model {model}') from exc
    pdfs = sorted(ROOT.glob('reports/report_*.pdf'))
    if len(pdfs) != 4:
        raise ValueError(f'Expected 4 report PDFs, found {len(pdfs)}')
    for pdf in pdfs:
        if pdf.read_bytes()[:5] != b'%PDF-':
            raise ValueError(f'Invalid PDF header: {pdf}')
    for folder in sorted((ROOT / 'reports/latex').glob('report_*')):
        if not (folder / 'document.tex').is_file():
            raise ValueError(f'Missing LaTeX source: {folder}')
    for bad in ('BallandBeam.slx', 'report_04_ball_beam.pdf'):
        if any(x.name == bad for x in ROOT.rglob('*')):
            raise ValueError(f'Out-of-scope ball-and-beam asset found: {bad}')
    manifest = ROOT / 'docs/SOURCE_MANIFEST.json'
    data = json.loads(manifest.read_text(encoding='utf-8'))
    if not data.get('original_files'):
        raise ValueError('Source manifest is missing original file records')
    for item in data['original_files']:
        if not (ROOT / item['path']).is_file():
            raise ValueError(f'Manifest file not found: {item["path"]}')
    return {'simulink_models': len(models), 'report_pdfs': len(pdfs), 'source_records': len(data['original_files'])}


def main() -> None:
    try:
        result = check()
    except Exception as exc:
        print(f'FAILED: {exc}', file=sys.stderr)
        raise SystemExit(1) from exc
    print('Flexible-joint project static verification passed:', result)


if __name__ == '__main__':
    main()
