# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt

# sigma^2をsigmaとしている。
def quadratic_function(sigma, mu):
    return (1 / np.sqrt(2 * np.pi * sigma ) ) * np.exp(-(x - mu) ** 2 / (2 * sigma) )


x = np.arange(-8, 8, 0.01)
y = quadratic_function(0.2, 0)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-3, 3)
plt.ylim(0, 1)
plt.plot(x, y)
plt.show()
