import numpy as np
import matplotlib.pyplot as plt


rp = 10
rs = 10*rp
a = rs

size_of_final_matrix = 2*a+4*rp+1
finsiz = size_of_final_matrix
star = np.zeros((finsiz,finsiz), dtype=np.float64)

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
for i in range(-a,a+1):
    for j in range(-a,a+1):
        #print(i, j)
        if (i**2 + j**2)>a**2:
            star[[i+a+2*rp],[j+a+2*rp]] = 0
        else:
            I = 1-0.6096*(1-np.sqrt((a**2 - (i**2 + j**2))/a**2))
            star[[i+a+2*rp],[j+a+2*rp]] = I

# you can comment this out to not plot if you'd like
#plotarray(star)

planet = np.ones_like(star, dtype=np.bool)
planet[:, :] = True

pos_ind = []
for k in range(2*a+3*rp+1):
    for i in range(-rp,rp+1):
        for j in range(-rp,rp+1):
                if (i**2 + j**2)>rp**2:
                    planet[[i+a+2*rp],[j+k]] = True
                else:
                    planet[[i+a+2*rp],[j+k]] = False
                planet[[a+2*rp],[0,k-rp-1]]=True

    planet_ma = np.ma.masked_array(np.zeros(star.shape), mask=planet)
    pos_ind.append(star[planet].sum())

plt.imshow(star)
plt.imshow(planet, alpha = .5)
plt.show()


plt.plot(pos_ind)
plt.show()

'''
plt.imshow(star)
plt.imshow(planet_ma)
plt.show()
'''
