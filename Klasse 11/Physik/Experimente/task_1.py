import matplotlib.pyplot as plt
import numpy

x1 = numpy.array([0,1,2,3,4,5,6])
y1 = numpy.array([0.88,0.67,0.61,0.54,0.5,0.48,0.45])

plt.plot(x1, y1)
m, b = numpy.polyfit(x1, y1, 1)
print(m, b)
plt.plot(x1, m*x1+b)

x2 =  numpy.array([0,1,2,3,4,5,6])
y2 =  numpy.array([0.87,0.83,0.81,0.78,0.76,0.71, 0.70])

plt.plot(x2, y2)
m, b = numpy.polyfit(x2, y2, 1)
print(m, b)
plt.plot(x2, m*x2+b)

plt.legend(["Werte Pappe", "Regression", "Werte Papier", "Regression"])
plt.xlabel("Schichtdichte [N]")
plt.ylabel("Spannung [V]")
plt.show()
