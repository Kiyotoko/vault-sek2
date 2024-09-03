# Entladung Kondensator

# Startwerte
R = 100;        # Widerstand in Ohm
C = 4700*10^-6; # Kapazität des Kondensators in Farad
U0 = 5;         # anfägnliche Spannung in Volt
I0 = U0/R;      # anfängliche Stromstärke in Ampere
dt = 0.001;     # Zeitintervalle in Sekunden
n = 1;          # Stelle im jeweiligen Zeilenvektor

# Simulation von Spannung und Stromstärke

u = U0;   # Startwert für Spannung festlegen
i = I0;  # Startwert für Stromstärke festlegen

for k=0:dt:5        # Zeitintervall in Schrittweite dt

  du = -u/(R*C)*dt; # Berechnung der Spannungsänderung
  u = u + du;       # Berechnung der neuen Spannung

  di = du/R;    # Ber~~~echnung der Stromstärkeänderung
  i = i + di;

  I(n) = -i;         # Zeilenvektor für Stromstärke
  U(n) = u;         # Zeilenvektor für Spannung
  t(n) = k;         # Zeilenvektor für Zeit

  n++;

endfor

# Spannungsberechnung über Formel

Ug = U0*e.^(-t/(R*C));

# Stromstärkeberechnung über Formel

Ig = -I0*e.^(-t/(R*C));

# graphische Darstellung
# Entladungskurve Spannung

subplot(2,1,1)
plot(t,U, "-b")
title("Spannungs-Zeit-Diagramm")
xlabel("Zeit t [s]")
ylabel("Spannung U [V]")
grid on
set(gca, "Fontsize", 12)

# Entladungskurve Stromstärke

subplot(2,1,2)
plot(t,I, "-b")
title("Stromstärke-Zeit-Diagramm")
xlabel("Zeit t [s]")
ylabel("Stromstärke I [A]")
grid on
set(gca, "Fontsize", 12)


