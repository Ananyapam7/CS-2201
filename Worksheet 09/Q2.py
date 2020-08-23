import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

A=(1-np.exp(-4))*0.5
f=lambda x: x*np.exp(-x*x)
E=[]
H=[]
def fit(x,k,n):
	return k*(x**n) 

for N in range(10,110,10):
	x,h=np.linspace(0,2,2*N+1,retstep=True)
	y=f(x)
	I=(y[0]+y[-1]+4*sum(y[1:-1:2])+2*sum(y[2:-2:2]))*(h/3)
	E.append(np.abs(I-A))
	H.append(h)

fig=plt.figure()
fig.suptitle("Simpson's 1/3rd rule")
plt.plot(H,E,'o')
plt.xlabel('Stepsize(h)')
plt.ylabel('Error(E)')
plt.grid()

popt, pcov = curve_fit(fit, H, E)
print "Order of error is 0.0306*h^(4)"

xs=np.linspace(0,0.1,1000)
plt.plot(xs,fit(xs,popt[0],popt[1]),label="Fit fn = 0.0306*h^(4)")
plt.legend()
plt.show()
