import numpy as np
import matplotlib.pyplot as plt

xs, h = np.linspace(-1,1,1000, retstep=True)
ys = xs**2 * np.exp(-xs**2)
plt.plot(xs, ys, label='f(x)')
dydx = (ys[1:] - ys[:-1])/h
plt.plot(xs[:-1], dydx, label='f\'(x)')
plt.legend(loc='upper right')
plt.show()
