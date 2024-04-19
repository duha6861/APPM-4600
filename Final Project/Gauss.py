import numpy as np
import matplotlib.pyplot as plt

def eval_legendre(n,x):
    p = np.zeros(n+1)

    phi0 = 1
    phi1 = x

    p[0] = phi0
    p[1] = phi1

    for i in range(1,n):
        p[i+1] = ((2*i+1)*x*p[i] - i*p[i-1]) / (i+1)

    return(p[n])

def weight(xj,x):
    prod = 1
    for i in range(len(x)):
        if x[i] != xj:
            prod = prod * (xj - x[i])
    wj = 1/prod
    return(wj)

def eval_bary_lagrange(xeval,xint,yint):
    sum1 = 0
    sum2 = 0
    for j in range(len(xint)):
        if xeval != xint[j]:
            wj = weight(xint[j], xint)
            sum1 = sum1 + (wj * yint[j]) / (xeval - xint[j])
            sum2 = sum2 + wj / (xeval - xint[j])
    yeval = sum1/sum2
    return(yeval)

f = lambda x: np.exp(x)/np.sqrt(x)

n_node = 4
n_int = 2*n_node

a = 0
b = 1
xint = np.zeros(n_int)
for i in range(n_int):
    xint[i] = a + (i + 1)*(b - a)/(n_int + 1)
print(xint)
yint = f(xint)

x1 = 3/7 + 2*np.sqrt(30)/35
x2 = 3/7 - 2*np.sqrt(30)/35
xnode = [np.sqrt(x1), -np.sqrt(x1), np.sqrt(x2), -np.sqrt(x2)]
w = np.zeros(len(xnode))
pn_prime = lambda x: 1/8*(140*x**2 - 60*x)
sum = 0
for i in range(len(xnode)):
    w[i] = 2 / ((1 - xnode[i]**2) * (pn_prime(xnode[i])))
    sum  = sum + w[i]*eval_bary_lagrange(xnode[i],xint,yint)

N = 1000
xeval = np.linspace(0.001, 1, N)
yeval = f(xeval)
ybary = np.zeros(len(xeval))
for i in range(len(xeval)):
    ybary[i] = eval_bary_lagrange(xeval[i],xint,yint)

plt.figure(1)
plt.plot(xeval,yeval, label = 'f(x)')
plt.plot(xeval,ybary, label = 'poly')
plt.legend()
plt.show()

print(sum)
