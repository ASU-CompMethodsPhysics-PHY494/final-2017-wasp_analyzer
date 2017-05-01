import numpy as np
import matplotlib.pyplot as plt

a = 50
b = np.zeros((51,51), dtype=np.float64)
print(b, b.shape)


for i in range(51):
    for j in range(51):
        if (i**2 + j**2)>a**2:
            b[[i],[j]] = 0
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            b[[i],[j]] = I
            #b.append(I)
print()
print(b)

#c = b[::-1] + b[1::]

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(b)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()
