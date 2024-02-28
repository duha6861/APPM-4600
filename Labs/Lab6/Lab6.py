# get libraries
import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 


# define routines
def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 4*x[0]**2 + x[1]**2 - 4
    F[1] = x[0] + x[1] - np.sin(x[0] - x[1])
    return F
    
def evalJ(x): 

    J = np.array([[8*x[0], 2*x[1]],
                 [(1 - np.cos(x[0] - x[1])), (1 + np.cos(x[0] - x[1]))]])
    return J


def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]
           
def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)

       if (norm(evalF(x1)) > norm(evalF(x0))):
          J = evalJ(x1)
          Jinv = inv(J)
          x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   

def ForDiff(f, s, h):
    f_prime = (f(s + h) - f(s))/h
    return (f_prime)

def CenDiff(f, s, h):
    f_prime = (f(s + h) - f(s - h))/(2*h)
    return (f_prime)

def NewtonApprox(x0,h,tol,Nmax):
  
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       F = evalF(x0)
       F1 = evalF(x0 + np.array([h, 0]))
       F2 = evalF(x0 + np.array([0, h]))

       J = np.array([[(F1[0]-F[0])/h, (F2[0]-F[0])/h],
                     [(F1[1]-F[1])/h, (F2[1]-F[1])/h]])
       Jinv = inv(J)

       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]

# use routines
x0 = np.array([0, 1])

Nmax = 1000
tol = 1e-10

#t = time.time()
#for j in range(20):
  #[xstar,ier,its] =  Newton(x0,tol,Nmax)
#elapsed = time.time()-t
#print(xstar)
#print('Newton: the error message reads:',ier)
#print('Newton: took this many seconds:',elapsed/20)
#print('Netwon: number of iterations is:',its)
 
t = time.time()
for j in range(20):
  [xstar,ier,its] =  LazyNewton(x0,tol,Nmax)
elapsed = time.time()-t
print(xstar)
print('Lazy Newton: the error message reads:',ier)
print('Lazy Newton: took this many seconds:',elapsed/20)
print('Lazy Newton: number of iterations is:',its)

h = 1e-7
t = time.time()
for j in range(20):
  [xstar,ier,its] =  NewtonApprox(x0,h,tol,Nmax)
elapsed = time.time()-t
print(xstar)
print('Approximate Newton 1: the error message reads:',ier)
print('Approximate Newton 1: took this many seconds:',elapsed/20)
print('Approximate Newton 1: number of iterations is:',its)

h = 1e-3
t = time.time()
for j in range(20):
  [xstar,ier,its] =  NewtonApprox(x0,h,tol,Nmax)
elapsed = time.time()-t
print(xstar)
print('Approximate Newton 2: the error message reads:',ier)
print('Approximate Newton 2: took this many seconds:',elapsed/20)
print('Approximate Newton 2: number of iterations is:',its)

'''t = time.time()
for j in range(20):
  [xstar,ier,its] = Broyden(x0, tol,Nmax)     
elapsed = time.time()-t
print(xstar)
print('Broyden: the error message reads:',ier)
print('Broyden: took this many seconds:',elapsed/20)
print('Broyden: number of iterations is:',its)'''
     
