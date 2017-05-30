from pyswarm import pso
import math

def lossFun(input):
    x = input[0]
    y = input[1]
    return math.sin(x)*math.sin(y)

lb = [-2, -2]
ub = [ 2,  2]

xopt, fopt = pso(lossFun, lb, ub,ieqcons=[], f_ieqcons=None, args=(), kwargs={},
    swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100, minstep=1e-9,
    minfunc=1e-9, debug=False)

print(xopt)
print(fopt)

