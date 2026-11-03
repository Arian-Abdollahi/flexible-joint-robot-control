# Project scope and source provenance

The user supplied **five** RAR archives. This repository intentionally takes **only flexible-joint robotic control** material from four of them:

| Source archive | Selected material | Included? |
| --- | --- | --- |
| `40023055 (1).rar` | Report 5 (lead compensation) | Yes |
| `Report 6 (1).rar` | Report 6 (lag compensation) | Yes |
| `Report 7 (1).rar` | Report 7 (combined lead–lag compensation) | Yes |
| `Report 8 (1).rar` | Report 8 (state-feedback pole placement) | Yes |
| `Report 4.rar` | Report 4 (ball-and-beam / PV control) | **No** |

Original file contents were copied without modification. The three byte-identical `Equation_Solve.m` files appearing in Reports 5–7 were represented by one unchanged shared copy. Source-relative paths and SHA-256 checksums are in [`SOURCE_MANIFEST.json`](SOURCE_MANIFEST.json).

LaTeX transient build files (`.aux`, `.log`, `.synctex.gz`) and redundant `Latex/document.pdf` copies were removed where the exact equivalent report was already retained. Report 7's only compiled PDF was stored as `reports/report_07_lead_lag.pdf`.

The original author credits are preserved in the PDFs and summarized in `CREDITS.md`. No external dataset, invented simulation results, third-party license assertion or unprovided hardware experiment was added.
