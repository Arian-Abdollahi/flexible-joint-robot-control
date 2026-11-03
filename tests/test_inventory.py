"""No-dependency repository tests. MATLAB/Simulink execution not included."""
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_project import check


class ProjectStructureTests(unittest.TestCase):
    def test_core_inventory_and_binary_integrity(self):
        result = check()
        self.assertEqual(result['simulink_models'], 3)
        self.assertEqual(result['report_pdfs'], 4)

    def test_controller_scripts(self):
        for relative in (
            'matlab/lead/Matrix_Lead.m',
            'matlab/lag/Matrix_Lag.m',
            'matlab/lead_lag/Matrix_Lead.m',
            'matlab/state_feedback/M8.m',
        ):
            self.assertTrue((ROOT / relative).is_file())

    def test_shared_symbolic_model(self):
        source = (ROOT / 'matlab/modeling/Equation_Solve.m').read_text()
        self.assertIn('syms th th_dot', source)
        self.assertIn('Kstiff', source)

    def test_state_feedback_poles_present(self):
        source = (ROOT / 'matlab/state_feedback/M8.m').read_text()
        for pole in ('-4.968', '5.211', '-50', '-51'):
            self.assertIn(pole, source)

    def test_no_ball_beam(self):
        for path in ROOT.rglob('*'):
            self.assertNotIn('ballandbeam', path.name.lower())

    def test_latex_sources(self):
        dirs = list((ROOT / 'reports/latex').glob('report_*'))
        self.assertEqual(len(dirs), 4)
        for folder in dirs:
            self.assertTrue((folder / 'document.tex').is_file())

if __name__ == '__main__':
    unittest.main()
