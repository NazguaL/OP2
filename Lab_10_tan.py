import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2 * np.pi, 2 * np.pi, 10000)
plt.plot(x, (np.tan(x)))
plt.xlabel('X(n)')
plt.ylabel('Y(m)')
plt.ylim(-5, 5)
plt.show()

