import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-2 * np.pi, 2 * np.pi,0.001)   # start,stop,step
y = np.sin(x)
plt.xlabel('X(n)')
plt.ylabel('Y(m)')
plt.plot(x,y)
plt.show()