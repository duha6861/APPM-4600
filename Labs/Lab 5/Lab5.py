  # import libraries
import numpy as np

def Newtons_mod(f,fp,fpp,a,b,tol,Nmax):
    fa = f(a)
    fb = f(b)

    if (fa*fb>0):
       ier = 1
       pstar = a
       return [pstar, ier]

    if (fa == 0):
      pstar = a
      ier =0
      return [pstar, ier]

    if (fb ==0):
      pstar = b
      ier = 0
      return [pstar, ier]

    count = 0
    while (count < Nmax):
      c = 0.5*(a+b)
      fc = f(c)
      fcp = fp(c)
      fcpp = fpp(c)

      if (fc ==0):
        pstar = c
        ier = 0
        return [pstar, ier]

      if (fa*fc<0):
         b = c
      elif (fb*fc<0):
        a = c
        fa = fc
      else:
        pstar = c
        ier = 3
        return [pstar, ier]

      if (abs(fc*fcpp/fcp**2) < 1):
        p0 = a

        for it in range(Nmax):
            p1 = p0-f(p0)/fp(p0)

            if (abs(p1-p0) < tol):
                pstar = p1
                ier = 0
                return [pstar,ier]
            
            p0 = p1
            pstar = p1
            ier = 1
            return [pstar,ier]
        
      
      count = count +1

    pstar = a
    ier = 2
    return [pstar,ier] 

        
# use routine
f = lambda x: np.e**(x**2 + 7*x - 30)
fp = lambda x: (2*x - 7)*np.e**(x**2 + 7*x - 30)
fpp = lambda x: 2*np.e**(x**2 + 7*x - 30) + ((2*x - 7)**2 * np.e**(x**2 + 7*x - 30))

a = 2
b = 4
Nmax = 100
tol = 1.e-14

[pstar,info] = Newtons_mod(f,fp,fpp,a,b,tol, Nmax)
print('the approximate root is', '%16.16e' % pstar)
print('the error message reads:', '%d' % info)


