#!/usr/bin/python


import numpy as np
import subprocess as subP
import sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy as sp
from scipy.optimize import leastsq
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from mpltools import color

mpl.rc('font',size=18)
mpl.rc('text', usetex=True)
figsize = plt.figaspect(0.5)*1.2

def main():
    
    thEn = {'90.9':[],'91.3':[],'90.7':[],'91.9':[],'91.1':[],'92.1':[],
    '91.5':[],'92.3':[],'91.7':[],'90.5':[],'90.1':[]}
    
    fList = ['ZHSEvent_17.5_Maxenth.txt','ZHSEvent_18_Maxenth.txt','ZHSEvent_18.5_Maxenth.txt']
    en = [17.5,18,18.5]

    n_lines = 3
    color.cycle_cmap(n_lines, cmap='gnuplot')
    plt.figure(figsize=figsize)
    
    for fName in fList:
        idx = fList.index(fName)
        print fName
        cData = np.loadtxt(fName)
        for x in cData:
            thEn['{:4.1f}'.format(180-x[1])].append([en[idx],x[2]])
        
        plt.plot([180-x for x in cData[:,1]],cData[:,2],marker='o',ls='',ms=8,label='{}'.format(en[idx]))
    plt.grid()
    plt.legend(title=r'{\rm $\log{E_v}$}')
    plt.yscale("log", nonposy='clip')
    plt.xlabel(r'$\theta\ [deg]$')
    plt.ylabel(r'$E_{max}\ [\mu V/m]$')
    plt.savefig('eMaxTh.png')
    
    ##########
    
    n_lines = len(thEn)
    color.cycle_cmap(n_lines, cmap='gnuplot')
    plt.figure(figsize=figsize)
    
    for key in sorted(thEn.keys()):
        print(key)
        plt.plot([x[0] for x in thEn[key]],[x[1] for x in thEn[key]],lw=1.5,label='{}'.format(key))
    
    plt.grid()
    plt.legend(title=r'{\rm $\theta\ [deg]$}',loc=4,ncol=4,fontsize=16)
    plt.yscale("log", nonposy='clip')
    plt.xlabel(r'$\log{E_v}$')
    plt.ylabel(r'$E_{max}\ [\mu V/m]$')
    plt.savefig('eMaxThEv.png')
    
    
    ##########
    xdEn = {' 75':[],'  0':[],'100':[],' 25':[],' 50':[],'200':[],'150':[]
    ,'300':[]}
    
    fList = ['ZHSEvent_17.5_Maxenxd.txt','ZHSEvent_18_Maxenxd.txt','ZHSEvent_18.5_Maxenxd.txt']
    en = [17.5,18,18.5]

    n_lines = 3
    color.cycle_cmap(n_lines, cmap='gnuplot')
    plt.figure(figsize=figsize)
    
    for fName in fList:
        idx = fList.index(fName)
        print fName
        cData = np.loadtxt(fName)
        for x in cData:
            xdEn['{:3g}'.format(x[1])].append([en[idx],x[2]])
            
        plt.plot(cData[:,1],cData[:,2],marker='o',ls='',ms=8,label='{}'.format(en[idx]))
        
    plt.grid()
    plt.legend(title=r'{\rm $\log{E_v}$}')
    plt.yscale("log", nonposy='clip')
    plt.xlabel(r'$x_d\ [m]$')
    plt.ylabel(r'$E_{max}\ [\mu V/m]$')
    plt.savefig('eMaxXd.png')
    
    ##########
    
    n_lines = len(xdEn)
    color.cycle_cmap(n_lines, cmap='gnuplot')
    plt.figure(figsize=figsize)
    
    for key in sorted(xdEn.keys()):
        print(key)
        plt.plot([x[0] for x in xdEn[key]],[x[1] for x in xdEn[key]],lw=1.5,label='{}'.format(key))
    
    plt.grid()
    plt.legend(title=r'{\rm $x_d [m]$}',loc=2,ncol=2,fontsize=16)
    plt.yscale("log", nonposy='clip')
    plt.xlabel(r'$\log{E_v}$')
    plt.ylabel(r'$E_{max}\ [\mu V/m]$')
    plt.savefig('eMaxXdEv.png')
    
    
    plt.show()
        
    
    return 0

if __name__ == '__main__': main() 

