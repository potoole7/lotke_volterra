import numpy as np
import matplotlib.pyplot as plt

import fwd_euler
import evolve
import evolve_vec

# solve dz/dt = -z using forward euler method
z = evolve.evolve(phi=fwd_euler.fwd_euler, 
                  f=lambda t, z: -z,
                  Df=lambda t, z: np.array([-1]), 
                  t=0,
                  z0=1,
                  T=1,
                  N=50
                  )

# plot numerical solution of dz/dz=-z against actual e^(-z)
t_span=np.linspace(0,1,51)
plt.plot(t_span,z)
plt.plot(t_span, np.exp(-t_span), "--o")
plt.show()

# lotka-volterra parameters
a=1.1
b=0.5
d=0.4
g=0.3

lotka=evolve_vec.evolve_vec(phi=fwd_euler.fwd_euler,
                    f=lambda t,X: np.array([t, a*X[0]-b*X[0]*X[1],d*X[0]*X[1]-g*X[1]]),
                    Df=lambda t,x,y: np.array([0,0]),
                    t=0,
                    z0=np.array([10,10], ndmin=2),
                    T=50,
                    N=100
                    )

