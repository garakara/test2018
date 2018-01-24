from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.25)
y = np.arange(-3, 3, 0.25)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)

fig = plt.figure()
ax = Axes3D(fig)


# wireframe
# ax.plot_wireframe(X, Y, Z)

# surface
# ax.plot_surface(X, Y, Z, rstride = 1, cstride =1)

# plot3D
# ax.plot3D(np.ravel(X), np.ravel(Y), np.ravel(Z))

# contour3D
# ax.contour3D(X, Y, Z)
# ax.contourf3D(X, Y, Z)

# contour3D
ax.scatter3D(np.ravel(X), np.ravel(Y), np.ravel(Z))

plt.show()
