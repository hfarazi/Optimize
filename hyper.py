import math
import pickle
import time
from hyperopt import fmin, tpe, hp, STATUS_OK

def lossFun(input):
    x = input[0]
    y = input[1]
    return {'loss': (math.sin(x)*math.sin(y)), 'status': STATUS_OK }


best = fmin(lossFun,
    space=[hp.uniform('x', -2, 2),hp.uniform('y', -2, 2)],
    algo=tpe.suggest,
    max_evals=100)

print best
test=[best['x'],best['y']]
print lossFun(test)['loss']
