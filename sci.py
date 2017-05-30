import numpy as np
from scipy.optimize import minimize
import math

def lossFun(input):
    x = input[0]
    y = input[1]
    if x > 2 or x < -2 or y > 2 or y < -2:
    	return 1000
    return math.sin(x)*math.sin(y)

x0 = np.array([0,0])
res = minimize(lossFun, x0, method='Nelder-Mead',options={'xtol': 1e-8, 'disp': True})
print(res.x)
