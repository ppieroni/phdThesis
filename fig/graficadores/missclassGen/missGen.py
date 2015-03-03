#!/usr/bin/python

import numpy as np
import sys
import matplotlib.pyplot as plt

def main(argv):
    print "Corriendo..."
    
    
    eES_ES = 0.167
    eES_ESyDG = 0.622
    eES_DG = 0.042
    eDG_ES = 0.027
    eDG_ESyDG = 0.067
    eDG_DG = 0.045
    
    pES_ESyDG = eES_ESyDG/(eES_ESyDG+eDG_ESyDG)
    pDG_ESyDG = eDG_ESyDG/(eES_ESyDG+eDG_ESyDG)
    
    pES_ES = eES_ES/(eES_ES+eDG_ES)
    pDG_ES = eDG_ES/(eES_ES+eDG_ES)
    
    pES_DG = eES_DG/(eES_DG+eDG_DG)
    pDG_DG = eDG_DG/(eES_DG+eDG_DG)
    
    pDG = eDG_DG + eES_DG
    pES = eES_ES + eDG_ES
    pDGyES = eES_ESyDG + eDG_ESyDG
    
    print pES_ESyDG,pDG_ESyDG
    print pES_ES,pDG_ES
    print pES_DG,pDG_DG
    print pDG,pES,pDGyES,pDG+pES+pDGyES
    

if __name__ == '__main__': main(sys.argv[1:])
