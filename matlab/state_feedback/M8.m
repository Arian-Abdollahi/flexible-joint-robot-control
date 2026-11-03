clc
clear
%sys=tf([],[]);
A = [0 1 0 0; 0 -34.69 594.52 0; 0, 0 , 0, 1 ; 0, 34.69 , -1251.63 , 0];
B = [0 ; 61.065 ; 0 ; -61.065];
C = [1 0 0 0];
D = 0;
%poles(sys)
p=[-4.968+1i*5.211 ,-4.968-1i*5.211 , -50 , -51];
k=place(A,B,p);
An=A-B*k;
[a,b]=ss2tf(An,B,C,D);
sys_new=tf(a,b);

eig(A);
eig(An);
k;
step(sys_new,1)
stepinfo(ss(An,B,C,D))
