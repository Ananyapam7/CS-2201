import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
values = np.empty(0)
step_size = np.empty(0)
for i in range (10,100,10):
    x,h = np.linspace(-1.0, 2.0, num=i, retstep=True)
    y = ((np.sin(x))**2)/(1+np.cos(x))
    result = simps(y,x)
    step_size = np.append(step_size, h)
    values = np.append(values, result)

exact = 2*np.arctan(np.sin(2)/(np.cos(2)+1))+2*np.arctan(np.sin(1)/(np.cos(1)+1))-np.sin(2)-np.sin(1)
error = values - exact
fig = plt.figure()
plt.plot(error,step_size)
fig.suptitle('Error variation with step size', fontsize=14)
plt.xlabel('Step Size', fontsize=14)
plt.ylabel('Error', fontsize=14)
plt.show()