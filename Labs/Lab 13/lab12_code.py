import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time as time


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 500
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)
     t_start = time.perf_counter()
     x = scila.solve(A,b)
     t_end = time.perf_counter()
     test = np.matmul(A,x)
     r = la.norm(test-b)

     t_start1 = time.perf_counter()
     [LU, piv] = scila.lu_factor(A)
     t_end1 = time.perf_counter()

     t_start2 = time.perf_counter()
     x = scila.lu_solve((LU, piv), b)
     t_end2 = time.perf_counter()

     t = t_end - t_start
     print('Method 1: ', t)
     t1 = t_end1 - t_start1
     print('LU Factorization: ', t1)
     t2 = t_end2 - t_start2
     print('LU solving: ', t2)

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)


     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
