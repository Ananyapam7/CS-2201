import numpy as np
from scipy.integrate import quad
result1 = quad(lambda x: ((np.sin(x))**2)/(1+(x)**2), 0, np.pi)
print result1
result2 = quad(lambda x: x**4*(np.exp(-x)), 0, 1)
print result2
result3 = quad(lambda x: ((x**4)/(1+x**3)), 0, 1)
print result3
result4 = quad(lambda x: np.exp(-(x**2)), -np.inf, np.inf)
print result4