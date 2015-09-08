#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>
#include <math.h>

#include "TCanvas.h"
#include "TGraph.h"
#include "TAxis.h"
#include "TMath.h"
#include "TRandom3.h"

using namespace std;
using namespace TMath;


const double kPi = asin(1.)*2.;
const double kDeg2Rad = kPi/180.;
const double keV2EeV = 1e-18;
const double kGeV2EeV = 1e-9;
const double kGrndRefIndex = 1.000325;
const double kChTheta = ACos(1./kGrndRefIndex);

int main(int argc, char *argv[]){
    
    int nTries = 1e9;
    int nMaxAnt = 6;
    
    TRandom3* rand = new TRandom3();
    rand->SetSeed(123457);
    double pVec[nMaxAnt];
    double phis[nMaxAnt];
    for(int j = 0; j<nMaxAnt; j++)
        pVec[j] = 1. / (100 * nTries);
        
    
    for(int i = 0; i<nTries; i++){
        if(i%10000000 == 0)
            cout << i << "/" << nTries << '\r';
        
        for(int j = 0; j<nMaxAnt; j++){
            double cPhi = 360*rand->Rndm();
            bool flag = true;
            for(unsigned int k = 0; k<j; k++)
                if(fabs(cPhi-phis[k])>3)
                    flag = false;
            if(flag){
                phis[j] = cPhi;
                pVec[j]++;
            } else
                break;
        }
    }
    cout << endl;
    
    TCanvas* v = new TCanvas("v","v",0,8,1200,750);
    v->SetGrid();
    TGraph* g = new TGraph();
    
    for(int j = 1; j<nMaxAnt; j++){
        pVec[j] /= nTries;
        g->SetPoint(j-1,j,pVec[j]);
    }
    
    v->SetLogy();
    g->SetMarkerStyle(34);
    g->SetMarkerSize(2.3);
    g->SetMarkerColor(kPink);
    g->Draw("ap");
    g->SetTitle("Probabilidad de coincidencia aleatoria en una ventana de 3 grados");
    g->GetXaxis()->SetTitle("# antenas");
    g->GetYaxis()->SetTitle("Probilidad");
    
    v->Print("randomTriggerProb.png","png");
    v->Print("randomTriggerProb.C","cxx");
    
        
    return 0;
}
