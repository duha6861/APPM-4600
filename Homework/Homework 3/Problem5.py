import numpy as np
import matplotlib.pyplot as plt

# Part (a)
x = np.linspace(-1,5,1000)
y = x - 4*np.sin(2*x) - 3

plt.figure(1)
plt.plot(x,y)
plt.axhline(y=0, color="black")
plt.axvline(x=0, color="black")
plt.show()

# Part (b)
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier]
    

# use routines 
f1 = lambda x: -np.sin(2*x) + 5/4*x - 3/4

Nmax = 100
tol = 1e-11

''' test f1 '''
x0_1 = -1.0
[xstar1,ier1] = fixedpt(f1,x0_1,tol,Nmax)
print('the approximate fixed point is:',xstar1)
print('f1(xstar1):',f1(xstar1))
print('Error message reads:',ier1)

x0_2 = -0.5
[xstar2,ier2] = fixedpt(f1,x0_2,tol,Nmax)
print('the approximate fixed point is:',xstar2)
print('f1(xstar2):',f1(xstar2))
print('Error message reads:',ier2)

x0_3 = 2.0
[xstar3,ier3] = fixedpt(f1,x0_3,tol,Nmax)
print('the approximate fixed point is:',xstar3)
print('f1(xstar3):',f1(xstar3))
print('Error message reads:',ier3)

x0_4 = 3
[xstar4,ier4] = fixedpt(f1,x0_4,tol,Nmax)
print('the approximate fixed point is:',xstar4)
print('f1(xstar4):',f1(xstar4))
print('Error message reads:',ier4)

x0_5 = 4.5
[xstar5,ier5] = fixedpt(f1,x0_5,tol,Nmax)
print('the approximate fixed point is:',xstar5)
print('f1(xstar5):',f1(xstar5))
print('Error message reads:',ier5)