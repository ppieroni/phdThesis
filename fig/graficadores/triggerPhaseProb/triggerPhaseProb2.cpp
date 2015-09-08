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
const double kPhiWindow = 4;

bool FindConf(double* phis, double* ths, vector<unsigned int>& eCand, vector<unsigned int>& evt, unsigned int eSize){
    
    int eCandSize = eCand.size();
    int evtSize = evt.size();
    
    //~ cout << "tamanos " << eCandSize << " " << evtSize << endl;
    
    if(eCandSize == 0)
        return false;
    
    unsigned int cIdx = eCand[eCandSize-1];
    double cPhi = phis[cIdx];
    double cTh = ths[cIdx];
    
    //~ cout << "cIdx " << cIdx << " " << cPhi << " " << cTh << endl;
    
    bool evtFlag = true;
    for(int i = 0; i<evtSize; i++){
        //~ cout << "evt i " << i << " " << evt[i] << " " << phis[evt[i]] << " " << ths[evt[i]] << endl;
        if(!(fabs(cPhi-phis[evt[i]])<kPhiWindow && cTh*ths[evt[i]]>0)){
            evtFlag = false;
            break;
        }
    }
    
    if(evtFlag)
        evt.push_back(cIdx);
    
    eCand.pop_back();
    
    if(evt.size() == eSize)
        return true;
    
    if(FindConf(phis,ths,eCand,evt,eSize))
        return true;
    
    return false;
}

int main(int argc, char *argv[]){
    
    int nTries = 1e6;
    int nMaxAnt = 7;
    int nDetAnt = 15;
    
    TRandom3* rand = new TRandom3();
    rand->SetSeed(123457);
    double pVec[nDetAnt];
    for(int j = 0; j<nDetAnt; j++)
        pVec[j] = 0.;
    
    double phis[nDetAnt];
    double ths[nDetAnt];
    
    vector<unsigned int> idxs;
    for(int j = 0; j<nDetAnt; j++)
        idxs.push_back(j);

    for(int i = 0; i<nTries; i++){
        if(i%1000 == 0){
            cout << i << "/" << nTries << '\r';
            cout.flush();
        }
        
        
        for(int j = 0; j<nDetAnt; j++){
            double cPhi = 360*rand->Rndm();
            double cTh = rand->Rndm()-0.5;
            phis[j] = cPhi;
            ths[j] = cTh;
        }
        
        for(int j = nMaxAnt; j>1; j--){
            vector<unsigned int> tmpCand1 = idxs;
            while(tmpCand1.size() > j){
                int candLeft = tmpCand1.size();
                //~ cout << "Inicio -> "<<  j << " "  << candLeft << " " << tmpCand1[candLeft-1] << endl;
                vector<unsigned int> evt(1,tmpCand1[candLeft-1]);
                tmpCand1.pop_back();
                vector<unsigned int> tmpCand2 = tmpCand1;
                //~ cout << "- " << evt.size() << " " << tmpCand1.size() << endl;
                
                if(FindConf(phis,ths,tmpCand2,evt,j)){
                    //~ cout << "   evt!" << endl;
                    pVec[j]++;
                } else {
                    //~ cout << "no evt!" << endl;
                    continue;
                }
            }
        }
    }
    
    for(int j = 2; j<=nMaxAnt; j++){
        pVec[j] /= nTries;
        cout << j << " " << pVec[j] << endl;
    }
    
        //~ for(int j = nMaxAnt; j>0; j--){
            //~ for(int k = 0; k<idxs.size(); k++){
                //~ for(int l = k; l<idxs.size(); k++){
                    //~ 
                    //~ 
                    //~ 
                    //~ 
                    //~ 
                    //~ 
            //~ bool flag = true;
            //~ for(unsigned int k = 0; k<j; k++)
                //~ if(fabs(cPhi-phis[k])>3)
                    //~ flag = false;
            //~ if(flag){
                //~ 
                //~ pVec[j]++;
            //~ } else
                //~ break;
        //~ }
    //~ }
    //~ cout << endl;
    
    //~ TCanvas* v = new TCanvas("v","v",0,8,1200,750);
    //~ v->SetGrid();
    //~ TGraph* g = new TGraph();
    
    //~ for(int j = 1; j<nMaxAnt; j++){
        //~ pVec[j] /= nTries;
        //~ g->SetPoint(j-1,j+1,pVec[j]);
    //~ }
    
    //~ v->SetLogy();
    //~ g->SetMarkerStyle(34);
    //~ g->SetMarkerSize(2.3);
    //~ g->SetMarkerColor(kPink);
    //~ g->Draw("ap");
    //~ g->SetTitle("Probabilidad de coincidencia aleatoria en una ventana de 3 grados");
    //~ g->GetXaxis()->SetTitle("# antenas");
    //~ g->GetYaxis()->SetTitle("Probilidad");
    //~ 
    //~ v->Print("randomTriggerProb.png","png");
    //~ v->Print("randomTriggerProb.C","cxx");
    
        
    return 0;
}
