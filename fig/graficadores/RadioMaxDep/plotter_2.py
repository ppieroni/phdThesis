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
    '91.5':[],'92.3':[],'92.5':[],'92.7':[],'92.9':[],'91.7':[],'90.5':[],'90.1':[]}
    
    fList = ['maxInfo_en_17.5_th_All_phi_All_xd_100.dat',
    'maxInfo_en_18_th_All_phi_All_xd_100.dat',
    'maxInfo_en_18.5_th_All_phi_All_xd_100.dat']
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
    plt.savefig('eMaxTh_100.png')
    
    ##########
    
    n_lines = len(thEn)
    color.cycle_cmap(n_lines, cmap='gnuplot')
    plt.figure(figsize=figsize)
    
    for key in sorted(thEn.keys()):
        print(key)
        plt.plot([x[0] for x in thEn[key]],[x[1] for x in thEn[key]],lw=1.5,label='{}'.format(key))
    
    plt.grid()
    plt.legend(title=r'{\rm $\theta\ [deg]$}',loc=2,ncol=4,fontsize=14)
    plt.yscale("log", nonposy='clip')
    plt.xlabel(r'$\log{E_v}$')
    plt.ylabel(r'$E_{max}\ [\mu V/m]$')
    plt.savefig('eMaxThEv_100.png')
    
    
    plt.show()
        
    
    return 0

if __name__ == '__main__': main() 

