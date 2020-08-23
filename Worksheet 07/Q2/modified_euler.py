f = open('modified_euler_h=0.001.out','w+')

def update(t,I):
    p = dy(t,I)
    q = dy(t + h, I + h*p)

    I += (p+q)*h/2
    t += h
    return t,I

def dy(t,I):
    return (2*I - t )/(I + 2*t)

ti = 0
tf = 20
h = 0.001

t = ti
I = 1

while t<tf:
    t,I = update(t,I)
    f.write('{0}\t{1}\n'.format(t,I))
