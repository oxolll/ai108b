import gd as gd

def f(p):
    [x,y] =p
    return x*x + y*y

p = [1.0, 3.0]
print('grad(f,p)=',gd.grad(f,p))
#gd.gradientDescendent(f,p)