import numpy as np
import matplotlib.pyplot as plt

h = 1.0
step = np.array([])
err = np.array([])
for i in range(15):
    err = np.append(err, np.abs((np.exp(h) - np.exp(-h))/(2*h) - 1))
    step = np.append(step, h)
    h/=10

plt.plot(step, err)
plt.xlabel('step size')
plt.ylabel('error')
plt.xscale('log')
plt.yscale('log')
plt.show()
