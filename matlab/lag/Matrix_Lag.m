clc;
close all
clear all

%% Define State-Space Matrix From Variables derived from equations.


A = [0 1 0 0; 0 -34.69 594.52 0; 0, 0 , 0, 1 ; 0, 34.69 , -1251.63 , 0];
B = [0 ; 61.065 ; 0 ; -61.065];
C = [1 0 0 0];
D = 0;
[num,den]= ss2tf(A,B,C,D);
sys=tf(num,den);
sys
% margin(sys)

%% Finiding Gain and Z&P of Lead Controller

% K1 = 5.682;
% C_Lead = tf([0.1175 1],[0.075 1]);
% Sys_Lead = K1*C_Lead*sys;
% margin (Sys_Lead);
% Sys_Lead;
%% Finiding Gain and Z&P of Lag Controller

K2 = 2.841;
C_Lag = tf([1 0.483],[1 0.0483]);
Sys_Lag = K2*C_Lag*sys;
margin (Sys_Lag);

