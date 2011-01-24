#include "TH1.h"
#include "TH1F.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TPostScript.h"
#include "TStyle.h"
#include "TLatex.h"
#include "TPaveText.h"
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;


void compare_v2() {

  gStyle->SetOptStat(0);

  //TFile* _file0 = new TFile("file:/localdata/dsperka/CMSSW_3_8_5/src/WprimeTrigEff/WprimeMuValidation/test/WprimeTrigEff_MultiJet_148031.root","OLD");
  TFile* _file0 = new TFile("file:/afs/cern.ch/user/d/dsperka/CMSSW_3_8_5/src/WprimeTrigEff/WprimeMuValidation/test/WprimeTrigEff_MultiJet_148822-149294-v2.root","OLD");


  _file0->cd();
  TH1* reco_pt = (TH1*)demo->Get("reco_pt"); reco_pt->SetDirectory(0);
  reco_pt->Sumw2();
  TH1* reco_eta_25 = (TH1*)demo->Get("reco_eta_25"); reco_eta_25->SetDirectory(0);
  reco_eta_25->Sumw2();

  TH1* l1mu7_pt = (TH1*)demo->Get("l1mu7_pt"); l1mu7_pt->SetDirectory(0);
  l1mu7_pt->Sumw2();
  TH1* l1mu7_eta_25 = (TH1*)demo->Get("l1mu7_eta_25"); l1mu7_eta_25->SetDirectory(0);
  l1mu7_eta_25->Sumw2();
  TH1* l1andhltmu9_pt = (TH1*)demo->Get("l1andhltmu9_pt"); l1andhltmu9_pt->SetDirectory(0);
  l1andhltmu9_pt->Sumw2();
  TH1* l1andhltmu11_pt = (TH1*)demo->Get("l1andhltmu11_pt"); l1andhltmu11_pt->SetDirectory(0);
  l1andhltmu11_pt->Sumw2();
  TH1* l1andhltmu13_pt = (TH1*)demo->Get("l1andhltmu13_pt"); l1andhltmu13_pt->SetDirectory(0);
  l1andhltmu13_pt->Sumw2();
  TH1* l1andhltmu15_pt = (TH1*)demo->Get("l1andhltmu15_pt"); l1andhltmu15_pt->SetDirectory(0);
  l1andhltmu15_pt->Sumw2();
  TH1* l1andhltmuFinalOR_pt = (TH1*)demo->Get("l1andhltmuFinalOR_pt"); l1andhltmuFinalOR_pt->SetDirectory(0);
  l1andhltmuFinalOR_pt->Sumw2();

  TH1* l1andhltmu9_eta_25 = (TH1*)demo->Get("l1andhltmu9_eta_25"); l1andhltmu9_eta_25->SetDirectory(0);
  l1andhltmu9_eta_25->Sumw2();
  TH1* l1andhltmu11_eta_25 = (TH1*)demo->Get("l1andhltmu11_eta_25"); l1andhltmu11_eta_25->SetDirectory(0);
  l1andhltmu11_eta_25->Sumw2();
  TH1* l1andhltmu13_eta_25 = (TH1*)demo->Get("l1andhltmu13_eta_25"); l1andhltmu13_eta_25->SetDirectory(0);
  l1andhltmu13_eta_25->Sumw2();
  TH1* l1andhltmu15_eta_25 = (TH1*)demo->Get("l1andhltmu15_eta_25"); l1andhltmu15_eta_25->SetDirectory(0);
  l1andhltmu15_eta_25->Sumw2();
  TH1* l1andhltmuFinalOR_eta_25 = (TH1*)demo->Get("1landhltmuFinalOR_eta_25"); l1andhltmuFinalOR_eta_25->SetDirectory(0);
  l1andhltmuFinalOR_eta_25->Sumw2();

  //Barrel
  TH1* reco_pt_b = (TH1*)demo->Get("reco_pt_b"); reco_pt_b->SetDirectory(0);
  reco_pt_b->Sumw2();
  TH1* l1mu7_pt_b = (TH1*)demo->Get("l1mu7_pt_b"); l1mu7_pt_b->SetDirectory(0);
  l1mu7_pt_b->Sumw2();
  TH1* l1andhltmu9_pt_b = (TH1*)demo->Get("l1andhltmu9_pt_b"); l1andhltmu9_pt_b->SetDirectory(0);
  l1andhltmu9_pt_b->Sumw2();
  TH1* l1andhltmu11_pt_b = (TH1*)demo->Get("l1andhltmu11_pt_b"); l1andhltmu11_pt_b->SetDirectory(0);
  l1andhltmu11_pt_b->Sumw2();
  TH1* l1andhltmu13_pt_b = (TH1*)demo->Get("l1andhltmu13_pt_b"); l1andhltmu13_pt_b->SetDirectory(0);
  l1andhltmu13_pt_b->Sumw2();
  TH1* l1andhltmu15_pt_b = (TH1*)demo->Get("l1andhltmu15_pt_b"); l1andhltmu15_pt_b->SetDirectory(0);
  l1andhltmu15_pt_b->Sumw2();
  TH1* l1andhltmuFinalOR_pt_b = (TH1*)demo->Get("l1andhltmuFinalOR_pt_b"); l1andhltmuFinalOR_pt_b->SetDirectory(0);
  l1andhltmuFinalOR_pt_b->Sumw2();

  // Endcap
  TH1* reco_pt_e = (TH1*)demo->Get("reco_pt_e"); reco_pt_e->SetDirectory(0);
  reco_pt_e->Sumw2();
  TH1* l1mu7_pt_e = (TH1*)demo->Get("l1mu7_pt_e"); l1mu7_pt_e->SetDirectory(0);
  l1mu7_pt_e->Sumw2();
  TH1* l1andhltmu9_pt_e = (TH1*)demo->Get("l1andhltmu9_pt_e"); l1andhltmu9_pt_e->SetDirectory(0);
  l1andhltmu9_pt_e->Sumw2();
  TH1* l1andhltmu11_pt_e = (TH1*)demo->Get("l1andhltmu11_pt_e"); l1andhltmu11_pt_e->SetDirectory(0);
  l1andhltmu11_pt_e->Sumw2();
  TH1* l1andhltmu13_pt_e = (TH1*)demo->Get("l1andhltmu13_pt_e"); l1andhltmu13_pt_e->SetDirectory(0);
  l1andhltmu13_pt_e->Sumw2();
  TH1* l1andhltmu15_pt_e = (TH1*)demo->Get("l1andhltmu15_pt_e"); l1andhltmu15_pt_e->SetDirectory(0);
  l1andhltmu15_pt_e->Sumw2();
  TH1* l1andhltmuFinalOR_pt_e = (TH1*)demo->Get("l1andhltmuFinalOR_pt_e"); l1andhltmuFinalOR_pt_e->SetDirectory(0);
  l1andhltmuFinalOR_pt_e->Sumw2();
 

  // Overlap
  TH1* reco_pt_o = (TH1*)demo->Get("reco_pt_o"); reco_pt_o->SetDirectory(0);
  reco_pt_o->Sumw2();
  TH1* l1mu7_pt_o = (TH1*)demo->Get("l1mu7_pt_o"); l1mu7_pt_o->SetDirectory(0);
  l1mu7_pt_o->Sumw2();

  TH1* l1andhltmu9_pt_o = (TH1*)demo->Get("l1andhltmu9_pt_o"); l1andhltmu9_pt_o->SetDirectory(0);
  l1andhltmu9_pt_o->Sumw2();
  TH1* l1andhltmu11_pt_o = (TH1*)demo->Get("l1andhltmu11_pt_o"); l1andhltmu11_pt_o->SetDirectory(0);
  l1andhltmu11_pt_o->Sumw2();
  TH1* l1andhltmu13_pt_o = (TH1*)demo->Get("l1andhltmu13_pt_o"); l1andhltmu13_pt_o->SetDirectory(0);
  l1andhltmu13_pt_o->Sumw2();
  TH1* l1andhltmu15_pt_o = (TH1*)demo->Get("l1andhltmu15_pt_o"); l1andhltmu15_pt_o->SetDirectory(0);
  l1andhltmu15_pt_o->Sumw2();
  TH1* l1andhltmuFinalOR_pt_o = (TH1*)demo->Get("l1andhltmuFinalOR_pt_o"); l1andhltmuFinalOR_pt_o->SetDirectory(0);
  l1andhltmuFinalOR_pt_o->Sumw2();

  eff_l1mu7 = new TGraphAsymmErrors;
  eff_l1mu7->BayesDivide(l1mu7_pt, reco_pt,"");
  etaeff_l1mu7 = new TGraphAsymmErrors;
  etaeff_l1mu7->BayesDivide(l1mu7_eta_25, reco_eta_25,"");
  eff_l1mu7_b = new TGraphAsymmErrors;
  eff_l1mu7_b->BayesDivide(l1mu7_pt_b, reco_pt_b,"");
  eff_l1mu7_o = new TGraphAsymmErrors;
  eff_l1mu7_o->BayesDivide(l1mu7_pt_o, reco_pt_o,"");
  eff_l1mu7_e = new TGraphAsymmErrors;
  eff_l1mu7_e->BayesDivide(l1mu7_pt_e, reco_pt_e,"");

  eff_l1andhltmu9 = new TGraphAsymmErrors;
  eff_l1andhltmu9->BayesDivide(l1andhltmu9_pt, reco_pt,"");
  eff_l1andhltmu11 = new TGraphAsymmErrors;
  eff_l1andhltmu11->BayesDivide(l1andhltmu11_pt, reco_pt,"");
  eff_l1andhltmu13 = new TGraphAsymmErrors;
  eff_l1andhltmu13->BayesDivide(l1andhltmu13_pt, reco_pt,"");
  eff_l1andhltmu15 = new TGraphAsymmErrors;
  eff_l1andhltmu15->BayesDivide(l1andhltmu15_pt, reco_pt,"");
  eff_l1andhltmuFinalOR = new TGraphAsymmErrors;
  eff_l1andhltmuFinalOR->BayesDivide(l1andhltmuFinalOR_pt, reco_pt,"");

  etaeff_l1andhltmu9 = new TGraphAsymmErrors;
  etaeff_l1andhltmu9->BayesDivide(l1andhltmu9_eta_25, reco_eta_25,"");
  etaeff_l1andhltmu11 = new TGraphAsymmErrors;
  etaeff_l1andhltmu11->BayesDivide(l1andhltmu11_eta_25, reco_eta_25,"");
  etaeff_l1andhltmu13 = new TGraphAsymmErrors;
  etaeff_l1andhltmu13->BayesDivide(l1andhltmu13_eta_25, reco_eta_25,"");
  etaeff_l1andhltmu15 = new TGraphAsymmErrors;
  etaeff_l1andhltmu15->BayesDivide(l1andhltmu15_eta_25, reco_eta_25,"");
  etaeff_l1andhltmuFinalOR = new TGraphAsymmErrors;
  etaeff_l1andhltmuFinalOR->BayesDivide(l1andhltmuFinalOR_eta_25, reco_eta_25,"");

  eff_l1andhltmu9_b = new TGraphAsymmErrors;
  eff_l1andhltmu9_b->BayesDivide(l1andhltmu9_pt_b, reco_pt_b,"");
  eff_l1andhltmu11_b = new TGraphAsymmErrors;
  eff_l1andhltmu11_b->BayesDivide(l1andhltmu11_pt_b, reco_pt_b,"");
  eff_l1andhltmu13_b = new TGraphAsymmErrors;
  eff_l1andhltmu13_b->BayesDivide(l1andhltmu13_pt_b, reco_pt_b,"");
  eff_l1andhltmu15_b = new TGraphAsymmErrors;
  eff_l1andhltmu15_b->BayesDivide(l1andhltmu15_pt_b, reco_pt_b,"");
  eff_l1andhltmuFinalOR_b = new TGraphAsymmErrors;
  eff_l1andhltmuFinalOR_b->BayesDivide(l1andhltmuFinalOR_pt_b, reco_pt_b,"");

  eff_l1andhltmu9_o = new TGraphAsymmErrors;
  eff_l1andhltmu9_o->BayesDivide(l1andhltmu9_pt_o, reco_pt_o,"");
  eff_l1andhltmu11_o = new TGraphAsymmErrors;
  eff_l1andhltmu11_o->BayesDivide(l1andhltmu11_pt_o, reco_pt_o,"");
  eff_l1andhltmu13_o = new TGraphAsymmErrors;
  eff_l1andhltmu13_o->BayesDivide(l1andhltmu13_pt_o, reco_pt_o,"");
  eff_l1andhltmu15_o = new TGraphAsymmErrors;
  eff_l1andhltmu15_o->BayesDivide(l1andhltmu15_pt_o, reco_pt_o,"");
  eff_l1andhltmuFinalOR_o = new TGraphAsymmErrors;
  eff_l1andhltmuFinalOR_o->BayesDivide(l1andhltmuFinalOR_pt_o, reco_pt_o,"");

  eff_l1andhltmu9_e = new TGraphAsymmErrors;
  eff_l1andhltmu9_e->BayesDivide(l1andhltmu9_pt_e, reco_pt_e,"");
  eff_l1andhltmu11_e = new TGraphAsymmErrors;
  eff_l1andhltmu11_e->BayesDivide(l1andhltmu11_pt_e, reco_pt_e,"");
  eff_l1andhltmu13_e = new TGraphAsymmErrors;
  eff_l1andhltmu13_e->BayesDivide(l1andhltmu13_pt_e, reco_pt_e,"");
  eff_l1andhltmu15_e = new TGraphAsymmErrors;
  eff_l1andhltmu15_e->BayesDivide(l1andhltmu15_pt_e, reco_pt_e,"");
  eff_l1andhltmuFinalOR_e = new TGraphAsymmErrors;
  eff_l1andhltmuFinalOR_e->BayesDivide(l1andhltmuFinalOR_pt_e, reco_pt_e,"");

  TF1 *f1 = new TF1("f1","pol0",25.0,300.0);

  TCanvas *c9 = new TCanvas("c9","c9",500,500);
  c9->Divide(2,2);
  c9->cd(1);
  eff_l1mu7->SetMarkerStyle(20);
  eff_l1mu7->SetLineColor(1);
  eff_l1mu7->SetMarkerColor(1);
  eff_l1mu7->Draw("AP");
  eff_l1mu7->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1mu7->GetYaxis()->SetTitle("Eff (L1|RECO)");
  eff_l1mu7->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1mu7,"L1SingleMu7","lp");
  legend->Draw("same");
  c9->cd(2);
  eff_l1mu7_b->SetMarkerStyle(20);
  eff_l1mu7_b->SetLineColor(1);
  eff_l1mu7_b->SetMarkerColor(1);
  eff_l1mu7_b->Draw("AP");
  eff_l1mu7_b->Fit("f1", "RME");
  eff_l1mu7_b->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1mu7_b->GetYaxis()->SetTitle("Eff (L1|RECO)");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<0.9");
  legend->AddEntry(eff_l1mu7_b,"L1SingleMu7","lp");
  legend->Draw("same");
  c9->cd(3);
  eff_l1mu7_o->SetMarkerStyle(20);
  eff_l1mu7_o->SetLineColor(1);
  eff_l1mu7_o->SetMarkerColor(1);
  eff_l1mu7_o->Draw("AP");
  eff_l1mu7_o->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1mu7_o->GetYaxis()->SetTitle("Eff (L1|RECO)");
  eff_l1mu7_o->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"0.9<|#eta|<1.2");
  legend->AddEntry(eff_l1mu7_o,"L1SingleMu7","lp");
  legend->Draw("same");
  c9->cd(4);
  eff_l1mu7_e->SetMarkerStyle(20);
  eff_l1mu7_e->SetLineColor(1);
  eff_l1mu7_e->SetMarkerColor(1);
  eff_l1mu7_e->Draw("AP");
  eff_l1mu7_e->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1mu7_e->GetYaxis()->SetTitle("Eff (L1|RECO)");
  eff_l1mu7_e->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"1.2<|#eta|<2.1");
  legend->AddEntry(eff_l1mu7_e,"L1SingleMu7","lp");
  legend->Draw("same");
 
  TCanvas *c16 = new TCanvas("c16","c16",600,600);
  c16->Divide(1,2);
  c16->cd(1);
  eff_l1andhltmu11->SetMarkerStyle(20);
  eff_l1andhltmu11->SetLineColor(1);
  eff_l1andhltmu11->SetMarkerColor(1);
  eff_l1andhltmu11->Draw("AP");
  eff_l1andhltmu11->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu11->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu11->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu11,"HLT_Mu11","lp");
  legend->Draw("same");
  c16->cd(2);
  eff_l1andhltmu15->SetMarkerStyle(20);
  eff_l1andhltmu15->SetLineColor(1);
  eff_l1andhltmu15->SetMarkerColor(1);
  eff_l1andhltmu15->Draw("AP");
  eff_l1andhltmu15->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu15->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu15,"HLT_Mu15","lp");
  legend->Draw("same");

  TCanvas *c10 = new TCanvas("c10","c10",500,500);
  c10->Divide(2,2);
  c10->cd(1);
  eff_l1andhltmu11->SetMarkerStyle(20);
  eff_l1andhltmu11->SetLineColor(1);
  eff_l1andhltmu11->SetMarkerColor(1);
  eff_l1andhltmu11->Draw("AP");
  eff_l1andhltmu11->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu11->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu11->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu11,"HLT_Mu11","lp");
  legend->Draw("same");
  c10->cd(2);
  eff_l1andhltmu11_b->SetMarkerStyle(20);
  eff_l1andhltmu11_b->SetLineColor(1);
  eff_l1andhltmu11_b->SetMarkerColor(1);
  eff_l1andhltmu11_b->Draw("AP");
  eff_l1andhltmu11_b->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu11_b->GetYaxis()->SetTitle("Eff (HLT|L1)");
  eff_l1andhltmu11->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<0.9");
  legend->AddEntry(eff_l1andhltmu11_b,"HLT_Mu11","lp");
  legend->Draw("same");
  c10->cd(3);
  eff_l1andhltmu11_o->SetMarkerStyle(20);
  eff_l1andhltmu11_o->SetLineColor(1);
  eff_l1andhltmu11_o->SetMarkerColor(1);
  eff_l1andhltmu11_o->Draw("AP");
  eff_l1andhltmu11_o->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu11_o->GetYaxis()->SetTitle("Eff (HLT|L1)");
  eff_l1andhltmu11_o->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"0.9<|#eta|<1.2");
  legend->AddEntry(eff_l1andhltmu11_o,"HLT_Mu11","lp");
  legend->Draw("same");
  c10->cd(4);
  eff_l1andhltmu11_e->SetMarkerStyle(20);
  eff_l1andhltmu11_e->SetLineColor(1);
  eff_l1andhltmu11_e->SetMarkerColor(1);
  eff_l1andhltmu11_e->Draw("AP");
  eff_l1andhltmu11_e->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu11_e->GetYaxis()->SetTitle("Eff (HLT|L1)");
  eff_l1andhltmu11_e->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"1.2<|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu11_e,"HLT_Mu11","lp");
  legend->Draw("same");

  TCanvas *c13 = new TCanvas("c13","c13",500,500);
  c13->Divide(2,2);
  c13->cd(1);
  eff_l1andhltmu15->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu15->SetMarkerStyle(20);
  eff_l1andhltmu15->SetLineColor(1);
  eff_l1andhltmu15->SetMarkerColor(1);
  eff_l1andhltmu15->Draw("AP");
  eff_l1andhltmu15->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu15,"HLT_Mu15","lp");
  legend->Draw("same");
  c13->cd(2);
  eff_l1andhltmu15_b->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15_b->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu15_b->SetMarkerStyle(20);
  eff_l1andhltmu15_b->SetLineColor(1);
  eff_l1andhltmu15_b->SetMarkerColor(1);
  eff_l1andhltmu15_b->Draw("AP");
  eff_l1andhltmu15_b->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<0.9");
  legend->AddEntry(eff_l1andhltmu15_b,"HLT_Mu15","lp");
  legend->Draw("same");
  c13->cd(3);
  eff_l1andhltmu15_o->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15_o->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu15_o->SetMarkerStyle(20);
  eff_l1andhltmu15_o->SetLineColor(1);
  eff_l1andhltmu15_o->SetMarkerColor(1);
  eff_l1andhltmu15_o->Draw("AP");
  eff_l1andhltmu15_o->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"0.9<|#eta|<1.2");
  legend->AddEntry(eff_l1andhltmu15_o,"HLT_Mu15","lp");
  legend->Draw("same");
  c13->cd(4);
  eff_l1andhltmu15_e->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15_e->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  eff_l1andhltmu15_e->SetMarkerStyle(20);
  eff_l1andhltmu15_e->SetLineColor(1);
  eff_l1andhltmu15_e->SetMarkerColor(1);
  eff_l1andhltmu15_e->Draw("AP");
  eff_l1andhltmu15_e->Fit("f1", "RME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"1.2<|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu15_e,"HLT_Mu15","lp");
  legend->Draw("same");

  TCanvas *c11 = new TCanvas("c11","c11",500,500);
  c11->Divide(2,2);
  c11->cd(1);
  etaeff_l1mu7->SetMarkerStyle(20);
  etaeff_l1mu7->SetLineColor(1);
  etaeff_l1mu7->SetMarkerColor(1);
  etaeff_l1mu7->Draw("AP");
  etaeff_l1mu7->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_l1mu7->GetYaxis()->SetTitle("Eff (L1|RECO)");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"p_{T} > 25 GeV");
  legend->AddEntry(etaeff_l1mu7,"L1SingleMu7","lp");
  legend->Draw("same");
  c11->cd(2);
  etaeff_l1andhltmu11->SetMarkerStyle(20);
  etaeff_l1andhltmu11->SetLineColor(1);
  etaeff_l1andhltmu11->SetMarkerColor(1);
  etaeff_l1andhltmu11->Draw("AP");
  etaeff_l1andhltmu11->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_l1andhltmu11->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.44,"p_{T} > 25 GeV");
  legend->AddEntry(etaeff_l1andhltmu11,"HLT_Mu11","lp");
  legend->Draw("same");
  c11->cd(3);
  etaeff_l1andhltmu13->SetMarkerStyle(20);
  etaeff_l1andhltmu13->SetLineColor(1);
  etaeff_l1andhltmu13->SetMarkerColor(1);
  etaeff_l1andhltmu13->Draw("AP");
  etaeff_l1andhltmu13->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_l1andhltmu13->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.44,"p_{T} > 25 GeV");
  legend->AddEntry(etaeff_l1andhltmu13,"HLT_Mu13","lp");
  legend->Draw("same");
  c11->cd(4);
  etaeff_l1andhltmu15->SetMarkerStyle(20);
  etaeff_l1andhltmu15->SetLineColor(1);
  etaeff_l1andhltmu15->SetMarkerColor(1);
  etaeff_l1andhltmu15->Draw("AP");
  etaeff_l1andhltmu15->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_l1andhltmu15->GetYaxis()->SetTitle("Eff (L1+HLT|RECO)");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.44,"p_{T} > 25 GeV");
  legend->AddEntry(etaeff_l1andhltmu15,"HLT_Mu15","lp");
  legend->Draw("same");


}
