# Execution and verification boundaries

## What is included

- Four original reports (lead, lag, lead–lag, state feedback), each with a PDF and LaTeX source/figures.
- Five distinct MATLAB `.m` scripts, three Simulink `.slx` models and multiple saved MATLAB `.mat` / `.fig` files.
- MATLAB source file names preserved within their experiment-specific directories, including the two different `Matrix_Lead.m` files used for different tasks.

## What was checked

- All three Simulink `.slx` files have valid ZIP container structure and include Simulink model XML.
- All four PDF reports open successfully.
- Local no-dependency Python tests check expected file inventory and separation from the ball-and-beam experiment.

## What was NOT checked

- MATLAB or Simulink compilation, model execution, closed-loop stability, controller specifications or matching figures with regenerated plots.
- Physical robot hardware behavior, motor parameters or calibration.
- MATLAB version, Simulink model block compatibility or extra installed toolboxes beyond those evident from scripts.

## Running the scripts

MATLAB with Control System Toolbox and Simulink is needed for most experiments. `Equation_Solve.m` also requires Symbolic Math Toolbox. Open MATLAB at the repository root and run the scripts separately to avoid state from previous experiments.

Some saved result files depend on original MATLAB data and simulation configurations; they are preserved as archived artifacts rather than promised to reproduce on all installations.

The original source and reports list multiple collaborators. The reports may contain personal email addresses. Review the source files before making a public repository.
