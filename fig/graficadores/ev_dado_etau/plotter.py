#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

figsize = plt.figaspect(0.55)*1.5


data = np.loadtxt('Etau2Ev.txt')

print(np.trapz(data[:,1],data[:,0]))
print(np.trapz(data[-13:,1],data[-13:,0]))
print(np.trapz(data[-24:-13,1],data[-24:-13,0]))
print(data[-13:,1])
print(data[-24:-13,1])
plt.figure(figsize=figsize)
plt.plot(data[:-1,0],data[:-1,1],lw=3,label=r'Distribucion de $E_v$ dado $E_\tau$')
plt.xlabel(r'$E_v$',fontsize=19)
plt.ylabel(r'p.d.f.',fontsize=19)
plt.yscale('log', nonposy='clip')
plt.legend(loc=2,fontsize=22)
plt.grid()
plt.savefig('ev_etau.png')
#plt.show()


