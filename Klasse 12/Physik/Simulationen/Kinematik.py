from matplotlib import pyplot as plt

t_array = []
s_array = []
v_array = []
a_array = []

t = 0
s = 0
v = 0
a = 0
m = 0.1
D = 5

dt = 0.01

F_R = 0.02

for _ in range(int(10 / dt)):
    F_Sp = D * (0.04 - s)
    if s < 0: F_Sp = 0
    F_ges = F_Sp - F_R

    a = F_ges / m

    v += a * dt
    if v < 0: break
    s += v * dt
    t += dt

    t_array.append(t)
    s_array.append(s)
    v_array.append(v)
    a_array.append(a)

plt.subplot(3, 1, 1)
plt.plot(t_array, s_array, label="Ort")
plt.title("s(t)")
plt.xlabel("t [s]")
plt.ylabel("s [m]")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t_array, v_array, label="Geschwindigkeit")
plt.title("v(t)")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_array, a_array, label="Beschleunigung")
plt.title("a(t)")
plt.xlabel("t [s]")
plt.ylabel("a [m/s^2]")
plt.legend()

plt.show()
