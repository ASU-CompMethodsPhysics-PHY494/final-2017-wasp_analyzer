import numpy as np
import matplotlib.pyplot as plt

rp = 40

a = 100
star = np.zeros((2*a+1+4*rp,2*a+1+4*rp), dtype=np.float64)

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

# giving (x,y) points their respective brightness on the surface of the star
for i in range(-a,a):
    for j in range(-a,a):
        #print(i, j)
        if (i**2 + j**2)>a**2:
            star[[i+a],[j+a]] = 0
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            star[[i+a+rp,[j+a+rp]] = I

# you can comment this out to not plot if you'd like
plotarray(star)

planet = np.ones_like(star, dtype=np.bool)
planet[:, :] = True

pos_ind = []
for k in range(2*a+1+4*rp):
    for i in range(-rp,rp):
        for j in range(-rp,rp):
                if (i**2 + j**2)>rp**2:
                    planet[[i+rp],[j+rp+k]] = True
                else:
                    planet[[i+rp],[j+rp+k]] = False
    planet_ma = np.ma.masked_array(np.ones(planet.shape), mask=planet)
    pos_ind.append(star[planet_ma].sum())

plt.imshow(star)
plt.imshow(planet.T)
plt.show()
