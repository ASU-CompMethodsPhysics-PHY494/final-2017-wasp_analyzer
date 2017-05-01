import numpy as np
import matplotlib.pyplot as plt

a = 50
b = [[],[]]
c = []

for i in range(51):
    for j in range(51):
        if (i**2 + j**2)>a**2:
            I = 0
            b.append(I)
            break
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            b.append(I)
#print(b)

c = b[::-1] + b[1::]

print(c)
#print(b)
#plt.plot(c)
#plt.show()
