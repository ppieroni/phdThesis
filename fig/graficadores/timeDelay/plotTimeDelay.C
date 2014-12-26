
using namespace TMath;

Double_t timeDelayF(Double_t *x, Double_t *par){
    
    Double_t l0 = x[0];
    Double_t c = par[0];
    Double_t n = par[1];
    Double_t hd = par[2];
    Double_t da = par[3];
    Double_t theta = par[4];
    
    Double_t dt = 1/c * (l0 + n * (Sqrt(hd*hd+da*da+l0*l0+2*hd*l0*Sin(theta)-2*da*l0*Cos(theta)) - Sqrt(da*da+hd*hd)));

    return dt;
      
}

Double_t compFactorF(Double_t *x, Double_t *par){
    
    Double_t l0 = x[0];
    Double_t c = par[0];
    Double_t n = par[1];
    Double_t hd = par[2];
    Double_t da = par[3];
    Double_t theta = par[4];
    
    Double_t cf = 1/c * (1 + n * 1/(2 * Sqrt(hd*hd+da*da+l0*l0+2*hd*l0*Sin(theta)-2*da*l0*Cos(theta)))
    * (2 * Abs(l0) + 2 * hd * Sin(theta) - 2 * da * Cos(theta))
    );

    return cf;
      
}

Double_t compFactorF2D(Double_t *x, Double_t *par){
    
    Double_t l0 = x[0];
    Double_t theta = x[1];
    Double_t c = par[0];
    Double_t n = par[1];
    Double_t hd = par[2];
    Double_t da = par[3];
    
    Double_t cf = 1/c * (1 + n * 1/(2 * Sqrt(hd*hd+da*da+l0*l0+2*hd*l0*Sin(theta)-2*da*l0*Cos(theta)))
    * (2 * Abs(l0) + 2 * hd * Sin(theta) - 2 * da * Cos(theta))
    );

    return cf;
      
}

void plotTimeDelay(){
    
    const double kRad2Deg(180./ACos(-1));
    const double c = 0.299792458;
    const double n = 1.000325;
    double hd = 0;
    double da = 30000;
    double theta = 0.5 * 0.0174532925;
    
    TCanvas* v = new TCanvas("v","v",0,8,1200,750);
    //~ v->SetLogy();
    //~ v->SetLogz();
    //~ v->SetLogx();
    
    TF1* timeDelay = new TF1("timeDelay",timeDelayF,0,3e4,5);
    
    timeDelay -> SetParameter(0,c);
    timeDelay -> SetParameter(1,n);
    timeDelay -> SetParameter(2,hd);
    timeDelay -> SetParameter(3,da+10000);
    timeDelay -> SetParameter(4,theta);
    
    //~ TF1* timeDelayClone = timeDelay->Clone();
    //~ timeDelayClone ->GetYaxis()->SetRangeUser(1e-6,1);
    //~ timeDelayClone ->GetYaxis()->SetRangeUser(-1e-1,1e-1);
    //~ timeDelayClone -> DrawDerivative();
    
    //~ for(double dax = 10000; dax <= 100000; dax += 10000){
        //~ timeDelay -> SetParameter(3,dax);
        //~ TF1* timeDelayCloneX = timeDelay->Clone();
        //~ timeDelay -> DrawD();
    //~ }
    //~ 
    //~ 
    timeDelay->GetYaxis()->SetRangeUser(-50,0);
    timeDelay->DrawCopy();
    timeDelay -> SetParameter(3,da);
    timeDelay->Draw("same");
    //~ 
    //~ TF1* compFactor = new TF1("compFactor",compFactorF,0,2.5e4,5);
    //~ 
    //~ compFactor -> SetParameter(0,c);
    //~ compFactor -> SetParameter(1,n);
    //~ compFactor -> SetParameter(2,hd);
    //~ compFactor -> SetParameter(3,da);
    //~ compFactor -> SetParameter(4,theta);
    //~ compFactor->GetYaxis()->SetRangeUser(-1e-1,1e-1);
    //~ compFactor->Draw("l");
    //~ 
    //~ timeDelay -> SetParameter(3,da+1000);
    //~ timeDelay->DrawCopy("same");
    
    //~ TF2* compFactor2D = new TF2("compFactor2D",compFactorF2D,0,1e4,0.1 * 0.0174532925 * kRad2Deg,0.5 * 0.0174532925 * kRad2Deg,4);
    //~ compFactor2D -> SetParameter(0,c);
    //~ compFactor2D -> SetParameter(1,n);
    //~ compFactor2D -> SetParameter(2,hd);
    //~ compFactor2D -> SetParameter(3,da);
    //~ 
    //~ compFactor2D->Draw("colz");
    
}
