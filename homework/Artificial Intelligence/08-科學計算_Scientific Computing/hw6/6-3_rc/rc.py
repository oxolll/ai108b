from sympy import *
from sympy.abc import t, R, C
V = Function("V")
ans = dsolve(C*Derivative(V(t))+V(t)/R ,V(t))
print("dsolve(C*Derivative(V(t))+V(t)/R ,V(t))=", ans.doit())