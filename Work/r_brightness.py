import numpy as np
import matplotlib.pyplot as plt

a = 50

b = []

for r in range(51):
    I = 1-0.6096*(1-np.sqrt((a**2 - r**2)/a**2)
    b.append(I)

print(b)

'''
N = 50
x_start, x_end = -2.0, 2.0
y_start, y_end = -1.0, 1.0

x = np.linspace(x_start, x_end, N)
y = np.linspace(y_start, y_end, N)

x0, y0, radius = 0.0, 0.0, 0.5

x, y = np.meshgrid(x, y)
r = np.sqrt((x - x0)**2 + (y - y0)**2)

outside = r < radius

fig, ax = plt.subplots()
ax.set(xlabel='X', ylabel='Y', aspect=1.0)

ax.scatter(x[outside], y[outside])

plt.show()
'''
