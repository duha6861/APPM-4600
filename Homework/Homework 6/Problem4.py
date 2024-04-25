import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def driver():
    f = lambda x,t: x**(t-1)*np.exp(-x)
    a = 0
    b = 100
    N = 1000
    t = [2, 4, 6, 8, 10]

    for i in range(len(t)):
        area = comp_Trap(a,b,N,f,t[i])
        print('The trapezoidal estimate for t =',t[i],' is: ', area)
        gamma = sp.special.gamma(t[i])
        error = np.abs(area - gamma)
        print('The error for t =',t[i],' is: ', error)
        g = lambda x: f(x,t[i])
        quad, err, info = sp.integrate.quad(g, a, b, full_output=1)
        print('The python quad function gives:', quad)
        error = np.abs(quad - gamma)
        print('The error for the python quad funciton for t =',t[i],' is: ',error)
        print('The number of functions for t =',t[i],' is: ', info['neval'])

def comp_Trap(a,b,N,f,t):
    h = (b-a)/N
    area = f(a,t)
    for i in range(1,N-1):
        area = area + 2*f(a + i*h, t)
    area = area + f(b,t)
    area = area*h/2
    return(area)

driver()