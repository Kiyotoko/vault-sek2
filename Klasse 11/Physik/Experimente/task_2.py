import matplotlib.pyplot as plt

w = [-0.01,-0.03,-0.11,-0.25,-0.30,-0.01,-0.52,-0.32,-0.03,0.2]
x = [t * 0.02 for t in range(9)]
f = lambda i: (w[i] + w[i+1])/2*0.02/-1200
a = [f(i) for i in range(9)]
t = [sum(a[:i]) for i in range(9)]

plt.plot(x, a)
plt.plot(x, t)
plt.legend(["Anstieg", "Total"])
plt.xlabel("Zeit [s]")
plt.ylabel("Phi [V]")
plt.show()
