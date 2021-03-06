#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("toPlot.txt")

intPes = np.trapz(data[:,1],data[:,0])
intRef = np.trapz(data[:,3],data[:,0])
intOpt = np.trapz(data[:,5],data[:,0])

intePes = np.sum(np.multiply(data[:,1],data[:,0]))/np.sum(data[:,1])
inteRef = np.sum(np.multiply(data[:,3],data[:,0]))/np.sum(data[:,3])
inteOpt = np.sum(np.multiply(data[:,5],data[:,0]))/np.sum(data[:,5])

print intPes,intRef,intOpt
print intePes,inteRef,inteOpt

fig = plt.figure(figsize=plt.figaspect(0.55))

pes, = plt.plot(data[:,0],data[:,1],c="b",ls='--',lw=2)
ref, = plt.plot(data[:,0],data[:,3],c="k",ls='-',lw=3)
opt, = plt.plot(data[:,0],data[:,5],c="r",ls='-.',lw=2)
plt.plot([intePes,intePes],[0,0.03],c="b",ls='--',lw=1)
plt.plot([inteRef,inteRef],[0,0.03],c="k",ls='-',lw=1)
plt.plot([inteOpt,inteOpt],[0,0.03],c="r",ls='-.',lw=1)

plt.grid()
plt.xlim([16,18])
plt.rc('text', usetex=True)
plt.xlabel(r"$\log\frac{E_\tau}{eV}$",fontsize="20")
plt.ylabel(r"$\frac{dN_\tau}{d\log\frac{E\tau}{eV}}$",fontsize="20")
plt.legend([ref,pes,opt],["Referencia - 1.6\%","Pesimista - 0.9\%","Optimista - 2.2\%"],loc=2,fontsize="20")
plt.title(r"$E_\nu=10^{18}{\rm eV\ -\ }\theta = 90.111^\circ$",fontsize="20")
plt.savefig("pdfSyst.pdf")
