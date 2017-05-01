import numpy as np
import matplotlib.pyplot as plt

a = 50
b = np.zeros((51,51), dtype=np.float64)
print(b, b.shape)
c = []

for i in range(51):
    for j in range(51):
        if (i**2 + j**2)>a**2:
            break
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            b[[i],[j]] = I
            #b.append(I)
print()
print(b)

c = b[::-1] + b[1::]

#print(c, len(c))

plt.plot(c)
plt.show()
