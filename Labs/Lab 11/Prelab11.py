def trapezoidal(a,b,N,f):
    h = (b - a)/N
    area = (f(a) + f(a+h))/2 * h
    x = h

    while x < b:
        area = area + (f(x) + f(x+h))/2 * h
        x = x + h

    return(area)

def comp_trapezoidal(a,b,N,f,f2):
    h = (b - a)/N
    u = (a + b)/2
    area = f(a)*h/2
    x = a + h

    for i in range(1,N-1):
        area = area + h * f(x)
        x = x + h
    
    area = area + f(b)*h/2 #- (b - a)/12*h**2*f2(u)

    return(area)