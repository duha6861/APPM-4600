import numpy as np

def driver():
    a = -1
    b = 1
    tol = 10**-3
    its_max = 100

    v = [0]
    n = 5
    for i in range(2,n+1):
        [p, roots, info, it] = Interlacing_Newton(i, a, b, v, tol, its_max)
        v = roots
    print(roots)

def Newton(n,p0,tol,Nmax):
    """
    Newton iteration.
    Inputs:
    n - The order of the polynomial we are finding roots for
    p0 - Initial guess for root
    tol - Iteration stops when p_n,p_{n+1} are within tol
    Nmax - Max number of iterations

    Outputs:
    p - An array of the iterates
    pstar - The last iterate
    info - Success message
    - 0 if we met tol
    - 1 if we hit Nmax iterations (fail)
    """
    [P, P_prime] = FindPoly(n,p0)
    p = np.zeros(Nmax+1)
    p[0] = p0
    for it in range(Nmax):
        p1 = p0-P/P_prime
        p[it+1] = p1
        if (abs(p1-p0) < tol):
            pstar = p1
            info = 0
            return [p,pstar,info,it]
        p0 = p1
        [P, P_prime] = FindPoly(n,p0)
    pstar = p1
    info = 1
    return [p,pstar,info,it]

def Interlacing_Newton(n,a,b,v,tol,Nmax):
    '''
    Intended to be used with a Newton function to more quickly find roots

    Inputs:
    n - The order of the above polynomial
    a - The first endpoint of the larger interval containing all roots
    b - The second endpoint of the larger interval containing all roots
    v - A vector containing the roots of the last polynomial (of power n-1)
    tol - The tolerance to be used by the newton funciton
    Nmax - The maximum number of iterations to be used by the newton function

    Outputs:
    r - a vector of the roots for our current polynomial (of power n)
    info - a vector containing the info output from the Newton function for each root
    it - a vecgtor containing the iteration output from the Newton function for each root
    '''
    p = np.zeros([Nmax+1,n])
    r = np.zeros(n)
    info = np.zeros(n)
    it = np.zeros(n)

    x0 = (a + v[0])/2
    [p[:,0], r[0], info, it] = Newton(n, x0, tol, Nmax)

    for i in range(1,n-1):
        x0 = (v[i-1] + v[i])/2
        [p[:,i], r[i], info, it] = Newton(n, x0, tol, Nmax)
    
    x0 = (v[n-2] + b)/2
    [p[:,n-1], r[n-1], info, it] = Newton(n, x0, tol, Nmax)

    return[p, r, info, it]

def FindPoly(n,x):
    '''
    This function will use our three term recurrence to find the nth order polynomial
    and its derivative (using chainrule) evaluated at some value x

    Inputs:
    n - The order of the polynomial we want to find
    x - where this polynomial will be evaluated

    Outputs:
    p2 - The nth order polynomial evaluated at x
    p2_prime - The derivative fo the nth order polynomial evaluated at x
    '''
    p0 = 1
    p0_prime = 0
    p1 = x
    p1_prime = 1

    for i in range(1,n):
        p2 = 2*x*p1 - p0
        p2_prime = 2*p1 + 2*x*p1_prime - p0_prime
        p0 = p1
        p0_prime = p1_prime
        p1 = p2
        p1_prime = p2_prime

    return(p2, p2_prime)

driver()