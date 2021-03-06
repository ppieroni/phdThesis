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

def main(argv):
    
    names = []
    with open(argv[0]) as inF:
        data = []
        currCurve = []
        for line in inF:
            if line.strip() == "":
                continue
            if line[0]=='#':
                if currCurve:
                    data.append(np.array(currCurve))
                    currCurve = []
                if line.strip() == '#END':
                    break
                names.append(line.strip()[1:])
                continue
            pLine = map(float,line.strip().split())
            currCurve.append(np.array(pLine))
    data = np.array(data)
    for name,dat in zip(names,data):
        print name,dat.shape
    
    plt.figure(figsize=plt.figaspect(0.55)*1.6)
    
    plots = []
    lgnds = []
    #Fe, FRII & SFR (Kampert '12)
    plt.plot(data[0][:,0],data[0][:,1],color='black',ls='--',lw=0)
    plt.fill_between(data[0][:,0],data[0][:,1],color="none",hatch='//',edgecolor="red")
    aux = plt.Rectangle((0,0),1,1,fc="none",hatch='//',edgecolor="red")
    plots.append(aux)
    lgnds.append(names[0])
    

    #p, Fermi-LAT (Ahlers '10)
    aux, = plt.plot(data[1][:,0],data[1][:,1],color="black",ls='--',lw=3)
    plots.append(aux)
    lgnds.append(names[1])
    
    ##Waxman-Bachall '01
    aux, = plt.plot([1.00688e+16,1.02415e+20],[2.23e-08,2.23e-08],color="black",ls=':',lw=5)
    plots.append(aux)
    lgnds.append("Waxman-Bachall '01")
    
    #p & mixed (Kotera '10)
    plt.plot(data[2][:,0],data[2][:,1],color="black",ls='--',lw=0)
    plt.fill_between(data[2][:,0],data[2][:,1],color="black",alpha=0.3)
    aux = plt.Rectangle((0,0),1,1,color="black",alpha=0.3)
    plots.append(aux)
    lgnds.append(names[2])
    
    
    
    #IceCube 2013
    aux, = plt.plot(data[3][:,0],data[3][:,1],color="green",ls='--',lw=5)
    plots.append(aux)
    lgnds.append(names[3])
    
    #IceCube 2013 Diff
    plt.plot(data[4][:,0],data[4][:,1],color="green",ls='--',lw=5)
    
    #Auger 2013
    aux, = plt.plot(data[5][:,0],data[5][:,1],color="red",ls='-',lw=5)
    plots.append(aux)
    lgnds.append(names[5])
    
    #Auger 2013 Diff
    plt.plot(data[6][:,0],data[6][:,1],color="red",ls='-',lw=5)
    
    #Anita 2013 Diff
    aux, = plt.plot(data[7][:,0],data[7][:,1],color="magenta",ls='-.',lw=5)
    plots.append(aux)
    lgnds.append(names[7])
    
    #Anita 2013
    plt.plot(data[8][:,0],data[8][:,1],color="magenta",ls='-.',lw=5)
    
    plt.title("Single flavor",fontsize=20)
    plt.xlabel(r'$E_\nu \rm[eV]$',fontsize=20)
    plt.ylabel(r'$E^{2} dN/dE\  \rm [GeV^2 cm^{-2} s^{-1} sr^{-1}]$',fontsize=20)
    
    plt.loglog()
    plt.xlim([1e16,1e21])
    plt.ylim([2e-10,1e-5])
    plt.legend(plots,lgnds,loc=2,fontsize=16)
    plt.savefig("limits_2013.pdf",format="pdf")
    
    
    
    
    
    
if __name__ == "__main__":
    main(sys.argv[1:])
