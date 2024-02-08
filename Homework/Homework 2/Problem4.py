import numpy as np
import matplotlib.pyplot as plt

# Part a

t = np.arange(0, np.pi, np.pi/30)
y = np.cos(t)

i = 0
N = len(t)
for i in range(N):
    S = t[i]*y[i]

print('The sum is:', S)
