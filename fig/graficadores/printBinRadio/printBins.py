#!/usr/bin/python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("binList.txt")

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(data[:,0],data[:,1],data[:,2],s=20)
plt.show()

