from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.25)
y = np.arange(-3, 3, 0.25)

X, Y = np.meshgrid(x, y)
Z = np.cos(X) + np.sin(Y)

fig = plt.figure()
ax = Axes3D(fig)
plt.xlabel("x")
plt.ylabel("y")
ax.plot_wireframe(X, Y, Z)

plt.show()
