# Controller experiments

This document summarizes **what is present in the supplied reports and scripts**. Report conclusions are not new simulation results.

## 05 · Lead compensation

- Original MATLAB: [`../matlab/lead/Matrix_Lead.m`](../matlab/lead/Matrix_Lead.m)
- Original Simulink: [`../matlab/lead/Lead.slx`](../matlab/lead/Lead.slx)
- Saved report: [`../reports/report_05_lead.pdf`](../reports/report_05_lead.pdf)
- Script uses `K1 = 5.682`, `C_Lead = tf([0.1175 1], [0.075 1])`, and `margin(Sys_Lead)`.
- The report discusses increased phase margin and improved transient performance. The report quotes slightly different rounded zero/pole values than those implied by the script coefficients; both are retained unchanged.

## 06 · Lag compensation

- MATLAB: [`../matlab/lag/Matrix_Lag.m`](../matlab/lag/Matrix_Lag.m)
- Simulink: [`../matlab/lag/Lag.slx`](../matlab/lag/Lag.slx)
- Saved MATLAB outputs: `flexible_lag.mat`, `flexible with lag.fig`
- Script uses `K2 = 2.841`, `C_Lag = tf([1 0.483], [1 0.0483])`.
- The report describes a slower response and reduced overshoot in its saved result.

## 07 · Combined lead–lag compensation

- MATLAB: [`../matlab/lead_lag/Matrix_Lead.m`](../matlab/lead_lag/Matrix_Lead.m); despite its original filename, this script implements both lead and lag.
- Saved MATLAB outputs: `data.mat`, `margin.fig`, `step response.fig`, `flexible joint response.fig`
- Report: [`../reports/report_07_lead_lag.pdf`](../reports/report_07_lead_lag.pdf)
- The script uses gain `28.408`, `Lead = tf([1 4.08],[1 6.12])` and `Lag = tf([1 0.5],[1 0.05])`, followed by a closed-loop step plot.
- No corresponding `.slx` model was included in the supplied Report 7 archive.

## 08 · State-feedback pole placement

- MATLAB: [`../matlab/state_feedback/M8.m`](../matlab/state_feedback/M8.m)
- Simulink: [`../matlab/state_feedback/simulin8.slx`](../matlab/state_feedback/simulin8.slx)
- Report: [`../reports/report_08_state_feedback.pdf`](../reports/report_08_state_feedback.pdf)
- Desired poles in the script: `-4.968 ± 5.211i`, `-50`, `-51`.
- The report targets less than 5% overshoot and a rise time below 250 ms. It reports achieving the overshoot target but a rise time slightly above the target. That is a **reported outcome**, not freshly verified.

The scripts retain their original variable names, MATLAB API usage, and calculation choices. Controller designs have not been tuned or altered as part of this repository organization.
