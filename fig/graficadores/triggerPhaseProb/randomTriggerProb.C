{
//=========Macro generated from canvas: v/v
//=========  (Sun Aug 23 17:04:46 2015) by ROOT version5.34/18
   TCanvas *v = new TCanvas("v", "v",0,0,1200,750);
   v->SetHighLightColor(2);
   v->Range(1,-9.959134,7,-0.8253702);
   v->SetFillColor(0);
   v->SetBorderMode(0);
   v->SetBorderSize(2);
   v->SetLogy();
   v->SetGridx();
   v->SetGridy();
   v->SetFrameBorderMode(0);
   v->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("");
   graph->SetTitle("Probabilidad de coincidencia aleatoria en una ventana de 3 grados");
   graph->SetFillColor(1);

   Int_t ci;   // for color index setting
   ci = TColor::GetColor("#ff0033");
   graph->SetMarkerColor(ci);
   graph->SetMarkerStyle(34);
   graph->SetMarkerSize(2.3);
   graph->SetPoint(0,2,0.016590545);
   graph->SetPoint(1,3,0.00020665);
   graph->SetPoint(2,4,2.27e-06);
   graph->SetPoint(3,5,2e-08);
   graph->SetPoint(4,6,1.000000001e-09);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","Probabilidad de coincidencia aleatoria en una ventana de 3 grados",100,1.6,6.4);
   Graph_Graph1->SetMinimum(9e-10);
   Graph_Graph1->SetMaximum(0.0182496);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);

   ci = TColor::GetColor("#000099");
   Graph_Graph1->SetLineColor(ci);
   Graph_Graph1->GetXaxis()->SetTitle("# antenas");
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetTitle("Probilidad");
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph1);
   
   graph->Draw("ap");
   
   TPaveText *pt = new TPaveText(0.15,0.9351662,0.85,0.995,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(0);
   pt->SetFillColor(0);
   pt->SetFillStyle(0);
   pt->SetTextFont(42);
   TText *text = pt->AddText("Probabilidad de coincidencia aleatoria en una ventana de 3 grados");
   pt->Draw();
   v->Modified();
   v->cd();
   v->SetSelected(v);
}
