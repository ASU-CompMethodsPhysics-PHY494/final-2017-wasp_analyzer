import numpy as np
import matplotlib.pyplot as plt

a = 200
rp = 40
b = np.zeros((2*a+1,2*a+1+rp), dtype=np.float64)

#making a new code that may or may not be used

# checking to see that it's the proper array that we want
# print(b, b.shape)

# giving (x,y) points their respective brightness on the surface of the star
for i in range(-a,a):
    for j in range(-a,a):
        #print(i, j)
        if (i**2 + j**2)>a**2:
            b[[i+a],[j+a]] = 0
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            b[[i+a],[j+a]] = I

print()
#print(b)

#c = b[::-1] + b[1::]
# the core plotting code was found/taken from stack overflow
def plotarray(x):
    fig = plt.figure(figsize=(6, 3.2))

    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(x)
    ax.set_aspect('equal')

    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    plt.show()

# you can comment this out to not plot if you'd like
plotarray(b)

# this is supposed to be 8-trivial so if you run and get a number you
# definitely did not expect, it COULD be right
for i in range(10):
    print(np.sum(b)+i)
'''
for i in range(-a,a):
    for j in range(-a,a):
        if np.sqrt((i-i)**2 + j**2)
            b[[i+a],[j+a]] = 0
        else:
            b[[i+a],[j+a]] = I
'''
