# import libraries
import numpy as np
def driver():
    # test functions
    f1 = lambda x: (10 / (x+4))**0.5
    # fixed point is alpha1 = 1.4987....


    Nmax = 100
    tol = 1e-10
# test f1 '''
    x0 = 1.5
    [xstar,ier,vector_p] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    print('Vector P is', vector_p)

    [new_vector_p] = Aitkens(vector_p)
    print('The new vector P from Aitkens is', new_vector_p)

    [new_xstar, new_ier, new_new_vector_p] = Steffensons(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',new_xstar)
    print('f1(xstar):',f1(new_xstar))
    print('Error message reads:',new_ier)
    print('The new vector P from Steffensons is', new_new_vector_p)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    vector_p = []

    while (count <Nmax):
        
        x1 = f(x0)
        vector_p.append(x1)
        count = count +1

        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar, ier, vector_p]
        x0 = x1


    xstar = x1
    ier = 1
    return [xstar, ier, vector_p]


def Aitkens(v):

    i = 1
    p = []

    while i < (len(v) - 2):
        p.append(v[i] + (v[i+1]-v[i])**2 / (v[i+2]-2*v[i+1]+v[i]))
        i = i + 1
    
    return[p]

def Steffensons(f, x0, tol, Nmax):
    
    count = 0
    v = []

    while (count < Nmax):

        a = x0
        b = f(x0)
        c = f(b)

        x1 = a - ((b - a)**2 / (c - 2*b + a))
        v.append(x1)
        count = count + 1

        if (abs(x1 - x0) < tol):
            xstar = x1
            ier  = 0
            return[xstar, ier, v]
        x0 = x1

    xstar = x1
    ierr = 1
    return[xstar, ier, v]



driver()