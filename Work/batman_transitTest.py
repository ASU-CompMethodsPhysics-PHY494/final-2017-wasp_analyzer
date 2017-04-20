import batman
import numpy as np
import matplotlib.pyplot as plt


params = batman.TransitParams()
params.t0 = 0.
params.per = 1.
params.rp =0.1
params.a = 15.
params.inc = 87.
params.ecc = 0
params.w  = 90.
params.u = [0.1,0.3]
params.limb_dark = "quadratic"

t = np.linspace(-0.05, 0.05, 100)

m = batman.TransitModel(params, t)
flux = m.light_curve(params)

plt.plot(t, flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.show()
