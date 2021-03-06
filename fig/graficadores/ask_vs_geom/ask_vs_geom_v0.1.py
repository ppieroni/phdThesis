#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 15:48:12 2014

@author: ppieroni
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mplt
from mayavi import mlab

font = {'size'   : 18}

mplt.rc('font', **font)

kDeg2Rad = np.arccos(-1)/180.

def getGeoMComps(th,phi,dec):

    radTh = th * kDeg2Rad
    radPh = phi * kDeg2Rad
    radDe = dec * kDeg2Rad

    xComp = - np.cos(radTh) * np.sin(radPh) * np.cos(radDe)
    yComp = + (np.sin(radTh) * np.sin(radDe) + np.cos(radTh) * np.cos(radPh) * np.cos(radDe))
    zComp = + np.cos(radTh) * np.sin(radPh) * np.sin(radDe)

    return np.array([xComp,yComp,zComp])

def getGeoM2DComps(th,phi,dec):

    radTh = th * kDeg2Rad
    radPh = phi * kDeg2Rad
    radDe = dec * kDeg2Rad

    grxProy = - np.sin(radPh)
    gryProy =   np.cos(radPh)

    xComp = - np.cos(radTh) * np.sin(radPh) * np.cos(radDe)
    yComp = + (np.sin(radTh) * np.sin(radDe) + np.cos(radTh) * np.cos(radPh) * np.cos(radDe))
    zComp = + np.cos(radTh) * np.sin(radPh) * np.sin(radDe)

    trComp = np.multiply(grxProy,xComp) + np.multiply(gryProy,yComp)

    return np.array([trComp,zComp])


def main(argv):

    #phi = np.arange(0,180)
    phi = np.linspace(0,180,90,True)
#    phi = 0
    geom = getGeoMComps(-0.5,phi,18.45)
    geom2D = getGeoM2DComps(-0.5,phi,18.45)

    norm = []
    for x in np.transpose(geom):
        norm.append(np.linalg.norm(x))
    norm = np.array(norm)
    print norm
    x, y, z = np.meshgrid(geom,geom,geom)

#    src = mlab.pipeline.vector_field(x,y,z)
#    mlab.pipeline.vector_cut_plane(src)
#    mlab.outline()
#    mlab.show()
#    print geom,geom2D
    plt.figure(figsize=[15,9])
    gx, = plt.plot(phi,geom[0,:],c="#0026FF",ls='--',lw=1.2)
    gy, = plt.plot(phi,geom[1,:],c="#FFA600",ls='--',lw=1.2)
    gz, = plt.plot(phi,geom[2,:],c="#D20010",ls='--',lw=2)
    gt, = plt.plot(phi,geom2D[0,:],c="#008702",ls='--',lw=2)
    gm, = plt.plot(phi,norm,c="#000000",ls='-',lw=3)
    plt.xlabel(r'$\phi \rm [deg]$',fontsize=22)
    plt.ylabel(r'$E\  \rm [arb\ units]$',fontsize=22)
    plt.legend([gx,gy,gz,gt,gm],['Ex','Ey','Ez','Etr','|E|'],loc=3)
    plt.savefig("geomComps_Tunka.pdf",format = "pdf")


if __name__ == '__main__':
    main(sys.argv[1:])
