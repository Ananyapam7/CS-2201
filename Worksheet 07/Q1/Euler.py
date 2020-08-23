# This program uses the Euler algorithm
#   y_(n+1) = y_n + f(x_n,y_n)*h
# to solve the differential equation
#   dI/dt = (E-I*R)/L


f = open('Euler_h=0.001.out','w')

def update(t,I):
    p = dI(t,I)

    I += p*h
    t += h
    return t,I

def dI(t,I):
    return (2*I - t )/(I + 2*t)

ti = 0.0
tf = 20.0
h = 0.001

t = ti
I = 1.0

while t<tf:
    t,I = update(t,I)
    f.write('{0}\t{1}\n'.format(t,I))
