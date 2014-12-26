#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys

kdeg2rad = np.pi/180.
krad2deg = 1./kdeg2rad

def timeDelayF(x, par):
    
    l0 = x
    c = par[0]
    n = par[1]
    hd = par[2]
    da = par[3]
    theta = par[4]
    
    dt = 1/c * (l0 + n * (np.sqrt(hd**2+da**2+l0**2+2*hd*l0*np.sin(theta)-2*da*l0*np.cos(theta)) - np.sqrt(da**2+hd**2)))
    return dt


def main(argv):
    x = np.linspace(0,3e4,100)
    #pars c, n, hd, da, theta
    for i in np.arange(5e3,55e3,5e3):
        par = np.array([0.299792458,1.000325,0,i,0.5*kdeg2rad])
        timeDelay = timeDelayF(x,par)
        timeDelay = np.where(timeDelay<0,timeDelay,0)
        plt.plot(x,timeDelay,lw=3)
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
