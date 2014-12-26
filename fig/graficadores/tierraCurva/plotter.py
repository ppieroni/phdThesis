#! /usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess as subp
import neurolab as nl
import sys
import os
import re
import matplotlib.cm as cm

R=6.371e6
kdeg2rad = np.arccos(-1)/180.
krad2deg = 1./kdeg2rad

def getTC(xd):
    td = 180-180/np.pi*np.arccos(np.sqrt((2*R*xd+np.power(xd,2))/np.power((R+xd),2)))
    return td

def main(argv):
    
    plt.figure(figsize=plt.figaspect(0.55))
    xd=np.linspace(0,4000,100)
    td = getTC(xd)
    plt1, = plt.plot(td,xd,'b--',lw=3)
    plt.grid()
    plt.xlabel(r'$\theta_D \rm[deg]$',fontsize=18)
    plt.ylabel(r'$x_d \rm[m]$',fontsize=18)
    
    plt.text(91.55, 1200, 'Zona permitida',
        bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})
    
    plt.legend([plt1],["$x_d^{CUT}$"],loc=2)
    
    plt.savefig("thetaDCut.pdf",format="pdf")
    
    
    thD = np.arange(90.1,95,0.00001)
    cThD = np.cos(thD*kdeg2rad)
    Xd = np.arange(100,1700,200)
    
    plt.figure(figsize=plt.figaspect(0.55))
    plots = []
    xds = []
    for x in Xd:
        cThE = np.sqrt((R**2 - ((R+x)**2) * (1-cThD**2))/R**2)
        auxP, = plt.plot(thD,(x*(R*cThE-(R+x)*cThD))/((R**2 - (R+x)**2)*cThD),c=cm.gist_rainbow(float(x-5)/Xd[-1],1),lw=2.5)
        plots.append(auxP)
        xds.append(str(x))
    plt.grid()
    plt.legend(plots,xds,loc=4,title=r'$\bf{x_d \rm [m]}$')
    plt.xlabel(r'$\theta_D$',fontsize=18)
    plt.ylabel(r'$\frac{l_{plano}}{l_{curvo}}$',fontsize=18)
    plt.savefig("lPlane_lCurve.pdf",format="pdf")
    
    
    plt.figure(figsize=plt.figaspect(0.55))
    plots = []
    xds = []
    for x in Xd:
        cThE = -np.sqrt((R**2 - ((R+x)**2) * (1-cThD**2))/R**2)
        thE = np.arccos(cThE)*krad2deg
        auxP, = plt.plot(thD,thE,lw=2.5,c=cm.gist_rainbow(float(x-5)/Xd[-1],1))
        plots.append(auxP)
        xds.append(str(x))
    plt.grid()
    plt.legend(plots,xds,loc=4,title=r'$\bf{x_d \rm [m]}$')
    plt.xlabel(r'$\theta_D$',fontsize=18)
    plt.ylabel(r'$\theta_E$',fontsize=18)
    plt.savefig("thE_thD.pdf",format="pdf")
    
if __name__ == "__main__":
    main(sys.argv[1:])
