import sys, os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


def get_field(s1, s2):
    """
    get_field(s1, s2):
    return: np array matrix
    """
    ff = s1+s2
    fin = open(ff,'r')
    y = np.loadtxt(fin)
    yy = y.reshape(257,128)
    return yy

abspath = '/Users/sandre/Desktop/variational_code/optimal_solver/DATA/'
label = '0_100_theta.txt'
yy = get_field(abspath, label)
label = '0_100_stream.txt'
ss = get_field(abspath, label)
z = np.linspace(0, np.pi, 256+1)
z = np.cos(z)/2+0.5
x = np.linspace(0,2,128)
X, Z = np.meshgrid(x, z)
print(len(yy))
pl1=plt.contourf(X, Z, 1-Z+0.5*yy, 24, cmap = plt.cm.coolwarm)
plt.colorbar(pl1, shrink=0.8, extend='both')
matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
pl2=plt.contour(X, Z, ss, 20, alpha=0.35, colors='k')

plt.show()

plt.contourf(X, Z, yy, cmap = plt.cm.gist_heat)
plt.show()

plt.contourf(X, Z, 1-Z+0.5*yy, 513 , cmap = plt.cm.RdYlBu_r)
plt.show()

a = np.array([[1, 2, 3], [4, 5, 6]], float)
b = a[0:2:1,0:2:1]
x = b[0:,0]
y = b[0:,1]
plt.plot(x,y,'ro')
plt.axis([0, 6, 0, 20])

