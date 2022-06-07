import math
import sympy as sp
from trapezoidal_integration import *
from sympy.utilities.lambdify import lambdify

# x = sp.symbols('x')
# # f = math.sin
# f = 2*x
# f = lambdify(x, f)
# f_2 =x**3
# f_2_tag = sp.diff(sp.diff(f_2,x),x)
# f_2_tag = lambdify(x,f_2_tag)

if __name__ == "__main__":
    print(trapezoidal_integration(f, 4, 0, 2))
    print(find_required_partitions(f_2_tag,0.000002,0,math.pi))
    print(find_error_presicion(f_2_tag,1137,0,math.pi))
