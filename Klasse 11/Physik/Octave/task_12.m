U0 = 10; % Quellspannung
R = 47; % Widerstand
I0 = U0 / R; % maximale Stromstärke
L = 100; % Induktivität
dt = 0.001; % deltaT
n = 1; % Index

X0 = [];
Y0 = [];
I = 0;

for t=0:dt:20
  X0(n) = t;
  Y0(n) = I;
  dI = dt * (U0 - R * I) / L;
  I += dI;
  n += 1;
endfor

n = 1;
X1 = [];
Y1 = [];

for t=0:dt:20
  X1(n) = t;
  Y1(n) = I;
  dI = -dt * (R * I) / L;
  I += dI;
  n += 1;
endfor

n = 1;
X2 = [];
Y2 = [];
I = 0;

for t=0:1:20
  X2(n) = t;
  Y2(n) = I;
  I = I0 * (1- e^(-R/L*t));
  n += 1;
endfor

n = 1;
X3 = [];
Y3 = [];

for t=0:1:20
  X3(n) = t;
  Y3(n) = I;
  I = I0 * e^(-R/L*t);
  n += 1;
endfor

grid on
set(gca, "Fontsize", 18)

subplot(1, 2, 1)
plot(X0, Y0, "-b")
% legend(legend("Simulation"), "location", "southeast")
hold on
plot(X2, Y2, "^g")
title("Einschaltvorgang")
% legend(legend("Formel"), "location", "southeast")
xlabel("Zeit t [s]")
ylabel("Stromstärke I [A]")

subplot(1, 2, 2)
plot(X1, Y1, "-b")
% legend(legend("Simulation"), "location", "southeast")
hold on
plot(X3, Y3, "^g")
% legend(legend("Formel"), "location", "southeast")
title("Ausschaltvorgang")
xlabel("Zeit t [s]")
ylabel("Stromstärke I [A]")

