# Flexible-joint dynamics and assumptions

The supplied reports describe a geared DC motor driving a flexible robotic joint, with motor-side coordinate `theta` and a relative flexible angle `alpha`. They use the state vector:

`x = [theta, theta_dot, alpha, alpha_dot]^T`.

The original symbolic modeling script is [`../matlab/modeling/Equation_Solve.m`](../matlab/modeling/Equation_Solve.m). It expresses the two second-order dynamics and solves for `theta_ddot` and `alpha_ddot`:

```
Jeq * theta_ddot + Jarm * (theta_ddot + alpha_ddot) = T - Beq * theta_dot
Jarm * (theta_ddot + alpha_ddot) + Kstiff * alpha = 0

T = (nm * ng * kt * kg / Rm) * V
    - (nm * ng * kt * km * kg^2 / Rm) * theta_dot
```

## Parameters assigned in the original symbolic script

| Source variable | Value | Meaning in the source |
| --- | ---: | --- |
| `Rm` | 2.6 | Motor electrical resistance |
| `kt`, `km` | 0.00767 each | Motor constants |
| `kg` | 70 | Gear ratio |
| `nm` | 0.69 | Motor efficiency |
| `ng` | 0.9 | Gear efficiency |
| `Beq` | 0.004 | Equivalent viscous damping |
| `Jeq` | 0.0021 | Equivalent inertia |
| `Kstiff` | 1.2485 | Joint torsional stiffness |
| `Jarm` | 0.0019 | Arm inertia |

These numerical values are transcribed directly from the supplied MATLAB script. The source itself does not clearly document units for every parameter; do not infer missing units without checking equipment documentation.

The numerical controller scripts use:

```matlab
A = [0 1 0 0;
     0 -34.69 594.52 0;
     0 0 0 1;
     0 34.69 -1251.63 0];
B = [0; 61.065; 0; -61.065];
C = [1 0 0 0];
D = 0;
```

The original model is preserved for reproducibility. No independent derivation, dimensional analysis, hardware identification, or measurement validation has been performed here.
