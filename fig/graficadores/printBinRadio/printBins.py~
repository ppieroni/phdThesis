#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("binList.txt")

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(data[:,0],180.-data[:,1],data[:,2],s=20,c=data[:,0])
ax.set_xlabel(r'$\log E_v$',fontsize=20)
ax.set_ylabel(r'$\theta_D$',fontsize=20)
ax.set_zlabel(r'${\rm x_d}$',fontsize=20)
ax.set_zlim([0,1200])
plt.show()

