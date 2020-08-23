import numpy as np
#a1=float(raw_input("Enter lower limit of integration :"))
#a2=float(raw_input("Enter upper limit of integration :"))

guass=np.loadtxt('gauss32.dat')
W=guass[:,1]
X=guass[:,2]

def I(a,b,f):
	Z=(((b-a)*0.5*X)+(b+a)*0.5)
	return np.dot(f(Z),W)*(b-a)*0.5

f=lambda x: (np.sin(x))**2
g=lambda x: x*np.exp(-x*x)
F=0.5-(np.sin(2.0))*0.25
G=(1-np.exp(-4))*0.5

print "Integral of (sinx)^2 from 0 to 1 is :", I(0,1,f)		#Can substitute a1,a2 in the place of 0,1
print "Error =",np.abs(I(0,1,f)-F) 
print "Integral of xe^(-x^2) from 0 to 2 is :",I(0,2,g)
print "Error =",np.abs(I(0,2,g)-G)
 
