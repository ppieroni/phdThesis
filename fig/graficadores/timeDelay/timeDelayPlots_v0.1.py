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
    maxSh = par[5]
    
    dt = 1/c * (l0 + n * (np.sqrt(hd**2+da**2+l0**2+2*hd*l0*np.sin(theta)-2*da*l0*np.cos(theta)) - n * np.sqrt(da**2+hd**2)))
    #~ dt = np.where(l0<=da,dt,0)
    dt = np.where(dt<0,dt,0)
    
    #Gaiser-Hillas weights
    #~ lnda = 5 * maxSh
    #~ xeff = l0/lnda
    #~ xmax = (maxSh - l0) / lnda
    #~ w = (xeff/xmax)**xmax * np.exp(xmax-xeff)
    #~ w = np.where(dt<0,w,0)
    
    #Aproximated weights http://arxiv.org/pdf/1106.1073v2.pdf (eq. 122)
    t = l0/10000
    tmax = maxSh/10000
    w = np.exp(-2*(np.sqrt(t)-np.sqrt(tmax))**2)
    w = np.where(dt<0,w,0)
    return dt,w

def timeIntegral(l0,timeDelay,weights):
    timeBins = np.arange(np.amin(timeDelay)-0.1,0,0.1)
    hist = np.histogram(timeDelay[timeDelay<0],timeBins,weights=weights[timeDelay<0])
    return hist

def getRGBColorFromMap(cm,i,imax):
    return cm(int(i/imax*(cm.N-5)))

def main(argv):
    l0 = np.linspace(0,6e4,100000)
    #~ l0 = np.linspace(0,6e4,100)
    
    fig = plt.figure(figsize=plt.figaspect(0.55)*1.5)
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    
    cm = plt.get_cmap("spectral")
    
    minDa = 5e3
    maxDa = 50e3
    stpDa = 5e3
    
    constC = 0.299792458
    constN = 1.000325
    constHd = 0
    constTh = 0.5*kdeg2rad
    constXmax = 1e4
    
    absTime = []
    maxField = []
    plots = []
    names = []
    colors = []
    
    for da in np.arange(minDa,maxDa,stpDa):
        #pars c, n, hd, da, theta, xMax
        par = np.array([constC,constN,constHd,da,constTh,constXmax])
        
        #Calcula
        timeDelay,weights = timeDelayF(l0,par)
        particles = timeIntegral(l0,timeDelay,weights)
        
        #Grafica
        currColor = getRGBColorFromMap(cm,da,maxDa)
        colors.append(currColor)
        tDelay, = ax1.plot(l0,timeDelay,lw=3,color=currColor)
        partDe, = ax2.plot(l0[l0<50e3],weights[l0<50e3],lw=3,color=currColor)
        eHisto, = ax3.plot(particles[1][:-1],particles[0],lw=3,color=currColor)
        #~ absTime.append(particles[1][0]+np.sqrt(da**2+constHd**2))
        absTime.append(da)
        maxField.append(np.amax(particles[0]))
        
        plots.append(tDelay)
        names.append(str(da))
    
    #~ ax4.scatter(np.array(absTime),np.array(maxField),c=range(len(absTime)), s=100)
    #~ ax4.scatter(np.array(absTime),np.array(maxField),c=np.array(absTime), s=100)
    ax4.scatter(np.array(absTime),np.array(maxField),c=colors, s=100)
    ax1.legend(np.array(plots),np.array(names),title="da [m]")
    #~ ax1.xlabel("l")
    #~ ax1.ylabel("time delay")
    ax1.set_title("Arrival time")
    ax2.set_title("Particle density")
    ax3.set_title("Accumulated signal")
    ax4.set_title("Signal peak amplitude")
    ax1.set_xlabel("l [m]")
    ax1.set_ylabel("t [ns]")
    ax2.set_xlabel("l [m]")
    ax2.set_ylabel("~ N")
    ax3.set_xlabel("t [ns]")
    ax3.set_ylabel("~ E")
    ax4.set_xlabel("da [m]")
    ax4.set_ylabel("~ E")
    #~ ax4.colorbar()
    
    #~ ax2.set_title("Particle density")
    #~ ax3.set_title("Accumulated signal")
    #~ ax4.set_title("Signal peak amplitude")
    
    
    plt.savefig("timeDelay.png")

if __name__ == '__main__':
    main(sys.argv[1:])
