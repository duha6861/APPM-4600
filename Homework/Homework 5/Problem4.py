import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt


xpoint = [0, 1, 2, 3]
ypoint = [1, 4, 2, 6]

N = 1000
xeval = np.linspace(0, 3, N)

M = ([1, 0],
     [1, 1],
     [1, 2],
     [1, 3])

M_transpose = np.transpose(M)

MtM = np.dot(M_transpose, M)

a1 = np.dot(inv(MtM), np.dot(M_transpose, np.transpose(ypoint)))

p1 = lambda x: a1[0] + a1[1]*x
yeval1 = p1(xeval)

w = [1, 4, 9, 6]

D = [[np.sqrt(w[0]), 0, 0, 0],
     [0, np.sqrt(w[1]), 0, 0],
     [0, 0, np.sqrt(w[2]), 0],
     [0, 0, 0, np.sqrt(w[3])]]

MtDM = np.dot(np.dot(M_transpose, D), M)

a2 = np.dot(inv(MtDM), np.dot(np.dot(M_transpose, D), np.transpose(ypoint)))

p2 = lambda x: a2[0] + a2[1]*x
yeval2 = p2(xeval)

plt.figure(1)
plt.plot(xpoint, ypoint, 'o', label = 'Data Points')
plt.plot(xeval, yeval1, label = 'Ls')
plt.plot(xeval, yeval2, label = 'Weighted LS')
plt.legend()
plt.show()




