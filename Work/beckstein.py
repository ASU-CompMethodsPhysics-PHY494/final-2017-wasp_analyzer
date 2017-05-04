
# coding: utf-8

# In[24]:

import numpy as np
import matplotlib.pyplot as plt


# In[25]:

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


# In[63]:

rp = 10
rs = 10*rp
a = rs
center = a+2*rp


star = np.zeros((2*a+1+4*rp,2*a+1+4*rp), dtype=np.float64)

for i in range(-a,a+1):
    for j in range(-a,a+1):
        if (i**2 + j**2)>a**2:
            star[[i+center],[j+center]] = 0
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            star[[i+center],[j+center]] = I

plotarray(star)


# In[61]:

planet = np.ones_like(star, dtype=np.bool)

# In[122]:

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
            ix = (i + x)
            jy = (j + y)
            if 0 < ix < NX and 0 < jy < NY:
                planet[ix, jy] = (i**2 + j**2 > rp**2)
    return planet



# In[123]:

planet_positions = []
for x in range(2*center):
    planet_positions.append(shift_planet(star.shape, rp, x))


# In[125]:

plt.imshow(planet_positions[len(planet_positions)-1].T)
plt.show()


# In[126]:

plt.imshow(star)
planet_ma = np.ma.masked_array(np.ones(planet.shape), mask=planet_positions[center].T)
plt.imshow(planet_ma)
plt.show()


# In[127]:

sums = []
for i in range(len(planet_positions)):
    sums.append(star[planet_positions[i]].sum())


# In[128]:

plt.plot(sums)
plt.show()
