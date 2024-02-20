  # import libraries
import numpy as np

def bisection_mod(f,fp,fpp,a,b,tol,Nmax):

    fa = f(a)
    fb = f(b)

    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)
      fcp = fp(c)
      fcpp = fpp(c)

      if (fc ==0):
        astar = c
        ier = 0
        return [astar, ier]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        astar = c
        ier = 3
        return [astar, ier]

      if (abs(fc*fcpp/fcp**2) < 1):
        astar = a
        ier =0
        return [astar, ier]
      
      count = count +1

    astar = a
    ier = 2
    return [astar,ier] 

def Newtons_mod(f,fp,fpp,x0,tol,Nmax):

  p = np.zeros(Nmax+1)
  p[0] = p0



  for it in range(Nmax):
      p1 = p0-f(p0)/fp(p0)
      p[it+1] = p1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it]
        
# use routine
f = lambda x: (x-2)**3
fp = lambda x: 3*(x-2)**2
fpp = lambda x: 6*(x-2)

p0 = 1.2
Nmax = 100
tol = 1.e-14

p,pstar,info,it = newton(f,fp,p0,tol, Nmax)
print('the approximate root is', '%16.16e' % pstar)
print('the error message reads:', '%d' % info)


