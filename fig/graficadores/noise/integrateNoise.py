#! /usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess as subp
import neurolab as nl
import sys
import os
import cmath
import matplotlib.cm as cm

def printHelp():
    print "Asi no!"
    print "Uso: plotNoise.py <noiseFile>"

def main(argv):
    
    if len(argv) != 1:
        printHelp()
        return
    
    inFile = argv[0]
    noise = np.loadtxt(inFile,comments='#')
    
    frec = noise[:,0]
    galactic = noise[:,1]
    reciever = noise[:,2]
    #print frec,reciever
    iFrecG = np.linspace(30,80,301)
    spectrumG = np.interp(iFrecG,frec,galactic)
    iFrecR = np.linspace(120,900,301)
    spectrumR = np.interp(iFrecR,frec,reciever)
    spectrumG2 = np.interp(iFrecR,frec,galactic)
    iFrecG3 = np.linspace(80,120,301)
    spectrumG3 = np.interp(iFrecG3,frec,galactic)
    iFrecG4 = np.linspace(30,900,1001)
    spectrumG4 = np.interp(iFrecG4,frec,galactic)
    
    N1 = np.trapz(np.multiply(spectrumG**2,iFrecG),np.log(iFrecG))
    D1 = (iFrecG[-1]-iFrecG[0])
    N2 = np.trapz(np.multiply(spectrumR**2,iFrecR),np.log(iFrecR))
    D2 = (iFrecR[-1]-iFrecR[0])
    N3 = np.trapz(np.multiply(spectrumG2**2,iFrecR),np.log(iFrecR))
    D3 = (iFrecR[-1]-iFrecR[0])
    N4 = np.trapz(np.multiply(spectrumG3**2,iFrecG3),np.log(iFrecG3))
    D4 = (iFrecG3[-1]-iFrecG3[0])
    N5 = np.trapz(np.multiply(spectrumG4**2,iFrecG4),np.log(iFrecG4))
    D5 = (iFrecG4[-1]-iFrecG4[0])
    
    print "G+R =",np.sqrt((N1+N2+N3))#/D1+D2)
    print "G+G =",np.sqrt((N1+N3))#/D1+D3)
    
    return

if __name__ == "__main__":
    main(sys.argv[1:])
