import matplotlib.pyplot as plt

t_vec = [] # Liste für die Zeit
x_vec = [] # Liste für den Ort
v_vec = [] # Liste für die Geschwindigkeit
a_vec = [] # Liste für die Beschleunigung

D = 5 # Federkonstante
r = 0.05 # Reibung
m = 0.15 # Masse

dt = 0.01 # Änderung der Zeit
t = 0 # Zeit
x = 0.05 # Ort
v = 0 # Geschwindigkeit
a = 0 # Beschleunigung

for _ in range(int(20 / dt)): # Von 0 bis 20 Sekunden in 0.01 Schritten iterieren

    F_D = -D * x # Federkraft
    F_R = r * v # Reibungskraft
    F_ges = F_D - F_R # Gesamtkraft

    a = F_ges / m # Beschleuningung neu berechnen

    dv = a * dt # Änderung der Geschwindigkeit
    v += dv # Änderung addieren

    dx = v * dt # Änderung des Ortes
    x += dx # Änderung addieren

    t += dt # Zeitänderung

    # Werte hinzugügen
    t_vec.append(t)
    x_vec.append(x)
    v_vec.append(v)
    a_vec.append(a)

# Graphen plotten
plt.subplot(3,1,1)
plt.plot(t_vec, x_vec, label="Auslenkung")
plt.title("x(t)")
plt.xlabel("t [s]")
plt.ylabel("s [m]")
plt.legend()

plt.subplot(3,1,2)
plt.plot(t_vec, v_vec, label="Geschwindigkeit")
plt.title("v(t)")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.legend()

plt.subplot(3,1,3)
plt.plot(t_vec, a_vec, label="Beschleunigung")
plt.title("a(t)")
plt.xlabel("t [s]")
plt.ylabel("a [m/s^2]")
plt.legend()

plt.show()