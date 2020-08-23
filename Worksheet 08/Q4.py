import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 * np.exp(-x**2)

f = np.vectorize(f)
xs, h = np.linspace(-1, 1, 1000, retstep=True)
ys = f(xs)
dys = (8 * (f(xs[4:]) - f(xs[2:-2])) - (f(xs[4:]) - f(xs[:-4])))/(12*h)
plt.plot(xs, ys, label='f(x)')
plt.plot(xs[2:-2], dys, label='f\'(x)')
plt.legend(loc='upper right')
plt.show()
