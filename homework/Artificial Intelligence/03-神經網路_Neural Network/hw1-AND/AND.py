import numpy as np
import gd as gd
#from numpy.linalg import norm

def sig(t):
    return 1.0/(1.0+np.exp(-t))

o = [0.0,0,0,1]

def f(p):
    [w1,w2,b] = p
    o0 = sig(b)
    o1 = sig(w2+b)
    o2 = sig(w1+b)
    o3 = sig(w1+w2+b)
    res = np.array([[o0-o[0]],[o1-o[1]],[o2-o[2]],[o3-o[3]]])
    print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    return np.linalg.norm(res,2)

p = [0.0, 0.0, 0.0]
gd.gradientDescendent(f, p, max_loops=3000)