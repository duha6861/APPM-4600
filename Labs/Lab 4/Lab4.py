# import libraries
import numpy as np
def driver():
    # test functions
    f1 = lambda x: 1+0.5*np.sin(x)
    # fixed point is alpha1 = 1.4987....


    Nmax = 100
    tol = 1e-6
# test f1 '''
    x0 = 0.0
    [xstar,ier,vector_p] = fixedpt(f1,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f1(xstar):',f1(xstar))
    print('Error message reads:',ier)
    print('Vector p is', vector_p)

    [a] = ConvOrder(vector_p, 5, 1.5)

    if (a == 1):
        print('linear')
    elif(a == 2):
        print('quad')
    else:
        print('error')




# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    vector_p = np.zeros((Nmax, 1))

    while (count <Nmax):
        
        x1 = f(x0)
        vector_p[count] = x1
        count = count +1

        if (abs(x1-x0) <tol):
            xstar = x1
            ier = 0
            return [xstar, ier, vector_p]
        x0 = x1

    

    xstar = x1
    ier = 1
    return [xstar, ier, vector_p]

def ConvOrder(p, n, conv):

    AEC1 = (p[n + 1] - conv)/(p[n] - conv)

    if (AEC1 < 1):
        a = 1

        return[a]
    
    if (AEC1 > 1):
        AEC2 = (p[n + 1] - conv)/((p[n] - conv)**2)
        if (AEC2 > 0):
            a = 2

            return[a]
        
    a = 0
    return[a]



driver()