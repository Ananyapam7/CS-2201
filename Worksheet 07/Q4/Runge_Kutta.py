f = open('Runge_Kutta_h=0.05.out','w+')

def update(x,y):

    p = dy(x,y)
    q = dy(x + h/2, y + h*p/2)
    r = dy(x + h, y + h*(2*q - p))

    y += h*(p + 4*q + r)/6
    x += h

    return x,y

def dy(x,y):
    return x**3 + y/x

xi = 1
xf = 5
h = 0.05

x = xi
y = 1

while x<xf:

    x,y = update(x,y)
    f.write('{0}\t{1}\n'.format(x,y))
