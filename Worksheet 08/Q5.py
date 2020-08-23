import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 * np.exp(-x**2)

f = np.vectorize(f)
xs, h = np.linspace(-1, 1, 1000, retstep=True)
ys = f(xs)
d2ys = (f(xs[2:]) - 2*f(xs[1:-1]) + f(xs[:-2]))/h**2
plt.plot(xs, ys, label='f(x)')
plt.plot(xs[1:-1], d2ys, label='f"(x)')
plt.legend(loc='upper right')
plt.show()
