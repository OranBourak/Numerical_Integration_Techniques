import math
from functools import reduce
import sympy as sp

x = sp.symbols('x')
my_f = math.sin
f = sp.lambdify(x, my_f)





def trapezoidal_integration(function,n, start_point, end_point):
    h = abs(end_point-start_point)/n
    I = h *(0.5*(function(start_point)+function(end_point)) +reduce(lambda x, y:function(x)+function(y), [start_point+h*i for i in range(1, n)]))
    return I


print(trapezoidal_integration(f,4,0,math.pi))