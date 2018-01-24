# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

def quadratic_function(x):
    return 0.01 * x ** 2 + 0.1 * x

x = np.arange(0.0, 20, 0.1)
y = quadratic_function(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()
