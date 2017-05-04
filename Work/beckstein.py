import numpy as np
import matplotlib.pyplot as plt

a=100
rp=20
center = a+2*rp


star = np.zeros((2*a+1+4*rp,2*a+1+4*rp), dtype=np.float64)

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

for i in range(-a,a+1):
    for j in range(-a,a+1):
        if (i**2 + j**2)>a**2:
            star[[i+center],[j+center]] = 0
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            star[[i+center],[j+center]] = I

plotarray(star)

def shift_planet(shape, rp, x, y=None):
    """Shift planet with radius rp to position x, y.

    Arguments
    ---------
    shape : (NX, NY)
         size of star array in pixels (array indices)
    rp : float
        radius (in pixels)
    x : float
        position in pixels
    y : float
        position in pixels, default is at half, NY/2
    """
    NX, NY = shape
    if y is None:
        y = NY/2
    x = round(x)
    y = round(y)

    planet = np.zeros(shape, dtype=np.bool)
    planet[:,:] = True
    for i in range(-rp,rp):
        for j in range(-rp,rp):
            ix = (i+rp + x+2)
            jy = (j + y)
            if 0 < ix < NX and 0 < jy < NY:
                planet[ix, jy] = (i**2 + j**2 > rp**2)
    return planet

planet_positions = []
for x in range(2*center):
    planet_positions.append(shift_planet(star.shape, rp, x))

center

plt.imshow(planet_positions[len(planet_positions)-1].T)
plt.show()
