#!/usr/bin/python

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

figsize = plt.figaspect(0.5)*1.2

kDeg2Rad = np.arccos(-1)/180

def main(argv):
    
    als = np.linspace(15,90,101)
    As = np.linspace(200,2000,19)
    nAnt = 9e4
    
    # choose a colormap
    c_m = matplotlib.cm.gist_rainbow_r
    #c_m = matplotlib.cm.jet
    
    norm = matplotlib.colors.Normalize(
                                       vmin=np.min(As),
                                       vmax=np.max(As))

    # create a ScalarMappable and initialize a data structure
    s_m = matplotlib.cm.ScalarMappable(cmap=c_m, norm=norm)
    s_m.set_array([])
    
    plt.figure(figsize=figsize)
    
    for i,A in enumerate(As):
        area = [nAnt * (A**2 * np.sin(al * kDeg2Rad)) * 1.5 / 1e6 for al in als]
        edge = [np.sqrt(a) for a in area]
        plt.plot(als,edge,color=s_m.to_rgba(A),lw=2)
    
    plt.axhline(250,color='k',lw=1,ls='--',label='GRAND')
    plt.axhline(500,color='k',lw=3,ls='--',label='Max')
    
    cb = plt.colorbar(s_m)
    cb.set_label(r'$a_1,a_2\,{\rm [m]}$',fontsize=18)
    plt.xlabel(r'$\alpha\,{\rm [deg]}$',fontsize=18)
    plt.ylabel(r'$L\,{\rm [km]}$',fontsize=18)
    plt.title('Lado equivalente de un SD cuadrado - Arreglo regular',fontsize=20)
    plt.legend(loc=2,fontsize=18)
#    plt.yscale('log')
    plt.savefig('Area_hc.pdf',format='pdf')
    
if __name__ == '__main__':
    main(sys.argv[1:])
