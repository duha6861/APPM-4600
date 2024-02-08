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


# Part b

theta  = np.linspace(0, 2*np.pi, 1000)
R = 1.2
dr = 0.1
f = 15
p=0

x = R*(1 + dr*np.sin(f*theta + p))*np.cos(theta)
y = R*(1 + dr*np.sin(f*theta + p))*np.sin(theta)

plt.figure(1)
plt.plot(x,y)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()


plt.figure(2)

i = 1
N = 10

for i in range(N):
    R = i
    f = 2 + i
    dr = 0.05
    p = np.random.uniform(0, 2)

    x2 = R*(1 + dr*np.sin(f*theta + p))*np.cos(theta)
    y2 = R*(1 + dr*np.sin(f*theta + p))*np.sin(theta)

    plt.plot(x2, y2)
plt.show()

 