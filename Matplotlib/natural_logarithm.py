# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

x = np.arange(0.001, 1.0, 0.001)
y = np.log(x)
plt.xlabel("x")
plt.ylabel("log(x)")
plt.xlim(0.0, 1.0)
plt.ylim(-5.0, 0.0)
plt.plot(x, y)
plt.show()
