import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

A=(1/2.0)-(np.sin(2.0))*0.25
f=lambda x: (np.sin(x))**2
E=[]
H=[]
def fit(x,k,n):
	return k*(x**n) 

for N in range(10,110,10):
	x,h=np.linspace(0,1,N+1,retstep=True)
	y=f(x)
	I=(0.5*(y[0]+y[-1])+sum(y[1:-1]))*h
	E.append(np.abs(I-A))
	H.append(h)

fig=plt.figure()
fig.suptitle("Trapezoidal rule")
plt.plot(H,E,'o')
plt.xlabel('Stepsize(h)')
plt.ylabel('Error(E)')
plt.grid()

popt, pcov = curve_fit(fit, H, E)
print "Order of error is 0.0756*h^(2)"

xs=np.linspace(0,0.1,1000)
plt.plot(xs,fit(xs,popt[0],popt[1]),label="Fit fn = 0.0756*h^(2)")
plt.legend()
plt.show()
