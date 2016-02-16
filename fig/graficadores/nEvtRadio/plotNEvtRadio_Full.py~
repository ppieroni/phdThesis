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
    
    expo = np.loadtxt('radio/exposure_090deg-092.5deg.txt',comments='#')
    area = 50000000**2
    expV.append(expo[:,1] * time * area)
    
    area = 25000000**2
    expV.append(expo[:,1] * time * area)
    
    expE = 10**(expo[:,0]-9)
    
    keys = ['Modelo','500 km','250 km']
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
