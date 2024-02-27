import numpy as np

def ForDiff(f, s, h):
    f_prime = (f(s + h) - f(s))/h
    return (f_prime)

def CenDiff(f, s, h):
    f_prime = (f(s + h) - f(s - h))/(2*h)
    return (f_prime)

f = lambda x: np.cos(x)
s = np.pi/2
h = 0.01 / 2 ** (np.arange(0,10))

y_prime1 = ForDiff(f,s,h)
y_prime2 = CenDiff(f,s,h)

print('The approximate slopes using forward difference are:', y_prime1)
print('The approximate slopes using center difference are:', y_prime2)