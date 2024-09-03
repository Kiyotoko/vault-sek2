from matplotlib import pyplot as plt

U_array = []
I_array = []
t_array = []

U_0 = 15
R = 7
L = 1.5

t = 0
U = 0
I = 0

dt = 0.01

for _ in range(int(1 / dt)):
    U = R * I

    dI = dt * (U_0 - U) / L
    I += dI

    t += dt

    t_array.append(t)
    I_array.append(I)
    U_array.append(U)

plt.subplot(2, 1, 1)
plt.plot(t_array, I_array, label="Stromstärke")
plt.title("I(t)")
plt.xlabel("t [s]")
plt.ylabel("I [A]")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_array, U_array, label="Spannung")
plt.title("U(t)")
plt.xlabel("t [s]")
plt.ylabel("U [V]")
plt.legend()

plt.show()