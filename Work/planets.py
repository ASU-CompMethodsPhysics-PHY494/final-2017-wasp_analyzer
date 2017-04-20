import numpy as np
import vpython as vp

M_earth = 3.003467e-6
M_sun = 1.0

G_grav = 4*np.pi**2

def F_gravity(r, m=M_earth, M=M_sun):
    rr = np.sum(r*r)
    rhat = r/np.sqrt(rr)
    return -G_grav*m*M/rr * rhat

def vp_planet_orbit(r0=np.array([1.017, 0, 0]), v0=np.array([0, 6.179, 0]), mass=M_earth, dt=0.001):
    """Visualize 2D planetary motion with velocity verlet"""
    dim = len(r0)
    assert len(v0) == dim

    r = np.array(r0, copy=True)
    v = np.array(v0, copy=True)


    scene = vp.display(title="Earth around Sun", background=vp.color.black,
                      forward=vp.vec(0, 2, -1))
    planet = vp.sphere(pos=vp.vec(*r), radius=0.1, make_trail=True,
                      texture=vp.textures.earth,
                      up=vp.vec(0, 0, 1))
    sun = vp.sphere(pos=vp.vec(0, 0, 0), radius=0.2, color=vp.color.yellow,
                    emissive=True)
    sunlight = vp.local_light(pos=vp.vec(0, 0, 0), color=vp.color.yellow)

    # start force evaluation for first step
    Ft = F_gravity(r, m=mass)
    while True:
        vhalf = v + 0.5*dt * Ft/mass
        r += dt * vhalf
        Ftdt = F_gravity(r, m=mass)
        v = vhalf + 0.5*dt * Ftdt/mass
        # new force becomes old force
        Ft = Ftdt

        vp.rate(200)
        planet.pos = vp.vec(*r)


vp_planet_orbit()
