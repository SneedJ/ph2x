import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 8:
    print("Usage: fx, fy, Ax, Ay, theta, delta t, N")
    quit()

[nam, fx, fy, ax, ay, th, dt, n] = sys.argv

t=x=y=z = np.zeros((1,int(n)))

for i in range(int(n)):
    t[i] = i*float(dt)
    x[i] = float(ax)*np.cos(2*np.pi*(float(fx)**t[i]))
    y[i] = float(ay)*np.sin(2*np.pi*(float(fy)**t[i]))
    z[i] = x[i]+y[i]

plt.plot(x,y)
plt.show()
