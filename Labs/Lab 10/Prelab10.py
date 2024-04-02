import numpy as np

def eval_legendre(n,x):
    p = np.zeros([1,n+1])

    phi0 = 1
    phi1 = x

    p[0] = phi0
    p[1] = phi1

    for i in range(2,n):
        p[i] = 1/(n+1) * ((2*n+1)*x*p[i-1] + n*p[i-2])

    return(p)

