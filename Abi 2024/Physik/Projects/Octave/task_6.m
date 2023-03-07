# values
h=1.5;
v=5;
g=-9.81;
dt=0.01;

T=[];
S=[];
V=[];

# iteration
n=1;
for t=0:dt:3
  T(n)=t;     # type: time
  V(n)=v;  # type: speed
  S(n)=h;  # type: location

  dv=g*dt;
  v+=dv;
  ds=v*dt;
  h+=ds;

  n++;
endfor

subplot(2,1,1)
title("Weg-Zeit-Diagramm")
plot(T, S, '-b')

subplot(2,1,2)
title("Geschwindigkeit-Zeit-Diagramm")
plot(T, V, '-g')
