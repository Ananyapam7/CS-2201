import numpy as np
#a=float(raw_input("Enter lower limit of integration :"))
#b=float(raw_input("Enter upper limit of integration :"))

gauss=np.loadtxt('GK7_15.txt',max_rows=7)
kronrod=np.loadtxt('GK7_15.txt',skiprows=8)
xg=gauss[:,0]
xk=kronrod[:,0]
wg=gauss[:,1]
wk=kronrod[:,1]

def I(x,w,a,b,f):
	Z=(((b-a)*0.5*x)+(b+a)*0.5)
	return (np.dot(f(Z),w))*(b-a)*0.5
def Error(a,b,f):
	return np.abs(I(xg,wg,a,b,f)-I(xk,wk,a,b,f))
	
f=lambda x: np.exp(-x*x)

print "value of the integral for e^(-x^2) is :",I(xg,wg,0,1,f)
print "Error =",Error(0,1,f) 
#put a,b in the place of 0,1 in the above lines for integration over any interval

 
