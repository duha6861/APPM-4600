import numpy as np
from numpy.linalg import inv

def VAndermonde(x,y,N):

    V = np.zeros( (N, N) )
    i = 0
    j = 0

    for i in N:
        for j in N:
            V[i][j] = x[i]**j
    
    Vinv = inv(V)

    a = np.dot(Vinv, y)

    return(a)


