import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 8:
    print("Usage: fx, fy, Ax, Ay, theta, delta t, N")
    quit()

[nam, fx, fy, ax, ay, th, dt, n] = sys.argv

x = []
y = []
z = []

for i in range(int(n)):
    t = i * float(dt)
    x.append(float(ax)*np.cos(2*np.pi*(float(fx)**t)))
    y.append(float(ay)*np.sin(2*np.pi*(float(fy)**t + float(th))))
    z.append(x[i] + y[i])

plt.plot(x,y)
plt.show()
