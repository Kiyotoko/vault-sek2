% Simsulation Skifahrer mit Reibung auf Piste
clear *

% Starwerte
n = 1;     %gibt Stelle im Zeilenvektor an
v = 0;     %Anfangsgeschwindigkeit in m/s
s = 0;     %Anfangshöhe in m
g = 9.81;  %Fallbeschleunigung g in m/s^2
dt = 0.01; %Schrittweite für die Zeit
a = 0;     %Anfangsbeschleunigung in m/s^2
c = 0.8;   %Strömungswiderstandszahl
r = 0.5;   %Querschnittsfläche in m^2
p = 1.35;  %Dichte des Mediums in kg/m^3
m = 75;    %Masse des Körpers in kg
mu = 0.1;  %Gleitreibungszahl
St = 0.5;  %Steigung in %
alpha = atan(St);      %Winkel in Bogenmaß

%Schleife

for t=0:dt:30  %von 0s bis 30s in dt-Schritten

  T(n) = t;     %Vektorbefüllung Zeitintervall
  A(n) = a;     %Vektorbefüllung Beschleunigun
  V(n) = v;     %Vektorbefüllung Geschwindigkeit
  S(n) = s;     %Vektorbefüllung Weg/Höhe

  a = g*sin(alpha)-((c*p*r*(v.^2))/(2*m))-mu*g*cos(alpha);  %Beschleunigunsänderung
  dv = a*dt;    %Geschwindigkeitsänderung
  v = dv + v;   %neue Geschwindigkeit

  ds = v * dt;  %Wegänderung
  s = s + ds;   %neuer Weg
  n++;          %Zeilenvektorstelle um 1 erhöhen

endfor

subplot(3,1,1)
plot(T,S, "-b")
title("Weg-Zeit-Diagramm")
xlabel("Zeit t in [s]")
ylabel("Weg s in [m]")
grid on
set(gca, "Fontsize", 12)


subplot(3,1,2)
plot(T,V, "-r")
title("Geschwindigkeit-Zeit-Diagramm")
xlabel("Zeit t in [s]")
ylabel("Geschwindigkeit s in [m/s]")
grid on
set(gca, "Fontsize", 12)

subplot(3,1,3)
plot(T,A, "-g")
title("Beschleuniguns-Zeit-Diagramm")
xlabel("Zeit t in [s]")
ylabel("Beschleunigung a in [m/s^2]")
grid on
set(gca, "Fontsize", 12)
