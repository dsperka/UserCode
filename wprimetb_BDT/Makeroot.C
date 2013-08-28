#include <TROOT.h>
#include <TCut.h>
#include <TMath.h>
#include <TChain.h>
#include <TFile.h>
#include <TList.h>
#include <TSystemFile.h>
#include <TSystemDirectory.h>
#include <TRint.h>
#include <TROOT.h>
#include <TTree.h>
#include <TChain.h>
#include <iostream>

//#include "cuts20percent.h"
#include "cuts.h"

void Makeroot () {
  
  TString outfile;
  bool ifsys = true;

  TString indir = "/uscms_data/d2/dsperka/8TeV/Samples/29May_All/";
  //TString indir = "/home/dsperka/CMS/Wprimetb/8TeV/plots_53x/";
  TString chan[2] = {"el", "mu"};
  
  //for (int j=0; j<1; j++) { // electron channel
  for (int j=1; j<2; j++) { // muon channel
  //for (int j=0; j<2; j++) { // both channels


    TString channel = chan[j];
     
    if (j==0) std::cout << "****Electron Channel*****" << std::endl;
    if (j==1) std::cout << "****Muon Channel*****" << std::endl;

    std::cout << " setting TChains... " << std::endl;

    TChain ch_data("ljmet");

    TChain ch_ttbar("ljmet");
    TChain ch_ttbar_JESUP("ljmet"); 
    TChain ch_ttbar_JESDOWN("ljmet"); 
    TChain ch_ttbar_BTAGUP("ljmet"); 
    TChain ch_ttbar_BTAGDOWN("ljmet"); 
    TChain ch_ttbar_JERUP("ljmet"); 
    TChain ch_ttbar_JERDOWN("ljmet"); 

    TChain ch_w1jets("ljmet");
    TChain ch_w1jets_JESUP("ljmet"); 
    TChain ch_w1jets_JESDOWN("ljmet"); 
    TChain ch_w1jets_BTAGUP("ljmet"); 
    TChain ch_w1jets_BTAGDOWN("ljmet"); 
    TChain ch_w1jets_JERUP("ljmet"); 
    TChain ch_w1jets_JERDOWN("ljmet"); 

    TChain ch_w2jets("ljmet");
    TChain ch_w2jets_JESUP("ljmet"); 
    TChain ch_w2jets_JESDOWN("ljmet"); 
    TChain ch_w2jets_BTAGUP("ljmet"); 
    TChain ch_w2jets_BTAGDOWN("ljmet"); 
    TChain ch_w2jets_JERUP("ljmet"); 
    TChain ch_w2jets_JERDOWN("ljmet"); 

    TChain ch_w3jets("ljmet");
    TChain ch_w3jets_JESUP("ljmet"); 
    TChain ch_w3jets_JESDOWN("ljmet"); 
    TChain ch_w3jets_BTAGUP("ljmet"); 
    TChain ch_w3jets_BTAGDOWN("ljmet"); 
    TChain ch_w3jets_JERUP("ljmet"); 
    TChain ch_w3jets_JERDOWN("ljmet"); 

    TChain ch_w4jets("ljmet");
    TChain ch_w4jets_JESUP("ljmet"); 
    TChain ch_w4jets_JESDOWN("ljmet"); 
    TChain ch_w4jets_BTAGUP("ljmet"); 
    TChain ch_w4jets_BTAGDOWN("ljmet"); 
    TChain ch_w4jets_JERUP("ljmet"); 
    TChain ch_w4jets_JERDOWN("ljmet"); 

    TChain ch_s("ljmet");
    TChain ch_s_JESUP("ljmet"); 
    TChain ch_s_JESDOWN("ljmet"); 
    TChain ch_s_BTAGUP("ljmet"); 
    TChain ch_s_BTAGDOWN("ljmet"); 
    TChain ch_s_JERUP("ljmet"); 
    TChain ch_s_JERDOWN("ljmet"); 

    TChain ch_bs("ljmet");
    TChain ch_bs_JESUP("ljmet"); 
    TChain ch_bs_JESDOWN("ljmet"); 
    TChain ch_bs_BTAGUP("ljmet"); 
    TChain ch_bs_BTAGDOWN("ljmet"); 
    TChain ch_bs_JERUP("ljmet"); 
    TChain ch_bs_JERDOWN("ljmet"); 

    TChain ch_t("ljmet");
    TChain ch_t_JESUP("ljmet"); 
    TChain ch_t_JESDOWN("ljmet"); 
    TChain ch_t_BTAGUP("ljmet"); 
    TChain ch_t_BTAGDOWN("ljmet"); 
    TChain ch_t_JERUP("ljmet"); 
    TChain ch_t_JERDOWN("ljmet"); 

    TChain ch_bt("ljmet");
    TChain ch_bt_JESUP("ljmet"); 
    TChain ch_bt_JESDOWN("ljmet"); 
    TChain ch_bt_BTAGUP("ljmet"); 
    TChain ch_bt_BTAGDOWN("ljmet"); 
    TChain ch_bt_JERUP("ljmet"); 
    TChain ch_bt_JERDOWN("ljmet"); 

    TChain ch_tw("ljmet");
    TChain ch_tw_JESUP("ljmet"); 
    TChain ch_tw_JESDOWN("ljmet"); 
    TChain ch_tw_BTAGUP("ljmet"); 
    TChain ch_tw_BTAGDOWN("ljmet"); 
    TChain ch_tw_JERUP("ljmet"); 
    TChain ch_tw_JERDOWN("ljmet"); 

    TChain ch_btw("ljmet");
    TChain ch_btw_JESUP("ljmet"); 
    TChain ch_btw_JESDOWN("ljmet"); 
    TChain ch_btw_BTAGUP("ljmet"); 
    TChain ch_btw_BTAGDOWN("ljmet"); 
    TChain ch_btw_JERUP("ljmet"); 
    TChain ch_btw_JERDOWN("ljmet"); 

    TChain ch_zjets("ljmet");
    TChain ch_zjets_JESUP("ljmet"); 
    TChain ch_zjets_JESDOWN("ljmet"); 
    TChain ch_zjets_BTAGUP("ljmet"); 
    TChain ch_zjets_BTAGDOWN("ljmet"); 
    TChain ch_zjets_JERUP("ljmet"); 
    TChain ch_zjets_JERDOWN("ljmet"); 

    TChain ch_ww("ljmet");
    TChain ch_ww_JESUP("ljmet"); 
    TChain ch_ww_JESDOWN("ljmet"); 
    TChain ch_ww_BTAGUP("ljmet"); 
    TChain ch_ww_BTAGDOWN("ljmet"); 
    TChain ch_ww_JERUP("ljmet"); 
    TChain ch_ww_JERDOWN("ljmet");

    TChain ch_qcd80to170("ljmet");
    TChain ch_qcd80to170_JESUP("ljmet"); 
    TChain ch_qcd80to170_JESDOWN("ljmet"); 
    TChain ch_qcd80to170_BTAGUP("ljmet"); 
    TChain ch_qcd80to170_BTAGDOWN("ljmet"); 
    TChain ch_qcd80to170_JERUP("ljmet"); 
    TChain ch_qcd80to170_JERDOWN("ljmet");
   
    TChain ch_qcd170to250("ljmet");
    TChain ch_qcd170to250_JESUP("ljmet"); 
    TChain ch_qcd170to250_JESDOWN("ljmet"); 
    TChain ch_qcd170to250_BTAGUP("ljmet"); 
    TChain ch_qcd170to250_BTAGDOWN("ljmet"); 
    TChain ch_qcd170to250_JERUP("ljmet"); 
    TChain ch_qcd170to250_JERDOWN("ljmet");

    TChain ch_qcd250to350("ljmet");
    TChain ch_qcd250to350_JESUP("ljmet"); 
    TChain ch_qcd250to350_JESDOWN("ljmet"); 
    TChain ch_qcd250to350_BTAGUP("ljmet"); 
    TChain ch_qcd250to350_BTAGDOWN("ljmet"); 
    TChain ch_qcd250to350_JERUP("ljmet"); 
    TChain ch_qcd250to350_JERDOWN("ljmet");

    TChain ch_qcd350("ljmet");
    TChain ch_qcd350_JESUP("ljmet"); 
    TChain ch_qcd350_JESDOWN("ljmet"); 
    TChain ch_qcd350_BTAGUP("ljmet"); 
    TChain ch_qcd350_BTAGDOWN("ljmet"); 
    TChain ch_qcd350_JERUP("ljmet"); 
    TChain ch_qcd350_JERDOWN("ljmet");

    TChain ch_wp800R("ljmet");
    TChain ch_wp800R_JESUP("ljmet"); 
    TChain ch_wp800R_JESDOWN("ljmet"); 
    TChain ch_wp800R_BTAGUP("ljmet"); 
    TChain ch_wp800R_BTAGDOWN("ljmet"); 
    TChain ch_wp800R_JERUP("ljmet"); 
    TChain ch_wp800R_JERDOWN("ljmet"); 

    TChain ch_wp900R("ljmet");
    TChain ch_wp900R_JESUP("ljmet"); 
    TChain ch_wp900R_JESDOWN("ljmet"); 
    TChain ch_wp900R_BTAGUP("ljmet"); 
    TChain ch_wp900R_BTAGDOWN("ljmet"); 
    TChain ch_wp900R_JERUP("ljmet"); 
    TChain ch_wp900R_JERDOWN("ljmet"); 

    TChain ch_wp1000R("ljmet");
    TChain ch_wp1000R_JESUP("ljmet"); 
    TChain ch_wp1000R_JESDOWN("ljmet"); 
    TChain ch_wp1000R_BTAGUP("ljmet"); 
    TChain ch_wp1000R_BTAGDOWN("ljmet"); 
    TChain ch_wp1000R_JERUP("ljmet"); 
    TChain ch_wp1000R_JERDOWN("ljmet"); 

    TChain ch_wp1100R("ljmet");
    TChain ch_wp1100R_JESUP("ljmet"); 
    TChain ch_wp1100R_JESDOWN("ljmet"); 
    TChain ch_wp1100R_BTAGUP("ljmet"); 
    TChain ch_wp1100R_BTAGDOWN("ljmet"); 
    TChain ch_wp1100R_JERUP("ljmet"); 
    TChain ch_wp1100R_JERDOWN("ljmet"); 

    TChain ch_wp1200R("ljmet");
    TChain ch_wp1200R_JESUP("ljmet"); 
    TChain ch_wp1200R_JESDOWN("ljmet"); 
    TChain ch_wp1200R_BTAGUP("ljmet"); 
    TChain ch_wp1200R_BTAGDOWN("ljmet"); 
    TChain ch_wp1200R_JERUP("ljmet"); 
    TChain ch_wp1200R_JERDOWN("ljmet"); 

    TChain ch_wp1300R("ljmet");
    TChain ch_wp1300R_JESUP("ljmet"); 
    TChain ch_wp1300R_JESDOWN("ljmet"); 
    TChain ch_wp1300R_BTAGUP("ljmet"); 
    TChain ch_wp1300R_BTAGDOWN("ljmet"); 
    TChain ch_wp1300R_JERUP("ljmet"); 
    TChain ch_wp1300R_JERDOWN("ljmet"); 

    TChain ch_wp1400R("ljmet");
    TChain ch_wp1400R_JESUP("ljmet"); 
    TChain ch_wp1400R_JESDOWN("ljmet"); 
    TChain ch_wp1400R_BTAGUP("ljmet"); 
    TChain ch_wp1400R_BTAGDOWN("ljmet"); 
    TChain ch_wp1400R_JERUP("ljmet"); 
    TChain ch_wp1400R_JERDOWN("ljmet"); 

    TChain ch_wp1500R("ljmet");
    TChain ch_wp1500R_JESUP("ljmet"); 
    TChain ch_wp1500R_JESDOWN("ljmet"); 
    TChain ch_wp1500R_BTAGUP("ljmet"); 
    TChain ch_wp1500R_BTAGDOWN("ljmet"); 
    TChain ch_wp1500R_JERUP("ljmet"); 
    TChain ch_wp1500R_JERDOWN("ljmet"); 

    TChain ch_wp1600R("ljmet");
    TChain ch_wp1600R_JESUP("ljmet"); 
    TChain ch_wp1600R_JESDOWN("ljmet"); 
    TChain ch_wp1600R_BTAGUP("ljmet"); 
    TChain ch_wp1600R_BTAGDOWN("ljmet"); 
    TChain ch_wp1600R_JERUP("ljmet"); 
    TChain ch_wp1600R_JERDOWN("ljmet"); 

    TChain ch_wp1700R("ljmet");
    TChain ch_wp1700R_JESUP("ljmet"); 
    TChain ch_wp1700R_JESDOWN("ljmet"); 
    TChain ch_wp1700R_BTAGUP("ljmet"); 
    TChain ch_wp1700R_BTAGDOWN("ljmet"); 
    TChain ch_wp1700R_JERUP("ljmet"); 
    TChain ch_wp1700R_JERDOWN("ljmet"); 

    TChain ch_wp1800R("ljmet");
    TChain ch_wp1800R_JESUP("ljmet"); 
    TChain ch_wp1800R_JESDOWN("ljmet"); 
    TChain ch_wp1800R_BTAGUP("ljmet"); 
    TChain ch_wp1800R_BTAGDOWN("ljmet"); 
    TChain ch_wp1800R_JERUP("ljmet"); 
    TChain ch_wp1800R_JERDOWN("ljmet"); 

    TChain ch_wp1900R("ljmet");
    TChain ch_wp1900R_JESUP("ljmet"); 
    TChain ch_wp1900R_JESDOWN("ljmet"); 
    TChain ch_wp1900R_BTAGUP("ljmet"); 
    TChain ch_wp1900R_BTAGDOWN("ljmet"); 
    TChain ch_wp1900R_JERUP("ljmet"); 
    TChain ch_wp1900R_JERDOWN("ljmet"); 

    TChain ch_wp2000R("ljmet");
    TChain ch_wp2000R_JESUP("ljmet"); 
    TChain ch_wp2000R_JESDOWN("ljmet"); 
    TChain ch_wp2000R_BTAGUP("ljmet"); 
    TChain ch_wp2000R_BTAGDOWN("ljmet"); 
    TChain ch_wp2000R_JERUP("ljmet"); 
    TChain ch_wp2000R_JERDOWN("ljmet"); 

    TChain ch_wp2100R("ljmet");
    TChain ch_wp2100R_JESUP("ljmet"); 
    TChain ch_wp2100R_JESDOWN("ljmet"); 
    TChain ch_wp2100R_BTAGUP("ljmet"); 
    TChain ch_wp2100R_BTAGDOWN("ljmet"); 
    TChain ch_wp2100R_JERUP("ljmet"); 
    TChain ch_wp2100R_JERDOWN("ljmet"); 

    TChain ch_wp2200R("ljmet");
    TChain ch_wp2200R_JESUP("ljmet"); 
    TChain ch_wp2200R_JESDOWN("ljmet"); 
    TChain ch_wp2200R_BTAGUP("ljmet"); 
    TChain ch_wp2200R_BTAGDOWN("ljmet"); 
    TChain ch_wp2200R_JERUP("ljmet"); 
    TChain ch_wp2200R_JERDOWN("ljmet"); 

    TChain ch_wp2300R("ljmet");
    TChain ch_wp2300R_JESUP("ljmet"); 
    TChain ch_wp2300R_JESDOWN("ljmet"); 
    TChain ch_wp2300R_BTAGUP("ljmet"); 
    TChain ch_wp2300R_BTAGDOWN("ljmet"); 
    TChain ch_wp2300R_JERUP("ljmet"); 
    TChain ch_wp2300R_JERDOWN("ljmet"); 

    TChain ch_wp2400R("ljmet");
    TChain ch_wp2400R_JESUP("ljmet"); 
    TChain ch_wp2400R_JESDOWN("ljmet"); 
    TChain ch_wp2400R_BTAGUP("ljmet"); 
    TChain ch_wp2400R_BTAGDOWN("ljmet"); 
    TChain ch_wp2400R_JERUP("ljmet"); 
    TChain ch_wp2400R_JERDOWN("ljmet"); 

    TChain ch_wp2500R("ljmet");
    TChain ch_wp2500R_JESUP("ljmet"); 
    TChain ch_wp2500R_JESDOWN("ljmet"); 
    TChain ch_wp2500R_BTAGUP("ljmet"); 
    TChain ch_wp2500R_BTAGDOWN("ljmet"); 
    TChain ch_wp2500R_JERUP("ljmet"); 
    TChain ch_wp2500R_JERDOWN("ljmet"); 

    TChain ch_wp2600R("ljmet");
    TChain ch_wp2600R_JESUP("ljmet"); 
    TChain ch_wp2600R_JESDOWN("ljmet"); 
    TChain ch_wp2600R_BTAGUP("ljmet"); 
    TChain ch_wp2600R_BTAGDOWN("ljmet"); 
    TChain ch_wp2600R_JERUP("ljmet"); 
    TChain ch_wp2600R_JERDOWN("ljmet"); 

    TChain ch_wp2700R("ljmet");
    TChain ch_wp2700R_JESUP("ljmet"); 
    TChain ch_wp2700R_JESDOWN("ljmet"); 
    TChain ch_wp2700R_BTAGUP("ljmet"); 
    TChain ch_wp2700R_BTAGDOWN("ljmet"); 
    TChain ch_wp2700R_JERUP("ljmet"); 
    TChain ch_wp2700R_JERDOWN("ljmet"); 

    TChain ch_wp2800R("ljmet");
    TChain ch_wp2800R_JESUP("ljmet"); 
    TChain ch_wp2800R_JESDOWN("ljmet"); 
    TChain ch_wp2800R_BTAGUP("ljmet"); 
    TChain ch_wp2800R_BTAGDOWN("ljmet"); 
    TChain ch_wp2800R_JERUP("ljmet"); 
    TChain ch_wp2800R_JERDOWN("ljmet"); 

    TChain ch_wp2900R("ljmet");
    TChain ch_wp2900R_JESUP("ljmet"); 
    TChain ch_wp2900R_JESDOWN("ljmet"); 
    TChain ch_wp2900R_BTAGUP("ljmet"); 
    TChain ch_wp2900R_BTAGDOWN("ljmet"); 
    TChain ch_wp2900R_JERUP("ljmet"); 
    TChain ch_wp2900R_JERDOWN("ljmet"); 

    TChain ch_wp3000R("ljmet");
    TChain ch_wp3000R_JESUP("ljmet"); 
    TChain ch_wp3000R_JESDOWN("ljmet"); 
    TChain ch_wp3000R_BTAGUP("ljmet"); 
    TChain ch_wp3000R_BTAGDOWN("ljmet"); 
    TChain ch_wp3000R_JERUP("ljmet"); 
    TChain ch_wp3000R_JERDOWN("ljmet"); 

    TChain ch_ttbar_matchingup("ljmet"); 
    TChain ch_ttbar_matchingdown("ljmet"); 
    TChain ch_ttbar_scaleup("ljmet"); 
    TChain ch_ttbar_scaledown("ljmet"); 

    std::cout << " setting TTrees... " << std::endl;

    TTree * _data;

    TTree * _ttbar;
    TTree * _w1jets;
    TTree * _w2jets;
    TTree * _w3jets;
    TTree * _w4jets;
    TTree * _s;
    TTree * _bs;
    TTree * _t;
    TTree * _bt;
    TTree * _tw;
    TTree * _btw;
    TTree * _zjets;
    TTree * _ww;

    TTree * _wp800R;
    TTree * _wp900R;
    TTree * _wp1000R;
    TTree * _wp1100R;
    TTree * _wp1200R;
    TTree * _wp1300R;
    TTree * _wp1400R;
    TTree * _wp1500R;
    TTree * _wp1600R;
    TTree * _wp1700R;
    TTree * _wp1800R;
    TTree * _wp1900R;
    TTree * _wp2000R;
    TTree * _wp2100R;
    TTree * _wp2200R;
    TTree * _wp2300R;
    TTree * _wp2400R;
    TTree * _wp2500R;
    TTree * _wp2600R;
    TTree * _wp2700R;
    TTree * _wp2800R;
    TTree * _wp2900R;
    TTree * _wp3000R;
  
    TTree * _ttbar_JESUP;
    TTree * _ttbar_JESDOWN;
    TTree * _ttbar_JERUP;
    TTree * _ttbar_JERDOWN;
    TTree * _ttbar_BTAGUP;
    TTree * _ttbar_BTAGDOWN;

    TTree * _w1jets_JESUP;
    TTree * _w1jets_JESDOWN;
    TTree * _w1jets_JERUP;
    TTree * _w1jets_JERDOWN;
    TTree * _w1jets_BTAGUP;
    TTree * _w1jets_BTAGDOWN;

    TTree * _w2jets_JESUP;
    TTree * _w2jets_JESDOWN;
    TTree * _w2jets_JERUP;
    TTree * _w2jets_JERDOWN;
    TTree * _w2jets_BTAGUP;
    TTree * _w2jets_BTAGDOWN;

    TTree * _w3jets_JESUP;
    TTree * _w3jets_JESDOWN;
    TTree * _w3jets_JERUP;
    TTree * _w3jets_JERDOWN;
    TTree * _w3jets_BTAGUP;
    TTree * _w3jets_BTAGDOWN;

    TTree * _w4jets_JESUP;
    TTree * _w4jets_JESDOWN;
    TTree * _w4jets_JERUP;
    TTree * _w4jets_JERDOWN;
    TTree * _w4jets_BTAGUP;
    TTree * _w4jets_BTAGDOWN;

    TTree * _s_JESUP;
    TTree * _s_JESDOWN;
    TTree * _s_JERUP;
    TTree * _s_JERDOWN;
    TTree * _s_BTAGUP;
    TTree * _s_BTAGDOWN;

    TTree * _bs_JESUP;
    TTree * _bs_JESDOWN;
    TTree * _bs_JERUP;
    TTree * _bs_JERDOWN;
    TTree * _bs_BTAGUP;
    TTree * _bs_BTAGDOWN;

    TTree * _t_JESUP;
    TTree * _t_JESDOWN;
    TTree * _t_JERUP;
    TTree * _t_JERDOWN;
    TTree * _t_BTAGUP;
    TTree * _t_BTAGDOWN;

    TTree * _bt_JESUP;
    TTree * _bt_JESDOWN;
    TTree * _bt_JERUP;
    TTree * _bt_JERDOWN;
    TTree * _bt_BTAGUP;
    TTree * _bt_BTAGDOWN;

    TTree * _tw_JESUP;
    TTree * _tw_JESDOWN;
    TTree * _tw_JERUP;
    TTree * _tw_JERDOWN;
    TTree * _tw_BTAGUP;
    TTree * _tw_BTAGDOWN;

    TTree * _btw_JESUP;
    TTree * _btw_JESDOWN;
    TTree * _btw_JERUP;
    TTree * _btw_JERDOWN;
    TTree * _btw_BTAGUP;
    TTree * _btw_BTAGDOWN;

    TTree * _zjets_JESUP;
    TTree * _zjets_JESDOWN;
    TTree * _zjets_JERUP;
    TTree * _zjets_JERDOWN;
    TTree * _zjets_BTAGUP;
    TTree * _zjets_BTAGDOWN;

    TTree * _ww_JESUP;
    TTree * _ww_JESDOWN;
    TTree * _ww_JERUP;
    TTree * _ww_JERDOWN;
    TTree * _ww_BTAGUP;
    TTree * _ww_BTAGDOWN;

    TTree * _qcd80to170_JESUP;
    TTree * _qcd80to170_JESDOWN;
    TTree * _qcd80to170_JERUP;
    TTree * _qcd80to170_JERDOWN;
    TTree * _qcd80to170_BTAGUP;
    TTree * _qcd80to170_BTAGDOWN;

    TTree * _qcd170to250_JESUP;
    TTree * _qcd170to250_JESDOWN;
    TTree * _qcd170to250_JERUP;
    TTree * _qcd170to250_JERDOWN;
    TTree * _qcd170to250_BTAGUP;
    TTree * _qcd170to250_BTAGDOWN;

    TTree * _qcd250to350_JESUP;
    TTree * _qcd250to350_JESDOWN;
    TTree * _qcd250to350_JERUP;
    TTree * _qcd250to350_JERDOWN;
    TTree * _qcd250to350_BTAGUP;
    TTree * _qcd250to350_BTAGDOWN;

    TTree * _qcd350_JESUP;
    TTree * _qcd350_JESDOWN;
    TTree * _qcd350_JERUP;
    TTree * _qcd350_JERDOWN;
    TTree * _qcd350_BTAGUP;
    TTree * _qcd350_BTAGDOWN;

    TTree * _ttbar_matchingup;
    TTree * _ttbar_matchingdown;
    TTree * _ttbar_scaleup;
    TTree * _ttbar_scaledown;

    TTree * _wp800R_JESUP;
    TTree * _wp800R_JESDOWN;
    TTree * _wp800R_JERUP;
    TTree * _wp800R_JERDOWN;
    TTree * _wp800R_BTAGUP;
    TTree * _wp800R_BTAGDOWN;

    TTree * _wp900R_JESUP;
    TTree * _wp900R_JESDOWN;
    TTree * _wp900R_JERUP;
    TTree * _wp900R_JERDOWN;
    TTree * _wp900R_BTAGUP;
    TTree * _wp900R_BTAGDOWN;

    TTree * _wp1000R_JESUP;
    TTree * _wp1000R_JESDOWN;
    TTree * _wp1000R_JERUP;
    TTree * _wp1000R_JERDOWN;
    TTree * _wp1000R_BTAGUP;
    TTree * _wp1000R_BTAGDOWN;

    TTree * _wp1100R_JESUP;
    TTree * _wp1100R_JESDOWN;
    TTree * _wp1100R_JERUP;
    TTree * _wp1100R_JERDOWN;
    TTree * _wp1100R_BTAGUP;
    TTree * _wp1100R_BTAGDOWN;

    TTree * _wp1200R_JESUP;
    TTree * _wp1200R_JESDOWN;
    TTree * _wp1200R_JERUP;
    TTree * _wp1200R_JERDOWN;
    TTree * _wp1200R_BTAGUP;
    TTree * _wp1200R_BTAGDOWN;

    TTree * _wp1300R_JESUP;
    TTree * _wp1300R_JESDOWN;
    TTree * _wp1300R_JERUP;
    TTree * _wp1300R_JERDOWN;
    TTree * _wp1300R_BTAGUP;
    TTree * _wp1300R_BTAGDOWN;

    TTree * _wp1400R_JESUP;
    TTree * _wp1400R_JESDOWN;
    TTree * _wp1400R_JERUP;
    TTree * _wp1400R_JERDOWN;
    TTree * _wp1400R_BTAGUP;
    TTree * _wp1400R_BTAGDOWN;

    TTree * _wp1500R_JESUP;
    TTree * _wp1500R_JESDOWN;
    TTree * _wp1500R_JERUP;
    TTree * _wp1500R_JERDOWN;
    TTree * _wp1500R_BTAGUP;
    TTree * _wp1500R_BTAGDOWN;

    TTree * _wp1600R_JESUP;
    TTree * _wp1600R_JESDOWN;
    TTree * _wp1600R_JERUP;
    TTree * _wp1600R_JERDOWN;
    TTree * _wp1600R_BTAGUP;
    TTree * _wp1600R_BTAGDOWN;

    TTree * _wp1700R_JESUP;
    TTree * _wp1700R_JESDOWN;
    TTree * _wp1700R_JERUP;
    TTree * _wp1700R_JERDOWN;
    TTree * _wp1700R_BTAGUP;
    TTree * _wp1700R_BTAGDOWN;

    TTree * _wp1800R_JESUP;
    TTree * _wp1800R_JESDOWN;
    TTree * _wp1800R_JERUP;
    TTree * _wp1800R_JERDOWN;
    TTree * _wp1800R_BTAGUP;
    TTree * _wp1800R_BTAGDOWN;

    TTree * _wp1900R_JESUP;
    TTree * _wp1900R_JESDOWN;
    TTree * _wp1900R_JERUP;
    TTree * _wp1900R_JERDOWN;
    TTree * _wp1900R_BTAGUP;
    TTree * _wp1900R_BTAGDOWN;

    TTree * _wp2000R_JESUP;
    TTree * _wp2000R_JESDOWN;
    TTree * _wp2000R_JERUP;
    TTree * _wp2000R_JERDOWN;
    TTree * _wp2000R_BTAGUP;
    TTree * _wp2000R_BTAGDOWN;

    TTree * _wp2100R_JESUP;
    TTree * _wp2100R_JESDOWN;
    TTree * _wp2100R_JERUP;
    TTree * _wp2100R_JERDOWN;
    TTree * _wp2100R_BTAGUP;
    TTree * _wp2100R_BTAGDOWN;

    TTree * _wp2200R_JESUP;
    TTree * _wp2200R_JESDOWN;
    TTree * _wp2200R_JERUP;
    TTree * _wp2200R_JERDOWN;
    TTree * _wp2200R_BTAGUP;
    TTree * _wp2200R_BTAGDOWN;

    TTree * _wp2300R_JESUP;
    TTree * _wp2300R_JESDOWN;
    TTree * _wp2300R_JERUP;
    TTree * _wp2300R_JERDOWN;
    TTree * _wp2300R_BTAGUP;
    TTree * _wp2300R_BTAGDOWN;

    TTree * _wp2400R_JESUP;
    TTree * _wp2400R_JESDOWN;
    TTree * _wp2400R_JERUP;
    TTree * _wp2400R_JERDOWN;
    TTree * _wp2400R_BTAGUP;
    TTree * _wp2400R_BTAGDOWN;

    TTree * _wp2500R_JESUP;
    TTree * _wp2500R_JESDOWN;
    TTree * _wp2500R_JERUP;
    TTree * _wp2500R_JERDOWN;
    TTree * _wp2500R_BTAGUP;
    TTree * _wp2500R_BTAGDOWN;

    TTree * _wp2600R_JESUP;
    TTree * _wp2600R_JESDOWN;
    TTree * _wp2600R_JERUP;
    TTree * _wp2600R_JERDOWN;
    TTree * _wp2600R_BTAGUP;
    TTree * _wp2600R_BTAGDOWN;

    TTree * _wp2700R_JESUP;
    TTree * _wp2700R_JESDOWN;
    TTree * _wp2700R_JERUP;
    TTree * _wp2700R_JERDOWN;
    TTree * _wp2700R_BTAGUP;
    TTree * _wp2700R_BTAGDOWN;

    TTree * _wp2800R_JESUP;
    TTree * _wp2800R_JESDOWN;
    TTree * _wp2800R_JERUP;
    TTree * _wp2800R_JERDOWN;
    TTree * _wp2800R_BTAGUP;
    TTree * _wp2800R_BTAGDOWN;

    TTree * _wp2900R_JESUP;
    TTree * _wp2900R_JESDOWN;
    TTree * _wp2900R_JERUP;
    TTree * _wp2900R_JERDOWN;
    TTree * _wp2900R_BTAGUP;
    TTree * _wp2900R_BTAGDOWN;

    TTree * _wp3000R_JESUP;
    TTree * _wp3000R_JESDOWN;
    TTree * _wp3000R_JERUP;
    TTree * _wp3000R_JERDOWN;
    TTree * _wp3000R_BTAGUP;
    TTree * _wp3000R_BTAGDOWN;


    std::cout << " adding nominal root files... " << std::endl;
    ch_ttbar . Add(indir + "TTbar_Madgraph.root");
    ch_w1jets . Add(indir + "W1Jets.root");
    ch_w2jets . Add(indir + "W2Jets.root");
    ch_w3jets . Add(indir + "W3Jets.root");
    ch_w4jets . Add(indir + "W4Jets.root");
    ch_s . Add(indir + "T_s.root");
    ch_bs . Add(indir + "Tbar_s.root");
    ch_t . Add(indir + "T_t.root");
    ch_bt . Add(indir + "Tbar_t.root");
    ch_tw . Add(indir + "T_tW.root");
    ch_btw . Add(indir + "Tbar_tW.root");
    ch_zjets . Add(indir + "ZJets_M50.root");
    ch_ww . Add(indir + "WW.root");
    ch_qcd80to170 . Add(indir + "QCD_Pt_80_170_EM.root");
    ch_qcd170to250 . Add(indir + "QCD_Pt_170_250_EM.root");
    ch_qcd250to350 . Add(indir + "QCD_Pt_250_350_EM.root");
    ch_qcd350 . Add(indir + "QCD_Pt_350_EM.root");
  
    ch_wp800R . Add(indir + "Wprime800Right.root");
    ch_wp900R . Add(indir + "Wprime900Right.root");
    ch_wp1000R . Add(indir + "Wprime1000Right.root");
    ch_wp1100R . Add(indir + "Wprime1100Right.root");
    ch_wp1200R . Add(indir + "Wprime1200Right.root");
    ch_wp1300R . Add(indir + "Wprime1300Right.root");
    ch_wp1400R . Add(indir + "Wprime1400Right.root");
    ch_wp1500R . Add(indir + "Wprime1500Right.root");
    ch_wp1600R . Add(indir + "Wprime1600Right.root");
    ch_wp1700R . Add(indir + "Wprime1700Right.root");
    ch_wp1800R . Add(indir + "Wprime1800Right.root");
    ch_wp1900R . Add(indir + "Wprime1900Right.root");
    ch_wp2000R . Add(indir + "Wprime2000Right.root");
    ch_wp2100R . Add(indir + "Wprime2100Right.root");
    ch_wp2200R . Add(indir + "Wprime2200Right.root");
    ch_wp2300R . Add(indir + "Wprime2300Right.root");
    ch_wp2400R . Add(indir + "Wprime2400Right.root");
    ch_wp2500R . Add(indir + "Wprime2500Right.root");
    ch_wp2600R . Add(indir + "Wprime2600Right.root");
    ch_wp2700R . Add(indir + "Wprime2700Right.root");
    ch_wp2800R . Add(indir + "Wprime2800Right.root");
    ch_wp2900R . Add(indir + "Wprime2900Right.root");
    ch_wp3000R . Add(indir + "Wprime3000Right.root");

    if (ifsys) {
      std::cout << " add _JESUP root files... " << std::endl;
      ch_ttbar_JESUP . Add(indir + "JESUP/TTbar_Madgraph_JESUP.root");
      ch_w1jets_JESUP . Add(indir + "JESUP/W1Jets_JESUP.root");
      ch_w2jets_JESUP . Add(indir + "JESUP/W2Jets_JESUP.root");
      ch_w3jets_JESUP . Add(indir + "JESUP/W3Jets_JESUP.root");
      ch_w4jets_JESUP . Add(indir + "JESUP/W4Jets_JESUP.root");
      ch_s_JESUP . Add(indir + "JESUP/T_s_JESUP.root");
      ch_bs_JESUP . Add(indir + "JESUP/Tbar_s_JESUP.root");
      ch_t_JESUP . Add(indir + "JESUP/T_t_JESUP.root");
      ch_bt_JESUP . Add(indir + "JESUP/Tbar_t_JESUP.root");
      ch_tw_JESUP . Add(indir + "JESUP/T_tW_JESUP.root");
      ch_btw_JESUP . Add(indir + "JESUP/Tbar_tW_JESUP.root");
      ch_zjets_JESUP . Add(indir + "JESUP/ZJets_M50_JESUP.root");
      ch_ww_JESUP . Add(indir + "JESUP/WW_JESUP.root");
      ch_qcd80to170_JESUP . Add(indir + "JESUP/QCD_Pt_80_170_EM_JESUP.root");
      ch_qcd170to250_JESUP . Add(indir + "JESUP/QCD_Pt_170_250_EM_JESUP.root");
      ch_qcd250to350_JESUP . Add(indir + "JESUP/QCD_Pt_250_350_EM_JESUP.root");
      ch_qcd350_JESUP . Add(indir + "JESUP/QCD_Pt_350_EM_JESUP.root");
       
      ch_wp800R_JESUP . Add(indir + "JESUP/Wprime800Right_JESUP.root");
      ch_wp900R_JESUP . Add(indir + "JESUP/Wprime900Right_JESUP.root");
      ch_wp1000R_JESUP . Add(indir + "JESUP/Wprime1000Right_JESUP.root");
      ch_wp1100R_JESUP . Add(indir + "JESUP/Wprime1100Right_JESUP.root");
      ch_wp1200R_JESUP . Add(indir + "JESUP/Wprime1200Right_JESUP.root");
      ch_wp1300R_JESUP . Add(indir + "JESUP/Wprime1300Right_JESUP.root");
      ch_wp1400R_JESUP . Add(indir + "JESUP/Wprime1400Right_JESUP.root");
      ch_wp1500R_JESUP . Add(indir + "JESUP/Wprime1500Right_JESUP.root");
      ch_wp1600R_JESUP . Add(indir + "JESUP/Wprime1600Right_JESUP.root");
      ch_wp1700R_JESUP . Add(indir + "JESUP/Wprime1700Right_JESUP.root");
      ch_wp1800R_JESUP . Add(indir + "JESUP/Wprime1800Right_JESUP.root");
      ch_wp1900R_JESUP . Add(indir + "JESUP/Wprime1900Right_JESUP.root");
      ch_wp2000R_JESUP . Add(indir + "JESUP/Wprime2000Right_JESUP.root");
      ch_wp2100R_JESUP . Add(indir + "JESUP/Wprime2100Right_JESUP.root");
      ch_wp2200R_JESUP . Add(indir + "JESUP/Wprime2200Right_JESUP.root");
      ch_wp2300R_JESUP . Add(indir + "JESUP/Wprime2300Right_JESUP.root");
      ch_wp2400R_JESUP . Add(indir + "JESUP/Wprime2400Right_JESUP.root");
      ch_wp2500R_JESUP . Add(indir + "JESUP/Wprime2500Right_JESUP.root");
      ch_wp2600R_JESUP . Add(indir + "JESUP/Wprime2600Right_JESUP.root");
      ch_wp2700R_JESUP . Add(indir + "JESUP/Wprime2700Right_JESUP.root");
      ch_wp2800R_JESUP . Add(indir + "JESUP/Wprime2800Right_JESUP.root");
      ch_wp2900R_JESUP . Add(indir + "JESUP/Wprime2900Right_JESUP.root");
      ch_wp3000R_JESUP . Add(indir + "JESUP/Wprime3000Right_JESUP.root");
   
 
      std::cout << " add _JESDOWN root files... " << std::endl;
      ch_ttbar_JESDOWN . Add(indir + "JESDOWN/TTbar_Madgraph_JESDOWN.root");
      ch_w1jets_JESDOWN . Add(indir + "JESDOWN/W1Jets_JESDOWN.root");
      ch_w2jets_JESDOWN . Add(indir + "JESDOWN/W2Jets_JESDOWN.root");
      ch_w3jets_JESDOWN . Add(indir + "JESDOWN/W3Jets_JESDOWN.root");
      ch_w4jets_JESDOWN . Add(indir + "JESDOWN/W4Jets_JESDOWN.root");
      ch_s_JESDOWN . Add(indir + "JESDOWN/T_s_JESDOWN.root");
      ch_bs_JESDOWN . Add(indir + "JESDOWN/Tbar_s_JESDOWN.root");
      ch_t_JESDOWN . Add(indir + "JESDOWN/T_t_JESDOWN.root");
      ch_bt_JESDOWN . Add(indir + "JESDOWN/Tbar_t_JESDOWN.root");
      ch_tw_JESDOWN . Add(indir + "JESDOWN/T_tW_JESDOWN.root");
      ch_btw_JESDOWN . Add(indir + "JESDOWN/Tbar_tW_JESDOWN.root");
      ch_zjets_JESDOWN . Add(indir + "JESDOWN/ZJets_M50_JESDOWN.root");
      ch_ww_JESDOWN . Add(indir + "JESDOWN/WW_JESDOWN.root");
      ch_qcd80to170_JESDOWN . Add(indir + "JESDOWN/QCD_Pt_80_170_EM_JESDOWN.root");
      ch_qcd170to250_JESDOWN . Add(indir + "JESDOWN/QCD_Pt_170_250_EM_JESDOWN.root");
      ch_qcd250to350_JESDOWN . Add(indir + "JESDOWN/QCD_Pt_250_350_EM_JESDOWN.root");
      ch_qcd350_JESDOWN . Add(indir + "JESDOWN/QCD_Pt_350_EM_JESDOWN.root");
      
      ch_wp800R_JESDOWN . Add(indir + "JESDOWN/Wprime800Right_JESDOWN.root");
      ch_wp900R_JESDOWN . Add(indir + "JESDOWN/Wprime900Right_JESDOWN.root");
      ch_wp1000R_JESDOWN . Add(indir + "JESDOWN/Wprime1000Right_JESDOWN.root");
      ch_wp1100R_JESDOWN . Add(indir + "JESDOWN/Wprime1100Right_JESDOWN.root");
      ch_wp1200R_JESDOWN . Add(indir + "JESDOWN/Wprime1200Right_JESDOWN.root");
      ch_wp1300R_JESDOWN . Add(indir + "JESDOWN/Wprime1300Right_JESDOWN.root");
      ch_wp1400R_JESDOWN . Add(indir + "JESDOWN/Wprime1400Right_JESDOWN.root");
      ch_wp1500R_JESDOWN . Add(indir + "JESDOWN/Wprime1500Right_JESDOWN.root");
      ch_wp1600R_JESDOWN . Add(indir + "JESDOWN/Wprime1600Right_JESDOWN.root");
      ch_wp1700R_JESDOWN . Add(indir + "JESDOWN/Wprime1700Right_JESDOWN.root");
      ch_wp1800R_JESDOWN . Add(indir + "JESDOWN/Wprime1800Right_JESDOWN.root");
      ch_wp1900R_JESDOWN . Add(indir + "JESDOWN/Wprime1900Right_JESDOWN.root");
      ch_wp2000R_JESDOWN . Add(indir + "JESDOWN/Wprime2000Right_JESDOWN.root");
      ch_wp2100R_JESDOWN . Add(indir + "JESDOWN/Wprime2100Right_JESDOWN.root");
      ch_wp2200R_JESDOWN . Add(indir + "JESDOWN/Wprime2200Right_JESDOWN.root");
      ch_wp2300R_JESDOWN . Add(indir + "JESDOWN/Wprime2300Right_JESDOWN.root");
      ch_wp2400R_JESDOWN . Add(indir + "JESDOWN/Wprime2400Right_JESDOWN.root");
      ch_wp2500R_JESDOWN . Add(indir + "JESDOWN/Wprime2500Right_JESDOWN.root");
      ch_wp2600R_JESDOWN . Add(indir + "JESDOWN/Wprime2600Right_JESDOWN.root");
      ch_wp2700R_JESDOWN . Add(indir + "JESDOWN/Wprime2700Right_JESDOWN.root");
      ch_wp2800R_JESDOWN . Add(indir + "JESDOWN/Wprime2800Right_JESDOWN.root");
      ch_wp2900R_JESDOWN . Add(indir + "JESDOWN/Wprime2900Right_JESDOWN.root");
      ch_wp3000R_JESDOWN . Add(indir + "JESDOWN/Wprime3000Right_JESDOWN.root");
   

      std::cout << " add _BTAGUP root files... " << std::endl;
      ch_ttbar_BTAGUP . Add(indir + "BTAGUP/TTbar_Madgraph_BTAGUP.root");
      ch_w1jets_BTAGUP . Add(indir + "BTAGUP/W1Jets_BTAGUP.root");
      ch_w2jets_BTAGUP . Add(indir + "BTAGUP/W2Jets_BTAGUP.root");
      ch_w3jets_BTAGUP . Add(indir + "BTAGUP/W3Jets_BTAGUP.root");
      ch_w4jets_BTAGUP . Add(indir + "BTAGUP/W4Jets_BTAGUP.root");
      ch_s_BTAGUP . Add(indir + "BTAGUP/T_s_BTAGUP.root");
      ch_bs_BTAGUP . Add(indir + "BTAGUP/Tbar_s_BTAGUP.root");
      ch_t_BTAGUP . Add(indir + "BTAGUP/T_t_BTAGUP.root");
      ch_bt_BTAGUP . Add(indir + "BTAGUP/Tbar_t_BTAGUP.root");
      ch_tw_BTAGUP . Add(indir + "BTAGUP/T_tW_BTAGUP.root");
      ch_btw_BTAGUP . Add(indir + "BTAGUP/Tbar_tW_BTAGUP.root");
      ch_zjets_BTAGUP . Add(indir + "BTAGUP/ZJets_M50_BTAGUP.root");
      ch_ww_BTAGUP . Add(indir + "BTAGUP/WW_BTAGUP.root");
      ch_qcd80to170_BTAGUP . Add(indir + "BTAGUP/QCD_Pt_80_170_EM_BTAGUP.root");
      ch_qcd170to250_BTAGUP . Add(indir + "BTAGUP/QCD_Pt_170_250_EM_BTAGUP.root");
      ch_qcd250to350_BTAGUP . Add(indir + "BTAGUP/QCD_Pt_250_350_EM_BTAGUP.root");
      ch_qcd350_BTAGUP . Add(indir + "BTAGUP/QCD_Pt_350_EM_BTAGUP.root");

      ch_wp800R_BTAGUP . Add(indir + "BTAGUP/Wprime800Right_BTAGUP.root");
      ch_wp900R_BTAGUP . Add(indir + "BTAGUP/Wprime900Right_BTAGUP.root");
      ch_wp1000R_BTAGUP . Add(indir + "BTAGUP/Wprime1000Right_BTAGUP.root");
      ch_wp1100R_BTAGUP . Add(indir + "BTAGUP/Wprime1100Right_BTAGUP.root");
      ch_wp1200R_BTAGUP . Add(indir + "BTAGUP/Wprime1200Right_BTAGUP.root");
      ch_wp1300R_BTAGUP . Add(indir + "BTAGUP/Wprime1300Right_BTAGUP.root");
      ch_wp1400R_BTAGUP . Add(indir + "BTAGUP/Wprime1400Right_BTAGUP.root");
      ch_wp1500R_BTAGUP . Add(indir + "BTAGUP/Wprime1500Right_BTAGUP.root");
      ch_wp1600R_BTAGUP . Add(indir + "BTAGUP/Wprime1600Right_BTAGUP.root");
      ch_wp1700R_BTAGUP . Add(indir + "BTAGUP/Wprime1700Right_BTAGUP.root");
      ch_wp1800R_BTAGUP . Add(indir + "BTAGUP/Wprime1800Right_BTAGUP.root");
      ch_wp1900R_BTAGUP . Add(indir + "BTAGUP/Wprime1900Right_BTAGUP.root");
      ch_wp2000R_BTAGUP . Add(indir + "BTAGUP/Wprime2000Right_BTAGUP.root");
      ch_wp2100R_BTAGUP . Add(indir + "BTAGUP/Wprime2100Right_BTAGUP.root");
      ch_wp2200R_BTAGUP . Add(indir + "BTAGUP/Wprime2200Right_BTAGUP.root");
      ch_wp2300R_BTAGUP . Add(indir + "BTAGUP/Wprime2300Right_BTAGUP.root");
      ch_wp2400R_BTAGUP . Add(indir + "BTAGUP/Wprime2400Right_BTAGUP.root");
      ch_wp2500R_BTAGUP . Add(indir + "BTAGUP/Wprime2500Right_BTAGUP.root");
      ch_wp2600R_BTAGUP . Add(indir + "BTAGUP/Wprime2600Right_BTAGUP.root");
      ch_wp2700R_BTAGUP . Add(indir + "BTAGUP/Wprime2700Right_BTAGUP.root");
      ch_wp2800R_BTAGUP . Add(indir + "BTAGUP/Wprime2800Right_BTAGUP.root");
      ch_wp2900R_BTAGUP . Add(indir + "BTAGUP/Wprime2900Right_BTAGUP.root");
      ch_wp3000R_BTAGUP . Add(indir + "BTAGUP/Wprime3000Right_BTAGUP.root");
  
      std::cout << " add _BTAGDOWN root files... " << std::endl;
      ch_ttbar_BTAGDOWN . Add(indir + "BTAGDOWN/TTbar_Madgraph_BTAGDOWN.root");
      ch_w1jets_BTAGDOWN . Add(indir + "BTAGDOWN/W1Jets_BTAGDOWN.root");
      ch_w2jets_BTAGDOWN . Add(indir + "BTAGDOWN/W2Jets_BTAGDOWN.root");
      ch_w3jets_BTAGDOWN . Add(indir + "BTAGDOWN/W3Jets_BTAGDOWN.root");
      ch_w4jets_BTAGDOWN . Add(indir + "BTAGDOWN/W4Jets_BTAGDOWN.root");
      ch_s_BTAGDOWN . Add(indir + "BTAGDOWN/T_s_BTAGDOWN.root");
      ch_bs_BTAGDOWN . Add(indir + "BTAGDOWN/Tbar_s_BTAGDOWN.root");
      ch_t_BTAGDOWN . Add(indir + "BTAGDOWN/T_t_BTAGDOWN.root");
      ch_bt_BTAGDOWN . Add(indir + "BTAGDOWN/Tbar_t_BTAGDOWN.root");
      ch_tw_BTAGDOWN . Add(indir + "BTAGDOWN/T_tW_BTAGDOWN.root");
      ch_btw_BTAGDOWN . Add(indir + "BTAGDOWN/Tbar_tW_BTAGDOWN.root");
      ch_zjets_BTAGDOWN . Add(indir + "BTAGDOWN/ZJets_M50_BTAGDOWN.root");
      ch_ww_BTAGDOWN . Add(indir + "BTAGDOWN/WW_BTAGDOWN.root");
      ch_qcd80to170_BTAGDOWN . Add(indir + "BTAGDOWN/QCD_Pt_80_170_EM_BTAGDOWN.root");
      ch_qcd170to250_BTAGDOWN . Add(indir + "BTAGDOWN/QCD_Pt_170_250_EM_BTAGDOWN.root");
      ch_qcd250to350_BTAGDOWN . Add(indir + "BTAGDOWN/QCD_Pt_250_350_EM_BTAGDOWN.root");
      ch_qcd350_BTAGDOWN . Add(indir + "BTAGDOWN/QCD_Pt_350_EM_BTAGDOWN.root");
      
      ch_wp800R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime800Right_BTAGDOWN.root");
      ch_wp900R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime900Right_BTAGDOWN.root");
      ch_wp1000R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1000Right_BTAGDOWN.root");
      ch_wp1100R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1100Right_BTAGDOWN.root");
      ch_wp1200R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1200Right_BTAGDOWN.root");
      ch_wp1300R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1300Right_BTAGDOWN.root");
      ch_wp1400R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1400Right_BTAGDOWN.root");
      ch_wp1500R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1500Right_BTAGDOWN.root");
      ch_wp1600R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1600Right_BTAGDOWN.root");
      ch_wp1700R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1700Right_BTAGDOWN.root");
      ch_wp1800R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1800Right_BTAGDOWN.root");
      ch_wp1900R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime1900Right_BTAGDOWN.root");
      ch_wp2000R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2000Right_BTAGDOWN.root");
      ch_wp2100R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2100Right_BTAGDOWN.root");
      ch_wp2200R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2200Right_BTAGDOWN.root");
      ch_wp2300R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2300Right_BTAGDOWN.root");
      ch_wp2400R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2400Right_BTAGDOWN.root");
      ch_wp2500R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2500Right_BTAGDOWN.root");
      ch_wp2600R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2600Right_BTAGDOWN.root");
      ch_wp2700R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2700Right_BTAGDOWN.root");
      ch_wp2800R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2800Right_BTAGDOWN.root");
      ch_wp2900R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime2900Right_BTAGDOWN.root");
      ch_wp3000R_BTAGDOWN . Add(indir + "BTAGDOWN/Wprime3000Right_BTAGDOWN.root");
  

      std::cout << " add _JERUP root files... " << std::endl;
      ch_ttbar_JERUP . Add(indir + "JERUP/TTbar_Madgraph_JERUP.root");
      ch_w1jets_JERUP . Add(indir + "JERUP/W1Jets_JERUP.root");
      ch_w2jets_JERUP . Add(indir + "JERUP/W2Jets_JERUP.root");
      ch_w3jets_JERUP . Add(indir + "JERUP/W3Jets_JERUP.root");
      ch_w4jets_JERUP . Add(indir + "JERUP/W4Jets_JERUP.root");
      ch_s_JERUP . Add(indir + "JERUP/T_s_JERUP.root");
      ch_bs_JERUP . Add(indir + "JERUP/Tbar_s_JERUP.root");
      ch_t_JERUP . Add(indir + "JERUP/T_t_JERUP.root");
      ch_bt_JERUP . Add(indir + "JERUP/Tbar_t_JERUP.root");
      ch_tw_JERUP . Add(indir + "JERUP/T_tW_JERUP.root");
      ch_btw_JERUP . Add(indir + "JERUP/Tbar_tW_JERUP.root");
      ch_zjets_JERUP . Add(indir + "JERUP/ZJets_M50_JERUP.root");
      ch_ww_JERUP . Add(indir + "JERUP/WW_JERUP.root");
      ch_qcd80to170_JERUP . Add(indir + "JERUP/QCD_Pt_80_170_EM_JERUP.root");
      ch_qcd170to250_JERUP . Add(indir + "JERUP/QCD_Pt_170_250_EM_JERUP.root");
      ch_qcd250to350_JERUP . Add(indir + "JERUP/QCD_Pt_250_350_EM_JERUP.root");
      ch_qcd350_JERUP . Add(indir + "JERUP/QCD_Pt_350_EM_JERUP.root");
      
      ch_wp800R_JERUP . Add(indir + "JERUP/Wprime800Right_JERUP.root");
      ch_wp900R_JERUP . Add(indir + "JERUP/Wprime900Right_JERUP.root");
      ch_wp1000R_JERUP . Add(indir + "JERUP/Wprime1000Right_JERUP.root");
      ch_wp1100R_JERUP . Add(indir + "JERUP/Wprime1100Right_JERUP.root");
      ch_wp1200R_JERUP . Add(indir + "JERUP/Wprime1200Right_JERUP.root");
      ch_wp1300R_JERUP . Add(indir + "JERUP/Wprime1300Right_JERUP.root");
      ch_wp1400R_JERUP . Add(indir + "JERUP/Wprime1400Right_JERUP.root");
      ch_wp1500R_JERUP . Add(indir + "JERUP/Wprime1500Right_JERUP.root");
      ch_wp1600R_JERUP . Add(indir + "JERUP/Wprime1600Right_JERUP.root");
      ch_wp1700R_JERUP . Add(indir + "JERUP/Wprime1700Right_JERUP.root");
      ch_wp1800R_JERUP . Add(indir + "JERUP/Wprime1800Right_JERUP.root");
      ch_wp1900R_JERUP . Add(indir + "JERUP/Wprime1900Right_JERUP.root");
      ch_wp2000R_JERUP . Add(indir + "JERUP/Wprime2000Right_JERUP.root");
      ch_wp2100R_JERUP . Add(indir + "JERUP/Wprime2100Right_JERUP.root");
      ch_wp2200R_JERUP . Add(indir + "JERUP/Wprime2200Right_JERUP.root");
      ch_wp2300R_JERUP . Add(indir + "JERUP/Wprime2300Right_JERUP.root");
      ch_wp2400R_JERUP . Add(indir + "JERUP/Wprime2400Right_JERUP.root");
      ch_wp2500R_JERUP . Add(indir + "JERUP/Wprime2500Right_JERUP.root");
      ch_wp2600R_JERUP . Add(indir + "JERUP/Wprime2600Right_JERUP.root");
      ch_wp2700R_JERUP . Add(indir + "JERUP/Wprime2700Right_JERUP.root");
      ch_wp2800R_JERUP . Add(indir + "JERUP/Wprime2800Right_JERUP.root");
      ch_wp2900R_JERUP . Add(indir + "JERUP/Wprime2900Right_JERUP.root");
      ch_wp3000R_JERUP . Add(indir + "JERUP/Wprime3000Right_JERUP.root");
  

      std::cout << " add _JERDOWN root files... " << std::endl;
      ch_ttbar_JERDOWN . Add(indir + "JERDOWN/TTbar_Madgraph_JERDOWN.root");
      ch_w1jets_JERDOWN . Add(indir + "JERDOWN/W1Jets_JERDOWN.root");
      ch_w2jets_JERDOWN . Add(indir + "JERDOWN/W2Jets_JERDOWN.root");
      ch_w3jets_JERDOWN . Add(indir + "JERDOWN/W3Jets_JERDOWN.root");
      ch_w4jets_JERDOWN . Add(indir + "JERDOWN/W4Jets_JERDOWN.root");
      ch_s_JERDOWN . Add(indir + "JERDOWN/T_s_JERDOWN.root");
      ch_bs_JERDOWN . Add(indir + "JERDOWN/Tbar_s_JERDOWN.root");
      ch_t_JERDOWN . Add(indir + "JERDOWN/T_t_JERDOWN.root");
      ch_bt_JERDOWN . Add(indir + "JERDOWN/Tbar_t_JERDOWN.root");
      ch_tw_JERDOWN . Add(indir + "JERDOWN/T_tW_JERDOWN.root");
      ch_btw_JERDOWN . Add(indir + "JERDOWN/Tbar_tW_JERDOWN.root");
      ch_zjets_JERDOWN . Add(indir + "JERDOWN/ZJets_M50_JERDOWN.root");
      ch_ww_JERDOWN . Add(indir + "JERDOWN/WW_JERDOWN.root");
      ch_qcd80to170_JERDOWN . Add(indir + "JERDOWN/QCD_Pt_80_170_EM_JERDOWN.root");
      ch_qcd170to250_JERDOWN . Add(indir + "JERDOWN/QCD_Pt_170_250_EM_JERDOWN.root");
      ch_qcd250to350_JERDOWN . Add(indir + "JERDOWN/QCD_Pt_250_350_EM_JERDOWN.root");
      ch_qcd350_JERDOWN . Add(indir + "JERDOWN/QCD_Pt_350_EM_JERDOWN.root");
      
      ch_wp800R_JERDOWN . Add(indir + "JERDOWN/Wprime800Right_JERDOWN.root");
      ch_wp900R_JERDOWN . Add(indir + "JERDOWN/Wprime900Right_JERDOWN.root");
      ch_wp1000R_JERDOWN . Add(indir + "JERDOWN/Wprime1000Right_JERDOWN.root");
      ch_wp1100R_JERDOWN . Add(indir + "JERDOWN/Wprime1100Right_JERDOWN.root");
      ch_wp1200R_JERDOWN . Add(indir + "JERDOWN/Wprime1200Right_JERDOWN.root");
      ch_wp1300R_JERDOWN . Add(indir + "JERDOWN/Wprime1300Right_JERDOWN.root");
      ch_wp1400R_JERDOWN . Add(indir + "JERDOWN/Wprime1400Right_JERDOWN.root");
      ch_wp1500R_JERDOWN . Add(indir + "JERDOWN/Wprime1500Right_JERDOWN.root");
      ch_wp1600R_JERDOWN . Add(indir + "JERDOWN/Wprime1600Right_JERDOWN.root");
      ch_wp1700R_JERDOWN . Add(indir + "JERDOWN/Wprime1700Right_JERDOWN.root");
      ch_wp1800R_JERDOWN . Add(indir + "JERDOWN/Wprime1800Right_JERDOWN.root");
      ch_wp1900R_JERDOWN . Add(indir + "JERDOWN/Wprime1900Right_JERDOWN.root");
      ch_wp2000R_JERDOWN . Add(indir + "JERDOWN/Wprime2000Right_JERDOWN.root");
      ch_wp2100R_JERDOWN . Add(indir + "JERDOWN/Wprime2100Right_JERDOWN.root");
      ch_wp2200R_JERDOWN . Add(indir + "JERDOWN/Wprime2200Right_JERDOWN.root");
      ch_wp2300R_JERDOWN . Add(indir + "JERDOWN/Wprime2300Right_JERDOWN.root");
      ch_wp2400R_JERDOWN . Add(indir + "JERDOWN/Wprime2400Right_JERDOWN.root");
      ch_wp2500R_JERDOWN . Add(indir + "JERDOWN/Wprime2500Right_JERDOWN.root");
      ch_wp2600R_JERDOWN . Add(indir + "JERDOWN/Wprime2600Right_JERDOWN.root");
      ch_wp2700R_JERDOWN . Add(indir + "JERDOWN/Wprime2700Right_JERDOWN.root");
      ch_wp2800R_JERDOWN . Add(indir + "JERDOWN/Wprime2800Right_JERDOWN.root");
      ch_wp2900R_JERDOWN . Add(indir + "JERDOWN/Wprime2900Right_JERDOWN.root");
      ch_wp3000R_JERDOWN . Add(indir + "JERDOWN/Wprime3000Right_JERDOWN.root");
  
      ch_ttbar_matchingdown . Add(indir + "TTbar_matchingdown.root");
      ch_ttbar_matchingup . Add(indir + "TTbar_matchingup.root");
      ch_ttbar_scaledown . Add(indir + "TTbar_scaledown.root");
      ch_ttbar_scaleup . Add(indir + "TTbar_scaleup.root");
    }
  
    TCut cut_bkg;
    TCut cut_data;
    TCut cut_sig;
    TCut cut_sys;

    //for (int i=0; i<1; i++) { // training 1 btag    
    //for (int i=1; i<2; i++) { // yields 1 btag
    //for (int i=2; i<3; i++) { // training 2 btag
    for (int i=3; i<4; i++) { // yields 2 btag

      if (channel == "el"){

	if (i==0 || i==1) cut_data = yieldsData1tags_el;  
	if (i==0 || i==1) cut_sys = yieldsSys1tags_el;

	if (i==2 || i==3) cut_data = yieldsData2tags_el;  
	if (i==2 || i==3) cut_sys = yieldsSys2tags_el;
	
	if (i==0) {
	  cut_bkg = trainsampleBkg1tags_el;
	  cut_sig = trainsampleSig1tags_el;
	  outfile = "TrainingSamples/TrainingTrees_1BTag_el.root";
	}      
	if (i==1){
	  cut_bkg = yieldsampleBkg1tags_el;
	  cut_sig = yieldsampleSig1tags_el;
	  outfile = "YieldSamples/YieldsTrees_1BTag_el.root";
	}
	if (i==2){
	  cut_bkg = trainsampleBkg2tags_el;
	  cut_sig = trainsampleSig2tags_el;
	  outfile = "TrainingSamples/TrainingTrees_2BTag_el.root";
	}      
	if (i==3){
	  cut_bkg = yieldsampleBkg2tags_el;
	  cut_sig = yieldsampleSig2tags_el;
	  outfile = "YieldSamples/YieldsTrees_2BTag_el.root";
	}

      }

      if (channel == "mu"){
	if (i==0 || i==1) cut_data = yieldsData1tags_mu;  
	if (i==0 || i==1) cut_sys = yieldsSys1tags_mu;

	if (i==2 || i==3) cut_data = yieldsData2tags_mu;  
	if (i==2 || i==3) cut_sys = yieldsSys2tags_mu;
	
	if (i==0) {
	  cut_bkg = trainsampleBkg1tags_mu;
	  cut_sig = trainsampleSig1tags_mu;
	  outfile = "TrainingSamples/TrainingTrees_1BTag_mu.root";
	}      
	if (i==1){
	  cut_bkg = yieldsampleBkg1tags_mu;
	  cut_sig = yieldsampleSig1tags_mu;
	  outfile = "YieldSamples/YieldsTrees_1BTag_mu.root";
	}      
	if (i==2){
	  cut_bkg = trainsampleBkg2tags_mu;
	  cut_sig = trainsampleSig2tags_mu;
	  outfile = "TrainingSamples/TrainingTrees_2BTag_mu.root";
	}      
	if (i==3){
	  cut_bkg = yieldsampleBkg2tags_mu;
	  cut_sig = yieldsampleSig2tags_mu;
	  outfile = "YieldSamples/YieldsTrees_2BTag_mu.root";
	}

      }

      std::cout<< channel << " " << outfile <<std::endl;
      std::cout << "cut_bkg " << cut_bkg.GetTitle() << std::endl;
      std::cout << "cut_data " << cut_data.GetTitle() << std::endl;
      std::cout << "cut_sig " << cut_sig.GetTitle() << std::endl;
      std::cout << "cut_sys " << cut_sys.GetTitle() << std::endl;

      TFile * out_file = new TFile(outfile, "RECREATE");
      out_file->cd();
      std::cout << "writing " << outfile << std::endl;

      if (channel == "el"){
	if (i==1 || i==3){
	  ch_data . Add(indir + "Data_el_19pt6fb.root");
	  ch_data . SetBranchStatus("*",1);
	  _data =  ch_data . CopyTree(cut_data);
	  _data->SetName("data");
	}
      }

      if (channel == "mu"){
	if (i==1 || i==3){
	  ch_data . Add(indir + "Data_mu_19pt6fb.root");
	  ch_data . SetBranchStatus("*",1);
	  _data = ch_data . CopyTree(cut_data);
	  _data->SetName("data");
	}
      }

      if (i==1 || i==3)  { 
	_data->Write();
	_data->Delete();
	std::cout << " wrote data ======== " << std::endl;
      }

      std::cout<<"starting ttbar..."<<std::endl;
          ch_ttbar . SetBranchStatus("*",1); 
      _ttbar = ch_ttbar . CopyTree(cut_bkg);
      _ttbar->SetName("ttbar");
      if (ifsys && (i==1 || i==3)) {
	ch_ttbar_JESUP . SetBranchStatus("*",1);
        _ttbar_JESUP = ch_ttbar_JESUP . CopyTree(cut_sys);
	_ttbar_JESUP->SetName("ttbar_JESUP"); 

	ch_ttbar_JESDOWN . SetBranchStatus("*",1);
	_ttbar_JESDOWN = ch_ttbar_JESDOWN . CopyTree(cut_sys);
	_ttbar_JESDOWN->SetName("ttbar_JESDOWN"); 

	ch_ttbar_BTAGUP . SetBranchStatus("*",1);
	_ttbar_BTAGUP = ch_ttbar_BTAGUP . CopyTree(cut_sys);
	_ttbar_BTAGUP->SetName("ttbar_BTAGUP"); 

	ch_ttbar_BTAGDOWN . SetBranchStatus("*",1);
	_ttbar_BTAGDOWN = ch_ttbar_BTAGDOWN . CopyTree(cut_sys);
	_ttbar_BTAGDOWN->SetName("ttbar_BTAGDOWN"); 

	ch_ttbar_JERUP . SetBranchStatus("*",1);
	_ttbar_JERUP = ch_ttbar_JERUP . CopyTree(cut_sys);
	_ttbar_JERUP->SetName("ttbar_JERUP"); 

	ch_ttbar_JERDOWN . SetBranchStatus("*",1);
	_ttbar_JERDOWN = ch_ttbar_JERDOWN . CopyTree(cut_sys);
	_ttbar_JERDOWN->SetName("ttbar_JERDOWN"); 
      }

      _ttbar->Write();
      _ttbar->Delete();
      if (ifsys && (i==1 || i==3)) {
	_ttbar_JESUP->Write();
	_ttbar_JESDOWN->Write();
	_ttbar_BTAGUP->Write();
	_ttbar_BTAGDOWN->Write();
	_ttbar_JERUP->Write();
	_ttbar_JERDOWN->Write();

	_ttbar_JESUP->Delete();
	_ttbar_JESDOWN->Delete();
	_ttbar_BTAGUP->Delete();
	_ttbar_BTAGDOWN->Delete();
	_ttbar_JERUP->Delete();
	_ttbar_JERDOWN->Delete();
      }
      std::cout << " wrote ttbar ======== " << std::endl;

      std::cout<<"starting w[n]jets..."<<std::endl; 
      ch_w1jets . SetBranchStatus("*",1); 
      _w1jets = ch_w1jets . CopyTree(cut_bkg);
      _w1jets->SetName("w1jets");
      _w1jets->Write();
      _w1jets->Delete();
      ch_w2jets . SetBranchStatus("*",1); 
      _w2jets = ch_w2jets . CopyTree(cut_bkg);
      _w2jets->SetName("w2jets");
      _w2jets->Write();
      _w2jets->Delete();
      ch_w3jets . SetBranchStatus("*",1); 
      _w3jets = ch_w3jets . CopyTree(cut_bkg);
      _w3jets->SetName("w3jets");
      _w3jets->Write();
      _w3jets->Delete();
      ch_w4jets . SetBranchStatus("*",1); 
      _w4jets = ch_w4jets . CopyTree(cut_bkg);
      _w4jets->SetName("w4jets");
      _w4jets->Write();
      _w4jets->Delete();
      
      if (ifsys && (i==1 || i==3)) {
	ch_w1jets_JESUP . SetBranchStatus("*",1);
	_w1jets_JESUP = ch_w1jets_JESUP . CopyTree(cut_sys);
	_w1jets_JESUP->SetName("w1jets_JESUP"); 
	ch_w1jets_JESDOWN . SetBranchStatus("*",1);
	_w1jets_JESDOWN = ch_w1jets_JESDOWN . CopyTree(cut_sys);
	_w1jets_JESDOWN->SetName("w1jets_JESDOWN"); 
	ch_w1jets_BTAGUP . SetBranchStatus("*",1);
	_w1jets_BTAGUP = ch_w1jets_BTAGUP . CopyTree(cut_sys);
	_w1jets_BTAGUP->SetName("w1jets_BTAGUP"); 
	ch_w1jets_BTAGDOWN . SetBranchStatus("*",1);
	_w1jets_BTAGDOWN = ch_w1jets_BTAGDOWN . CopyTree(cut_sys);
	_w1jets_BTAGDOWN->SetName("w1jets_BTAGDOWN"); 
	ch_w1jets_JERUP . SetBranchStatus("*",1);
	_w1jets_JERUP = ch_w1jets_JERUP . CopyTree(cut_sys);
	_w1jets_JERUP->SetName("w1jets_JERUP"); 
	ch_w1jets_JERDOWN . SetBranchStatus("*",1);
	_w1jets_JERDOWN = ch_w1jets_JERDOWN . CopyTree(cut_sys);
	_w1jets_JERDOWN->SetName("w1jets_JERDOWN"); 

	_w1jets_JESUP->Write();
	_w1jets_JESDOWN->Write();
	_w1jets_BTAGUP->Write();
	_w1jets_BTAGDOWN->Write();
	_w1jets_JERUP->Write();
	_w1jets_JERDOWN->Write();
	_w1jets_JESUP->Delete();
	_w1jets_JESDOWN->Delete();
	_w1jets_BTAGUP->Delete();
	_w1jets_BTAGDOWN->Delete();
	_w1jets_JERUP->Delete();
	_w1jets_JERDOWN->Delete();

	ch_w2jets_JESUP . SetBranchStatus("*",1);
	_w2jets_JESUP = ch_w2jets_JESUP . CopyTree(cut_sys);
	_w2jets_JESUP->SetName("w2jets_JESUP"); 
	ch_w2jets_JESDOWN . SetBranchStatus("*",1);
	_w2jets_JESDOWN = ch_w2jets_JESDOWN . CopyTree(cut_sys);
	_w2jets_JESDOWN->SetName("w2jets_JESDOWN"); 
	ch_w2jets_BTAGUP . SetBranchStatus("*",1);
	_w2jets_BTAGUP = ch_w2jets_BTAGUP . CopyTree(cut_sys);
	_w2jets_BTAGUP->SetName("w2jets_BTAGUP"); 
	ch_w2jets_BTAGDOWN . SetBranchStatus("*",1);
	_w2jets_BTAGDOWN = ch_w2jets_BTAGDOWN . CopyTree(cut_sys);
	_w2jets_BTAGDOWN->SetName("w2jets_BTAGDOWN"); 
	ch_w2jets_JERUP . SetBranchStatus("*",1);
	_w2jets_JERUP = ch_w2jets_JERUP . CopyTree(cut_sys);
	_w2jets_JERUP->SetName("w2jets_JERUP"); 
	ch_w2jets_JERDOWN . SetBranchStatus("*",1);
	_w2jets_JERDOWN = ch_w2jets_JERDOWN . CopyTree(cut_sys);
	_w2jets_JERDOWN->SetName("w2jets_JERDOWN"); 

	_w2jets_JESUP->Write();
	_w2jets_JESDOWN->Write();
	_w2jets_BTAGUP->Write();
	_w2jets_BTAGDOWN->Write();
	_w2jets_JERUP->Write();
	_w2jets_JERDOWN->Write();
	_w2jets_JESUP->Delete();
	_w2jets_JESDOWN->Delete();
	_w2jets_BTAGUP->Delete();
	_w2jets_BTAGDOWN->Delete();
	_w2jets_JERUP->Delete();
	_w2jets_JERDOWN->Delete();

	ch_w3jets_JESUP . SetBranchStatus("*",1);
	_w3jets_JESUP = ch_w3jets_JESUP . CopyTree(cut_sys);
	_w3jets_JESUP->SetName("w3jets_JESUP"); 
	ch_w3jets_JESDOWN . SetBranchStatus("*",1);
	_w3jets_JESDOWN = ch_w3jets_JESDOWN . CopyTree(cut_sys);
	_w3jets_JESDOWN->SetName("w3jets_JESDOWN"); 
	ch_w3jets_BTAGUP . SetBranchStatus("*",1);
	_w3jets_BTAGUP = ch_w3jets_BTAGUP . CopyTree(cut_sys);
	_w3jets_BTAGUP->SetName("w3jets_BTAGUP"); 
	ch_w3jets_BTAGDOWN . SetBranchStatus("*",1);
	_w3jets_BTAGDOWN = ch_w3jets_BTAGDOWN . CopyTree(cut_sys);
	_w3jets_BTAGDOWN->SetName("w3jets_BTAGDOWN"); 
	ch_w3jets_JERUP . SetBranchStatus("*",1);
	_w3jets_JERUP = ch_w3jets_JERUP . CopyTree(cut_sys);
	_w3jets_JERUP->SetName("w3jets_JERUP"); 
	ch_w3jets_JERDOWN . SetBranchStatus("*",1);
	_w3jets_JERDOWN = ch_w3jets_JERDOWN . CopyTree(cut_sys);
	_w3jets_JERDOWN->SetName("w3jets_JERDOWN"); 

	_w3jets_JESUP->Write();
	_w3jets_JESDOWN->Write();
	_w3jets_BTAGUP->Write();
	_w3jets_BTAGDOWN->Write();
	_w3jets_JERUP->Write();
	_w3jets_JERDOWN->Write();
	_w3jets_JESUP->Delete();
	_w3jets_JESDOWN->Delete();
	_w3jets_BTAGUP->Delete();
	_w3jets_BTAGDOWN->Delete();
	_w3jets_JERUP->Delete();
	_w3jets_JERDOWN->Delete();

	ch_w4jets_JESUP . SetBranchStatus("*",1);
	_w4jets_JESUP = ch_w4jets_JESUP . CopyTree(cut_sys);
	_w4jets_JESUP->SetName("w4jets_JESUP"); 
	ch_w4jets_JESDOWN . SetBranchStatus("*",1);
	_w4jets_JESDOWN = ch_w4jets_JESDOWN . CopyTree(cut_sys);
	_w4jets_JESDOWN->SetName("w4jets_JESDOWN"); 
	ch_w4jets_BTAGUP . SetBranchStatus("*",1);
	_w4jets_BTAGUP = ch_w4jets_BTAGUP . CopyTree(cut_sys);
	_w4jets_BTAGUP->SetName("w4jets_BTAGUP"); 
	ch_w4jets_BTAGDOWN . SetBranchStatus("*",1);
	_w4jets_BTAGDOWN = ch_w4jets_BTAGDOWN . CopyTree(cut_sys);
	_w4jets_BTAGDOWN->SetName("w4jets_BTAGDOWN"); 
	ch_w4jets_JERUP . SetBranchStatus("*",1);
	_w4jets_JERUP = ch_w4jets_JERUP . CopyTree(cut_sys);
	_w4jets_JERUP->SetName("w4jets_JERUP"); 
	ch_w4jets_JERDOWN . SetBranchStatus("*",1);
	_w4jets_JERDOWN = ch_w4jets_JERDOWN . CopyTree(cut_sys);
	_w4jets_JERDOWN->SetName("w4jets_JERDOWN"); 

	_w4jets_JESUP->Write();
	_w4jets_JESDOWN->Write();
	_w4jets_BTAGUP->Write();
	_w4jets_BTAGDOWN->Write();
	_w4jets_JERUP->Write();
	_w4jets_JERDOWN->Write();
	_w4jets_JESUP->Delete();
	_w4jets_JESDOWN->Delete();
	_w4jets_BTAGUP->Delete();
	_w4jets_BTAGDOWN->Delete();
	_w4jets_JERUP->Delete();
	_w4jets_JERDOWN->Delete();

      }
      std::cout << " wrote w[n]jets ======== " << std::endl;

      std::cout<<"starting s..."<<std::endl;
      ch_s . SetBranchStatus("*",1); 
      _s = ch_s . CopyTree(cut_bkg);
      _s->SetName("s");
      if (ifsys && (i==1 || i==3)) {
	ch_s_JESUP . SetBranchStatus("*",1);
	_s_JESUP = ch_s_JESUP . CopyTree(cut_sys);
	_s_JESUP->SetName("s_JESUP"); 

	ch_s_JESDOWN . SetBranchStatus("*",1);
	_s_JESDOWN = ch_s_JESDOWN . CopyTree(cut_sys);
	_s_JESDOWN->SetName("s_JESDOWN"); 

	ch_s_BTAGUP . SetBranchStatus("*",1);
	_s_BTAGUP = ch_s_BTAGUP . CopyTree(cut_sys);
	_s_BTAGUP->SetName("s_BTAGUP"); 

	ch_s_BTAGDOWN . SetBranchStatus("*",1);
	_s_BTAGDOWN = ch_s_BTAGDOWN . CopyTree(cut_sys);
	_s_BTAGDOWN->SetName("s_BTAGDOWN"); 

	ch_s_JERUP . SetBranchStatus("*",1);
	_s_JERUP = ch_s_JERUP . CopyTree(cut_sys);
	_s_JERUP->SetName("s_JERUP"); 

	ch_s_JERDOWN . SetBranchStatus("*",1);
	_s_JERDOWN = ch_s_JERDOWN . CopyTree(cut_sys);
	_s_JERDOWN->SetName("s_JERDOWN"); 

      }
      _s->Write();
      _s->Delete();
      if (ifsys && (i==1 || i==3)) {
	_s_JESUP->Write();
	_s_JESDOWN->Write();
	_s_BTAGUP->Write();
	_s_BTAGDOWN->Write();
	_s_JERUP->Write();
	_s_JERDOWN->Write();

	_s_JESUP->Delete();
	_s_JESDOWN->Delete();
	_s_BTAGUP->Delete();
	_s_BTAGDOWN->Delete();
	_s_JERUP->Delete();
	_s_JERDOWN->Delete();
      }
      std::cout << " wrote s ======== " << std::endl;

      std::cout<<"starting bs..."<<std::endl;
      ch_bs . SetBranchStatus("*",1); 
      _bs = ch_bs . CopyTree(cut_bkg);
      _bs->SetName("bs");
      if (ifsys && (i==1 || i==3)) {
	ch_bs_JESUP . SetBranchStatus("*",1);
	_bs_JESUP = ch_bs_JESUP . CopyTree(cut_sys);
	_bs_JESUP->SetName("bs_JESUP"); 

	ch_bs_JESDOWN . SetBranchStatus("*",1);
	_bs_JESDOWN = ch_bs_JESDOWN . CopyTree(cut_sys);
	_bs_JESDOWN->SetName("bs_JESDOWN"); 

	ch_bs_BTAGUP . SetBranchStatus("*",1);
	_bs_BTAGUP = ch_bs_BTAGUP . CopyTree(cut_sys);
	_bs_BTAGUP->SetName("bs_BTAGUP"); 

	ch_bs_BTAGDOWN . SetBranchStatus("*",1);
	_bs_BTAGDOWN = ch_bs_BTAGDOWN . CopyTree(cut_sys);
	_bs_BTAGDOWN->SetName("bs_BTAGDOWN"); 

	ch_bs_JERUP . SetBranchStatus("*",1);
	_bs_JERUP = ch_bs_JERUP . CopyTree(cut_sys);
	_bs_JERUP->SetName("bs_JERUP"); 

	ch_bs_JERDOWN . SetBranchStatus("*",1);
	_bs_JERDOWN = ch_bs_JERDOWN . CopyTree(cut_sys);
	_bs_JERDOWN->SetName("bs_JERDOWN"); 
      }
      _bs->Write();
      _bs->Delete();
      if (ifsys && (i==1 || i==3)) {
	_bs_JESUP->Write();
	_bs_JESDOWN->Write();
	_bs_BTAGUP->Write();
	_bs_BTAGDOWN->Write();
	_bs_JERUP->Write();
	_bs_JERDOWN->Write();

	_bs_JESUP->Delete();
	_bs_JESDOWN->Delete();
	_bs_BTAGUP->Delete();
	_bs_BTAGDOWN->Delete();
	_bs_JERUP->Delete();
	_bs_JERDOWN->Delete();
      }
      std::cout << " wrote bs ======== " << std::endl;
 
      std::cout << " starting t..." << std::endl;
      ch_t . SetBranchStatus("*",1); 
      _t = ch_t . CopyTree(cut_bkg);
      _t->SetName("t");
      if (ifsys && (i==1 || i==3)) {
	ch_t_JESUP . SetBranchStatus("*",1);
	_t_JESUP = ch_t_JESUP . CopyTree(cut_sys);
	_t_JESUP->SetName("t_JESUP"); 

	ch_t_JESDOWN . SetBranchStatus("*",1);
	_t_JESDOWN = ch_t_JESDOWN . CopyTree(cut_sys);
	_t_JESDOWN->SetName("t_JESDOWN"); 

	ch_t_BTAGUP . SetBranchStatus("*",1);
	_t_BTAGUP = ch_t_BTAGUP . CopyTree(cut_sys);
	_t_BTAGUP->SetName("t_BTAGUP"); 

	ch_t_BTAGDOWN . SetBranchStatus("*",1);
	_t_BTAGDOWN = ch_t_BTAGDOWN . CopyTree(cut_sys);
	_t_BTAGDOWN->SetName("t_BTAGDOWN"); 

	ch_t_JERUP . SetBranchStatus("*",1);
	_t_JERUP = ch_t_JERUP . CopyTree(cut_sys);
	_t_JERUP->SetName("t_JERUP"); 

	ch_t_JERDOWN . SetBranchStatus("*",1);
	_t_JERDOWN = ch_t_JERDOWN . CopyTree(cut_sys);
	_t_JERDOWN->SetName("t_JERDOWN"); 
      }
      _t->Write();
      _t->Delete();
      if (ifsys && (i==1 || i==3)) {
	_t_JESUP->Write();
	_t_JESDOWN->Write();
	_t_BTAGUP->Write();
	_t_BTAGDOWN->Write();
	_t_JERUP->Write();
	_t_JERDOWN->Write();

	_t_JESUP->Delete();
	_t_JESDOWN->Delete();
	_t_BTAGUP->Delete();
	_t_BTAGDOWN->Delete();
	_t_JERUP->Delete();
	_t_JERDOWN->Delete();
      }
      std::cout << " wrote t ======== " << std::endl;

      std::cout << " starting bt... " << std::endl;
      ch_bt . SetBranchStatus("*",1); 
      _bt = ch_bt . CopyTree(cut_bkg);
      _bt->SetName("bt");
      if (ifsys && (i==1 || i==3)) {
	ch_bt_JESUP . SetBranchStatus("*",1);
	_bt_JESUP = ch_bt_JESUP . CopyTree(cut_sys);
	_bt_JESUP->SetName("bt_JESUP"); 

	ch_bt_JESDOWN . SetBranchStatus("*",1);
	_bt_JESDOWN = ch_bt_JESDOWN . CopyTree(cut_sys);
	_bt_JESDOWN->SetName("bt_JESDOWN"); 

	ch_bt_BTAGUP . SetBranchStatus("*",1);
	_bt_BTAGUP = ch_bt_BTAGUP . CopyTree(cut_sys);
	_bt_BTAGUP->SetName("bt_BTAGUP"); 

	ch_bt_BTAGDOWN . SetBranchStatus("*",1);
	_bt_BTAGDOWN = ch_bt_BTAGDOWN . CopyTree(cut_sys);
	_bt_BTAGDOWN->SetName("bt_BTAGDOWN"); 

	ch_bt_JERUP . SetBranchStatus("*",1);
	_bt_JERUP = ch_bt_JERUP . CopyTree(cut_sys);
	_bt_JERUP->SetName("bt_JERUP"); 

	ch_bt_JERDOWN . SetBranchStatus("*",1);
	_bt_JERDOWN = ch_bt_JERDOWN . CopyTree(cut_sys);
	_bt_JERDOWN->SetName("bt_JERDOWN"); 
      }
      _bt->Write();
      _bt->Delete();
      if (ifsys && (i==1 || i==3)) {
	_bt_JESUP->Write();
	_bt_JESDOWN->Write();
	_bt_BTAGUP->Write();
	_bt_BTAGDOWN->Write();
	_bt_JERUP->Write();
	_bt_JERDOWN->Write();

	_bt_JESUP->Delete();
	_bt_JESDOWN->Delete();
	_bt_BTAGUP->Delete();
	_bt_BTAGDOWN->Delete();
	_bt_JERUP->Delete();
	_bt_JERDOWN->Delete();
      }
      std::cout << " wrote bt ======== " << std::endl;

      std::cout << " starting tw... " << std::endl;
      ch_tw . SetBranchStatus("*",1); 
      _tw = ch_tw . CopyTree(cut_bkg);
      _tw->SetName("tw");
      if (ifsys && (i==1 || i==3)) {
	ch_tw_JESUP . SetBranchStatus("*",1);
	_tw_JESUP = ch_tw_JESUP . CopyTree(cut_sys);
	_tw_JESUP->SetName("tw_JESUP"); 

	ch_tw_JESDOWN . SetBranchStatus("*",1);
	_tw_JESDOWN = ch_tw_JESDOWN . CopyTree(cut_sys);
	_tw_JESDOWN->SetName("tw_JESDOWN"); 

	ch_tw_BTAGUP . SetBranchStatus("*",1);
	TTree * t_tw_BTAGUP = ch_tw_BTAGUP . CopyTree(cut_sys);
	_tw_BTAGUP = t_tw_BTAGUP->CopyTree("","");
	_tw_BTAGUP->SetName("tw_BTAGUP"); 

	ch_tw_BTAGDOWN . SetBranchStatus("*",1);
	_tw_BTAGDOWN = ch_tw_BTAGDOWN . CopyTree(cut_sys);
	_tw_BTAGDOWN->SetName("tw_BTAGDOWN"); 

	ch_tw_JERUP . SetBranchStatus("*",1);
	_tw_JERUP = ch_tw_JERUP . CopyTree(cut_sys);
	_tw_JERUP->SetName("tw_JERUP"); 

	ch_tw_JERDOWN . SetBranchStatus("*",1);
	_tw_JERDOWN = ch_tw_JERDOWN . CopyTree(cut_sys);
	_tw_JERDOWN->SetName("tw_JERDOWN"); 
      }
      _tw->Write();
      _tw->Delete();
      if (ifsys && (i==1 || i==3)) {
	_tw_JESUP->Write();
	_tw_JESDOWN->Write();
	_tw_BTAGUP->Write();
	_tw_BTAGDOWN->Write();
	_tw_JERUP->Write();
	_tw_JERDOWN->Write();

	_tw_JESUP->Delete();
	_tw_JESDOWN->Delete();
	_tw_BTAGUP->Delete();
	_tw_BTAGDOWN->Delete();
	_tw_JERUP->Delete();
	_tw_JERDOWN->Delete();
      }
      std::cout << " wrote tw ======== " << std::endl;

      std::cout << " starting btw... " << std::endl;
      ch_btw . SetBranchStatus("*",1); 
      _btw = ch_btw . CopyTree(cut_bkg);
      _btw->SetName("btw");

      if (ifsys && (i==1 || i==3)) {
	ch_btw_JESUP . SetBranchStatus("*",1);
	_btw_JESUP = ch_btw_JESUP . CopyTree(cut_sys);
	_btw_JESUP->SetName("btw_JESUP"); 

	ch_btw_JESDOWN . SetBranchStatus("*",1);
	_btw_JESDOWN = ch_btw_JESDOWN . CopyTree(cut_sys);
	_btw_JESDOWN->SetName("btw_JESDOWN"); 

	ch_btw_BTAGUP . SetBranchStatus("*",1);
	_btw_BTAGUP = ch_btw_BTAGUP . CopyTree(cut_sys);
	_btw_BTAGUP->SetName("btw_BTAGUP"); 

	ch_btw_BTAGDOWN . SetBranchStatus("*",1);
	_btw_BTAGDOWN = ch_btw_BTAGDOWN . CopyTree(cut_sys);
	_btw_BTAGDOWN->SetName("btw_BTAGDOWN"); 

	ch_btw_JERUP . SetBranchStatus("*",1);
	_btw_JERUP = ch_btw_JERUP . CopyTree(cut_sys);
	_btw_JERUP->SetName("btw_JERUP"); 

	ch_btw_JERDOWN . SetBranchStatus("*",1);
	_btw_JERDOWN = ch_btw_JERDOWN . CopyTree(cut_sys);
	_btw_JERDOWN->SetName("btw_JERDOWN"); 
      }
      _btw->Write();
      _btw->Delete();
      if (ifsys && (i==1 || i==3)) {
	_btw_JESUP->Write();
	_btw_JESDOWN->Write();
	_btw_BTAGUP->Write();
	_btw_BTAGDOWN->Write();
	_btw_JERUP->Write();
	_btw_JERDOWN->Write();

	_btw_JESUP->Delete();
	_btw_JESDOWN->Delete();
	_btw_BTAGUP->Delete();
	_btw_BTAGDOWN->Delete();
	_btw_JERUP->Delete();
	_btw_JERDOWN->Delete();
      }
      std::cout << " wrote btw ======== " << std::endl;

      std::cout << " starting zjets... " << std::endl;
      ch_zjets . SetBranchStatus("*",1); 
      _zjets = ch_zjets . CopyTree(cut_bkg);
      _zjets->SetName("zjets");
      if (ifsys && (i==1 || i==3)) {
	ch_zjets_JESUP . SetBranchStatus("*",1);
	_zjets_JESUP = ch_zjets_JESUP . CopyTree(cut_sys);
	_zjets_JESUP->SetName("zjets_JESUP"); 

	ch_zjets_JESDOWN . SetBranchStatus("*",1);
	_zjets_JESDOWN = ch_zjets_JESDOWN . CopyTree(cut_sys);
	_zjets_JESDOWN->SetName("zjets_JESDOWN"); 

	ch_zjets_BTAGUP . SetBranchStatus("*",1);
	_zjets_BTAGUP = ch_zjets_BTAGUP . CopyTree(cut_sys);
	_zjets_BTAGUP->SetName("zjets_BTAGUP"); 

	ch_zjets_BTAGDOWN . SetBranchStatus("*",1);
	_zjets_BTAGDOWN = ch_zjets_BTAGDOWN . CopyTree(cut_sys);
	_zjets_BTAGDOWN->SetName("zjets_BTAGDOWN"); 

	ch_zjets_JERUP . SetBranchStatus("*",1);
	_zjets_JERUP = ch_zjets_JERUP . CopyTree(cut_sys);
	_zjets_JERUP->SetName("zjets_JERUP"); 

	ch_zjets_JERDOWN . SetBranchStatus("*",1);
	_zjets_JERDOWN = ch_zjets_JERDOWN . CopyTree(cut_sys);
	_zjets_JERDOWN->SetName("zjets_JERDOWN"); 
      }
      _zjets->Write();
      _zjets->Delete();
      if (ifsys && (i==1 || i==3)) {
	_zjets_JESUP->Write();
	_zjets_JESDOWN->Write();
	_zjets_BTAGUP->Write();
	_zjets_BTAGDOWN->Write();
	_zjets_JERUP->Write();
	_zjets_JERDOWN->Write();

	_zjets_JESUP->Delete();
	_zjets_JESDOWN->Delete();
	_zjets_BTAGUP->Delete();
	_zjets_BTAGDOWN->Delete();
	_zjets_JERUP->Delete();
	_zjets_JERDOWN->Delete();
      }
      std::cout << " wrote zjets ======== " << std::endl;

      std::cout << " starting ww... " << std::endl;
      ch_ww . SetBranchStatus("*",1); 
      _ww = ch_ww . CopyTree(cut_bkg);
      _ww->SetName("ww");
      if (ifsys && (i==1 || i==3)) {
	ch_ww_JESUP . SetBranchStatus("*",1);
	_ww_JESUP = ch_ww_JESUP . CopyTree(cut_sys);
	_ww_JESUP->SetName("ww_JESUP"); 

	ch_ww_JESDOWN . SetBranchStatus("*",1);
	_ww_JESDOWN = ch_ww_JESDOWN . CopyTree(cut_sys);
	_ww_JESDOWN->SetName("ww_JESDOWN"); 

	ch_ww_BTAGUP . SetBranchStatus("*",1);
	_ww_BTAGUP = ch_ww_BTAGUP . CopyTree(cut_sys);
	_ww_BTAGUP->SetName("ww_BTAGUP"); 

	ch_ww_BTAGDOWN . SetBranchStatus("*",1);
	_ww_BTAGDOWN = ch_ww_BTAGDOWN . CopyTree(cut_sys);
	_ww_BTAGDOWN->SetName("ww_BTAGDOWN"); 

	ch_ww_JERUP . SetBranchStatus("*",1);
	_ww_JERUP = ch_ww_JERUP . CopyTree(cut_sys);
	_ww_JERUP->SetName("ww_JERUP"); 

	ch_ww_JERDOWN . SetBranchStatus("*",1);
	_ww_JERDOWN = ch_ww_JERDOWN . CopyTree(cut_sys);
	_ww_JERDOWN->SetName("ww_JERDOWN"); 
      }
      _ww->Write();
      _ww->Delete();
      if (ifsys && (i==1 || i==3)) {
	_ww_JESUP->Write();
	_ww_JESDOWN->Write();
	_ww_BTAGUP->Write();
	_ww_BTAGDOWN->Write();
	_ww_JERUP->Write();
	_ww_JERDOWN->Write();

	_ww_JESUP->Delete();
	_ww_JESDOWN->Delete();
	_ww_BTAGUP->Delete();
	_ww_BTAGDOWN->Delete();
	_ww_JERUP->Delete();
	_ww_JERDOWN->Delete();
      }
      std::cout << " wrote ww ======== " << std::endl;

      if (channel == "el") {
	std::cout << " starting qcd... " << std::endl;
	ch_qcd80to170 . SetBranchStatus("*",1); 
	_qcd80to170 = ch_qcd80to170 . CopyTree(cut_bkg);
	_qcd80to170->SetName("qcd80to170");
	_qcd80to170->Write();
	_qcd80to170->Delete();
	std::cout << " starting qcd1... " << std::endl;

	ch_qcd170to250 . SetBranchStatus("*",1); 
	_qcd170to250 = ch_qcd170to250 . CopyTree(cut_bkg);
	_qcd170to250->SetName("qcd170to250");
	_qcd170to250->Write();
	_qcd170to250->Delete();
	std::cout << " starting qcd2... " << std::endl;

	ch_qcd250to350 . SetBranchStatus("*",1); 
	_qcd250to350 = ch_qcd250to350 . CopyTree(cut_bkg);
	_qcd250to350->SetName("qcd250to350");
	_qcd250to350->Write();
	_qcd250to350->Delete();
	std::cout << " starting qcd3... " << std::endl;

	ch_qcd350 . SetBranchStatus("*",1); 
	_qcd350 = ch_qcd350 . CopyTree(cut_bkg);
	_qcd350->SetName("qcd350");
	_qcd350->Write();
	_qcd350->Delete();
	std::cout << " starting qcd4... " << std::endl;

	if (ifsys && (i==1 || i==3)) {
	  ch_qcd80to170_JESUP . SetBranchStatus("*",1);
	  _qcd80to170_JESUP = ch_qcd80to170_JESUP . CopyTree(cut_sys);
	  _qcd80to170_JESUP->SetName("qcd80to170_JESUP"); 
	  _qcd80to170_JESUP->Write();
	  _qcd80to170_JESUP->Delete();
	  ch_qcd80to170_JESDOWN . SetBranchStatus("*",1);
	  _qcd80to170_JESDOWN = ch_qcd80to170_JESDOWN . CopyTree(cut_sys);
	  _qcd80to170_JESDOWN->SetName("qcd80to170_JESDOWN"); 
	  _qcd80to170_JESDOWN->Write();
	  _qcd80to170_JESDOWN->Delete();
	  ch_qcd80to170_BTAGUP . SetBranchStatus("*",1);
	  _qcd80to170_BTAGUP = ch_qcd80to170_BTAGUP . CopyTree(cut_sys);
	  _qcd80to170_BTAGUP->SetName("qcd80to170_BTAGUP"); 
	  _qcd80to170_BTAGUP->Write();
	  _qcd80to170_BTAGUP->Delete();
	  ch_qcd80to170_BTAGDOWN . SetBranchStatus("*",1);
	  _qcd80to170_BTAGDOWN = ch_qcd80to170_BTAGDOWN . CopyTree(cut_sys);
	  _qcd80to170_BTAGDOWN->SetName("qcd80to170_BTAGDOWN"); 
	  _qcd80to170_BTAGDOWN->Write();
	  _qcd80to170_BTAGDOWN->Delete();
	  ch_qcd80to170_JERUP . SetBranchStatus("*",1);
	  _qcd80to170_JERUP = ch_qcd80to170_JERUP . CopyTree(cut_sys);
	  _qcd80to170_JERUP->SetName("qcd80to170_JERUP"); 
	  _qcd80to170_JERUP->Write();
	  _qcd80to170_JERUP->Delete();
	  ch_qcd80to170_JERDOWN . SetBranchStatus("*",1);
	  _qcd80to170_JERDOWN = ch_qcd80to170_JERDOWN . CopyTree(cut_sys);
	  _qcd80to170_JERDOWN->SetName("qcd80to170_JERDOWN"); 
	  _qcd80to170_JERDOWN->Write();
	  _qcd80to170_JERDOWN->Delete();
      std::cout << " starting qcd5... " << std::endl;

	  ch_qcd170to250_JESUP . SetBranchStatus("*",1);
	  _qcd170to250_JESUP = ch_qcd170to250_JESUP . CopyTree(cut_sys);
	  _qcd170to250_JESUP->SetName("qcd170to250_JESUP"); 
	  _qcd170to250_JESUP->Write();
	  _qcd170to250_JESUP->Delete();
	  ch_qcd170to250_JESDOWN . SetBranchStatus("*",1);
	  _qcd170to250_JESDOWN = ch_qcd170to250_JESDOWN . CopyTree(cut_sys);
	  _qcd170to250_JESDOWN->SetName("qcd170to250_JESDOWN"); 
	  _qcd170to250_JESDOWN->Write();
	  _qcd170to250_JESDOWN->Delete();
	  ch_qcd170to250_BTAGUP . SetBranchStatus("*",1);
	  _qcd170to250_BTAGUP = ch_qcd170to250_BTAGUP . CopyTree(cut_sys);
	  _qcd170to250_BTAGUP->SetName("qcd170to250_BTAGUP"); 
	  _qcd170to250_BTAGUP->Write();
	  _qcd170to250_BTAGUP->Delete();
	  ch_qcd170to250_BTAGDOWN . SetBranchStatus("*",1);
	  _qcd170to250_BTAGDOWN = ch_qcd170to250_BTAGDOWN . CopyTree(cut_sys);
	  _qcd170to250_BTAGDOWN->SetName("qcd170to250_BTAGDOWN"); 
	  _qcd170to250_BTAGDOWN->Write();
	  _qcd170to250_BTAGDOWN->Delete();
	  ch_qcd170to250_JERUP . SetBranchStatus("*",1);
	  _qcd170to250_JERUP = ch_qcd170to250_JERUP . CopyTree(cut_sys);
	  _qcd170to250_JERUP->SetName("qcd170to250_JERUP"); 
	  _qcd170to250_JERUP->Write();
	  _qcd170to250_JERUP->Delete();
	  ch_qcd170to250_JERDOWN . SetBranchStatus("*",1);
	  _qcd170to250_JERDOWN = ch_qcd170to250_JERDOWN . CopyTree(cut_sys);
	  _qcd170to250_JERDOWN->SetName("qcd170to250_JERDOWN"); 
	  _qcd170to250_JERDOWN->Write();
	  _qcd170to250_JERDOWN->Delete();
      std::cout << " starting qcd6... " << std::endl;

	  ch_qcd250to350_JESUP . SetBranchStatus("*",1);
	  _qcd250to350_JESUP = ch_qcd250to350_JESUP . CopyTree(cut_sys);
	  _qcd250to350_JESUP->SetName("qcd250to350_JESUP"); 
	  _qcd250to350_JESUP->Write();
	  _qcd250to350_JESUP->Delete();
	  ch_qcd250to350_JESDOWN . SetBranchStatus("*",1);
	  _qcd250to350_JESDOWN = ch_qcd250to350_JESDOWN . CopyTree(cut_sys);
	  _qcd250to350_JESDOWN->SetName("qcd250to350_JESDOWN"); 
	  _qcd250to350_JESDOWN->Write();
	  _qcd250to350_JESDOWN->Delete();
	  ch_qcd250to350_BTAGUP . SetBranchStatus("*",1);
	  _qcd250to350_BTAGUP = ch_qcd250to350_BTAGUP . CopyTree(cut_sys);
	  _qcd250to350_BTAGUP->SetName("qcd250to350_BTAGUP"); 
	  _qcd250to350_BTAGUP->Write();
	  _qcd250to350_BTAGUP->Delete();
	  ch_qcd250to350_BTAGDOWN . SetBranchStatus("*",1);
	  _qcd250to350_BTAGDOWN = ch_qcd250to350_BTAGDOWN . CopyTree(cut_sys);
	  _qcd250to350_BTAGDOWN->SetName("qcd250to350_BTAGDOWN"); 
	  _qcd250to350_BTAGDOWN->Write();
	  _qcd250to350_BTAGDOWN->Delete();
	  ch_qcd250to350_JERUP . SetBranchStatus("*",1);
	  _qcd250to350_JERUP = ch_qcd250to350_JERUP . CopyTree(cut_sys);
	  _qcd250to350_JERUP->SetName("qcd250to350_JERUP"); 
	  _qcd250to350_JERUP->Write();
	  _qcd250to350_JERUP->Delete();
	  ch_qcd250to350_JERDOWN . SetBranchStatus("*",1);
	  _qcd250to350_JERDOWN = ch_qcd250to350_JERDOWN . CopyTree(cut_sys);
	  _qcd250to350_JERDOWN->SetName("qcd250to350_JERDOWN"); 
	  _qcd250to350_JERDOWN->Write();
	  _qcd250to350_JERDOWN->Delete();
      std::cout << " starting qcd7... " << std::endl;

	  ch_qcd350_JESUP . SetBranchStatus("*",1);
	  _qcd350_JESUP = ch_qcd350_JESUP . CopyTree(cut_sys);
	  _qcd350_JESUP->SetName("qcd350_JESUP"); 
	  _qcd350_JESUP->Write();
	  _qcd350_JESUP->Delete();
	  ch_qcd350_JESDOWN . SetBranchStatus("*",1);
	  _qcd350_JESDOWN = ch_qcd350_JESDOWN . CopyTree(cut_sys);
	  _qcd350_JESDOWN->SetName("qcd350_JESDOWN"); 
	  _qcd350_JESDOWN->Write();
	  _qcd350_JESDOWN->Delete();
	  ch_qcd350_BTAGUP . SetBranchStatus("*",1);
	  _qcd350_BTAGUP = ch_qcd350_BTAGUP . CopyTree(cut_sys);
	  _qcd350_BTAGUP->SetName("qcd350_BTAGUP"); 
	  _qcd350_BTAGUP->Write();
	  _qcd350_BTAGUP->Delete();
	  ch_qcd350_BTAGDOWN . SetBranchStatus("*",1);
	  _qcd350_BTAGDOWN = ch_qcd350_BTAGDOWN . CopyTree(cut_sys);
	  _qcd350_BTAGDOWN->SetName("qcd350_BTAGDOWN"); 
	  _qcd350_BTAGDOWN->Write();
	  _qcd350_BTAGDOWN->Delete();
	  ch_qcd350_JERUP . SetBranchStatus("*",1);
	  _qcd350_JERUP = ch_qcd350_JERUP . CopyTree(cut_sys);
	  _qcd350_JERUP->SetName("qcd350_JERUP"); 
	  _qcd350_JERUP->Write();
	  _qcd350_JERUP->Delete();
	  ch_qcd350_JERDOWN . SetBranchStatus("*",1);
	  _qcd350_JERDOWN = ch_qcd350_JERDOWN . CopyTree(cut_sys);
	  _qcd350_JERDOWN->SetName("qcd350_JERDOWN"); 
	  _qcd350_JERDOWN->Write();
	  _qcd350_JERDOWN->Delete();
      std::cout << " starting qcd8... " << std::endl;

	}
      }
      std::cout << " wrote qcd ======== " << std::endl;

      if (ifsys && (i==1 || i==3)) {
	ch_ttbar_matchingup . SetBranchStatus("*",1);
	_ttbar_matchingup = ch_ttbar_matchingup . CopyTree(cut_bkg);
	_ttbar_matchingup->SetName("ttbar_matchingup"); 

	ch_ttbar_matchingdown . SetBranchStatus("*",1);
	_ttbar_matchingdown = ch_ttbar_matchingdown . CopyTree(cut_bkg);
	_ttbar_matchingdown->SetName("ttbar_matchingdown"); 

	ch_ttbar_scaleup . SetBranchStatus("*",1);
	_ttbar_scaleup = ch_ttbar_scaleup . CopyTree(cut_bkg);
	_ttbar_scaleup->SetName("ttbar_scaleup"); 

	ch_ttbar_scaledown . SetBranchStatus("*",1);
	_ttbar_scaledown = ch_ttbar_scaledown . CopyTree(cut_bkg);
	_ttbar_scaledown->SetName("ttbar_scaledown"); 

	_ttbar_matchingup->Write();
	_ttbar_matchingdown->Write();
	_ttbar_scaleup->Write();
	_ttbar_scaledown->Write();

	_ttbar_matchingup->Delete();
	_ttbar_matchingdown->Delete();
	_ttbar_scaleup->Delete();
	_ttbar_scaledown->Delete();
      }

      /// SIGNAL ///
      std::cout<<" starting wp800..."<<std::endl;
      ch_wp800R . SetBranchStatus("*",1); 
      _wp800R = ch_wp800R . CopyTree(cut_sig);
      _wp800R->SetName("wp800R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp800R_JESUP . SetBranchStatus("*",1);
	_wp800R_JESUP = ch_wp800R_JESUP . CopyTree(cut_sys);
	_wp800R_JESUP->SetName("wp800R_JESUP"); 

	ch_wp800R_JESDOWN . SetBranchStatus("*",1);
	_wp800R_JESDOWN = ch_wp800R_JESDOWN . CopyTree(cut_sys);
	_wp800R_JESDOWN->SetName("wp800R_JESDOWN"); 

	ch_wp800R_BTAGUP . SetBranchStatus("*",1);
	_wp800R_BTAGUP = ch_wp800R_BTAGUP . CopyTree(cut_sys);
	_wp800R_BTAGUP->SetName("wp800R_BTAGUP"); 

	ch_wp800R_BTAGDOWN . SetBranchStatus("*",1);
	_wp800R_BTAGDOWN = ch_wp800R_BTAGDOWN . CopyTree(cut_sys);
	_wp800R_BTAGDOWN->SetName("wp800R_BTAGDOWN"); 

	ch_wp800R_JERUP . SetBranchStatus("*",1);
	_wp800R_JERUP = ch_wp800R_JERUP . CopyTree(cut_sys);
	_wp800R_JERUP->SetName("wp800R_JERUP"); 

	ch_wp800R_JERDOWN . SetBranchStatus("*",1);
	_wp800R_JERDOWN = ch_wp800R_JERDOWN . CopyTree(cut_sys);
	_wp800R_JERDOWN->SetName("wp800R_JERDOWN"); 

      }
      _wp800R->Write();
      _wp800R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp800R_JESUP->Write();
	_wp800R_JESDOWN->Write();
	_wp800R_BTAGUP->Write();
	_wp800R_BTAGDOWN->Write();
	_wp800R_JERUP->Write();
	_wp800R_JERDOWN->Write();

	_wp800R_JESUP->Delete();
	_wp800R_JESDOWN->Delete();
	_wp800R_BTAGUP->Delete();
	_wp800R_BTAGDOWN->Delete();
	_wp800R_JERUP->Delete();
	_wp800R_JERDOWN->Delete();

      }
      std::cout << " wrote wp800R ======== " << std::endl;

      std::cout<<" starting wp900..."<<std::endl;
      ch_wp900R . SetBranchStatus("*",1); 
      _wp900R = ch_wp900R . CopyTree(cut_sig);
      _wp900R->SetName("wp900R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp900R_JESUP . SetBranchStatus("*",1);
	_wp900R_JESUP = ch_wp900R_JESUP . CopyTree(cut_sys);
	_wp900R_JESUP->SetName("wp900R_JESUP"); 

	ch_wp900R_JESDOWN . SetBranchStatus("*",1);
	_wp900R_JESDOWN = ch_wp900R_JESDOWN . CopyTree(cut_sys);
	_wp900R_JESDOWN->SetName("wp900R_JESDOWN"); 

	ch_wp900R_BTAGUP . SetBranchStatus("*",1);
	_wp900R_BTAGUP = ch_wp900R_BTAGUP . CopyTree(cut_sys);
	_wp900R_BTAGUP->SetName("wp900R_BTAGUP"); 

	ch_wp900R_BTAGDOWN . SetBranchStatus("*",1);
	_wp900R_BTAGDOWN = ch_wp900R_BTAGDOWN . CopyTree(cut_sys);
	_wp900R_BTAGDOWN->SetName("wp900R_BTAGDOWN"); 

	ch_wp900R_JERUP . SetBranchStatus("*",1);
	_wp900R_JERUP = ch_wp900R_JERUP . CopyTree(cut_sys);
	_wp900R_JERUP->SetName("wp900R_JERUP"); 

	ch_wp900R_JERDOWN . SetBranchStatus("*",1);
	_wp900R_JERDOWN = ch_wp900R_JERDOWN . CopyTree(cut_sys);
	_wp900R_JERDOWN->SetName("wp900R_JERDOWN"); 

      }
      _wp900R->Write();
      _wp900R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp900R_JESUP->Write();
	_wp900R_JESDOWN->Write();
	_wp900R_BTAGUP->Write();
	_wp900R_BTAGDOWN->Write();
	_wp900R_JERUP->Write();
	_wp900R_JERDOWN->Write();

	_wp900R_JESUP->Delete();
	_wp900R_JESDOWN->Delete();
	_wp900R_BTAGUP->Delete();
	_wp900R_BTAGDOWN->Delete();
	_wp900R_JERUP->Delete();
	_wp900R_JERDOWN->Delete();

      }
      std::cout << " wrote wp900R ======== " << std::endl;

      std::cout<<" starting wp1000..."<<std::endl;
      ch_wp1000R . SetBranchStatus("*",1); 
      _wp1000R = ch_wp1000R . CopyTree(cut_sig);
      _wp1000R->SetName("wp1000R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1000R_JESUP . SetBranchStatus("*",1);
	_wp1000R_JESUP = ch_wp1000R_JESUP . CopyTree(cut_sys);
	_wp1000R_JESUP->SetName("wp1000R_JESUP"); 

	ch_wp1000R_JESDOWN . SetBranchStatus("*",1);
	_wp1000R_JESDOWN = ch_wp1000R_JESDOWN . CopyTree(cut_sys);
	_wp1000R_JESDOWN->SetName("wp1000R_JESDOWN"); 

	ch_wp1000R_BTAGUP . SetBranchStatus("*",1);
	_wp1000R_BTAGUP = ch_wp1000R_BTAGUP . CopyTree(cut_sys);
	_wp1000R_BTAGUP->SetName("wp1000R_BTAGUP"); 

	ch_wp1000R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1000R_BTAGDOWN = ch_wp1000R_BTAGDOWN . CopyTree(cut_sys);
	_wp1000R_BTAGDOWN->SetName("wp1000R_BTAGDOWN"); 

	ch_wp1000R_JERUP . SetBranchStatus("*",1);
	_wp1000R_JERUP = ch_wp1000R_JERUP . CopyTree(cut_sys);
	_wp1000R_JERUP->SetName("wp1000R_JERUP"); 

	ch_wp1000R_JERDOWN . SetBranchStatus("*",1);
	_wp1000R_JERDOWN = ch_wp1000R_JERDOWN . CopyTree(cut_sys);
	_wp1000R_JERDOWN->SetName("wp1000R_JERDOWN"); 

      }
      _wp1000R->Write();
      _wp1000R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1000R_JESUP->Write();
	_wp1000R_JESDOWN->Write();
	_wp1000R_BTAGUP->Write();
	_wp1000R_BTAGDOWN->Write();
	_wp1000R_JERUP->Write();
	_wp1000R_JERDOWN->Write();

	_wp1000R_JESUP->Delete();
	_wp1000R_JESDOWN->Delete();
	_wp1000R_BTAGUP->Delete();
	_wp1000R_BTAGDOWN->Delete();
	_wp1000R_JERUP->Delete();
	_wp1000R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1000R ======== " << std::endl;

      std::cout<<" starting wp1100..."<<std::endl;
      ch_wp1100R . SetBranchStatus("*",1); 
      _wp1100R = ch_wp1100R . CopyTree(cut_sig);
      _wp1100R->SetName("wp1100R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1100R_JESUP . SetBranchStatus("*",1);
	_wp1100R_JESUP = ch_wp1100R_JESUP . CopyTree(cut_sys);
	_wp1100R_JESUP->SetName("wp1100R_JESUP"); 

	ch_wp1100R_JESDOWN . SetBranchStatus("*",1);
	_wp1100R_JESDOWN = ch_wp1100R_JESDOWN . CopyTree(cut_sys);
	_wp1100R_JESDOWN->SetName("wp1100R_JESDOWN"); 

	ch_wp1100R_BTAGUP . SetBranchStatus("*",1);
	_wp1100R_BTAGUP = ch_wp1100R_BTAGUP . CopyTree(cut_sys);
	_wp1100R_BTAGUP->SetName("wp1100R_BTAGUP"); 

	ch_wp1100R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1100R_BTAGDOWN = ch_wp1100R_BTAGDOWN . CopyTree(cut_sys);
	_wp1100R_BTAGDOWN->SetName("wp1100R_BTAGDOWN"); 

	ch_wp1100R_JERUP . SetBranchStatus("*",1);
	_wp1100R_JERUP = ch_wp1100R_JERUP . CopyTree(cut_sys);
	_wp1100R_JERUP->SetName("wp1100R_JERUP"); 

	ch_wp1100R_JERDOWN . SetBranchStatus("*",1);
	_wp1100R_JERDOWN = ch_wp1100R_JERDOWN . CopyTree(cut_sys);
	_wp1100R_JERDOWN->SetName("wp1100R_JERDOWN"); 

      }
      _wp1100R->Write();
      _wp1100R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1100R_JESUP->Write();
	_wp1100R_JESDOWN->Write();
	_wp1100R_BTAGUP->Write();
	_wp1100R_BTAGDOWN->Write();
	_wp1100R_JERUP->Write();
	_wp1100R_JERDOWN->Write();

	_wp1100R_JESUP->Delete();
	_wp1100R_JESDOWN->Delete();
	_wp1100R_BTAGUP->Delete();
	_wp1100R_BTAGDOWN->Delete();
	_wp1100R_JERUP->Delete();
	_wp1100R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1100R ======== " << std::endl;

      std::cout<<" starting wp1200..."<<std::endl;
      ch_wp1200R . SetBranchStatus("*",1); 
      _wp1200R = ch_wp1200R . CopyTree(cut_sig);
      _wp1200R->SetName("wp1200R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1200R_JESUP . SetBranchStatus("*",1);
	_wp1200R_JESUP = ch_wp1200R_JESUP . CopyTree(cut_sys);
	_wp1200R_JESUP->SetName("wp1200R_JESUP"); 

	ch_wp1200R_JESDOWN . SetBranchStatus("*",1);
	_wp1200R_JESDOWN = ch_wp1200R_JESDOWN . CopyTree(cut_sys);
	_wp1200R_JESDOWN->SetName("wp1200R_JESDOWN"); 

	ch_wp1200R_BTAGUP . SetBranchStatus("*",1);
	_wp1200R_BTAGUP = ch_wp1200R_BTAGUP . CopyTree(cut_sys);
	_wp1200R_BTAGUP->SetName("wp1200R_BTAGUP"); 

	ch_wp1200R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1200R_BTAGDOWN = ch_wp1200R_BTAGDOWN . CopyTree(cut_sys);
	_wp1200R_BTAGDOWN->SetName("wp1200R_BTAGDOWN"); 

	ch_wp1200R_JERUP . SetBranchStatus("*",1);
	_wp1200R_JERUP = ch_wp1200R_JERUP . CopyTree(cut_sys);
	_wp1200R_JERUP->SetName("wp1200R_JERUP"); 

	ch_wp1200R_JERDOWN . SetBranchStatus("*",1);
	_wp1200R_JERDOWN = ch_wp1200R_JERDOWN . CopyTree(cut_sys);
	_wp1200R_JERDOWN->SetName("wp1200R_JERDOWN"); 

      }
      _wp1200R->Write();
      _wp1200R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1200R_JESUP->Write();
	_wp1200R_JESDOWN->Write();
	_wp1200R_BTAGUP->Write();
	_wp1200R_BTAGDOWN->Write();
	_wp1200R_JERUP->Write();
	_wp1200R_JERDOWN->Write();

	_wp1200R_JESUP->Delete();
	_wp1200R_JESDOWN->Delete();
	_wp1200R_BTAGUP->Delete();
	_wp1200R_BTAGDOWN->Delete();
	_wp1200R_JERUP->Delete();
	_wp1200R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1200R ======== " << std::endl;

      std::cout<<" starting wp1300..."<<std::endl;
      ch_wp1300R . SetBranchStatus("*",1); 
      _wp1300R = ch_wp1300R . CopyTree(cut_sig);
      _wp1300R->SetName("wp1300R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1300R_JESUP . SetBranchStatus("*",1);
	_wp1300R_JESUP = ch_wp1300R_JESUP . CopyTree(cut_sys);
	_wp1300R_JESUP->SetName("wp1300R_JESUP"); 

	ch_wp1300R_JESDOWN . SetBranchStatus("*",1);
	_wp1300R_JESDOWN = ch_wp1300R_JESDOWN . CopyTree(cut_sys);
	_wp1300R_JESDOWN->SetName("wp1300R_JESDOWN"); 

	ch_wp1300R_BTAGUP . SetBranchStatus("*",1);
	_wp1300R_BTAGUP = ch_wp1300R_BTAGUP . CopyTree(cut_sys);
	_wp1300R_BTAGUP->SetName("wp1300R_BTAGUP"); 

	ch_wp1300R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1300R_BTAGDOWN = ch_wp1300R_BTAGDOWN . CopyTree(cut_sys);
	_wp1300R_BTAGDOWN->SetName("wp1300R_BTAGDOWN"); 

	ch_wp1300R_JERUP . SetBranchStatus("*",1);
	_wp1300R_JERUP = ch_wp1300R_JERUP . CopyTree(cut_sys);
	_wp1300R_JERUP->SetName("wp1300R_JERUP"); 

	ch_wp1300R_JERDOWN . SetBranchStatus("*",1);
	_wp1300R_JERDOWN = ch_wp1300R_JERDOWN . CopyTree(cut_sys);
	_wp1300R_JERDOWN->SetName("wp1300R_JERDOWN"); 

      }
      _wp1300R->Write();
      _wp1300R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1300R_JESUP->Write();
	_wp1300R_JESDOWN->Write();
	_wp1300R_BTAGUP->Write();
	_wp1300R_BTAGDOWN->Write();
	_wp1300R_JERUP->Write();
	_wp1300R_JERDOWN->Write();

	_wp1300R_JESUP->Delete();
	_wp1300R_JESDOWN->Delete();
	_wp1300R_BTAGUP->Delete();
	_wp1300R_BTAGDOWN->Delete();
	_wp1300R_JERUP->Delete();
	_wp1300R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1300R ======== " << std::endl;

      std::cout<<" starting wp1400..."<<std::endl;
      ch_wp1400R . SetBranchStatus("*",1); 
      _wp1400R = ch_wp1400R . CopyTree(cut_sig);
      _wp1400R->SetName("wp1400R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1400R_JESUP . SetBranchStatus("*",1);
	_wp1400R_JESUP = ch_wp1400R_JESUP . CopyTree(cut_sys);
	_wp1400R_JESUP->SetName("wp1400R_JESUP"); 

	ch_wp1400R_JESDOWN . SetBranchStatus("*",1);
	_wp1400R_JESDOWN = ch_wp1400R_JESDOWN . CopyTree(cut_sys);
	_wp1400R_JESDOWN->SetName("wp1400R_JESDOWN"); 

	ch_wp1400R_BTAGUP . SetBranchStatus("*",1);
	_wp1400R_BTAGUP = ch_wp1400R_BTAGUP . CopyTree(cut_sys);
	_wp1400R_BTAGUP->SetName("wp1400R_BTAGUP"); 

	ch_wp1400R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1400R_BTAGDOWN = ch_wp1400R_BTAGDOWN . CopyTree(cut_sys);
	_wp1400R_BTAGDOWN->SetName("wp1400R_BTAGDOWN"); 

	ch_wp1400R_JERUP . SetBranchStatus("*",1);
	_wp1400R_JERUP = ch_wp1400R_JERUP . CopyTree(cut_sys);
	_wp1400R_JERUP->SetName("wp1400R_JERUP"); 

	ch_wp1400R_JERDOWN . SetBranchStatus("*",1);
	_wp1400R_JERDOWN = ch_wp1400R_JERDOWN . CopyTree(cut_sys);
	_wp1400R_JERDOWN->SetName("wp1400R_JERDOWN"); 

      }
      _wp1400R->Write();
      _wp1400R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1400R_JESUP->Write();
	_wp1400R_JESDOWN->Write();
	_wp1400R_BTAGUP->Write();
	_wp1400R_BTAGDOWN->Write();
	_wp1400R_JERUP->Write();
	_wp1400R_JERDOWN->Write();

	_wp1400R_JESUP->Delete();
	_wp1400R_JESDOWN->Delete();
	_wp1400R_BTAGUP->Delete();
	_wp1400R_BTAGDOWN->Delete();
	_wp1400R_JERUP->Delete();
	_wp1400R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1400R ======== " << std::endl;

      std::cout<<" starting wp1500..."<<std::endl;
      ch_wp1500R . SetBranchStatus("*",1); 
      _wp1500R = ch_wp1500R . CopyTree(cut_sig);
      _wp1500R->SetName("wp1500R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1500R_JESUP . SetBranchStatus("*",1);
	_wp1500R_JESUP = ch_wp1500R_JESUP . CopyTree(cut_sys);
	_wp1500R_JESUP->SetName("wp1500R_JESUP"); 

	ch_wp1500R_JESDOWN . SetBranchStatus("*",1);
	_wp1500R_JESDOWN = ch_wp1500R_JESDOWN . CopyTree(cut_sys);
	_wp1500R_JESDOWN->SetName("wp1500R_JESDOWN"); 

	ch_wp1500R_BTAGUP . SetBranchStatus("*",1);
	_wp1500R_BTAGUP = ch_wp1500R_BTAGUP . CopyTree(cut_sys);
	_wp1500R_BTAGUP->SetName("wp1500R_BTAGUP"); 

	ch_wp1500R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1500R_BTAGDOWN = ch_wp1500R_BTAGDOWN . CopyTree(cut_sys);
	_wp1500R_BTAGDOWN->SetName("wp1500R_BTAGDOWN"); 

	ch_wp1500R_JERUP . SetBranchStatus("*",1);
	_wp1500R_JERUP = ch_wp1500R_JERUP . CopyTree(cut_sys);
	_wp1500R_JERUP->SetName("wp1500R_JERUP"); 

	ch_wp1500R_JERDOWN . SetBranchStatus("*",1);
	_wp1500R_JERDOWN = ch_wp1500R_JERDOWN . CopyTree(cut_sys);
	_wp1500R_JERDOWN->SetName("wp1500R_JERDOWN"); 

      }
      _wp1500R->Write();
      _wp1500R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1500R_JESUP->Write();
	_wp1500R_JESDOWN->Write();
	_wp1500R_BTAGUP->Write();
	_wp1500R_BTAGDOWN->Write();
	_wp1500R_JERUP->Write();
	_wp1500R_JERDOWN->Write();

	_wp1500R_JESUP->Delete();
	_wp1500R_JESDOWN->Delete();
	_wp1500R_BTAGUP->Delete();
	_wp1500R_BTAGDOWN->Delete();
	_wp1500R_JERUP->Delete();
	_wp1500R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1500R ======== " << std::endl;

      std::cout<<" starting wp1600..."<<std::endl;
      ch_wp1600R . SetBranchStatus("*",1); 
      _wp1600R = ch_wp1600R . CopyTree(cut_sig);
      _wp1600R->SetName("wp1600R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1600R_JESUP . SetBranchStatus("*",1);
	_wp1600R_JESUP = ch_wp1600R_JESUP . CopyTree(cut_sys);
	_wp1600R_JESUP->SetName("wp1600R_JESUP"); 

	ch_wp1600R_JESDOWN . SetBranchStatus("*",1);
	_wp1600R_JESDOWN = ch_wp1600R_JESDOWN . CopyTree(cut_sys);
	_wp1600R_JESDOWN->SetName("wp1600R_JESDOWN"); 

	ch_wp1600R_BTAGUP . SetBranchStatus("*",1);
	_wp1600R_BTAGUP = ch_wp1600R_BTAGUP . CopyTree(cut_sys);
	_wp1600R_BTAGUP->SetName("wp1600R_BTAGUP"); 

	ch_wp1600R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1600R_BTAGDOWN = ch_wp1600R_BTAGDOWN . CopyTree(cut_sys);
	_wp1600R_BTAGDOWN->SetName("wp1600R_BTAGDOWN"); 

	ch_wp1600R_JERUP . SetBranchStatus("*",1);
	_wp1600R_JERUP = ch_wp1600R_JERUP . CopyTree(cut_sys);
	_wp1600R_JERUP->SetName("wp1600R_JERUP"); 

	ch_wp1600R_JERDOWN . SetBranchStatus("*",1);
	_wp1600R_JERDOWN = ch_wp1600R_JERDOWN . CopyTree(cut_sys);
	_wp1600R_JERDOWN->SetName("wp1600R_JERDOWN"); 

      }
      _wp1600R->Write();
      _wp1600R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1600R_JESUP->Write();
	_wp1600R_JESDOWN->Write();
	_wp1600R_BTAGUP->Write();
	_wp1600R_BTAGDOWN->Write();
	_wp1600R_JERUP->Write();
	_wp1600R_JERDOWN->Write();

	_wp1600R_JESUP->Delete();
	_wp1600R_JESDOWN->Delete();
	_wp1600R_BTAGUP->Delete();
	_wp1600R_BTAGDOWN->Delete();
	_wp1600R_JERUP->Delete();
	_wp1600R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1600R ======== " << std::endl;

      std::cout<<" starting wp1700..."<<std::endl;
      ch_wp1700R . SetBranchStatus("*",1); 
      _wp1700R = ch_wp1700R . CopyTree(cut_sig);
      _wp1700R->SetName("wp1700R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1700R_JESUP . SetBranchStatus("*",1);
	_wp1700R_JESUP = ch_wp1700R_JESUP . CopyTree(cut_sys);
	_wp1700R_JESUP->SetName("wp1700R_JESUP"); 

	ch_wp1700R_JESDOWN . SetBranchStatus("*",1);
	_wp1700R_JESDOWN = ch_wp1700R_JESDOWN . CopyTree(cut_sys);
	_wp1700R_JESDOWN->SetName("wp1700R_JESDOWN"); 

	ch_wp1700R_BTAGUP . SetBranchStatus("*",1);
	_wp1700R_BTAGUP = ch_wp1700R_BTAGUP . CopyTree(cut_sys);
	_wp1700R_BTAGUP->SetName("wp1700R_BTAGUP"); 

	ch_wp1700R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1700R_BTAGDOWN = ch_wp1700R_BTAGDOWN . CopyTree(cut_sys);
	_wp1700R_BTAGDOWN->SetName("wp1700R_BTAGDOWN"); 

	ch_wp1700R_JERUP . SetBranchStatus("*",1);
	_wp1700R_JERUP = ch_wp1700R_JERUP . CopyTree(cut_sys);
	_wp1700R_JERUP->SetName("wp1700R_JERUP"); 

	ch_wp1700R_JERDOWN . SetBranchStatus("*",1);
	_wp1700R_JERDOWN = ch_wp1700R_JERDOWN . CopyTree(cut_sys);
	_wp1700R_JERDOWN->SetName("wp1700R_JERDOWN"); 

      }
      _wp1700R->Write();
      _wp1700R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1700R_JESUP->Write();
	_wp1700R_JESDOWN->Write();
	_wp1700R_BTAGUP->Write();
	_wp1700R_BTAGDOWN->Write();
	_wp1700R_JERUP->Write();
	_wp1700R_JERDOWN->Write();

	_wp1700R_JESUP->Delete();
	_wp1700R_JESDOWN->Delete();
	_wp1700R_BTAGUP->Delete();
	_wp1700R_BTAGDOWN->Delete();
	_wp1700R_JERUP->Delete();
	_wp1700R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1700R ======== " << std::endl;

      std::cout<<" starting wp1800..."<<std::endl;
      ch_wp1800R . SetBranchStatus("*",1); 
      _wp1800R = ch_wp1800R . CopyTree(cut_sig);
      _wp1800R->SetName("wp1800R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1800R_JESUP . SetBranchStatus("*",1);
	_wp1800R_JESUP = ch_wp1800R_JESUP . CopyTree(cut_sys);
	_wp1800R_JESUP->SetName("wp1800R_JESUP"); 

	ch_wp1800R_JESDOWN . SetBranchStatus("*",1);
	_wp1800R_JESDOWN = ch_wp1800R_JESDOWN . CopyTree(cut_sys);
	_wp1800R_JESDOWN->SetName("wp1800R_JESDOWN"); 

	ch_wp1800R_BTAGUP . SetBranchStatus("*",1);
	_wp1800R_BTAGUP = ch_wp1800R_BTAGUP . CopyTree(cut_sys);
	_wp1800R_BTAGUP->SetName("wp1800R_BTAGUP"); 

	ch_wp1800R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1800R_BTAGDOWN = ch_wp1800R_BTAGDOWN . CopyTree(cut_sys);
	_wp1800R_BTAGDOWN->SetName("wp1800R_BTAGDOWN"); 

	ch_wp1800R_JERUP . SetBranchStatus("*",1);
	_wp1800R_JERUP = ch_wp1800R_JERUP . CopyTree(cut_sys);
	_wp1800R_JERUP->SetName("wp1800R_JERUP"); 

	ch_wp1800R_JERDOWN . SetBranchStatus("*",1);
	_wp1800R_JERDOWN = ch_wp1800R_JERDOWN . CopyTree(cut_sys);
	_wp1800R_JERDOWN->SetName("wp1800R_JERDOWN"); 

      }
      _wp1800R->Write();
      _wp1800R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1800R_JESUP->Write();
	_wp1800R_JESDOWN->Write();
	_wp1800R_BTAGUP->Write();
	_wp1800R_BTAGDOWN->Write();
	_wp1800R_JERUP->Write();
	_wp1800R_JERDOWN->Write();

	_wp1800R_JESUP->Delete();
	_wp1800R_JESDOWN->Delete();
	_wp1800R_BTAGUP->Delete();
	_wp1800R_BTAGDOWN->Delete();
	_wp1800R_JERUP->Delete();
	_wp1800R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1800R ======== " << std::endl;

      std::cout<<" starting wp1900..."<<std::endl;
      ch_wp1900R . SetBranchStatus("*",1); 
      _wp1900R = ch_wp1900R . CopyTree(cut_sig);
      _wp1900R->SetName("wp1900R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp1900R_JESUP . SetBranchStatus("*",1);
	_wp1900R_JESUP = ch_wp1900R_JESUP . CopyTree(cut_sys);
	_wp1900R_JESUP->SetName("wp1900R_JESUP"); 

	ch_wp1900R_JESDOWN . SetBranchStatus("*",1);
	_wp1900R_JESDOWN = ch_wp1900R_JESDOWN . CopyTree(cut_sys);
	_wp1900R_JESDOWN->SetName("wp1900R_JESDOWN"); 

	ch_wp1900R_BTAGUP . SetBranchStatus("*",1);
	_wp1900R_BTAGUP = ch_wp1900R_BTAGUP . CopyTree(cut_sys);
	_wp1900R_BTAGUP->SetName("wp1900R_BTAGUP"); 

	ch_wp1900R_BTAGDOWN . SetBranchStatus("*",1);
	_wp1900R_BTAGDOWN = ch_wp1900R_BTAGDOWN . CopyTree(cut_sys);
	_wp1900R_BTAGDOWN->SetName("wp1900R_BTAGDOWN"); 

	ch_wp1900R_JERUP . SetBranchStatus("*",1);
	_wp1900R_JERUP = ch_wp1900R_JERUP . CopyTree(cut_sys);
	_wp1900R_JERUP->SetName("wp1900R_JERUP"); 

	ch_wp1900R_JERDOWN . SetBranchStatus("*",1);
	_wp1900R_JERDOWN = ch_wp1900R_JERDOWN . CopyTree(cut_sys);
	_wp1900R_JERDOWN->SetName("wp1900R_JERDOWN"); 

      }
      _wp1900R->Write();
      _wp1900R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp1900R_JESUP->Write();
	_wp1900R_JESDOWN->Write();
	_wp1900R_BTAGUP->Write();
	_wp1900R_BTAGDOWN->Write();
	_wp1900R_JERUP->Write();
	_wp1900R_JERDOWN->Write();

	_wp1900R_JESUP->Delete();
	_wp1900R_JESDOWN->Delete();
	_wp1900R_BTAGUP->Delete();
	_wp1900R_BTAGDOWN->Delete();
	_wp1900R_JERUP->Delete();
	_wp1900R_JERDOWN->Delete();

      }
      std::cout << " wrote wp1900R ======== " << std::endl;

      std::cout<<" starting wp2000..."<<std::endl;
      ch_wp2000R . SetBranchStatus("*",1); 
      _wp2000R = ch_wp2000R . CopyTree(cut_sig);
      _wp2000R->SetName("wp2000R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2000R_JESUP . SetBranchStatus("*",1);
	_wp2000R_JESUP = ch_wp2000R_JESUP . CopyTree(cut_sys);
	_wp2000R_JESUP->SetName("wp2000R_JESUP"); 

	ch_wp2000R_JESDOWN . SetBranchStatus("*",1);
	_wp2000R_JESDOWN = ch_wp2000R_JESDOWN . CopyTree(cut_sys);
	_wp2000R_JESDOWN->SetName("wp2000R_JESDOWN"); 

	ch_wp2000R_BTAGUP . SetBranchStatus("*",1);
	_wp2000R_BTAGUP = ch_wp2000R_BTAGUP . CopyTree(cut_sys);
	_wp2000R_BTAGUP->SetName("wp2000R_BTAGUP"); 

	ch_wp2000R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2000R_BTAGDOWN = ch_wp2000R_BTAGDOWN . CopyTree(cut_sys);
	_wp2000R_BTAGDOWN->SetName("wp2000R_BTAGDOWN"); 

	ch_wp2000R_JERUP . SetBranchStatus("*",1);
	_wp2000R_JERUP = ch_wp2000R_JERUP . CopyTree(cut_sys);
	_wp2000R_JERUP->SetName("wp2000R_JERUP"); 

	ch_wp2000R_JERDOWN . SetBranchStatus("*",1);
	_wp2000R_JERDOWN = ch_wp2000R_JERDOWN . CopyTree(cut_sys);
	_wp2000R_JERDOWN->SetName("wp2000R_JERDOWN"); 

      }
      _wp2000R->Write();
      _wp2000R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2000R_JESUP->Write();
	_wp2000R_JESDOWN->Write();
	_wp2000R_BTAGUP->Write();
	_wp2000R_BTAGDOWN->Write();
	_wp2000R_JERUP->Write();
	_wp2000R_JERDOWN->Write();

	_wp2000R_JESUP->Delete();
	_wp2000R_JESDOWN->Delete();
	_wp2000R_BTAGUP->Delete();
	_wp2000R_BTAGDOWN->Delete();
	_wp2000R_JERUP->Delete();
	_wp2000R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2000R ======== " << std::endl;

      std::cout<<" starting wp2100..."<<std::endl;
      ch_wp2100R . SetBranchStatus("*",1); 
      _wp2100R = ch_wp2100R . CopyTree(cut_sig);
      _wp2100R->SetName("wp2100R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2100R_JESUP . SetBranchStatus("*",1);
	_wp2100R_JESUP = ch_wp2100R_JESUP . CopyTree(cut_sys);
	_wp2100R_JESUP->SetName("wp2100R_JESUP"); 

	ch_wp2100R_JESDOWN . SetBranchStatus("*",1);
	_wp2100R_JESDOWN = ch_wp2100R_JESDOWN . CopyTree(cut_sys);
	_wp2100R_JESDOWN->SetName("wp2100R_JESDOWN"); 

	ch_wp2100R_BTAGUP . SetBranchStatus("*",1);
	_wp2100R_BTAGUP = ch_wp2100R_BTAGUP . CopyTree(cut_sys);
	_wp2100R_BTAGUP->SetName("wp2100R_BTAGUP"); 

	ch_wp2100R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2100R_BTAGDOWN = ch_wp2100R_BTAGDOWN . CopyTree(cut_sys);
	_wp2100R_BTAGDOWN->SetName("wp2100R_BTAGDOWN"); 

	ch_wp2100R_JERUP . SetBranchStatus("*",1);
	_wp2100R_JERUP = ch_wp2100R_JERUP . CopyTree(cut_sys);
	_wp2100R_JERUP->SetName("wp2100R_JERUP"); 

	ch_wp2100R_JERDOWN . SetBranchStatus("*",1);
	_wp2100R_JERDOWN = ch_wp2100R_JERDOWN . CopyTree(cut_sys);
	_wp2100R_JERDOWN->SetName("wp2100R_JERDOWN"); 

      }
      _wp2100R->Write();
      _wp2100R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2100R_JESUP->Write();
	_wp2100R_JESDOWN->Write();
	_wp2100R_BTAGUP->Write();
	_wp2100R_BTAGDOWN->Write();
	_wp2100R_JERUP->Write();
	_wp2100R_JERDOWN->Write();

	_wp2100R_JESUP->Delete();
	_wp2100R_JESDOWN->Delete();
	_wp2100R_BTAGUP->Delete();
	_wp2100R_BTAGDOWN->Delete();
	_wp2100R_JERUP->Delete();
	_wp2100R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2100R ======== " << std::endl;

      std::cout<<" starting wp2200..."<<std::endl;
      ch_wp2200R . SetBranchStatus("*",1); 
      _wp2200R = ch_wp2200R . CopyTree(cut_sig);
      _wp2200R->SetName("wp2200R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2200R_JESUP . SetBranchStatus("*",1);
	_wp2200R_JESUP = ch_wp2200R_JESUP . CopyTree(cut_sys);
	_wp2200R_JESUP->SetName("wp2200R_JESUP"); 

	ch_wp2200R_JESDOWN . SetBranchStatus("*",1);
	_wp2200R_JESDOWN = ch_wp2200R_JESDOWN . CopyTree(cut_sys);
	_wp2200R_JESDOWN->SetName("wp2200R_JESDOWN"); 

	ch_wp2200R_BTAGUP . SetBranchStatus("*",1);
	_wp2200R_BTAGUP = ch_wp2200R_BTAGUP . CopyTree(cut_sys);
	_wp2200R_BTAGUP->SetName("wp2200R_BTAGUP"); 

	ch_wp2200R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2200R_BTAGDOWN = ch_wp2200R_BTAGDOWN . CopyTree(cut_sys);
	_wp2200R_BTAGDOWN->SetName("wp2200R_BTAGDOWN"); 

	ch_wp2200R_JERUP . SetBranchStatus("*",1);
	_wp2200R_JERUP = ch_wp2200R_JERUP . CopyTree(cut_sys);
	_wp2200R_JERUP->SetName("wp2200R_JERUP"); 

	ch_wp2200R_JERDOWN . SetBranchStatus("*",1);
	_wp2200R_JERDOWN = ch_wp2200R_JERDOWN . CopyTree(cut_sys);
	_wp2200R_JERDOWN->SetName("wp2200R_JERDOWN"); 

      }
      _wp2200R->Write();
      _wp2200R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2200R_JESUP->Write();
	_wp2200R_JESDOWN->Write();
	_wp2200R_BTAGUP->Write();
	_wp2200R_BTAGDOWN->Write();
	_wp2200R_JERUP->Write();
	_wp2200R_JERDOWN->Write();

	_wp2200R_JESUP->Delete();
	_wp2200R_JESDOWN->Delete();
	_wp2200R_BTAGUP->Delete();
	_wp2200R_BTAGDOWN->Delete();
	_wp2200R_JERUP->Delete();
	_wp2200R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2200R ======== " << std::endl;

      std::cout<<" starting wp2300..."<<std::endl;
      ch_wp2300R . SetBranchStatus("*",1); 
      _wp2300R = ch_wp2300R . CopyTree(cut_sig);
      _wp2300R->SetName("wp2300R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2300R_JESUP . SetBranchStatus("*",1);
	_wp2300R_JESUP = ch_wp2300R_JESUP . CopyTree(cut_sys);
	_wp2300R_JESUP->SetName("wp2300R_JESUP"); 

	ch_wp2300R_JESDOWN . SetBranchStatus("*",1);
	_wp2300R_JESDOWN = ch_wp2300R_JESDOWN . CopyTree(cut_sys);
	_wp2300R_JESDOWN->SetName("wp2300R_JESDOWN"); 

	ch_wp2300R_BTAGUP . SetBranchStatus("*",1);
	_wp2300R_BTAGUP = ch_wp2300R_BTAGUP . CopyTree(cut_sys);
	_wp2300R_BTAGUP->SetName("wp2300R_BTAGUP"); 

	ch_wp2300R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2300R_BTAGDOWN = ch_wp2300R_BTAGDOWN . CopyTree(cut_sys);
	_wp2300R_BTAGDOWN->SetName("wp2300R_BTAGDOWN"); 

	ch_wp2300R_JERUP . SetBranchStatus("*",1);
	_wp2300R_JERUP = ch_wp2300R_JERUP . CopyTree(cut_sys);
	_wp2300R_JERUP->SetName("wp2300R_JERUP"); 

	ch_wp2300R_JERDOWN . SetBranchStatus("*",1);
	_wp2300R_JERDOWN = ch_wp2300R_JERDOWN . CopyTree(cut_sys);
	_wp2300R_JERDOWN->SetName("wp2300R_JERDOWN"); 

      }
      _wp2300R->Write();
      _wp2300R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2300R_JESUP->Write();
	_wp2300R_JESDOWN->Write();
	_wp2300R_BTAGUP->Write();
	_wp2300R_BTAGDOWN->Write();
	_wp2300R_JERUP->Write();
	_wp2300R_JERDOWN->Write();

	_wp2300R_JESUP->Delete();
	_wp2300R_JESDOWN->Delete();
	_wp2300R_BTAGUP->Delete();
	_wp2300R_BTAGDOWN->Delete();
	_wp2300R_JERUP->Delete();
	_wp2300R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2300R ======== " << std::endl;

      std::cout<<" starting wp2400..."<<std::endl;
      ch_wp2400R . SetBranchStatus("*",1); 
      _wp2400R = ch_wp2400R . CopyTree(cut_sig);
      _wp2400R->SetName("wp2400R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2400R_JESUP . SetBranchStatus("*",1);
	_wp2400R_JESUP = ch_wp2400R_JESUP . CopyTree(cut_sys);
	_wp2400R_JESUP->SetName("wp2400R_JESUP"); 

	ch_wp2400R_JESDOWN . SetBranchStatus("*",1);
	_wp2400R_JESDOWN = ch_wp2400R_JESDOWN . CopyTree(cut_sys);
	_wp2400R_JESDOWN->SetName("wp2400R_JESDOWN"); 

	ch_wp2400R_BTAGUP . SetBranchStatus("*",1);
	_wp2400R_BTAGUP = ch_wp2400R_BTAGUP . CopyTree(cut_sys);
	_wp2400R_BTAGUP->SetName("wp2400R_BTAGUP"); 

	ch_wp2400R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2400R_BTAGDOWN = ch_wp2400R_BTAGDOWN . CopyTree(cut_sys);
	_wp2400R_BTAGDOWN->SetName("wp2400R_BTAGDOWN"); 

	ch_wp2400R_JERUP . SetBranchStatus("*",1);
	_wp2400R_JERUP = ch_wp2400R_JERUP . CopyTree(cut_sys);
	_wp2400R_JERUP->SetName("wp2400R_JERUP"); 

	ch_wp2400R_JERDOWN . SetBranchStatus("*",1);
	_wp2400R_JERDOWN = ch_wp2400R_JERDOWN . CopyTree(cut_sys);
	_wp2400R_JERDOWN->SetName("wp2400R_JERDOWN"); 

      }
      _wp2400R->Write();
      _wp2400R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2400R_JESUP->Write();
	_wp2400R_JESDOWN->Write();
	_wp2400R_BTAGUP->Write();
	_wp2400R_BTAGDOWN->Write();
	_wp2400R_JERUP->Write();
	_wp2400R_JERDOWN->Write();

	_wp2400R_JESUP->Delete();
	_wp2400R_JESDOWN->Delete();
	_wp2400R_BTAGUP->Delete();
	_wp2400R_BTAGDOWN->Delete();
	_wp2400R_JERUP->Delete();
	_wp2400R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2400R ======== " << std::endl;

      std::cout<<" starting wp2500..."<<std::endl;
      ch_wp2500R . SetBranchStatus("*",1); 
      _wp2500R = ch_wp2500R . CopyTree(cut_sig);
      _wp2500R->SetName("wp2500R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2500R_JESUP . SetBranchStatus("*",1);
	_wp2500R_JESUP = ch_wp2500R_JESUP . CopyTree(cut_sys);
	_wp2500R_JESUP->SetName("wp2500R_JESUP"); 

	ch_wp2500R_JESDOWN . SetBranchStatus("*",1);
	_wp2500R_JESDOWN = ch_wp2500R_JESDOWN . CopyTree(cut_sys);
	_wp2500R_JESDOWN->SetName("wp2500R_JESDOWN"); 

	ch_wp2500R_BTAGUP . SetBranchStatus("*",1);
	_wp2500R_BTAGUP = ch_wp2500R_BTAGUP . CopyTree(cut_sys);
	_wp2500R_BTAGUP->SetName("wp2500R_BTAGUP"); 

	ch_wp2500R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2500R_BTAGDOWN = ch_wp2500R_BTAGDOWN . CopyTree(cut_sys);
	_wp2500R_BTAGDOWN->SetName("wp2500R_BTAGDOWN"); 

	ch_wp2500R_JERUP . SetBranchStatus("*",1);
	_wp2500R_JERUP = ch_wp2500R_JERUP . CopyTree(cut_sys);
	_wp2500R_JERUP->SetName("wp2500R_JERUP"); 

	ch_wp2500R_JERDOWN . SetBranchStatus("*",1);
	_wp2500R_JERDOWN = ch_wp2500R_JERDOWN . CopyTree(cut_sys);
	_wp2500R_JERDOWN->SetName("wp2500R_JERDOWN"); 

      }
      _wp2500R->Write();
      _wp2500R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2500R_JESUP->Write();
	_wp2500R_JESDOWN->Write();
	_wp2500R_BTAGUP->Write();
	_wp2500R_BTAGDOWN->Write();
	_wp2500R_JERUP->Write();
	_wp2500R_JERDOWN->Write();

	_wp2500R_JESUP->Delete();
	_wp2500R_JESDOWN->Delete();
	_wp2500R_BTAGUP->Delete();
	_wp2500R_BTAGDOWN->Delete();
	_wp2500R_JERUP->Delete();
	_wp2500R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2500R ======== " << std::endl;

      std::cout<<" starting wp2600..."<<std::endl;
      ch_wp2600R . SetBranchStatus("*",1); 
      _wp2600R = ch_wp2600R . CopyTree(cut_sig);
      _wp2600R->SetName("wp2600R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2600R_JESUP . SetBranchStatus("*",1);
	_wp2600R_JESUP = ch_wp2600R_JESUP . CopyTree(cut_sys);
	_wp2600R_JESUP->SetName("wp2600R_JESUP"); 

	ch_wp2600R_JESDOWN . SetBranchStatus("*",1);
	_wp2600R_JESDOWN = ch_wp2600R_JESDOWN . CopyTree(cut_sys);
	_wp2600R_JESDOWN->SetName("wp2600R_JESDOWN"); 

	ch_wp2600R_BTAGUP . SetBranchStatus("*",1);
	_wp2600R_BTAGUP = ch_wp2600R_BTAGUP . CopyTree(cut_sys);
	_wp2600R_BTAGUP->SetName("wp2600R_BTAGUP"); 

	ch_wp2600R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2600R_BTAGDOWN = ch_wp2600R_BTAGDOWN . CopyTree(cut_sys);
	_wp2600R_BTAGDOWN->SetName("wp2600R_BTAGDOWN"); 

	ch_wp2600R_JERUP . SetBranchStatus("*",1);
	_wp2600R_JERUP = ch_wp2600R_JERUP . CopyTree(cut_sys);
	_wp2600R_JERUP->SetName("wp2600R_JERUP"); 

	ch_wp2600R_JERDOWN . SetBranchStatus("*",1);
	_wp2600R_JERDOWN = ch_wp2600R_JERDOWN . CopyTree(cut_sys);
	_wp2600R_JERDOWN->SetName("wp2600R_JERDOWN"); 

      }
      _wp2600R->Write();
      _wp2600R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2600R_JESUP->Write();
	_wp2600R_JESDOWN->Write();
	_wp2600R_BTAGUP->Write();
	_wp2600R_BTAGDOWN->Write();
	_wp2600R_JERUP->Write();
	_wp2600R_JERDOWN->Write();

	_wp2600R_JESUP->Delete();
	_wp2600R_JESDOWN->Delete();
	_wp2600R_BTAGUP->Delete();
	_wp2600R_BTAGDOWN->Delete();
	_wp2600R_JERUP->Delete();
	_wp2600R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2600R ======== " << std::endl;

      std::cout<<" starting wp2700..."<<std::endl;
      ch_wp2700R . SetBranchStatus("*",1); 
      _wp2700R = ch_wp2700R . CopyTree(cut_sig);
      _wp2700R->SetName("wp2700R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2700R_JESUP . SetBranchStatus("*",1);
	_wp2700R_JESUP = ch_wp2700R_JESUP . CopyTree(cut_sys);
	_wp2700R_JESUP->SetName("wp2700R_JESUP"); 

	ch_wp2700R_JESDOWN . SetBranchStatus("*",1);
	_wp2700R_JESDOWN = ch_wp2700R_JESDOWN . CopyTree(cut_sys);
	_wp2700R_JESDOWN->SetName("wp2700R_JESDOWN"); 

	ch_wp2700R_BTAGUP . SetBranchStatus("*",1);
	_wp2700R_BTAGUP = ch_wp2700R_BTAGUP . CopyTree(cut_sys);
	_wp2700R_BTAGUP->SetName("wp2700R_BTAGUP"); 

	ch_wp2700R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2700R_BTAGDOWN = ch_wp2700R_BTAGDOWN . CopyTree(cut_sys);
	_wp2700R_BTAGDOWN->SetName("wp2700R_BTAGDOWN"); 

	ch_wp2700R_JERUP . SetBranchStatus("*",1);
	_wp2700R_JERUP = ch_wp2700R_JERUP . CopyTree(cut_sys);
	_wp2700R_JERUP->SetName("wp2700R_JERUP"); 

	ch_wp2700R_JERDOWN . SetBranchStatus("*",1);
	_wp2700R_JERDOWN = ch_wp2700R_JERDOWN . CopyTree(cut_sys);
	_wp2700R_JERDOWN->SetName("wp2700R_JERDOWN"); 

      }
      _wp2700R->Write();
      _wp2700R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2700R_JESUP->Write();
	_wp2700R_JESDOWN->Write();
	_wp2700R_BTAGUP->Write();
	_wp2700R_BTAGDOWN->Write();
	_wp2700R_JERUP->Write();
	_wp2700R_JERDOWN->Write();

	_wp2700R_JESUP->Delete();
	_wp2700R_JESDOWN->Delete();
	_wp2700R_BTAGUP->Delete();
	_wp2700R_BTAGDOWN->Delete();
	_wp2700R_JERUP->Delete();
	_wp2700R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2700R ======== " << std::endl;

      std::cout<<" starting wp2800..."<<std::endl;
      ch_wp2800R . SetBranchStatus("*",1); 
      _wp2800R = ch_wp2800R . CopyTree(cut_sig);
      _wp2800R->SetName("wp2800R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2800R_JESUP . SetBranchStatus("*",1);
	_wp2800R_JESUP = ch_wp2800R_JESUP . CopyTree(cut_sys);
	_wp2800R_JESUP->SetName("wp2800R_JESUP"); 

	ch_wp2800R_JESDOWN . SetBranchStatus("*",1);
	_wp2800R_JESDOWN = ch_wp2800R_JESDOWN . CopyTree(cut_sys);
	_wp2800R_JESDOWN->SetName("wp2800R_JESDOWN"); 

	ch_wp2800R_BTAGUP . SetBranchStatus("*",1);
	_wp2800R_BTAGUP = ch_wp2800R_BTAGUP . CopyTree(cut_sys);
	_wp2800R_BTAGUP->SetName("wp2800R_BTAGUP"); 

	ch_wp2800R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2800R_BTAGDOWN = ch_wp2800R_BTAGDOWN . CopyTree(cut_sys);
	_wp2800R_BTAGDOWN->SetName("wp2800R_BTAGDOWN"); 

	ch_wp2800R_JERUP . SetBranchStatus("*",1);
	_wp2800R_JERUP = ch_wp2800R_JERUP . CopyTree(cut_sys);
	_wp2800R_JERUP->SetName("wp2800R_JERUP"); 

	ch_wp2800R_JERDOWN . SetBranchStatus("*",1);
	_wp2800R_JERDOWN = ch_wp2800R_JERDOWN . CopyTree(cut_sys);
	_wp2800R_JERDOWN->SetName("wp2800R_JERDOWN"); 

      }
      _wp2800R->Write();
      _wp2800R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2800R_JESUP->Write();
	_wp2800R_JESDOWN->Write();
	_wp2800R_BTAGUP->Write();
	_wp2800R_BTAGDOWN->Write();
	_wp2800R_JERUP->Write();
	_wp2800R_JERDOWN->Write();

	_wp2800R_JESUP->Delete();
	_wp2800R_JESDOWN->Delete();
	_wp2800R_BTAGUP->Delete();
	_wp2800R_BTAGDOWN->Delete();
	_wp2800R_JERUP->Delete();
	_wp2800R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2800R ======== " << std::endl;

      std::cout<<" starting wp2900..."<<std::endl;
      ch_wp2900R . SetBranchStatus("*",1); 
      _wp2900R = ch_wp2900R . CopyTree(cut_sig);
      _wp2900R->SetName("wp2900R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp2900R_JESUP . SetBranchStatus("*",1);
	_wp2900R_JESUP = ch_wp2900R_JESUP . CopyTree(cut_sys);
	_wp2900R_JESUP->SetName("wp2900R_JESUP"); 

	ch_wp2900R_JESDOWN . SetBranchStatus("*",1);
	_wp2900R_JESDOWN = ch_wp2900R_JESDOWN . CopyTree(cut_sys);
	_wp2900R_JESDOWN->SetName("wp2900R_JESDOWN"); 

	ch_wp2900R_BTAGUP . SetBranchStatus("*",1);
	_wp2900R_BTAGUP = ch_wp2900R_BTAGUP . CopyTree(cut_sys);
	_wp2900R_BTAGUP->SetName("wp2900R_BTAGUP"); 

	ch_wp2900R_BTAGDOWN . SetBranchStatus("*",1);
	_wp2900R_BTAGDOWN = ch_wp2900R_BTAGDOWN . CopyTree(cut_sys);
	_wp2900R_BTAGDOWN->SetName("wp2900R_BTAGDOWN"); 

	ch_wp2900R_JERUP . SetBranchStatus("*",1);
	_wp2900R_JERUP = ch_wp2900R_JERUP . CopyTree(cut_sys);
	_wp2900R_JERUP->SetName("wp2900R_JERUP"); 

	ch_wp2900R_JERDOWN . SetBranchStatus("*",1);
	_wp2900R_JERDOWN = ch_wp2900R_JERDOWN . CopyTree(cut_sys);
	_wp2900R_JERDOWN->SetName("wp2900R_JERDOWN"); 

      }
      _wp2900R->Write();
      _wp2900R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp2900R_JESUP->Write();
	_wp2900R_JESDOWN->Write();
	_wp2900R_BTAGUP->Write();
	_wp2900R_BTAGDOWN->Write();
	_wp2900R_JERUP->Write();
	_wp2900R_JERDOWN->Write();

	_wp2900R_JESUP->Delete();
	_wp2900R_JESDOWN->Delete();
	_wp2900R_BTAGUP->Delete();
	_wp2900R_BTAGDOWN->Delete();
	_wp2900R_JERUP->Delete();
	_wp2900R_JERDOWN->Delete();

      }
      std::cout << " wrote wp2900R ======== " << std::endl;

      std::cout<<" starting wp3000..."<<std::endl;
      ch_wp3000R . SetBranchStatus("*",1); 
      _wp3000R = ch_wp3000R . CopyTree(cut_sig);
      _wp3000R->SetName("wp3000R");
      if (ifsys && (i==1 || i==3)) {
	ch_wp3000R_JESUP . SetBranchStatus("*",1);
	_wp3000R_JESUP = ch_wp3000R_JESUP . CopyTree(cut_sys);
	_wp3000R_JESUP->SetName("wp3000R_JESUP"); 

	ch_wp3000R_JESDOWN . SetBranchStatus("*",1);
	_wp3000R_JESDOWN = ch_wp3000R_JESDOWN . CopyTree(cut_sys);
	_wp3000R_JESDOWN->SetName("wp3000R_JESDOWN"); 

	ch_wp3000R_BTAGUP . SetBranchStatus("*",1);
	_wp3000R_BTAGUP = ch_wp3000R_BTAGUP . CopyTree(cut_sys);
	_wp3000R_BTAGUP->SetName("wp3000R_BTAGUP"); 

	ch_wp3000R_BTAGDOWN . SetBranchStatus("*",1);
	_wp3000R_BTAGDOWN = ch_wp3000R_BTAGDOWN . CopyTree(cut_sys);
	_wp3000R_BTAGDOWN->SetName("wp3000R_BTAGDOWN"); 

	ch_wp3000R_JERUP . SetBranchStatus("*",1);
	_wp3000R_JERUP = ch_wp3000R_JERUP . CopyTree(cut_sys);
	_wp3000R_JERUP->SetName("wp3000R_JERUP"); 

	ch_wp3000R_JERDOWN . SetBranchStatus("*",1);
	_wp3000R_JERDOWN = ch_wp3000R_JERDOWN . CopyTree(cut_sys);
	_wp3000R_JERDOWN->SetName("wp3000R_JERDOWN"); 

      }
      _wp3000R->Write();
      _wp3000R->Delete();
      if (ifsys && (i==1 || i==3)) {
	_wp3000R_JESUP->Write();
	_wp3000R_JESDOWN->Write();
	_wp3000R_BTAGUP->Write();
	_wp3000R_BTAGDOWN->Write();
	_wp3000R_JERUP->Write();
	_wp3000R_JERDOWN->Write();

	_wp3000R_JESUP->Delete();
	_wp3000R_JESDOWN->Delete();
	_wp3000R_BTAGUP->Delete();
	_wp3000R_BTAGDOWN->Delete();
	_wp3000R_JERUP->Delete();
	_wp3000R_JERDOWN->Delete();

      }
      std::cout << " wrote wp3000R ======== " << std::endl;

    
      out_file->Write();
      std::cout << " wrote out file  "<< outfile << std::endl ;
      out_file->Close();
      std::cout << " closed out file  "<< outfile << std::endl ;
      delete out_file;
      std::cout << " deleted out file  "<< outfile << std::endl ;

    }
    std::cout << " done ... " << std::endl;
 
  }// train and yield 
}
