import matplotlib.pyplot as plot
import math

t_values = []
s_values = []
v_values = []
a_values = []

m = 80
g = 9.81
c = 0.3
psi = 1.3
A = 1.2
alpha = 0.1

s = 0
v = 0
a = 0

t = 0
dt = 0.1

for step in range(1000):
    t += dt

    F_H = m * g * math.sin(alpha)
    F_W = 1/2 * c * psi * v**2 * A

    F_gesamt = F_H - F_W

    a = F_gesamt / m

    dv = a * dt
    v += dv

    ds = v * dt
    s += ds

    t_values.append(t)
    s_values.append(s)
    v_values.append(v)
    a_values.append(a)

plot.subplot(3, 1, 1)
plot.plot(t_values, s_values)
plot.title("s(t) - Diagramm")
plot.xlabel("t [s]")
plot.ylabel("s [m]")
plot.subplot(3, 1, 2)
plot.plot(t_values, v_values)
plot.title("v(t) - Diagramm")
plot.xlabel("t [s]")
plot.ylabel("v [m/s]")
plot.subplot(3, 1, 3)
plot.plot(t_values, a_values)
plot.title("a(t) - Diagramm")
plot.xlabel("t [s]")
plot.ylabel("a [m/s^2]")
plot.show()