import numpy as np
import matplotlib.pyplot as plt

a = 50
b = []

for r in range(51):
   I = 1-0.6096*(1-np.sqrt((a**2 - r**2)/a**2))
   b.append(I)

print(b)

plt.plot()
