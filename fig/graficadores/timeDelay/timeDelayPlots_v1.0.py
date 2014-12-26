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
    R = np.sqrt(hd**2+da**2+l0**2+2*hd*l0*np.sin(theta)-2*da*l0*np.cos(theta))
    dt = 1/c * (l0 + n * ( R - np.sqrt(da**2+hd**2)))
    #~ dt = np.where(l0<=da,dt,0)
    dt = np.where(dt<0,dt,0)
    
    
    #Aproximated weights http://arxiv.org/pdf/1106.1073v2.pdf (eq. 122)
    t = l0/10000
    tmax = maxSh/10000
    pd = np.exp(-23*(np.sqrt(t)-np.sqrt(tmax))**2)
    iR = np.array(map(lambda x : 1/x, R))
    W = np.multiply(pd,iR)
    W = np.where(l0<=da,W,0)
    
    return dt,W,pd,iR

def timeIntegral(l0,timeDelay,weights):
    timeBins = np.arange(np.amin(timeDelay)-0.1,0,0.1)
    hist = np.histogram(timeDelay[timeDelay<0],timeBins,weights=weights[timeDelay<0])
    return hist

def getRGBColorFromMap(cm,i,imax):
    return cm(int(i/imax*(cm.N-5)))

def main(argv):
    l0 = np.linspace(0,35e3,100000)
    #~ l0 = np.linspace(0,6e4,10000)
    #~ l0 = np.linspace(0,6e4,100)
    
    fig1 = plt.figure(1,figsize=plt.figaspect(0.55)*1.3)
    fig2 = plt.figure(2,figsize=plt.figaspect(0.55)*1.3)
    fig3 = plt.figure(3,figsize=plt.figaspect(0.55)*1.3)
    fig4 = plt.figure(4,figsize=plt.figaspect(0.55)*1.3)
    
    cm = plt.get_cmap("spectral")
    
    minDa = 2e3
    maxDa = 30e3
    stpDa = 2e3
    
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
        timeDelay,weights,pd,iR = timeDelayF(l0,par)
        particles = timeIntegral(l0,timeDelay,weights)
        
        #Grafica
        currColor = getRGBColorFromMap(cm,da,maxDa)
        colors.append(currColor)
        plt.figure(1)
        tDelay, = plt.plot(l0,timeDelay,lw=3,color=currColor)
        plt.figure(2)
        #~ partDe, = plt.plot(l0[l0<maxDa],weights[l0<maxDa],lw=3,color=currColor)
        partDe, = plt.plot(l0[l0<maxDa],20*iR[l0<maxDa],lw=3,color=currColor)
        partDe, = plt.plot(l0[l0<maxDa],pd[l0<maxDa],lw=3,color=currColor,ls="--")
        plt.figure(3)
        eHisto, = plt.plot(particles[1][:-1],particles[0],lw=3,color=currColor)
        #~ absTime.append(particles[1][0]+np.sqrt(da**2+constHd**2))
        absTime.append(da)
        maxField.append(np.amax(particles[0]))
        
        plots.append(tDelay)
        names.append(str(da))
    
    plt.figure(4)
    plt.scatter(np.array(absTime),np.array(maxField),c=colors, s=100)
    
    plt.figure(1)
    plt.legend(np.array(plots),np.array(names),title="da [m]",fontsize=20)
    plt.title("Arrival time",fontsize=20)
    plt.xlabel(r'$\rm l [m]$',fontsize=20)
    plt.ylabel(r'$\rm t [ns]$',fontsize=20)
    plt.savefig("timeDelay_at.png",fontsize=20)

    plt.figure(2)
    plt.title("Particle density - $1/R$ weight",fontsize=20)
    plt.xlabel(r'$\rm l [m]$',fontsize=20)
    plt.ylabel(r'$\sim N$',fontsize=20)
    plt.savefig("timeDelay_pd.png",fontsize=20)

    plt.figure(3)
    plt.title("Accumulated signal",fontsize=20)
    plt.xlabel(r'$\rm t [ns]$',fontsize=20)
    plt.ylabel(r'$\sim E$',fontsize=20)
    plt.savefig("timeDelay_as.png",fontsize=20)
    
    plt.figure(4)
    plt.title("Signal peak amplitude",fontsize=20)
    plt.xlabel(r'$\rm da [m]$',fontsize=20)
    plt.ylabel(r'$\sim E$',fontsize=20)
    plt.savefig("timeDelay_spa.png",fontsize=20)

if __name__ == '__main__':
    main(sys.argv[1:])
