import math

import sympy as sp


def trapezoidal_integration(function, start_point, end_point, n=0):
    if (n <= 0):
        n = 100
    h = abs(end_point - start_point) / n
    I = h * (0.5 * (function(start_point) + function(end_point)) + sum(
        map(lambda x: function(x), [start_point + h * i for i in range(1, n)])))
    return I


def find_required_partitions(second_derivative,required_epsilon,start_point,end_point) :
    maximum_derivative = max(map(lambda x: second_derivative(x), [start_point + 0.1 * i for i in range(0, int((end_point-start_point)/0.1))]))
    n = math.sqrt(abs((end_point-start_point)**3 * maximum_derivative / (12*required_epsilon)))
    return math.ceil(n)


def find_error_precision(second_derivative,n,start_point,end_point):
    maximum_derivative = max(map(lambda x: second_derivative(x), [start_point + 0.1 * i for i in range(0, int((end_point - start_point) / 0.1))]))
    return abs((end_point-start_point)**3*maximum_derivative/(12*(n**2)))

