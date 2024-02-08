import numpy as np
import math as math

def problem3(x):
    y = math.e**x
    return y -1

x1 = 10.6
y_star1 = problem3(x1)
print('y1 - 1 is', y_star1)

delta_x = 0.1

x2 = x1 + delta_x
y_star2 = problem3(x2)
print('y2 - 1 is', y_star2)

delta_y = y_star2 - y_star1

rel_error_x = delta_x/x1
rel_error_y = delta_y/y_star1

cond_num = rel_error_y/rel_error_x

print('The condition value is', cond_num)

x0 = 9.999999995000000 * 10**-10
y_star0 = problem3(x0)
print('The value of y-1 is', y_star0)

def e_taylor_series(x,N):
    y = 0
    i = 1
    for i in range(N):
        y = y + x**i/math.factorial(i)
    return y-1

n = 100
poly_estimate = e_taylor_series(x0, n)

print('Using a polynomial approximation of power', n, ',the estimated value is', poly_estimate)

rel_error = (poly_estimate - 10**-9)/10**-9

print('The relative error is', rel_error)