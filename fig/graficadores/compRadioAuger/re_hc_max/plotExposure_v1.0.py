#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

def getUniqeVlues(nplst):
    return np.unique(np.sort(nplst))

def main(argv):
    
    fileList = open(argv[0])
    i=1
    resDict = {"re":[], "hc":[], "de":[]}
    for fName in fileList:
        fName = fName.strip()
        #~ print i,fName
        inFile = open(fName)
        firstLine = inFile.readline().strip().split()
        th = firstLine[1]
        an = firstLine[2]
        a1 = firstLine[3]
        a2 = firstLine[4]
        al = firstLine[5]
        ef = firstLine[6]
        top = firstLine[7]
        inFile.close()
        data = np.loadtxt(fName,comments='#')
        #factor contempla comparacion topografica con Auger:
        #90000/1600=56.25 detectores 
        #float(a1)*float(a2)*np.sin(float(al)*np.pi/180.) area de la celda primitiva del array de radio
        #(1500**2*np.sin(60./180*np.pi) area de la celda primitiva de Auger
        topFactor = 1
        if top == "hc":
           topFactor = 1.5 
        factor = 56.25 *float(a1)*float(a2)*np.sin(float(al)*np.pi/180.)*topFactor/(1500**2*np.sin(60./180*np.pi))
        if top == "de":
            nCells = 90000./(2.*float(a2)/float(a1)-1)
#            print (2.*float(a2)/float(a1)-1)
            factor = nCells * (float(a2) **2) / (1600*1500**2*np.sin(60./180*np.pi))
        resDict[top].append([float(th),float(an),float(a1),float(a2),float(al),float(ef),np.trapz(data[:,1]/(10**data[:,0])*factor,x=data[:,0])])
        i = i+1
    for key in resDict:
        print key
        if len(resDict[key]) == 0:
            continue
        res = np.array(resDict[key])
        data = np.loadtxt("exposure_combined_ES_1Jan04-31May10.dat")
        intAug = np.trapz(data[:,1]/data[:,0]/3.5/3.15569e7/3e13,x=np.log10(data[:,0]))
        
        thrs = getUniqeVlues(res[:,0])
        ants = getUniqeVlues(res[:,1])
        effs = getUniqeVlues(res[:,5])
        
        fig1 = plt.figure(figsize=plt.figaspect(0.55))
        
        for th in thrs:
            for an in ants:
                for ef in effs:
                    title = r'Threshold: '+str(th)+r'$\rm \mu Vm$ - Trigger: '+str(an)+r'aOT - ID eff: '+str(0.9)
                    print title
                    name1 = "CompRadioAuger_"+str(th)+"_"+str(an)+"_"+str(ef)+"_"+key+"_modo1.pdf"
                    name2 = "CompRadioAuger_"+str(th)+"_"+str(an)+"_"+str(ef)+"_"+key+"_modo2.pdf"
                    cond1 = res[:,0] == th
                    cond2 = res[:,1] == an 
                    cond3 = res[:,5] == ef
                    cond = np.multiply(cond1,np.multiply(cond2,cond3))
                    
                    fig1.clf()
                    plt.scatter(res[cond,4],np.multiply(res[cond,6],1./intAug),c=res[cond,2],s=80)
                    cb = plt.colorbar()
                    cb.set_label(r'$a_1,a_2$',fontsize=18)
                    plt.xlabel(r'$\alpha$',fontsize=18)
                    plt.ylabel(r'$N_{Radio}/N_{Auger}$',fontsize=18)
                    plt.ylim([0.,plt.ylim()[1]])
                    plt.title(title)
                    plt.savefig(name1,format="pdf")
                
                    #~ fig2 = plt.figure(figsize=plt.figaspect(0.55))
                    fig1.clf()
                    if key == 'de':
                        plt.scatter(res[cond,2],np.multiply(res[cond,6],1./intAug),c=res[cond,3],s=80)
                        cb.set_label(r'$a_2$',fontsize=18)
                        plt.xlabel(r'$a_1$',fontsize=18)
                    else:
                        plt.scatter(res[cond,2],np.multiply(res[cond,6],1./intAug),c=res[cond,4],s=80)
                        cb.set_label(r'$\alpha$',fontsize=18)
                        plt.xlabel(r'$a_1,a_2$',fontsize=18)
                    cb = plt.colorbar()
                    plt.ylabel(r'$N_{Radio}/N_{Auger}$',fontsize=18)
                    plt.ylim([0.,plt.ylim()[1]])
                    plt.title(title)
                    plt.savefig(name2,format="pdf")
                    

if __name__ == '__main__':
    main(sys.argv[1:])
