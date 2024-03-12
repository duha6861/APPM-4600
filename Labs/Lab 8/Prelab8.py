import numpy as np

def Line(a,p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    m = (y1 - y2)/(x1 - x2)

    b1 = y1 - m*x1
    b2 = y2 - m*x2

    if b1 != b2:
        err = 1
        f = 0

    err = 0
    f = m*a + b1

    return(err, f)

p1 = [2, 3]
p2 = [-1, 0]

a = 0

(err, f) = Line(a,p1,p2)

print(f,err)