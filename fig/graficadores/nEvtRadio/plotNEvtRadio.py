#! /usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess as subp
import neurolab as nl
import sys
import os
import re
from pprint import pprint as pp
import matplotlib.cm as cm
import tabulate as tb

kdeg2rad = np.arccos(-1)/180.
krad2deg = 1./kdeg2rad

def main(argv):
    
    time = 9.46708e7
    expV = []
    
    expo = np.loadtxt('Integral_050_05_2000_2000_090_1.00_re.txt',comments='#')
    area = 200000*200000*np.sin(90*kdeg2rad)* 1. * 9e4 # area de la celda primitiva in cm^2 * regular (1.) * 9e4 celdas
    expV.append(expo[:,1] * time * area)
    
    expo = np.loadtxt('Integral_050_05_2000_2000_090_1.00_hc.txt',comments='#')
    area = 200000*200000*np.sin(90*kdeg2rad)* 1.5 * 9e4 # area de la celda primitiva in cm^2 * hclattice (1.5) * 9e4 celdas
    expV.append(expo[:,1] * time * area)
    
    expo = np.loadtxt('Integral_050_05_1000_10000_090_1.00_de.txt',comments='#')
    nCells = 90000./(2.*10.-1) # 2*float(a2)/float(a1)-1 a1=1000 a2=10000
    area = 1e12*np.sin(90*kdeg2rad)* nCells # area de la celda primitiva in cm^2 * dense edge number of cells
    expV.append(expo[:,1] * time * area)
    
    expE = 10**(expo[:,0]-9)
    
    keys = ['Modelo','Regular','Panal de abeja','Bordes densos']
    result = {}
    
    fListF = open('fileList.txt')
    for iFile in fListF:
        iFile = iFile.strip()
        if iFile[0] == '#':
            continue
        print 'Proc..',iFile
        data = np.loadtxt(iFile,comments='#')
        fluxE = data[:,0]*1e-9
        fluxV = data[:,1]/3. * fluxE**-2
        name = iFile.replace('.dat','')

        result[name] = []
        for cExpV in expV:
            expFixed = np.interp(fluxE,expE,cExpV)
            result[name].append(np.trapz(fluxV * expFixed,fluxE))
    pRes = []
    for it in result.items():
        pRes.append([it[0]]+['{:.1f}'.format(x) for x in it[1]])
    print tb.tabulate(pRes,headers=keys,tablefmt="latex")
    
    
if __name__ == '__main__':
    main(sys.argv[1:])
