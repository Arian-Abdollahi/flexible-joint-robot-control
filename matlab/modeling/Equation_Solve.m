clc;
clear all
close all
%% Define Variables & Symbols

syms th th_dot th_ddot a a_dot a_ddot V 
% Rm kt km kg nm ng Beq g Jeq r L m Jarm Kstiff;  
% We can solve it parametrically by define all variables by syms 

Rm = 2.6;
kt = 0.00767;
km = 0.00767;
kg = 70;
nm = 0.69;
ng = 0.9;
Beq = 0.004;
Jeq = 0.0021;
Kstiff=1.2485;
Jarm=0.0019;

%% Define Equations and Solve them

T = (nm*ng*kt*kg*V)/Rm - (nm*ng*kt*km*kg^2*th_dot)/Rm;

eqns = [Jeq*th_ddot + Jarm*(th_ddot + a_ddot)==T-Beq*th_dot;
        Jarm*(th_ddot + a_ddot) + Kstiff*a==0];

S = solve(eqns,[th_ddot a_ddot]);
vpa(S.th_ddot)
vpa(S.a_ddot)
