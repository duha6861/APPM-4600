import numpy as np
import math as math

def driver():
    a = -5
    b = 5
    f = lambda s: 1/(1 + s**2)
    N_trap = 1000
    N_simp = 1000

    print('Actual area is: 2arctan(5) = ', 2*math.atan(5))

    trap_area = comp_Trap(a,b,N_trap,f)
    print('Area for composite trapezoidal is: ', trap_area)
    print('Error is: ', np.abs(2*math.atan(5) - trap_area))

    simp_area = comp_Simp(a,b,N_simp,f)
    print("Area for composite Simpson's is:", simp_area)
    print('Error is: ', np.abs(2*math.atan(5) - simp_area))

def comp_Trap(a,b,N,f):
    h = (b-a)/N
    area = f(a)
    for i in range(1,N-1):
        area = area + 2*f(a + i*h)
    area = area + f(b)
    area = area*h/2
    return(area)


def comp_Simp(a,b,N,f):
    h = (b-a)/N
    area = f(a)
    for i in range(1,N-1):
        if i%2 == 0:
            area = area + 2*f(a + i*h)
        else:
            area = area + 4*f(a + i*h)
    area = area + f(b)
    area = area*h/3
    return(area)

driver()