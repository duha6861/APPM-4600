# import libraries
import numpy as np


# define routines
def bisection(f,a,b,tol,Nmax):
    '''
    Inputs:
      f,a,b       - function and endpoints of initial interval
      tol, Nmax   - bisection stops when interval length < tol
                  - or if Nmax iterations have occured
    Returns:
      astar - approximation of root
      ier   - error message
            - ier = 1 => cannot tell if there is a root in the interval
            - ier = 0 == success
            - ier = 2 => ran out of iterations
            - ier = 3 => other error ==== You can explain
    '''

    '''     first verify there is a root we can find in the interval '''
    fa = f(a); fb = f(b);

    count = 0

    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier, count]

    ''' verify end point is not a root '''
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier, count]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier, count]

    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)

      if (fc ==0):
        astar = c
        ier = 0
        return [astar, ier, count]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier, count]

      if (abs(b-a)<tol):
        astar = a
        ier =0
        return [astar, ier, count]
      
      count = count + 1

    astar = a
    ier = 2
    return [astar,ier, count] 

# use routines    
f1 = lambda x: (x - 5)**9
f2 = lambda x: x**9 -45*x**8 + 900*x**7 - 10500*x**6 + 78750*x**5 - 393750*x**4 + 1312500*x**3 - 2812500*x**2 + 3515625*x -1953125
a = 4.82
b = 5.2

Nmax = 1000
tol = 1e-4

[astar1,ier1,count1] = bisection(f1,a,b,tol,Nmax)
print('The approximate root for (x-5)^9 is',astar1)
print('The error message for (x-5)^9 reads:',ier1)
print('The number of iterations for (x-5)^9 is', count1)

[astar2,ier2,count2] = bisection(f2,a,b,tol,Nmax)
print('The approximate root for the expanded version is',astar2)
print('The error message for the expanded version reads:',ier2)
print('The number of iterations for the expanded version is', count2)