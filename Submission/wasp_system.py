import numpy as np
import pylab

R_center = 0.0
R_star = 1.0
circles = 11.  
lines   = 21.
origin = (0, 0)
Area_pl = (np.pi)*(0.1)**2

def Limb_darkening(R_pl = 0.1, R_star = 1., r = np.linspace(0.0, 1.0, 10.)):
    """This function calculates the specific intensity "I" with respect to the 
    radial distance from the center of the WASP55"""
    I = 1 - 0.6096(1 - ((R_star**2 - r**2)/R_star**2)**0.5)
    return I

def flux_deficit(R_pl = 0.1, R_star = 1.):
    x = np.arange(0.,1.,0.1)
    mu = (1. - x)**0.5
    flux_deficit = ((mu + (2/3))*R_pl**2)/((4/3)*R**2)
    return flux_deficit

"""Transit time
p = 385827.84 # orbital period in seconds
b = 0.15 # impact parameter
a = 7829770 # semi-major axis in Au is 0.0533, value used given in km
R = np.arange(0., 1.,0.1)
R_pl = 0.1
T_duration = (p/(np.pi))*np.arcsin((((R + R_pl)**2 - (b*R)**2)**0.5)/a)"""


for r in np.linspace(R_center, R_star, circles):
    pylab.gca().add_patch(pylab.Circle(origin, radius=r, fill=False, color='black'))
    
r_ab = np.array([R_center, R_star])
for theta in np.linspace(0, 2 * np.pi, lines):
    pylab.plot(np.cos(theta) * r_ab, np.sin(theta) * r_ab, color='red')

pylab.axis('scaled')
pylab.show()
