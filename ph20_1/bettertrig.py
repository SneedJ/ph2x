import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 8:
    print("Usage: fx, fy, Ax, Ay, theta, delta t, N")
    quit()

[nam, fx, fy, ax, ay, th, dt, n] = sys.argv

t = np.fromfunction(lambda i: i*float(dt),(1,n))
x = np.fromfunction(lambda i: float(ax)*np.cos(2*np.pi*(float(fx)**t[i])),(1,n))
y = np.fromfunction(lambda i: float(ay)*np.sin(2*np.pi*(float(fy)**t[i])),(1,n))
z = np.fromfunction(lambda i: x[i]+y[i],(1,n))

#x = []
#y = []
#z = []

#for i in range(int(n)):
#    t = i * float(dt)
#    x.append(float(ax)*np.cos(2*np.pi*(float(fx)**t)))
#    y.append(float(ay)*np.sin(2*np.pi*(float(fy)**t + float(th))))
#    z.append(x[i] + y[i])

plt.plot(x,y)
plt.show()
