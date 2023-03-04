# values
h=0;
v=0;
g=9.81;
c=0.45;
A=1;
r=1.25;
m=1
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

  a=g-((c*A*r*v.^2)/(2*m));
  dv=a*dt;
  v+=dv;
  ds=v*dt;
  h+=ds;

  n++;
endfor

subplot(1,2,1)
plot(T, S, '-b')
title("Weg-Zeit-Diagramm")
xlabel("Zeit")
ylabel("Weg")
axis([0 3 0 20])

subplot(1,2,2)
plot(T, V, '-g')
title("Geschwindigkeit-Zeit-Diagramm")
xlabel("Zeit")
ylabel("Geschwindigkeit")
axis([0 3 0 7])
