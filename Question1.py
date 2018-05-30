import numpy as np
from scipy.optimize import minimize

# The objective function 
def func(x, sign=-1.0):
	""" Objective function """
	return sign*(np.sin(x))

# The derivitive function 
def func_deriv(x, sign=-1.0):
	""" Derivative of objective function """
	return sign*(np.cos(x))

x0 = 5.0 # Initial guess
# unconstrained optimization results: 
res = minimize(func, x0, jac=func_deriv, method='BFGS', options={'disp': True})
print(res.x)
