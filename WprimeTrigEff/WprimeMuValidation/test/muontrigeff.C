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

void muontrigeff() {
      TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

  // For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(600); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

  // For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(false);
  tdrStyle->SetGridColor(0);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

  // For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);

  // For the histo:
  // tdrStyle->SetHistFillColor(1);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

  tdrStyle->SetEndErrorSize(2);
  //  tdrStyle->SetErrorMarker(20);
  tdrStyle->SetErrorX(0.);

  tdrStyle->SetMarkerStyle(20);

  //For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

  //For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Float_t x = 0.01);
  // tdrStyle->SetDateY(Float_t y = 0.01);

  // For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat("emr"); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(1);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Float_t x = 0);
  // tdrStyle->SetStatY(Float_t y = 0);

  // Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.13);
  tdrStyle->SetPadRightMargin(0.05);

  // For the Global title:
  tdrStyle->SetOptTitle(0);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleFontSize(0.05);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  // tdrStyle->SetTitleX(0); // Set the position of the title box
  // tdrStyle->SetTitleY(0.985); // Set the position of the title box
  // tdrStyle->SetTitleStyle(Style_t style = 1001);
  // tdrStyle->SetTitleBorderSize(2);

  // For the axis titles:
  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.05);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

  // For the axis labels:
  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.05, "XYZ");

  // For the axis:
  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

  // Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

  // Postscript options:
  tdrStyle->SetPaperSize(20.,20.);
  // tdrStyle->SetLineScalePS(Float_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

   //tdrStyle->SetBarOffset(Float_t baroff = 0.5);
   //tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
   //tdrStyle->SetPaintTextFormat(const char* format = "g");
   tdrStyle->SetPalette(1);
   //tdrStyle->SetTimeOffset(Double_t toffset);
   //tdrStyle->SetHistMinimumZero(kTRUE);






   const Int_t NRGBs = 5;
   const Int_t NCont = 255;

   Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
   Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
   Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
   Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
   TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
   TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
   tdrStyle->SetNumberContours(NCont);


   //TLatex *lab = new TLatex(0.70,0.85, "CMS 2008");
   //lab->SetNDC();
   //lab->SetTextFont(42);
   //lab->SetTextSize(0.05);
   //lab->Draw("same");

  gROOT -> ForceStyle();

  tdrStyle->cd();

  gStyle->SetPalette(1);
  gStyle->SetTitleYSize(0.10);
  gStyle->SetTitleYOffset(0.70);
  gStyle->SetLabelSize(0.07,"Y");
  gStyle->SetMarkerStyle(20);
  gStyle->SetMarkerSize(0.6);
  gStyle->SetLineColor(1);
  gStyle->SetMarkerColor(1);
  gStyle->SetOptFit(0);

  TFile* _file0 = new TFile("file:/localdata/dsperka/CMSSW_3_8_5/src/WprimeTrigEff/WprimeMuValidation/test/MuonTrigEff_Nov4JetSkim_146644andup_Apr14.root","OLD");
  TFile* _file1 = new TFile("file:/localdata/dsperka/CMSSW_3_8_5/src/WprimeTrigEff/WprimeMuValidation/test/MuonTrigEff_Wmunu-powheg_Mar12.root","OLD");


  _file0->cd();
  TH1* reco_eta_20 = (TH1*)demo->Get("reco_eta_20"); reco_eta_20->SetDirectory(0);
  reco_eta_20->Sumw2();
  TH1* l1mu7_eta_20 = (TH1*)demo->Get("l1mu7_eta_20"); l1mu7_eta_20->SetDirectory(0);
  l1mu7_eta_20->Sumw2();
  TH1* hltmu15_eta_20 = (TH1*)demo->Get("hltmu15_eta_20"); hltmu15_eta_20->SetDirectory(0);
  hltmu15_eta_20->Sumw2();
  TH1* l1andhltmu15_eta_20 = (TH1*)demo->Get("l1andhltmu15_eta_20"); l1andhltmu15_eta_20->SetDirectory(0);
  l1andhltmu15_eta_20->Sumw2();

  TH1* reco_pt = (TH1*)demo->Get("reco_pt"); reco_pt->SetDirectory(0);
  reco_pt->Sumw2();
  TH1* l1mu7_pt = (TH1*)demo->Get("l1mu7_pt"); l1mu7_pt->SetDirectory(0);
  l1mu7_pt->Sumw2();
  TH1* hltmu15_pt = (TH1*)demo->Get("hltmu15_pt"); hltmu15_pt->SetDirectory(0);
  hltmu15_pt->Sumw2();
  TH1* l1andhltmu15_pt = (TH1*)demo->Get("l1andhltmu15_pt"); l1andhltmu15_pt->SetDirectory(0);
  l1andhltmu15_pt->Sumw2();

  TH1* reco_pt_b = (TH1*)demo->Get("reco_pt_b"); reco_pt_b->SetDirectory(0);
  reco_pt_b->Sumw2();
  TH1* l1mu7_pt_b = (TH1*)demo->Get("l1mu7_pt_b"); l1mu7_pt_b->SetDirectory(0);
  l1mu7_pt_b->Sumw2();
  TH1* hltmu15_pt_b = (TH1*)demo->Get("hltmu15_pt_b"); hltmu15_pt_b->SetDirectory(0);
  hltmu15_pt_b->Sumw2();
  TH1* l1andhltmu15_pt_b = (TH1*)demo->Get("l1andhltmu15_pt_b"); l1andhltmu15_pt_b->SetDirectory(0);
  l1andhltmu15_pt_b->Sumw2();

  TH1* reco_pt_o = (TH1*)demo->Get("reco_pt_o"); reco_pt_o->SetDirectory(0);
  reco_pt_o->Sumw2();
  TH1* l1mu7_pt_o = (TH1*)demo->Get("l1mu7_pt_o"); l1mu7_pt_o->SetDirectory(0);
  l1mu7_pt_o->Sumw2();
  TH1* hltmu15_pt_o = (TH1*)demo->Get("hltmu15_pt_o"); hltmu15_pt_o->SetDirectory(0);
  hltmu15_pt_o->Sumw2();
  TH1* l1andhltmu15_pt_o = (TH1*)demo->Get("l1andhltmu15_pt_o"); l1andhltmu15_pt_o->SetDirectory(0);
  l1andhltmu15_pt_o->Sumw2();

  TH1* reco_drmujet1_pt20 = (TH1*)demo->Get("reco_drmujet1_pt20"); reco_drmujet1_pt20->SetDirectory(0);
  reco_drmujet1_pt20->Sumw2();
  TH1* hltmu15_drmujet1_pt20 = (TH1*)demo->Get("hltmu15_drmujet1_pt20"); hltmu15_drmujet1_pt20->SetDirectory(0);
  hltmu15_drmujet1_pt20->Sumw2();
  TH1* l1mu7_drmujet1_pt20 = (TH1*)demo->Get("l1mu7_drmujet1_pt20"); l1mu7_drmujet1_pt20->SetDirectory(0);
  l1mu7_drmujet1_pt20->Sumw2();
  TH1* l1andhltmu15_drmujet1_pt20 = (TH1*)demo->Get("l1andhltmu15_drmujet1_pt20"); l1andhltmu15_drmujet1_pt20->SetDirectory(0);
  l1andhltmu15_drmujet1_pt20->Sumw2();

  TH1* reco_iso_pt20 = (TH1*)demo->Get("reco_iso_pt20"); reco_iso_pt20->SetDirectory(0);
  reco_iso_pt20->Sumw2();
  TH1* hltmu15_iso_pt20 = (TH1*)demo->Get("hltmu15_iso_pt20"); hltmu15_iso_pt20->SetDirectory(0);
  hltmu15_iso_pt20->Sumw2();
  TH1* l1mu7_iso_pt20 = (TH1*)demo->Get("l1mu7_iso_pt20"); l1mu7_iso_pt20->SetDirectory(0);
  l1mu7_iso_pt20->Sumw2();
  TH1* l1andhltmu15_iso_pt20 = (TH1*)demo->Get("l1andhltmu15_iso_pt20"); l1andhltmu15_iso_pt20->SetDirectory(0);
  l1andhltmu15_iso_pt20->Sumw2();

  TH1* reco_ptdR1_pt20 = (TH1*)demo->Get("reco_ptdR1_pt20"); reco_ptdR1_pt20->SetDirectory(0);
  reco_ptdR1_pt20->Sumw2();
  TH1* hltmu15_ptdR1_pt20 = (TH1*)demo->Get("hltmu15_ptdR1_pt20"); hltmu15_ptdR1_pt20->SetDirectory(0);
  hltmu15_ptdR1_pt20->Sumw2();
  TH1* l1mu7_ptdR1_pt20 = (TH1*)demo->Get("l1mu7_ptdR1_pt20"); l1mu7_ptdR1_pt20->SetDirectory(0);
  l1mu7_ptdR1_pt20->Sumw2();
  TH1* l1andhltmu15_ptdR1_pt20 = (TH1*)demo->Get("l1andhltmu15_ptdR1_pt20"); l1andhltmu15_ptdR1_pt20->SetDirectory(0);
  l1andhltmu15_ptdR1_pt20->Sumw2();

  _file1->cd();
  TH1* mcreco_eta_20 = (TH1*)demo->Get("reco_eta_20"); mcreco_eta_20->SetDirectory(0);
  mcreco_eta_20->Sumw2();
  TH1* mcl1mu7_eta_20 = (TH1*)demo->Get("l1mu7_eta_20"); mcl1mu7_eta_20->SetDirectory(0);
  mcl1mu7_eta_20->Sumw2();
  TH1* mchltmu15_eta_20 = (TH1*)demo->Get("hltmu15_eta_20"); mchltmu15_eta_20->SetDirectory(0);
  mchltmu15_eta_20->Sumw2();
  TH1* mcl1andhltmu15_eta_20 = (TH1*)demo->Get("l1andhltmu15_eta_20"); mcl1andhltmu15_eta_20->SetDirectory(0);
  mcl1andhltmu15_eta_20->Sumw2();

  TH1* mcreco_pt = (TH1*)demo->Get("reco_pt"); mcreco_pt->SetDirectory(0);
  mcreco_pt->Sumw2();
  TH1* mcl1mu7_pt = (TH1*)demo->Get("l1mu7_pt"); mcl1mu7_pt->SetDirectory(0);
  mcl1mu7_pt->Sumw2();
  TH1* mchltmu15_pt = (TH1*)demo->Get("hltmu15_pt"); mchltmu15_pt->SetDirectory(0);
  mchltmu15_pt->Sumw2();
  TH1* mcl1andhltmu15_pt = (TH1*)demo->Get("l1andhltmu15_pt"); mcl1andhltmu15_pt->SetDirectory(0);
  mcl1andhltmu15_pt->Sumw2();

  TH1* mcreco_pt_b = (TH1*)demo->Get("reco_pt_b"); mcreco_pt_b->SetDirectory(0);
  mcreco_pt_b->Sumw2();
  TH1* mcl1mu7_pt_b = (TH1*)demo->Get("l1mu7_pt_b"); mcl1mu7_pt_b->SetDirectory(0);
  mcl1mu7_pt_b->Sumw2();
  TH1* mchltmu15_pt_b = (TH1*)demo->Get("hltmu15_pt_b"); mchltmu15_pt_b->SetDirectory(0);
  mchltmu15_pt_b->Sumw2();
  TH1* mcl1andhltmu15_pt_b = (TH1*)demo->Get("l1andhltmu15_pt_b"); mcl1andhltmu15_pt_b->SetDirectory(0);
  mcl1andhltmu15_pt_b->Sumw2();

  TH1* mcreco_pt_o = (TH1*)demo->Get("reco_pt_o"); mcreco_pt_o->SetDirectory(0);
  mcreco_pt_o->Sumw2();
  TH1* mcl1mu7_pt_o = (TH1*)demo->Get("l1mu7_pt_o"); mcl1mu7_pt_o->SetDirectory(0);
  mcl1mu7_pt_o->Sumw2();
  TH1* mchltmu15_pt_o = (TH1*)demo->Get("hltmu15_pt_o"); mchltmu15_pt_o->SetDirectory(0);
  mchltmu15_pt_o->Sumw2();
  TH1* mcl1andhltmu15_pt_o = (TH1*)demo->Get("l1andhltmu15_pt_o"); mcl1andhltmu15_pt_o->SetDirectory(0);
  mcl1andhltmu15_pt_o->Sumw2();

  TH1* mcreco_drmujet1_pt20 = (TH1*)demo->Get("reco_drmujet1_pt20"); mcreco_drmujet1_pt20->SetDirectory(0);
  mcreco_drmujet1_pt20->Sumw2();
  TH1* mchltmu15_drmujet1_pt20 = (TH1*)demo->Get("hltmu15_drmujet1_pt20"); mchltmu15_drmujet1_pt20->SetDirectory(0);
  mchltmu15_drmujet1_pt20->Sumw2();
  TH1* mcl1mu7_drmujet1_pt20 = (TH1*)demo->Get("l1mu7_drmujet1_pt20"); mcl1mu7_drmujet1_pt20->SetDirectory(0);
  mcl1mu7_drmujet1_pt20->Sumw2();
  TH1* mcl1andhltmu15_drmujet1_pt20 = (TH1*)demo->Get("l1andhltmu15_drmujet1_pt20"); mcl1andhltmu15_drmujet1_pt20->SetDirectory(0);
  mcl1andhltmu15_drmujet1_pt20->Sumw2();

  TH1* mcreco_iso_pt20 = (TH1*)demo->Get("reco_iso_pt20"); mcreco_iso_pt20->SetDirectory(0);
  mcreco_iso_pt20->Sumw2();
  TH1* mchltmu15_iso_pt20 = (TH1*)demo->Get("hltmu15_iso_pt20"); mchltmu15_iso_pt20->SetDirectory(0);
  mchltmu15_iso_pt20->Sumw2();
  TH1* mcl1mu7_iso_pt20 = (TH1*)demo->Get("l1mu7_iso_pt20"); mcl1mu7_iso_pt20->SetDirectory(0);
  mcl1mu7_iso_pt20->Sumw2();
  TH1* mcl1andhltmu15_iso_pt20 = (TH1*)demo->Get("l1andhltmu15_iso_pt20"); mcl1andhltmu15_iso_pt20->SetDirectory(0);
  mcl1andhltmu15_iso_pt20->Sumw2();

  TH1* mcreco_ptdR1_pt20 = (TH1*)demo->Get("reco_ptdR1_pt20"); mcreco_ptdR1_pt20->SetDirectory(0);
  mcreco_ptdR1_pt20->Sumw2();
  TH1* mchltmu15_ptdR1_pt20 = (TH1*)demo->Get("hltmu15_ptdR1_pt20"); mchltmu15_ptdR1_pt20->SetDirectory(0);
  mchltmu15_ptdR1_pt20->Sumw2();
  TH1* mcl1mu7_ptdR1_pt20 = (TH1*)demo->Get("l1mu7_ptdR1_pt20"); mcl1mu7_ptdR1_pt20->SetDirectory(0);
  mcl1mu7_ptdR1_pt20->Sumw2();
  TH1* mcl1andhltmu15_ptdR1_pt20 = (TH1*)demo->Get("l1andhltmu15_ptdR1_pt20"); mcl1andhltmu15_ptdR1_pt20->SetDirectory(0);
  mcl1andhltmu15_ptdR1_pt20->Sumw2();



  etaeff_l1mu7 = new TGraphAsymmErrors;
  etaeff_l1mu7->BayesDivide(l1mu7_eta_20, reco_eta_20,"");
  etaeff_hltmu15 = new TGraphAsymmErrors;
  etaeff_hltmu15->BayesDivide(hltmu15_eta_20, l1mu7_eta_20,"");
  etaeff_l1andhltmu15 = new TGraphAsymmErrors;
  etaeff_l1andhltmu15->BayesDivide(l1andhltmu15_eta_20, reco_eta_20,"");

  eff_l1mu7 = new TGraphAsymmErrors;
  eff_l1mu7->BayesDivide(l1mu7_pt, reco_pt,"");
  eff_hltmu15 = new TGraphAsymmErrors;
  eff_hltmu15->BayesDivide(hltmu15_pt, l1mu7_pt,"");
  eff_l1andhltmu15 = new TGraphAsymmErrors;
  eff_l1andhltmu15->BayesDivide(l1andhltmu15_pt, reco_pt,"");
 
  eff_l1mu7_b = new TGraphAsymmErrors;
  eff_l1mu7_b->BayesDivide(l1mu7_pt_b, reco_pt_b,"");
  eff_hltmu15_b = new TGraphAsymmErrors;
  eff_hltmu15_b->BayesDivide(hltmu15_pt_b, l1mu7_pt_b,"");
  eff_l1andhltmu15_b = new TGraphAsymmErrors;
  eff_l1andhltmu15_b->BayesDivide(l1andhltmu15_pt_b, reco_pt_b,"");
 
  eff_l1mu7_o = new TGraphAsymmErrors;
  eff_l1mu7_o->BayesDivide(l1mu7_pt_o, reco_pt_o,"");
  eff_hltmu15_o = new TGraphAsymmErrors;
  eff_hltmu15_o->BayesDivide(hltmu15_pt_o, l1mu7_pt_o,"");
  eff_l1andhltmu15_o = new TGraphAsymmErrors;
  eff_l1andhltmu15_o->BayesDivide(l1andhltmu15_pt_o, reco_pt_o,"");
 
  double l1eff = l1mu7_pt->Integral(10,17)/reco_pt->Integral(10,17);
  double dl1eff = sqrt(l1eff*(1-l1eff)/reco_pt->Integral(10,17));
  double l1eff_b = l1mu7_pt_b->Integral(10,17)/reco_pt_b->Integral(10,17);
  double dl1eff_b = sqrt(l1eff_b*(1-l1eff_b)/reco_pt_b->Integral(10,17));
  double l1eff_o = l1mu7_pt_o->Integral(10,17)/reco_pt_o->Integral(10,17);
  double dl1eff_o = sqrt(l1eff_o*(1-l1eff_o)/reco_pt_o->Integral(10,17));

  double hlteff = hltmu15_pt->Integral(10,17)/l1mu7_pt->Integral(10,17);
  double dhlteff = sqrt(hlteff*(1-hlteff)/l1mu7_pt->Integral(10,17));
  double hlteff_b = hltmu15_pt_b->Integral(10,17)/l1mu7_pt_b->Integral(10,17);
  double dhlteff_b = sqrt(hlteff_b*(1-hlteff_b)/l1mu7_pt_b->Integral(10,17));
  double hlteff_o = hltmu15_pt_o->Integral(10,17)/l1mu7_pt_o->Integral(10,17);
  double dhlteff_o = sqrt(hlteff_o*(1-hlteff_o)/l1mu7_pt_o->Integral(10,17));

  double l1hlteff = l1andhltmu15_pt->Integral(10,17)/reco_pt->Integral(10,17);
  double dl1hlteff = sqrt(l1hlteff*(1-l1hlteff)/reco_pt->Integral(10,17));
  double l1hlteff_b = l1andhltmu15_pt_b->Integral(10,17)/reco_pt_b->Integral(10,17);
  double dl1hlteff_b = sqrt(l1hlteff_b*(1-l1hlteff_b)/reco_pt_b->Integral(10,17));
  double l1hlteff_o = l1andhltmu15_pt_o->Integral(10,17)/reco_pt_o->Integral(10,17);
  double dl1hlteff_o = sqrt(l1hlteff_o*(1-l1hlteff_o)/reco_pt_o->Integral(10,17));

  double mcl1eff = mcl1mu7_pt->Integral(10,17)/mcreco_pt->Integral(10,17);
  double mcdl1eff = sqrt(mcl1eff*(1-mcl1eff)/mcreco_pt->Integral(10,17));
  double mcl1eff_b = mcl1mu7_pt_b->Integral(10,17)/mcreco_pt_b->Integral(10,17);
  double mcdl1eff_b = sqrt(mcl1eff_b*(1-mcl1eff_b)/mcreco_pt_b->Integral(10,17));
  double mcl1eff_o = mcl1mu7_pt_o->Integral(10,17)/mcreco_pt_o->Integral(10,17);
  double mcdl1eff_o = sqrt(mcl1eff_o*(1-mcl1eff_o)/mcreco_pt_o->Integral(10,17));

  double mchlteff = mchltmu15_pt->Integral(10,17)/mcl1mu7_pt->Integral(10,17);
  double mcdhlteff = sqrt(mchlteff*(1-mchlteff)/mcl1mu7_pt->Integral(10,17));
  double mchlteff_b = mchltmu15_pt_b->Integral(10,17)/mcl1mu7_pt_b->Integral(10,17);
  double mcdhlteff_b = sqrt(mchlteff_b*(1-mchlteff_b)/mcl1mu7_pt_b->Integral(10,17));
  double mchlteff_o = mchltmu15_pt_o->Integral(10,17)/mcl1mu7_pt_o->Integral(10,17);
  double mcdhlteff_o = sqrt(mchlteff_o*(1-mchlteff_o)/mcl1mu7_pt_o->Integral(10,17));

  double mcl1hlteff = mcl1andhltmu15_pt->Integral(10,17)/mcreco_pt->Integral(10,17);
  double mcdl1hlteff = sqrt(mcl1hlteff*(1-mcl1hlteff)/mcreco_pt->Integral(10,17));
  double mcl1hlteff_b = mcl1andhltmu15_pt_b->Integral(10,17)/mcreco_pt_b->Integral(10,17);
  double mcdl1hlteff_b = sqrt(mcl1hlteff_b*(1-mcl1hlteff_b)/mcreco_pt_b->Integral(10,17));
  double mcl1hlteff_o = mcl1andhltmu15_pt_o->Integral(10,17)/mcreco_pt_o->Integral(10,17);
  double mcdl1hlteff_o = sqrt(mcl1hlteff_o*(1-mcl1hlteff_o)/mcreco_pt_o->Integral(10,17));

  cout<<"                 L1 Eff:                  "<<"HLT Eff:                    "<<"L1+HLT Eff:                  "<<endl;
  cout<<"Total:        "<<l1eff<<" \pm  "<<dl1eff<<"  "<<hlteff<<" \pm "<<dhlteff<<"  "<<l1hlteff<<" \pm "<<dl1hlteff<<endl;
  cout<<"Data/MC-1:    "<<l1eff/mcl1eff-1<<"          "<<hlteff/mchlteff-1<<"         "<<l1hlteff/mcl1hlteff-1<<endl;  
  cout<<"Barrel:       "<<l1eff_b<<" \pm  "<<dl1eff_b<<"  "<<hlteff_b<<" \pm "<<dhlteff_b<<"  "<<l1hlteff_b<<" \pm "<<dl1hlteff_b<<endl;
  cout<<"Data/MC-1:    "<<l1eff_b/mcl1eff_b-1<<"          "<<hlteff_b/mchlteff_b-1<<"         "<<l1hlteff_b/mcl1hlteff_b-1<<endl;  
  cout<<"Endcap:       "<<l1eff_o<<" \pm  "<<dl1eff_o<<"  "<<hlteff_o<<" \pm "<<dhlteff_o<<"  "<<l1hlteff_o<<" \pm "<<dl1hlteff_o<<endl;
  cout<<"Data/MC-1:    "<<l1eff_o/mcl1eff_o-1<<"          "<<hlteff_o/mchlteff_o-1<<"         "<<l1hlteff_o/mcl1hlteff_o-1<<endl;  


  eff_hltmu15_iso_pt20 = new TGraphAsymmErrors;
  eff_hltmu15_iso_pt20->BayesDivide(hltmu15_iso_pt20, l1mu7_iso_pt20,"");
  eff_l1mu7_iso_pt20 = new TGraphAsymmErrors;
  eff_l1mu7_iso_pt20->BayesDivide(l1mu7_iso_pt20, reco_iso_pt20,"");
  eff_l1andhltmu15_iso_pt20 = new TGraphAsymmErrors;
  eff_l1andhltmu15_iso_pt20->BayesDivide(l1andhltmu15_iso_pt20, reco_iso_pt20,"");
  
  eff_hltmu15_drmujet1_pt20 = new TGraphAsymmErrors;
  eff_hltmu15_drmujet1_pt20->BayesDivide(hltmu15_drmujet1_pt20, l1mu7_drmujet1_pt20,"");
  eff_l1mu7_drmujet1_pt20 = new TGraphAsymmErrors;
  eff_l1mu7_drmujet1_pt20->BayesDivide(l1mu7_drmujet1_pt20, reco_drmujet1_pt20,"");
  eff_l1andhltmu15_drmujet1_pt20 = new TGraphAsymmErrors;
  eff_l1andhltmu15_drmujet1_pt20->BayesDivide(l1andhltmu15_drmujet1_pt20, reco_drmujet1_pt20,"");

  eff_hltmu15_ptdR1_pt20 = new TGraphAsymmErrors;
  eff_hltmu15_ptdR1_pt20->BayesDivide(hltmu15_ptdR1_pt20, l1mu7_ptdR1_pt20,"");
  eff_l1mu7_ptdR1_pt20 = new TGraphAsymmErrors;
  eff_l1mu7_ptdR1_pt20->BayesDivide(l1mu7_ptdR1_pt20, reco_ptdR1_pt20,"");
  eff_l1andhltmu15_ptdR1_pt20 = new TGraphAsymmErrors;
  eff_l1andhltmu15_ptdR1_pt20->BayesDivide(l1andhltmu15_ptdR1_pt20, reco_ptdR1_pt20,"");


  mceff_l1mu7 = new TGraphAsymmErrors;
  mceff_l1mu7->BayesDivide(mcl1mu7_pt, mcreco_pt,"");
  mceff_hltmu15 = new TGraphAsymmErrors;
  mceff_hltmu15->BayesDivide(mchltmu15_pt, mcl1mu7_pt,"");
  mceff_l1andhltmu15 = new TGraphAsymmErrors;
  mceff_l1andhltmu15->BayesDivide(mcl1andhltmu15_pt, mcreco_pt,"");
 
  etamceff_l1mu7 = new TGraphAsymmErrors;
  etamceff_l1mu7->BayesDivide(mcl1mu7_eta_20, mcreco_eta_20,"");
  etamceff_hltmu15 = new TGraphAsymmErrors;
  etamceff_hltmu15->BayesDivide(mchltmu15_eta_20, mcl1mu7_eta_20,"");
  etamceff_l1andhltmu15 = new TGraphAsymmErrors;
  etamceff_l1andhltmu15->BayesDivide(mcl1andhltmu15_eta_20, mcreco_eta_20,"");
 
  mceff_l1mu7_b = new TGraphAsymmErrors;
  mceff_l1mu7_b->BayesDivide(mcl1mu7_pt_b, mcreco_pt_b,"");
  mceff_hltmu15_b = new TGraphAsymmErrors;
  mceff_hltmu15_b->BayesDivide(mchltmu15_pt_b, mcl1mu7_pt_b,"");
  mceff_l1andhltmu15_b = new TGraphAsymmErrors;
  mceff_l1andhltmu15_b->BayesDivide(mcl1andhltmu15_pt_b, mcreco_pt_b,"");
 
  mceff_l1mu7_o = new TGraphAsymmErrors;
  mceff_l1mu7_o->BayesDivide(mcl1mu7_pt_o, mcreco_pt_o,"");
  mceff_hltmu15_o = new TGraphAsymmErrors;
  mceff_hltmu15_o->BayesDivide(mchltmu15_pt_o, mcl1mu7_pt_o,"");
  mceff_l1andhltmu15_o = new TGraphAsymmErrors;
  mceff_l1andhltmu15_o->BayesDivide(mcl1andhltmu15_pt_o, mcreco_pt_o,"");


  mceff_hltmu15_iso_pt20 = new TGraphAsymmErrors;
  mceff_hltmu15_iso_pt20->BayesDivide(mchltmu15_iso_pt20, mcl1mu7_iso_pt20,"");
  mceff_l1mu7_iso_pt20 = new TGraphAsymmErrors;
  mceff_l1mu7_iso_pt20->BayesDivide(mcl1mu7_iso_pt20, mcreco_iso_pt20,"");
  mceff_l1andhltmu15_iso_pt20 = new TGraphAsymmErrors;
  mceff_l1andhltmu15_iso_pt20->BayesDivide(mcl1andhltmu15_iso_pt20, mcreco_iso_pt20,"");
  
  mceff_hltmu15_drmujet1_pt20 = new TGraphAsymmErrors;
  mceff_hltmu15_drmujet1_pt20->BayesDivide(mchltmu15_drmujet1_pt20, mcl1mu7_drmujet1_pt20,"");
  mceff_l1mu7_drmujet1_pt20 = new TGraphAsymmErrors;
  mceff_l1mu7_drmujet1_pt20->BayesDivide(mcl1mu7_drmujet1_pt20, mcreco_drmujet1_pt20,"");
  mceff_l1andhltmu15_drmujet1_pt20 = new TGraphAsymmErrors;
  mceff_l1andhltmu15_drmujet1_pt20->BayesDivide(mcl1andhltmu15_drmujet1_pt20, mcreco_drmujet1_pt20,"");

  mceff_hltmu15_ptdR1_pt20 = new TGraphAsymmErrors;
  mceff_hltmu15_ptdR1_pt20->BayesDivide(mchltmu15_ptdR1_pt20, mcl1mu7_ptdR1_pt20,"");
  mceff_l1mu7_ptdR1_pt20 = new TGraphAsymmErrors;
  mceff_l1mu7_ptdR1_pt20->BayesDivide(mcl1mu7_ptdR1_pt20, mcreco_ptdR1_pt20,"");
  mceff_l1andhltmu15_ptdR1_pt20 = new TGraphAsymmErrors;
  mceff_l1andhltmu15_ptdR1_pt20->BayesDivide(mcl1andhltmu15_ptdR1_pt20, mcreco_ptdR1_pt20,"");



  TF1 *f1 = new TF1("f1","pol0",20.0,460.0);
  TF1 *f2 = new TF1("f2","pol0",0.0,4.0);
  TF1 *f3 = new TF1("f3","pol1",0.0,4.0);

/*
  TCanvas *c1 = new TCanvas("c1","c1",600,600);
  c1->cd();
  eff_l1mu7_ptdR1_pt20->SetMinimum(0.0);
  eff_l1mu7_ptdR1_pt20->SetMaximum(1.4);
  eff_l1mu7_ptdR1_pt20->Draw("AP");
  eff_l1mu7_ptdR1_pt20->GetXaxis()->SetTitle("#Delta R(#mu,jet) #times 10^{3} / p_{T}^{jet}");
  eff_l1mu7_ptdR1_pt20->GetYaxis()->SetTitle("Efficiency");
  eff_hltmu15_ptdR1_pt20->SetLineColor(4);
  eff_hltmu15_ptdR1_pt20->SetMarkerColor(4);
  eff_hltmu15_ptdR1_pt20->Draw("Psame");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1, p_{T}^{#mu}  20 GeV");
  legend->AddEntry(eff_l1mu7_ptdR1_pt20, "L1SingleMu7|RECO", "lp");
  legend->AddEntry(eff_hltmu15_ptdR1_pt20,"HLT_Mu15|L1SingleMu7","lp");
  legend->Draw("same"); 
  TPaveText *pt = new TPaveText(0.0,1.4,0.8.,1.1);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  pt->Draw("same");   
 
  TCanvas *c2 = new TCanvas("c2","c2",600,600);
  c2->cd();
  eff_l1mu7_drmujet1_pt20->SetMinimum(0.0);
  eff_l1mu7_drmujet1_pt20->SetMaximum(1.4);
  eff_l1mu7_drmujet1_pt20->Draw("AP");
  eff_l1mu7_drmujet1_pt20->GetXaxis()->SetTitle("#Delta R(#mu,jet)");
  eff_l1mu7_drmujet1_pt20->GetYaxis()->SetTitle("Efficiency");
  eff_hltmu15_drmujet1_pt20->SetLineColor(4);
  eff_hltmu15_drmujet1_pt20->SetMarkerColor(4);
  eff_hltmu15_drmujet1_pt20->Draw("Psame");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1, p_{T}^{#mu} > 20 GeV");
  legend->AddEntry(eff_l1mu7_drmujet1_pt20, "L1SingleMu7|RECO", "lp");
  legend->AddEntry(eff_hltmu15_drmujet1_pt20,"HLT_Mu15|L1SingleMu7","lp");
  legend->Draw("same"); 
  TPaveText *pt = new TPaveText(0.0,1.4,0.5,1.1);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  pt->Draw("same");   

  TCanvas *c3 = new TCanvas("c3","c3",600,600);
  c3->cd();
  eff_l1mu7_iso_pt20->SetMinimum(0.0);
  eff_l1mu7_iso_pt20->SetMaximum(1.4);
  eff_l1mu7_iso_pt20->Draw("AP");
  eff_l1mu7_iso_pt20->GetXaxis()->SetTitle("Isolation");
  eff_l1mu7_iso_pt20->GetYaxis()->SetTitle("Efficiency");
  eff_hltmu15_iso_pt20->SetLineColor(4);
  eff_hltmu15_iso_pt20->SetMarkerColor(4);
  eff_hltmu15_iso_pt20->Draw("Psame");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1,  p_{T}^{#mu} > 20 GeV");
  legend->AddEntry(eff_l1mu7_iso_pt20, "L1SingleMu7|RECO","lp");
  legend->AddEntry(eff_hltmu15_iso_pt20," HLT_Mu15|L1SingleMu7","lp");
  legend->Draw("same"); 
  TPaveText *pt = new TPaveText(0.0,1.4,2.0,1.1);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  pt->Draw("same");   
*/

  TCanvas *c1 = new TCanvas("c1","c1",600,600);
  c1->cd();
  eff_l1andhltmu15_ptdR1_pt20->SetMinimum(0.0);
  eff_l1andhltmu15_ptdR1_pt20->SetMaximum(1.4);
  eff_l1andhltmu15_ptdR1_pt20->Draw("AP");
  eff_l1andhltmu15_ptdR1_pt20->GetXaxis()->SetTitle("#Delta R(#mu,jet) #times 10^{3} / p_{T}^{jet}");
  eff_l1andhltmu15_ptdR1_pt20->GetYaxis()->SetTitle("Eff(HLT_Mu15|REC0)");
  mceff_l1andhltmu15_ptdR1_pt20->SetLineColor(2);
  mceff_l1andhltmu15_ptdR1_pt20->SetFillColor(2);
  mceff_l1andhltmu15_ptdR1_pt20->SetFillStyle(3001);
  mceff_l1andhltmu15_ptdR1_pt20->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1, p_{T}^{#mu} >  20 GeV");
  legend->AddEntry(eff_l1andhltmu15_ptdR1_pt20, "Data", "lp");
  legend->AddEntry(mceff_l1andhltmu15_ptdR1_pt20, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same"); 
  TPaveText *pt = new TPaveText(0.0,1.4,0.8.,1.1);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   
 
  TCanvas *c2 = new TCanvas("c2","c2",600,600);
  c2->cd();
  eff_l1andhltmu15_drmujet1_pt20->SetMinimum(0.0);
  eff_l1andhltmu15_drmujet1_pt20->SetMaximum(1.4);
  eff_l1andhltmu15_drmujet1_pt20->Draw("AP");
  eff_l1andhltmu15_drmujet1_pt20->GetXaxis()->SetTitle("#Delta R(#mu,jet)");
  eff_l1andhltmu15_drmujet1_pt20->GetYaxis()->SetTitle("Eff(HLT_Mu15|RECO)");
  mceff_l1andhltmu15_drmujet1_pt20->SetLineColor(2);
  mceff_l1andhltmu15_drmujet1_pt20->SetFillColor(2);
  mceff_l1andhltmu15_drmujet1_pt20->SetFillStyle(3001);
  mceff_l1andhltmu15_drmujet1_pt20->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1, p_{T}^{#mu} > 20 GeV");
  legend->AddEntry(eff_l1andhltmu15_drmujet1_pt20,"Data","lp");
  legend->AddEntry(mceff_l1andhltmu15_drmujet1_pt20, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same"); 
  TPaveText *pt = new TPaveText(0.0,1.4,0.5,1.1);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   

  TCanvas *c3 = new TCanvas("c3","c3",600,600);
  c3->cd();
  eff_l1andhltmu15_iso_pt20->SetMinimum(0.0);
  eff_l1andhltmu15_iso_pt20->SetMaximum(1.4);
  eff_l1andhltmu15_iso_pt20->Draw("AP");
  eff_l1andhltmu15_iso_pt20->GetXaxis()->SetTitle("Isolation");
  eff_l1andhltmu15_iso_pt20->GetYaxis()->SetTitle("Eff(HLT_Mu15|RECO)");
  mceff_l1andhltmu15_iso_pt20->SetLineColor(2);
  mceff_l1andhltmu15_iso_pt20->SetFillColor(2);
  mceff_l1andhltmu15_iso_pt20->SetFillStyle(3001);
  mceff_l1andhltmu15_iso_pt20->Draw("e2same");
  eff_l1andhltmu15_iso_pt20->Fit("f2", "QRME");
  eff_l1andhltmu15_iso_pt20->Fit("f3", "QRME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1,  p_{T}^{#mu} > 20 GeV");
  legend->AddEntry(eff_l1andhltmu15_iso_pt20,"Data","lp");
  legend->AddEntry(mceff_l1andhltmu15_iso_pt20, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same"); 
  TPaveText *pt = new TPaveText(0.0,1.4,2.0,1.1);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   

 
  TCanvas *c4 = new TCanvas("c4","c4",600,600);
  c4->Divide(1,3);
  c4->cd(1);
  eff_l1mu7->SetMarkerStyle(20);
  eff_l1mu7->SetLineColor(1);
  eff_l1mu7->SetMarkerColor(1);
  eff_l1mu7->SetMinimum(0.0);
  eff_l1mu7->SetMaximum(1.4);
  eff_l1mu7->Draw("AP");
  eff_l1mu7->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  cout<<"L1 Overall Data: "<<endl;
  eff_l1mu7->GetYaxis()->SetTitle("L1 Efficiency");
  TFitResultPtr r = eff_l1mu7->Fit("f1", "NSRME");
  mceff_l1mu7->SetLineColor(2);
  mceff_l1mu7->SetFillColor(2);
  mceff_l1mu7->SetFillStyle(3001);
  mceff_l1mu7->Draw("e2same");
  cout<<"L1 Overall MC :"<<endl;
  TFitResultPtr r = mceff_l1mu7->Fit("f1", "NSRME");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1mu7,"Data","lp");
  legend->AddEntry(mceff_l1mu7, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  TPaveText *pt = new TPaveText(0.,1.0,150.,.8);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   
  c4->cd(2);
  eff_hltmu15->SetMarkerStyle(20);
  eff_hltmu15->SetLineColor(1);
  eff_hltmu15->SetMarkerColor(1);
  eff_hltmu15->SetMinimum(0.0);
  eff_hltmu15->SetMaximum(1.4);
  eff_hltmu15->Draw("AP");
  cout<<"HLT Overall Data"<<endl;
  TFitResultPtr r = eff_hltmu15->Fit("f1", "NSRME");
  mceff_hltmu15->SetLineColor(2);
  mceff_hltmu15->SetFillColor(2);
  mceff_hltmu15->SetFillStyle(3001);
  cout<<"HLT Overall MC"<<endl;
  TFitResultPtr r = mceff_hltmu15->Fit("f1", "NSRME");
  mceff_hltmu15->Draw("e2same");
  eff_hltmu15->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_hltmu15->GetYaxis()->SetTitle("HLT Efficiency");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_hltmu15,"Data","lp");
  legend->AddEntry(mceff_hltmu15, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  c4->cd(3);
  eff_l1andhltmu15->SetMarkerStyle(20);
  eff_l1andhltmu15->SetLineColor(1);
  eff_l1andhltmu15->SetMarkerColor(1);
  eff_l1andhltmu15->SetMinimum(0.0);
  eff_l1andhltmu15->SetMaximum(1.4);
  eff_l1andhltmu15->Draw("AP");
  cout<<"L1+HLT Overall Data"<<endl;
  TFitResultPtr r =  eff_l1andhltmu15->Fit("f1", "NSRME");
  mceff_l1andhltmu15->SetLineColor(2);
  mceff_l1andhltmu15->SetFillColor(2);
  mceff_l1andhltmu15->SetFillStyle(3001);
  mceff_l1andhltmu15->Draw("e2same");
  cout<<"L1+HLT Overall MC"<<endl;
  TFitResultPtr r =  mceff_l1andhltmu15->Fit("f1", "NSRME");
  eff_l1andhltmu15->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15->GetYaxis()->SetTitle("L1+HLT Efficiency");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu15,"Data","lp");
  legend->AddEntry(mceff_l1andhltmu15, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");


  TCanvas *c5 = new TCanvas("c5","c5",600,600);
  c5->Divide(1,3);
  c5->cd(1);
  eff_l1mu7_b->SetMarkerStyle(20);
  eff_l1mu7_b->SetLineColor(1);
  eff_l1mu7_b->SetMarkerColor(1);
  eff_l1mu7_b->SetMinimum(0.0);
  eff_l1mu7_b->SetMaximum(1.1);
  eff_l1mu7_b->Draw("AP");
  eff_l1mu7_b->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1mu7_b->GetYaxis()->SetTitle("L1 Efficiency");
  cout<<"L1 Barrel Data:"<<endl;
  TFitResultPtr r = eff_l1mu7_b->Fit("f1", "NSRME");
  mceff_l1mu7_b->SetLineColor(2);
  mceff_l1mu7_b->SetFillColor(2);
  mceff_l1mu7_b->SetFillStyle(3001);
  cout<<"L1 Barrel MC:"<<endl;
  TFitResultPtr r = mceff_l1mu7_b->Fit("f1", "NSRME");
  mceff_l1mu7_b->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<0.9");
  legend->AddEntry(eff_l1mu7_b,"Data","lp");
  legend->AddEntry(mceff_l1mu7_b, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  TPaveText *pt = new TPaveText(0.,1.0,150.,.8);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  ////pt->Draw("same");   
  c5->cd(2);
  eff_hltmu15_b->SetMarkerStyle(20);
  eff_hltmu15_b->SetLineColor(1);
  eff_hltmu15_b->SetMarkerColor(1);
  eff_hltmu15_b->SetMinimum(0.0);
  eff_hltmu15_b->SetMaximum(1.1);
  eff_hltmu15_b->Draw("AP");
  cout<<"HLT Barrel Data: "<<endl;
  TFitResultPtr r = eff_hltmu15_b->Fit("f1", "NSRME");
  eff_hltmu15_b->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_hltmu15_b->GetYaxis()->SetTitle("HLT Efficiency");
  mceff_hltmu15_b->SetLineColor(2);
  mceff_hltmu15_b->SetFillColor(2);
  mceff_hltmu15_b->SetFillStyle(3001);
  cout<<"HLT Barrel MC:"<<endl;
  TFitResultPtr r = mceff_hltmu15_b->Fit("f1", "NSRME");
  mceff_hltmu15_b->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<0.9");
  legend->AddEntry(eff_hltmu15_b,"Data","lp");
  legend->AddEntry(mceff_hltmu15_b, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  c5->cd(3);
  eff_l1andhltmu15_b->SetMarkerStyle(20);
  eff_l1andhltmu15_b->SetLineColor(1);
  eff_l1andhltmu15_b->SetMarkerColor(1);
  eff_l1andhltmu15_b->SetMinimum(0.0);
  eff_l1andhltmu15_b->SetMaximum(1.1);
  eff_l1andhltmu15_b->Draw("AP");
  cout<<"L1+HLT Barrel Data:"<<endl;
  TFitResultPtr r = eff_l1andhltmu15_b->Fit("f1", "NSRME");
  eff_l1andhltmu15_b->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15_b->GetYaxis()->SetTitle("L1+HLT Efficiency");
  mceff_l1andhltmu15_b->SetLineColor(2);
  mceff_l1andhltmu15_b->SetFillColor(2);
  mceff_l1andhltmu15_b->SetFillStyle(3001);
  cout<<"L1+HLT Barrel MC:"<<endl;
  TFitResultPtr r = mceff_l1andhltmu15_b->Fit("f1", "NSRME");
  mceff_l1andhltmu15_b->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta|<0.9");
  legend->AddEntry(eff_l1andhltmu15_b,"Data","lp");
  legend->AddEntry(mceff_l1andhltmu15_b, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");

  TCanvas *c6 = new TCanvas("c6","c6",600,600);
  c6->Divide(1,3);
  c6->cd(1);
  eff_l1mu7_o->SetMarkerStyle(20);
  eff_l1mu7_o->SetLineColor(1);
  eff_l1mu7_o->SetMarkerColor(1);
  eff_l1mu7_o->SetMinimum(0.0);
  eff_l1mu7_o->SetMaximum(1.1);
  eff_l1mu7_o->Draw("AP");
  eff_l1mu7_o->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1mu7_o->GetYaxis()->SetTitle("L1 Efficiency");
  cout<<"L1 Endcap Data:"<<endl;
  TFitResultPtr r = eff_l1mu7_o->Fit("f1", "NSRME");
  mceff_l1mu7_o->SetLineColor(2);
  mceff_l1mu7_o->SetFillColor(2);
  mceff_l1mu7_o->SetFillStyle(3001);
  cout<<"L1 Endcap MC:"<<endl;
  TFitResultPtr r = mceff_l1mu7_o->Fit("f1", "NSRME");
  mceff_l1mu7_o->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"0.9<|#eta|<2.1");
  legend->AddEntry(eff_l1mu7_o,"Data","lp");
  legend->AddEntry(mceff_l1mu7_o, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  TPaveText *pt = new TPaveText(0.,1.0,150.,.8);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   
  c6->cd(2);
  eff_hltmu15_o->SetMarkerStyle(20);
  eff_hltmu15_o->SetLineColor(1);
  eff_hltmu15_o->SetMarkerColor(1);
  eff_hltmu15_o->SetMinimum(0.0);
  eff_hltmu15_o->SetMaximum(1.1);
  eff_hltmu15_o->Draw("AP");
  cout<<"HLT Endcap Data:"<<endl;
  TFitResultPtr r = eff_hltmu15_o->Fit("f1", "NSRME"); 
  eff_hltmu15_o->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_hltmu15_o->GetYaxis()->SetTitle("HLT Efficiency");
  mceff_hltmu15_o->SetLineColor(2);
  mceff_hltmu15_o->SetFillColor(2);
  mceff_hltmu15_o->SetFillStyle(3001);
  cout<<"HLT Endcap MC:"<<endl;
  TFitResultPtr r = mceff_hltmu15_o->Fit("f1", "NSRME");
  mceff_hltmu15_o->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"0.9<|#eta|<2.1");
  legend->AddEntry(eff_hltmu15_o,"Data","lp");
  legend->AddEntry(mceff_hltmu15_o, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  c6->cd(3);
  eff_l1andhltmu15_o->SetMarkerStyle(20);
  eff_l1andhltmu15_o->SetLineColor(1);
  eff_l1andhltmu15_o->SetMarkerColor(1);
  eff_l1andhltmu15_o->SetMinimum(0.0);
  eff_l1andhltmu15_o->SetMaximum(1.1);
  eff_l1andhltmu15_o->Draw("AP");
  cout<<"L1+HLT Endcap Data:"<<endl;
  TFitResultPtr r = eff_l1andhltmu15_o->Fit("f1", "NSRME"); 
  eff_l1andhltmu15_o->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV/c]");
  eff_l1andhltmu15_o->GetYaxis()->SetTitle("L1+HLT Efficiency");
  mceff_l1andhltmu15_o->SetLineColor(2);
  mceff_l1andhltmu15_o->SetFillColor(2);
  mceff_l1andhltmu15_o->SetFillStyle(3001);
  cout<<"L1+HLT Endcap MC:"<<endl;
  TFitResultPtr r = mceff_l1andhltmu15_o->Fit("f1", "NSRME");
  mceff_l1andhltmu15_o->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"0.9<|#eta|<2.1");
  legend->AddEntry(eff_l1andhltmu15_o,"Data","lp");
  legend->AddEntry(mceff_l1andhltmu15_o, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");


  TCanvas *c7 = new TCanvas("c7","c7",600,600);
  c7->Divide(1,3);
  c7->cd(1);
  etaeff_l1mu7->SetMarkerStyle(20);
  etaeff_l1mu7->SetLineColor(1);
  etaeff_l1mu7->SetMarkerColor(1);
  etaeff_l1mu7->SetMinimum(0.0);
  etaeff_l1mu7->SetMaximum(1.1);
  etaeff_l1mu7->Draw("AP");
  etaeff_l1mu7->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_l1mu7->GetYaxis()->SetTitle("L1 Efficiency");
  etamceff_l1mu7->SetLineColor(2);
  etamceff_l1mu7->SetFillColor(2);
  etamceff_l1mu7->SetFillStyle(3001);
  etamceff_l1mu7->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"p_{T} > 20 GeV");
  legend->AddEntry(etaeff_l1mu7,"Data","lp");
  legend->AddEntry(etamceff_l1mu7, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  TPaveText *pt = new TPaveText(-2.,1.0,0.,.8);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   
  c7->cd(2);
  etaeff_hltmu15->SetMarkerStyle(20);
  etaeff_hltmu15->SetLineColor(1);
  etaeff_hltmu15->SetMarkerColor(1);
  etaeff_hltmu15->SetMinimum(0.0);
  etaeff_hltmu15->SetMaximum(1.1);
  etaeff_hltmu15->Draw("AP");
  etaeff_hltmu15->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_hltmu15->GetYaxis()->SetTitle("HLT Efficiency");
  etamceff_hltmu15->SetLineColor(2);
  etamceff_hltmu15->SetFillColor(2);
  etamceff_hltmu15->SetFillStyle(3001);
  etamceff_hltmu15->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"p_{T} > 20 GeV");
  legend->AddEntry(etaeff_hltmu15,"Data","lp");
  legend->AddEntry(etamceff_hltmu15, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  c7->cd(3);
  etaeff_l1andhltmu15->SetMarkerStyle(20);
  etaeff_l1andhltmu15->SetLineColor(1);
  etaeff_l1andhltmu15->SetMarkerColor(1);
  etaeff_l1andhltmu15->SetMinimum(0.0);
  etaeff_l1andhltmu15->SetMaximum(1.1);
  etaeff_l1andhltmu15->Draw("AP");
  etaeff_l1andhltmu15->GetXaxis()->SetTitle("#eta^{RECO}");
  etaeff_l1andhltmu15->GetYaxis()->SetTitle("L1+HLT Efficiency");
  etamceff_l1andhltmu15->SetLineColor(2);
  etamceff_l1andhltmu15->SetFillColor(2);
  etamceff_l1andhltmu15->SetFillStyle(3001);
  etamceff_l1andhltmu15->Draw("e2same");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"p_{T} > 20 GeV");
  legend->AddEntry(etaeff_l1andhltmu15,"Data","lp");
  legend->AddEntry(etamceff_l1andhltmu15, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");


  TCanvas *c8 = new TCanvas("c8","c8",600,600);
  c8->Divide(2,1);
  c8->cd(1);
  reco_eta_20->SetMarkerStyle(20);
  reco_eta_20->SetLineColor(1);
  reco_eta_20->SetMarkerColor(1);
  reco_eta_20->Scale(1/reco_eta_20->Integral());
  reco_eta_20->Draw();
  reco_eta_20->GetXaxis()->SetTitle("#eta^{RECO}");
  mcreco_eta_20->SetLineColor(2);
  mcreco_eta_20->SetFillColor(2);
  mcreco_eta_20->SetFillStyle(3001);
  mcreco_eta_20->Scale(1/mcreco_eta_20->Integral());
  etamceff_l1mu7->Draw("histsame");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"p_{T} > 20 GeV");
  legend->AddEntry(reco_eta_20,"Data","lp");
  legend->AddEntry(mcreco_eta_20, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");
  TPaveText *pt = new TPaveText(-2.,1.0,0.,.8);
  pt->AddText("CMS Preliminary 2010");
  pt->AddText("#sqrt{s} = 7 TeV");
  //pt->Draw("same");   
  c8->cd(2);
  reco_pt->SetMarkerStyle(20);
  reco_pt->SetLineColor(1);
  reco_pt->SetMarkerColor(1);
  reco_pt->Scale(1/reco_pt->Integral());
  reco_pt->Draw();
  reco_pt->GetXaxis()->SetTitle("p_{T}^{RECO} [GeV]");
  mcreco_pt->SetLineColor(2);
  mcreco_pt->SetFillColor(2);
  mcreco_pt->SetFillStyle(3001);
  mcreco_pt->Scale(1/mcreco_pt->Integral());
  mcreco_pt->Draw("histsame");
  TLegend *legend = new TLegend(0.4,0.2,0.55,0.4,"|#eta| < 2.1");
  legend->AddEntry(reco_pt,"Data","lp");
  legend->AddEntry(mcreco_pt, "MC (W #rightarrow #mu #nu)", "f");
  legend->Draw("same");

}
