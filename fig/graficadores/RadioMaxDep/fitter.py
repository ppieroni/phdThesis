#!/usr/bin/python


import numpy as np
import subprocess as subP
import sys
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import leastsq
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def fitF(x,p):
    X,Y = x
    A,B,C,D,E,F = p
    #~ retVal = A*np.exp(X/C)*np.exp((90-Y)/D)*np.exp(X*(90-Y)/B)+E
    #~ retVal = A*np.exp(X/C)*np.exp((90-Y)/D)+E
    retVal = A*np.exp(-X/(B*Y+C))*np.exp(-(90-Y)/(D*X+E))+F
    #~ retVal = A*np.exp(-(X+(90-Y)/(B*(90-Y)+C+D*X)))+F
    #~ print retVal
    return retVal

#~ def fitF(x,p):
#~ ##    print "fitF Call ",p
    #~ A,B1,B2,C = p
    #~ return 1*np.exp((89.9-x)/B1)

def regF(p,y,x):
    return y-fitF(x,p)

def plotFile(file):
    
    data = []
    
    for row in file:
        data.append(map(float,row.strip().split()))
    
    adata = np.array(data)
    adata = adata[np.argsort(adata[:,1])]
    norm = max(adata[:,2])
    adata[:,2] = np.multiply(adata[:,2],1./norm)
    #~ p0 = [1,-1,-80,-0.5,0.1]
    p0 = [1,-40,3660,1./375,13./30,0]
    #~ p0 = [1,-0.5,1,100,1,0]
    pOut = leastsq(regF,p0, args=(adata[:,2],(adata[:,0],adata[:,1])),full_output=1)
    print pOut[0]
    
    xs = adata[:,0]
    ys = adata[:,1]
    zs = adata[:,2]
    
    nPoints = 31
    xd = np.linspace(0, 300, nPoints)
    th = np.linspace(87, 90, nPoints)
    X,Y = np.meshgrid(xd, th)
    Z = fitF((X, Y),pOut[0])
    #~ aspect = 1./(1+np.sqrt(5)/2.)
    fig = plt.figure(figsize=plt.figaspect(0.55))
    ax = Axes3D(fig)
    ax.scatter(xs,ys,zs,c='y',marker='o',s=2000)
    ax.plot_wireframe(X, Y, Z,cmap='hot')
    #~ ax.plot_surface(X, Y, Z,cmap='hot')
    #~ ax2 = fig.add_subplot(333)
    #~ XX,YY = np.meshgrid(xs, ys)
    #~ ZZ = regF(pOut[0],zs) ###########################################
    #~ p = ax2.pcolor(X,Y,Z)
    #~ fig.colorbar(p,ax=ax2)
    
    
    #~ plt.plot(xvals,fitF((25,xvals),pOut[0]),adata[:,1],adata[:,2],'o')
    #~ plt.plot(adata[:,1],adata[:,2],)

def main():
    
    for fileName in sys.argv:
        if fileName.find("fitter") != -1:
            continue
        print fileName
        file = open(fileName,'r')
        #~ legend.append(fileName)
        #~ legend.append(fileName + " fit")
        plotFile(file)
    
    #~ plt.legend( legend)
    plt.show()
    
    return 0

if __name__ == '__main__': main()


##print fileList

##file = open("ZHSEvent_18_Maxenth.txt",'r')
##
##for row in file:
##    print row.strip().split()
##    

