import numpy as np
import math as math

def driver():
    a = -5
    b = 5
    f = lambda s: 1/(1 + s**2)
    f2 = lambda s: (-2*(-3*s**2 + 1))/((1+s**2)**3)
    f4 = lambda s: (24*(5*s**4 - 10*s**2 + 1)/((1+s**2)**5))
    N_trap = 1291
    N_simp = 108

    print('Actual area is: 2arctan(5) = ', 2*math.atan(5))

    trap_area = comp_Trap(a,b,N_trap,f)
    print('Area for composite trapezoidal is: ', trap_area)
    print('Error is: ', np.abs(2*math.atan(5) - trap_area))
    print('1: ', f2(-1),
          '2: ', f2(0), 
          '3: ', f2(1))

    simp_area = comp_Simp(a,b,N_simp,f)
    print("Area for composite Simpson's is:", simp_area)
    print('Error is: ', np.abs(2*math.atan(5) - simp_area))
    print('1: ', f4(-np.sqrt(3)), 
          '2: ', f4(-np.sqrt(1/3)), 
          '3: ', f4(0), 
          '4: ', f4(np.sqrt(1/3)),
          '5: ', f4(np.sqrt(3)))

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