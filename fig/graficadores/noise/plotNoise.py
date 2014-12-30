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

def printHelp():
    print "Asi no!"
    print "Uso: plotNoise.py <noiseFile>"

def main(argv):
    
    if len(argv) != 1:
        printHelp()
        return
    
    inFile = argv[0]
    noise = np.loadtxt(inFile,comments='#')
    plt.plot(noise[:,0],noise[:,1],noise[:,0],noise[:,2])
    plt.loglog()
    plt.show()
    print noise
    
    return

if __name__ == "__main__":
    main(sys.argv[1:])
