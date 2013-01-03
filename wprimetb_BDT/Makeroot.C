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

#include "cuts.h"

void Makeroot () {
  
  TString outfile;
  bool ifsys = true;

  TString indir = "/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/";
  //TString indir = "/home/dsperka/CMS/Wprimetb/8TeV/plots_53x/";
  TString chan[2] = {"el", "mu"};
  
  for (int j=0; j<2; j++) {

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

    TChain ch_wjets("ljmet");
    TChain ch_wjets_JESUP("ljmet"); 
    TChain ch_wjets_JESDOWN("ljmet"); 
    TChain ch_wjets_BTAGUP("ljmet"); 
    TChain ch_wjets_BTAGDOWN("ljmet"); 
    TChain ch_wjets_JERUP("ljmet"); 
    TChain ch_wjets_JERDOWN("ljmet"); 

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
    TTree * _wjets;
    TTree * _s;
    TTree * _bs;
    TTree * _t;
    TTree * _bt;
    TTree * _tw;
    TTree * _btw;
    TTree * _zjets;
    TTree * _ww;

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

    TTree * _wjets_JESUP;
    TTree * _wjets_JESDOWN;
    TTree * _wjets_JERUP;
    TTree * _wjets_JERDOWN;
    TTree * _wjets_BTAGUP;
    TTree * _wjets_BTAGDOWN;

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

    TTree * _ttbar_matchingup;
    TTree * _ttbar_matchingdown;
    TTree * _ttbar_scaleup;
    TTree * _ttbar_scaledown;

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
    ch_wjets . Add(indir + "WJets.root");
    ch_s . Add(indir + "T_s.root");
    ch_bs . Add(indir + "Tbar_s.root");
    ch_t . Add(indir + "T_t.root");
    ch_bt . Add(indir + "Tbar_t.root");
    ch_tw . Add(indir + "T_tW.root");
    ch_btw . Add(indir + "Tbar_tW.root");
    ch_zjets . Add(indir + "ZJets_M50.root");
    ch_ww . Add(indir + "WW.root");
      
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
      ch_wjets_JESUP . Add(indir + "JESUP/WJets_JESUP.root");
      ch_s_JESUP . Add(indir + "JESUP/T_s_JESUP.root");
      ch_bs_JESUP . Add(indir + "JESUP/Tbar_s_JESUP.root");
      ch_t_JESUP . Add(indir + "JESUP/T_t_JESUP.root");
      ch_bt_JESUP . Add(indir + "JESUP/Tbar_t_JESUP.root");
      ch_tw_JESUP . Add(indir + "JESUP/T_tW_JESUP.root");
      ch_btw_JESUP . Add(indir + "JESUP/Tbar_tW_JESUP.root");
      ch_zjets_JESUP . Add(indir + "JESUP/ZJets_M50_JESUP.root");
      ch_ww_JESUP . Add(indir + "JESUP/WW_JESUP.root");
      
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
      ch_wjets_JESDOWN . Add(indir + "JESDOWN/WJets_JESDOWN.root");
      ch_s_JESDOWN . Add(indir + "JESDOWN/T_s_JESDOWN.root");
      ch_bs_JESDOWN . Add(indir + "JESDOWN/Tbar_s_JESDOWN.root");
      ch_t_JESDOWN . Add(indir + "JESDOWN/T_t_JESDOWN.root");
      ch_bt_JESDOWN . Add(indir + "JESDOWN/Tbar_t_JESDOWN.root");
      ch_tw_JESDOWN . Add(indir + "JESDOWN/T_tW_JESDOWN.root");
      ch_btw_JESDOWN . Add(indir + "JESDOWN/Tbar_tW_JESDOWN.root");
      ch_zjets_JESDOWN . Add(indir + "JESDOWN/ZJets_M50_JESDOWN.root");
      ch_ww_JESDOWN . Add(indir + "JESDOWN/WW_JESDOWN.root");
      
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
      ch_wjets_BTAGUP . Add(indir + "BTAGUP/WJets_BTAGUP.root");
      ch_s_BTAGUP . Add(indir + "BTAGUP/T_s_BTAGUP.root");
      ch_bs_BTAGUP . Add(indir + "BTAGUP/Tbar_s_BTAGUP.root");
      ch_t_BTAGUP . Add(indir + "BTAGUP/T_t_BTAGUP.root");
      ch_bt_BTAGUP . Add(indir + "BTAGUP/Tbar_t_BTAGUP.root");
      ch_tw_BTAGUP . Add(indir + "BTAGUP/T_tW_BTAGUP.root");
      ch_btw_BTAGUP . Add(indir + "BTAGUP/Tbar_tW_BTAGUP.root");
      ch_zjets_BTAGUP . Add(indir + "BTAGUP/ZJets_M50_BTAGUP.root");
      ch_ww_BTAGUP . Add(indir + "BTAGUP/WW_BTAGUP.root");

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
      ch_wjets_BTAGDOWN . Add(indir + "BTAGDOWN/WJets_BTAGDOWN.root");
      ch_s_BTAGDOWN . Add(indir + "BTAGDOWN/T_s_BTAGDOWN.root");
      ch_bs_BTAGDOWN . Add(indir + "BTAGDOWN/Tbar_s_BTAGDOWN.root");
      ch_t_BTAGDOWN . Add(indir + "BTAGDOWN/T_t_BTAGDOWN.root");
      ch_bt_BTAGDOWN . Add(indir + "BTAGDOWN/Tbar_t_BTAGDOWN.root");
      ch_tw_BTAGDOWN . Add(indir + "BTAGDOWN/T_tW_BTAGDOWN.root");
      ch_btw_BTAGDOWN . Add(indir + "BTAGDOWN/Tbar_tW_BTAGDOWN.root");
      ch_zjets_BTAGDOWN . Add(indir + "BTAGDOWN/ZJets_M50_BTAGDOWN.root");
      ch_ww_BTAGDOWN . Add(indir + "BTAGDOWN/WW_BTAGDOWN.root");
      
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
      ch_wjets_JERUP . Add(indir + "JERUP/WJets_JERUP.root");
      ch_s_JERUP . Add(indir + "JERUP/T_s_JERUP.root");
      ch_bs_JERUP . Add(indir + "JERUP/Tbar_s_JERUP.root");
      ch_t_JERUP . Add(indir + "JERUP/T_t_JERUP.root");
      ch_bt_JERUP . Add(indir + "JERUP/Tbar_t_JERUP.root");
      ch_tw_JERUP . Add(indir + "JERUP/T_tW_JERUP.root");
      ch_btw_JERUP . Add(indir + "JERUP/Tbar_tW_JERUP.root");
      ch_zjets_JERUP . Add(indir + "JERUP/ZJets_M50_JERUP.root");
      ch_ww_JERUP . Add(indir + "JERUP/WW_JERUP.root");
      
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
      ch_wjets_JERDOWN . Add(indir + "JERDOWN/WJets_JERDOWN.root");
      ch_s_JERDOWN . Add(indir + "JERDOWN/T_s_JERDOWN.root");
      ch_bs_JERDOWN . Add(indir + "JERDOWN/Tbar_s_JERDOWN.root");
      ch_t_JERDOWN . Add(indir + "JERDOWN/T_t_JERDOWN.root");
      ch_bt_JERDOWN . Add(indir + "JERDOWN/Tbar_t_JERDOWN.root");
      ch_tw_JERDOWN . Add(indir + "JERDOWN/T_tW_JERDOWN.root");
      ch_btw_JERDOWN . Add(indir + "JERDOWN/Tbar_tW_JERDOWN.root");
      ch_zjets_JERDOWN . Add(indir + "JERDOWN/ZJets_M50_JERDOWN.root");
      ch_ww_JERDOWN . Add(indir + "JERDOWN/WW_JERDOWN.root");
      
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
  

      //ch_ttbar_matchingdown . Add(indir + "TTbar_Madgraph_MATCHINGDOWN.root");
      //ch_ttbar_matchingup . Add(indir + "TTbar_Madgraph_MATCHINGUP.root");
      //ch_ttbar_scaledown . Add(indir + "TTbar_Madgraph_SCALEDOWN.root");
      //ch_ttbar_scaleup . Add(indir + "TTbar_Madgraph_SCALEUP.root");
    }
  
    TCut cut_bkg;
    TCut cut_data;
    TCut cut_sig;
    TCut cut_sys;

    for (int i=0; i<2; i++) {      
 
      if (channel == "el"){
	cut_data = yieldsDataGE1tags_el;
	cut_sys = yieldsSysGE1tags_el;
	if (i==0) {
	  cut_bkg = trainsampleBkgGE1tags_el;
	  cut_sig = trainsampleSigGE1tags_el;
	  outfile = "TrainingSamples/TrainingTrees_GE1BTag_el.root";
	}      
	if (i==1){
	  cut_bkg = yieldsampleBkgGE1tags_el;
	  cut_sig = yieldsampleSigGE1tags_el;
	  outfile = "YieldSamples/YieldsTrees_GE1BTag_el.root";
	}
      }

      if (channel == "mu"){
	cut_data = yieldsDataGE1tags_mu;
	cut_sys = yieldsSysGE1tags_mu;
	if (i==0) {
	  cut_bkg = trainsampleBkgGE1tags_mu;
	  cut_sig = trainsampleSigGE1tags_mu;
	  outfile = "TrainingSamples/TrainingTrees_GE1BTag_mu.root";
	}      
	if (i==1){
	  cut_bkg = yieldsampleBkgGE1tags_mu;
	  cut_sig = yieldsampleSigGE1tags_mu;
	  outfile = "YieldSamples/YieldsTrees_GE1BTag_mu.root";
	}
      }

      std::cout<< channel << " " << outfile <<std::endl;
      std::cout << "cut_bkg " << cut_bkg.GetTitle() << std::endl;
      std::cout << "cut_data " << cut_data.GetTitle() << std::endl;
      std::cout << "cut_sig " << cut_sig.GetTitle() << std::endl;
      std::cout << "cut_sys " << cut_sys.GetTitle() << std::endl;

      if (channel == "el"){
	if (i==1){
	  ch_data . Add(indir + "Single_El_12pt2fb.root");
	  ch_data . SetBranchStatus("*",1);
	  TTree * t_data = ch_data . CopyTree(cut_data);
	  _data = t_data->CopyTree("","");      
	  _data->SetName("data");
	}
      }

      if (channel == "mu"){
	if (i==1){
	  ch_data . Add(indir + "Single_Mu_12pt2fb.root");
	  ch_data . SetBranchStatus("*",1);
	  TTree * t_data = ch_data . CopyTree(cut_data);
	  _data = t_data->CopyTree("","");
	  _data->SetName("data");
	}
      }
    
      std::cout << " set branches ======== " << std::endl;
      ch_ttbar . SetBranchStatus("*",1); 
      TTree * t_ttbar = ch_ttbar . CopyTree(cut_bkg);
      _ttbar = t_ttbar->CopyTree("","");
      _ttbar->SetName("ttbar");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_ttbar_JESUP . SetBranchStatus("*",1);
	TTree * t_ttbar_JESUP = ch_ttbar_JESUP . CopyTree(cut_sys);
        _ttbar_JESUP = t_ttbar_JESUP->CopyTree("","");
	_ttbar_JESUP->SetName("ttbar_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_ttbar_JESDOWN . SetBranchStatus("*",1);
	TTree * t_ttbar_JESDOWN = ch_ttbar_JESDOWN . CopyTree(cut_sys);
	_ttbar_JESDOWN = t_ttbar_JESDOWN->CopyTree("","");
	_ttbar_JESDOWN->SetName("ttbar_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_ttbar_BTAGUP . SetBranchStatus("*",1);
	TTree * t_ttbar_BTAGUP = ch_ttbar_BTAGUP . CopyTree(cut_sys);
	_ttbar_BTAGUP = t_ttbar_BTAGUP->CopyTree("","");
	_ttbar_BTAGUP->SetName("ttbar_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_ttbar_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_ttbar_BTAGDOWN = ch_ttbar_BTAGDOWN . CopyTree(cut_sys);
	_ttbar_BTAGDOWN = t_ttbar_BTAGDOWN->CopyTree("","");
	_ttbar_BTAGDOWN->SetName("ttbar_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_ttbar_JERUP . SetBranchStatus("*",1);
	TTree * t_ttbar_JERUP = ch_ttbar_JERUP . CopyTree(cut_sys);
	_ttbar_JERUP = t_ttbar_JERUP->CopyTree("","");
	_ttbar_JERUP->SetName("ttbar_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_ttbar_JERDOWN . SetBranchStatus("*",1);
	TTree * t_ttbar_JERDOWN = ch_ttbar_JERDOWN . CopyTree(cut_sys);
	_ttbar_JERDOWN = t_ttbar_JERDOWN->CopyTree("","");
	_ttbar_JERDOWN->SetName("ttbar_JERDOWN"); 
      }

      ch_wjets . SetBranchStatus("*",1); 
      TTree * t_wjets = ch_wjets . CopyTree(cut_bkg);
      _wjets = t_wjets->CopyTree("","");
      _wjets->SetName("wjets");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wjets_JESUP . SetBranchStatus("*",1);
	TTree * t_wjets_JESUP = ch_wjets_JESUP . CopyTree(cut_sys);
	_wjets_JESUP = t_wjets_JESUP->CopyTree("","");
	_wjets_JESUP->SetName("wjets_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wjets_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wjets_JESDOWN = ch_wjets_JESDOWN . CopyTree(cut_sys);
	_wjets_JESDOWN = t_wjets_JESDOWN->CopyTree("","");
	_wjets_JESDOWN->SetName("wjets_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wjets_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wjets_BTAGUP = ch_wjets_BTAGUP . CopyTree(cut_sys);
	_wjets_BTAGUP = t_wjets_BTAGUP->CopyTree("","");
	_wjets_BTAGUP->SetName("wjets_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wjets_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wjets_BTAGDOWN = ch_wjets_BTAGDOWN . CopyTree(cut_sys);
	_wjets_BTAGDOWN = t_wjets_BTAGDOWN->CopyTree("","");
	_wjets_BTAGDOWN->SetName("wjets_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wjets_JERUP . SetBranchStatus("*",1);
	TTree * t_wjets_JERUP = ch_wjets_JERUP . CopyTree(cut_sys);
	_wjets_JERUP = t_wjets_JERUP->CopyTree("","");
	_wjets_JERUP->SetName("wjets_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wjets_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wjets_JERDOWN = ch_wjets_JERDOWN . CopyTree(cut_sys);
	_wjets_JERDOWN = t_wjets_JERDOWN->CopyTree("","");
	_wjets_JERDOWN->SetName("wjets_JERDOWN"); 

      }

      ch_s . SetBranchStatus("*",1); 
      TTree * t_s = ch_s . CopyTree(cut_bkg);
      _s = t_s->CopyTree("","");
      _s->SetName("s");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_s_JESUP . SetBranchStatus("*",1);
	TTree * t_s_JESUP = ch_s_JESUP . CopyTree(cut_sys);
	_s_JESUP = t_s_JESUP->CopyTree("","");
	_s_JESUP->SetName("s_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_s_JESDOWN . SetBranchStatus("*",1);
	TTree * t_s_JESDOWN = ch_s_JESDOWN . CopyTree(cut_sys);
	_s_JESDOWN = t_s_JESDOWN->CopyTree("","");
	_s_JESDOWN->SetName("s_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_s_BTAGUP . SetBranchStatus("*",1);
	TTree * t_s_BTAGUP = ch_s_BTAGUP . CopyTree(cut_sys);
	_s_BTAGUP = t_s_BTAGUP->CopyTree("","");
	_s_BTAGUP->SetName("s_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_s_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_s_BTAGDOWN = ch_s_BTAGDOWN . CopyTree(cut_sys);
	_s_BTAGDOWN = t_s_BTAGDOWN->CopyTree("","");
	_s_BTAGDOWN->SetName("s_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_s_JERUP . SetBranchStatus("*",1);
	TTree * t_s_JERUP = ch_s_JERUP . CopyTree(cut_sys);
	_s_JERUP = t_s_JERUP->CopyTree("","");
	_s_JERUP->SetName("s_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_s_JERDOWN . SetBranchStatus("*",1);
	TTree * t_s_JERDOWN = ch_s_JERDOWN . CopyTree(cut_sys);
	_s_JERDOWN = t_s_JERDOWN->CopyTree("","");
	_s_JERDOWN->SetName("s_JERDOWN"); 

      }

      ch_bs . SetBranchStatus("*",1); 
      TTree * t_bs = ch_bs . CopyTree(cut_bkg);
      _bs = t_bs->CopyTree("","");
      _bs->SetName("bs");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_bs_JESUP . SetBranchStatus("*",1);
	TTree * t_bs_JESUP = ch_bs_JESUP . CopyTree(cut_sys);
	_bs_JESUP = t_bs_JESUP->CopyTree("","");
	_bs_JESUP->SetName("bs_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_bs_JESDOWN . SetBranchStatus("*",1);
	TTree * t_bs_JESDOWN = ch_bs_JESDOWN . CopyTree(cut_sys);
	_bs_JESDOWN = t_bs_JESDOWN->CopyTree("","");
	_bs_JESDOWN->SetName("bs_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_bs_BTAGUP . SetBranchStatus("*",1);
	TTree * t_bs_BTAGUP = ch_bs_BTAGUP . CopyTree(cut_sys);
	_bs_BTAGUP = t_bs_BTAGUP->CopyTree("","");
	_bs_BTAGUP->SetName("bs_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_bs_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_bs_BTAGDOWN = ch_bs_BTAGDOWN . CopyTree(cut_sys);
	_bs_BTAGDOWN = t_bs_BTAGDOWN->CopyTree("","");
	_bs_BTAGDOWN->SetName("bs_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_bs_JERUP . SetBranchStatus("*",1);
	TTree * t_bs_JERUP = ch_bs_JERUP . CopyTree(cut_sys);
	_bs_JERUP = t_bs_JERUP->CopyTree("","");
	_bs_JERUP->SetName("bs_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_bs_JERDOWN . SetBranchStatus("*",1);
	TTree * t_bs_JERDOWN = ch_bs_JERDOWN . CopyTree(cut_sys);
	_bs_JERDOWN = t_bs_JERDOWN->CopyTree("","");
	_bs_JERDOWN->SetName("bs_JERDOWN"); 

      }

      ch_t . SetBranchStatus("*",1); 
      TTree * t_t = ch_t . CopyTree(cut_bkg);
      _t = t_t->CopyTree("","");
      _t->SetName("t");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_t_JESUP . SetBranchStatus("*",1);
	TTree * t_t_JESUP = ch_t_JESUP . CopyTree(cut_sys);
	_t_JESUP = t_t_JESUP->CopyTree("","");
	_t_JESUP->SetName("t_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_t_JESDOWN . SetBranchStatus("*",1);
	TTree * t_t_JESDOWN = ch_t_JESDOWN . CopyTree(cut_sys);
	_t_JESDOWN = t_t_JESDOWN->CopyTree("","");
	_t_JESDOWN->SetName("t_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_t_BTAGUP . SetBranchStatus("*",1);
	TTree * t_t_BTAGUP = ch_t_BTAGUP . CopyTree(cut_sys);
	_t_BTAGUP = t_t_BTAGUP->CopyTree("","");
	_t_BTAGUP->SetName("t_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_t_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_t_BTAGDOWN = ch_t_BTAGDOWN . CopyTree(cut_sys);
	_t_BTAGDOWN = t_t_BTAGDOWN->CopyTree("","");
	_t_BTAGDOWN->SetName("t_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_t_JERUP . SetBranchStatus("*",1);
	TTree * t_t_JERUP = ch_t_JERUP . CopyTree(cut_sys);
	_t_JERUP = t_t_JERUP->CopyTree("","");
	_t_JERUP->SetName("t_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_t_JERDOWN . SetBranchStatus("*",1);
	TTree * t_t_JERDOWN = ch_t_JERDOWN . CopyTree(cut_sys);
	_t_JERDOWN = t_t_JERDOWN->CopyTree("","");
	_t_JERDOWN->SetName("t_JERDOWN"); 

      }
 
      ch_bt . SetBranchStatus("*",1); 
      TTree * t_bt = ch_bt . CopyTree(cut_bkg);
      _bt = t_bt->CopyTree("","");
      _bt->SetName("bt");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_bt_JESUP . SetBranchStatus("*",1);
	TTree * t_bt_JESUP = ch_bt_JESUP . CopyTree(cut_sys);
	_bt_JESUP = t_bt_JESUP->CopyTree("","");
	_bt_JESUP->SetName("bt_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_bt_JESDOWN . SetBranchStatus("*",1);
	TTree * t_bt_JESDOWN = ch_bt_JESDOWN . CopyTree(cut_sys);
	_bt_JESDOWN = t_bt_JESDOWN->CopyTree("","");
	_bt_JESDOWN->SetName("bt_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_bt_BTAGUP . SetBranchStatus("*",1);
	TTree * t_bt_BTAGUP = ch_bt_BTAGUP . CopyTree(cut_sys);
	_bt_BTAGUP = t_bt_BTAGUP->CopyTree("","");
	_bt_BTAGUP->SetName("bt_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_bt_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_bt_BTAGDOWN = ch_bt_BTAGDOWN . CopyTree(cut_sys);
	_bt_BTAGDOWN = t_bt_BTAGDOWN->CopyTree("","");
	_bt_BTAGDOWN->SetName("bt_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_bt_JERUP . SetBranchStatus("*",1);
	TTree * t_bt_JERUP = ch_bt_JERUP . CopyTree(cut_sys);
	_bt_JERUP = t_bt_JERUP->CopyTree("","");
	_bt_JERUP->SetName("bt_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_bt_JERDOWN . SetBranchStatus("*",1);
	TTree * t_bt_JERDOWN = ch_bt_JERDOWN . CopyTree(cut_sys);
	_bt_JERDOWN = t_bt_JERDOWN->CopyTree("","");
	_bt_JERDOWN->SetName("bt_JERDOWN"); 

      }

      ch_tw . SetBranchStatus("*",1); 
      TTree * t_tw = ch_tw . CopyTree(cut_bkg);
      _tw = t_tw->CopyTree("","");
      _tw->SetName("tw");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_tw_JESUP . SetBranchStatus("*",1);
	TTree * t_tw_JESUP = ch_tw_JESUP . CopyTree(cut_sys);
	_tw_JESUP = t_tw_JESUP->CopyTree("","");
	_tw_JESUP->SetName("tw_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_tw_JESDOWN . SetBranchStatus("*",1);
	TTree * t_tw_JESDOWN = ch_tw_JESDOWN . CopyTree(cut_sys);
	_tw_JESDOWN = t_tw_JESDOWN->CopyTree("","");
	_tw_JESDOWN->SetName("tw_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_tw_BTAGUP . SetBranchStatus("*",1);
	TTree * t_tw_BTAGUP = ch_tw_BTAGUP . CopyTree(cut_sys);
	_tw_BTAGUP = t_tw_BTAGUP->CopyTree("","");
	_tw_BTAGUP->SetName("tw_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_tw_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_tw_BTAGDOWN = ch_tw_BTAGDOWN . CopyTree(cut_sys);
	_tw_BTAGDOWN = t_tw_BTAGDOWN->CopyTree("","");
	_tw_BTAGDOWN->SetName("tw_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_tw_JERUP . SetBranchStatus("*",1);
	TTree * t_tw_JERUP = ch_tw_JERUP . CopyTree(cut_sys);
	_tw_JERUP = t_tw_JERUP->CopyTree("","");
	_tw_JERUP->SetName("tw_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_tw_JERDOWN . SetBranchStatus("*",1);
	TTree * t_tw_JERDOWN = ch_tw_JERDOWN . CopyTree(cut_sys);
	_tw_JERDOWN = t_tw_JERDOWN->CopyTree("","");
	_tw_JERDOWN->SetName("tw_JERDOWN"); 

      }

      ch_btw . SetBranchStatus("*",1); 
      TTree * t_btw = ch_btw . CopyTree(cut_bkg);
      _btw = t_btw->CopyTree("","");
      _btw->SetName("btw");

      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_btw_JESUP . SetBranchStatus("*",1);
	TTree * t_btw_JESUP = ch_btw_JESUP . CopyTree(cut_sys);
	_btw_JESUP = t_btw_JESUP->CopyTree("","");
	_btw_JESUP->SetName("btw_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_btw_JESDOWN . SetBranchStatus("*",1);
	TTree * t_btw_JESDOWN = ch_btw_JESDOWN . CopyTree(cut_sys);
	_btw_JESDOWN = t_btw_JESDOWN->CopyTree("","");
	_btw_JESDOWN->SetName("btw_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_btw_BTAGUP . SetBranchStatus("*",1);
	TTree * t_btw_BTAGUP = ch_btw_BTAGUP . CopyTree(cut_sys);
	_btw_BTAGUP = t_btw_BTAGUP->CopyTree("","");
	_btw_BTAGUP->SetName("btw_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_btw_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_btw_BTAGDOWN = ch_btw_BTAGDOWN . CopyTree(cut_sys);
	_btw_BTAGDOWN = t_btw_BTAGDOWN->CopyTree("","");
	_btw_BTAGDOWN->SetName("btw_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_btw_JERUP . SetBranchStatus("*",1);
	TTree * t_btw_JERUP = ch_btw_JERUP . CopyTree(cut_sys);
	_btw_JERUP = t_btw_JERUP->CopyTree("","");
	_btw_JERUP->SetName("btw_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_btw_JERDOWN . SetBranchStatus("*",1);
	TTree * t_btw_JERDOWN = ch_btw_JERDOWN . CopyTree(cut_sys);
	_btw_JERDOWN = t_btw_JERDOWN->CopyTree("","");
	_btw_JERDOWN->SetName("btw_JERDOWN"); 

      }

      ch_zjets . SetBranchStatus("*",1); 
      TTree * t_zjets = ch_zjets . CopyTree(cut_bkg);
      _zjets = t_zjets->CopyTree("","");
      _zjets->SetName("zjets");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_zjets_JESUP . SetBranchStatus("*",1);
	TTree * t_zjets_JESUP = ch_zjets_JESUP . CopyTree(cut_sys);
	_zjets_JESUP = t_zjets_JESUP->CopyTree("","");
	_zjets_JESUP->SetName("zjets_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_zjets_JESDOWN . SetBranchStatus("*",1);
	TTree * t_zjets_JESDOWN = ch_zjets_JESDOWN . CopyTree(cut_sys);
	_zjets_JESDOWN = t_zjets_JESDOWN->CopyTree("","");
	_zjets_JESDOWN->SetName("zjets_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_zjets_BTAGUP . SetBranchStatus("*",1);
	TTree * t_zjets_BTAGUP = ch_zjets_BTAGUP . CopyTree(cut_sys);
	_zjets_BTAGUP = t_zjets_BTAGUP->CopyTree("","");
	_zjets_BTAGUP->SetName("zjets_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_zjets_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_zjets_BTAGDOWN = ch_zjets_BTAGDOWN . CopyTree(cut_sys);
	_zjets_BTAGDOWN = t_zjets_BTAGDOWN->CopyTree("","");
	_zjets_BTAGDOWN->SetName("zjets_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_zjets_JERUP . SetBranchStatus("*",1);
	TTree * t_zjets_JERUP = ch_zjets_JERUP . CopyTree(cut_sys);
	_zjets_JERUP = t_zjets_JERUP->CopyTree("","");
	_zjets_JERUP->SetName("zjets_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_zjets_JERDOWN . SetBranchStatus("*",1);
	TTree * t_zjets_JERDOWN = ch_zjets_JERDOWN . CopyTree(cut_sys);
	_zjets_JERDOWN = t_zjets_JERDOWN->CopyTree("","");
	_zjets_JERDOWN->SetName("zjets_JERDOWN"); 

      }

      ch_ww . SetBranchStatus("*",1); 
      TTree * t_ww = ch_ww . CopyTree(cut_bkg);
      _ww = t_ww->CopyTree("","");
      _ww->SetName("ww");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_ww_JESUP . SetBranchStatus("*",1);
	TTree * t_ww_JESUP = ch_ww_JESUP . CopyTree(cut_sys);
	_ww_JESUP = t_ww_JESUP->CopyTree("","");
	_ww_JESUP->SetName("ww_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_ww_JESDOWN . SetBranchStatus("*",1);
	TTree * t_ww_JESDOWN = ch_ww_JESDOWN . CopyTree(cut_sys);
	_ww_JESDOWN = t_ww_JESDOWN->CopyTree("","");
	_ww_JESDOWN->SetName("ww_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_ww_BTAGUP . SetBranchStatus("*",1);
	TTree * t_ww_BTAGUP = ch_ww_BTAGUP . CopyTree(cut_sys);
	_ww_BTAGUP = t_ww_BTAGUP->CopyTree("","");
	_ww_BTAGUP->SetName("ww_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_ww_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_ww_BTAGDOWN = ch_ww_BTAGDOWN . CopyTree(cut_sys);
	_ww_BTAGDOWN = t_ww_BTAGDOWN->CopyTree("","");
	_ww_BTAGDOWN->SetName("ww_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_ww_JERUP . SetBranchStatus("*",1);
	TTree * t_ww_JERUP = ch_ww_JERUP . CopyTree(cut_sys);
	_ww_JERUP = t_ww_JERUP->CopyTree("","");
	_ww_JERUP->SetName("ww_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_ww_JERDOWN . SetBranchStatus("*",1);
	TTree * t_ww_JERDOWN = ch_ww_JERDOWN . CopyTree(cut_sys);
	_ww_JERDOWN = t_ww_JERDOWN->CopyTree("","");
	_ww_JERDOWN->SetName("ww_JERDOWN"); 

      }

      /*
      if (ifsys && i==1) {
	ch_ttbar_matchingup . SetBranchStatus("*",1);
	TTree * t_ttbar_matchingup = ch_ttbar_matchingup . CopyTree(cut_bkg);
	_ttbar_matchingup = t_ttbar_matchingup->CopyTree("","");
	_ttbar_matchingup->SetName("ttbar_matchingup"); 

	ch_ttbar_matchingdown . SetBranchStatus("*",1);
	TTree * t_ttbar_matchingdown = ch_ttbar_matchingdown . CopyTree(cut_bkg);
	_ttbar_matchingdown = t_ttbar_matchingdown->CopyTree("","");
	_ttbar_matchingdown->SetName("ttbar_matchingdown"); 

	ch_ttbar_scaleup . SetBranchStatus("*",1);
	TTree * t_ttbar_scaleup = ch_ttbar_scaleup . CopyTree(cut_bkg);
	_ttbar_scaleup = t_ttbar_scaleup->CopyTree("","");
	_ttbar_scaleup->SetName("ttbar_scaleup"); 

	ch_ttbar_scaledown . SetBranchStatus("*",1);
	TTree * t_ttbar_scaledown = ch_ttbar_scaledown . CopyTree(cut_bkg);
	_ttbar_scaledown = t_ttbar_scaledown->CopyTree("","");
	_ttbar_scaledown->SetName("ttbar_scaledown"); 

      }
      */

      /// SIGNAL ///
      std::cout << " set signal branches ======== " << std::endl;

      ch_wp1100R . SetBranchStatus("*",1); 
      TTree * t_wp1100R = ch_wp1100R . CopyTree(cut_sig);
      _wp1100R = t_wp1100R->CopyTree("","");
      _wp1100R->SetName("wp1100R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1100R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1100R_JESUP = ch_wp1100R_JESUP . CopyTree(cut_sys);
	_wp1100R_JESUP = t_wp1100R_JESUP->CopyTree("","");
	_wp1100R_JESUP->SetName("wp1100R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1100R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1100R_JESDOWN = ch_wp1100R_JESDOWN . CopyTree(cut_sys);
	_wp1100R_JESDOWN = t_wp1100R_JESDOWN->CopyTree("","");
	_wp1100R_JESDOWN->SetName("wp1100R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1100R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1100R_BTAGUP = ch_wp1100R_BTAGUP . CopyTree(cut_sys);
	_wp1100R_BTAGUP = t_wp1100R_BTAGUP->CopyTree("","");
	_wp1100R_BTAGUP->SetName("wp1100R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1100R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1100R_BTAGDOWN = ch_wp1100R_BTAGDOWN . CopyTree(cut_sys);
	_wp1100R_BTAGDOWN = t_wp1100R_BTAGDOWN->CopyTree("","");
	_wp1100R_BTAGDOWN->SetName("wp1100R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1100R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1100R_JERUP = ch_wp1100R_JERUP . CopyTree(cut_sys);
	_wp1100R_JERUP = t_wp1100R_JERUP->CopyTree("","");
	_wp1100R_JERUP->SetName("wp1100R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1100R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1100R_JERDOWN = ch_wp1100R_JERDOWN . CopyTree(cut_sys);
	_wp1100R_JERDOWN = t_wp1100R_JERDOWN->CopyTree("","");
	_wp1100R_JERDOWN->SetName("wp1100R_JERDOWN"); 

      }

      ch_wp1200R . SetBranchStatus("*",1); 
      TTree * t_wp1200R = ch_wp1200R . CopyTree(cut_sig);
      _wp1200R = t_wp1200R->CopyTree("","");
      _wp1200R->SetName("wp1200R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1200R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1200R_JESUP = ch_wp1200R_JESUP . CopyTree(cut_sys);
	_wp1200R_JESUP = t_wp1200R_JESUP->CopyTree("","");
	_wp1200R_JESUP->SetName("wp1200R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1200R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1200R_JESDOWN = ch_wp1200R_JESDOWN . CopyTree(cut_sys);
	_wp1200R_JESDOWN = t_wp1200R_JESDOWN->CopyTree("","");
	_wp1200R_JESDOWN->SetName("wp1200R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1200R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1200R_BTAGUP = ch_wp1200R_BTAGUP . CopyTree(cut_sys);
	_wp1200R_BTAGUP = t_wp1200R_BTAGUP->CopyTree("","");
	_wp1200R_BTAGUP->SetName("wp1200R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1200R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1200R_BTAGDOWN = ch_wp1200R_BTAGDOWN . CopyTree(cut_sys);
	_wp1200R_BTAGDOWN = t_wp1200R_BTAGDOWN->CopyTree("","");
	_wp1200R_BTAGDOWN->SetName("wp1200R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1200R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1200R_JERUP = ch_wp1200R_JERUP . CopyTree(cut_sys);
	_wp1200R_JERUP = t_wp1200R_JERUP->CopyTree("","");
	_wp1200R_JERUP->SetName("wp1200R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1200R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1200R_JERDOWN = ch_wp1200R_JERDOWN . CopyTree(cut_sys);
	_wp1200R_JERDOWN = t_wp1200R_JERDOWN->CopyTree("","");
	_wp1200R_JERDOWN->SetName("wp1200R_JERDOWN"); 

      }

      ch_wp1300R . SetBranchStatus("*",1); 
      TTree * t_wp1300R = ch_wp1300R . CopyTree(cut_sig);
      _wp1300R = t_wp1300R->CopyTree("","");
      _wp1300R->SetName("wp1300R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1300R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1300R_JESUP = ch_wp1300R_JESUP . CopyTree(cut_sys);
	_wp1300R_JESUP = t_wp1300R_JESUP->CopyTree("","");
	_wp1300R_JESUP->SetName("wp1300R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1300R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1300R_JESDOWN = ch_wp1300R_JESDOWN . CopyTree(cut_sys);
	_wp1300R_JESDOWN = t_wp1300R_JESDOWN->CopyTree("","");
	_wp1300R_JESDOWN->SetName("wp1300R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1300R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1300R_BTAGUP = ch_wp1300R_BTAGUP . CopyTree(cut_sys);
	_wp1300R_BTAGUP = t_wp1300R_BTAGUP->CopyTree("","");
	_wp1300R_BTAGUP->SetName("wp1300R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1300R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1300R_BTAGDOWN = ch_wp1300R_BTAGDOWN . CopyTree(cut_sys);
	_wp1300R_BTAGDOWN = t_wp1300R_BTAGDOWN->CopyTree("","");
	_wp1300R_BTAGDOWN->SetName("wp1300R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1300R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1300R_JERUP = ch_wp1300R_JERUP . CopyTree(cut_sys);
	_wp1300R_JERUP = t_wp1300R_JERUP->CopyTree("","");
	_wp1300R_JERUP->SetName("wp1300R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1300R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1300R_JERDOWN = ch_wp1300R_JERDOWN . CopyTree(cut_sys);
	_wp1300R_JERDOWN = t_wp1300R_JERDOWN->CopyTree("","");
	_wp1300R_JERDOWN->SetName("wp1300R_JERDOWN"); 

      }

      ch_wp1400R . SetBranchStatus("*",1); 
      TTree * t_wp1400R = ch_wp1400R . CopyTree(cut_sig);
      _wp1400R = t_wp1400R->CopyTree("","");
      _wp1400R->SetName("wp1400R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1400R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1400R_JESUP = ch_wp1400R_JESUP . CopyTree(cut_sys);
	_wp1400R_JESUP = t_wp1400R_JESUP->CopyTree("","");
	_wp1400R_JESUP->SetName("wp1400R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1400R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1400R_JESDOWN = ch_wp1400R_JESDOWN . CopyTree(cut_sys);
	_wp1400R_JESDOWN = t_wp1400R_JESDOWN->CopyTree("","");
	_wp1400R_JESDOWN->SetName("wp1400R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1400R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1400R_BTAGUP = ch_wp1400R_BTAGUP . CopyTree(cut_sys);
	_wp1400R_BTAGUP = t_wp1400R_BTAGUP->CopyTree("","");
	_wp1400R_BTAGUP->SetName("wp1400R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1400R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1400R_BTAGDOWN = ch_wp1400R_BTAGDOWN . CopyTree(cut_sys);
	_wp1400R_BTAGDOWN = t_wp1400R_BTAGDOWN->CopyTree("","");
	_wp1400R_BTAGDOWN->SetName("wp1400R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1400R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1400R_JERUP = ch_wp1400R_JERUP . CopyTree(cut_sys);
	_wp1400R_JERUP = t_wp1400R_JERUP->CopyTree("","");
	_wp1400R_JERUP->SetName("wp1400R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1400R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1400R_JERDOWN = ch_wp1400R_JERDOWN . CopyTree(cut_sys);
	_wp1400R_JERDOWN = t_wp1400R_JERDOWN->CopyTree("","");
	_wp1400R_JERDOWN->SetName("wp1400R_JERDOWN"); 

      }



      ch_wp1500R . SetBranchStatus("*",1); 
      TTree * t_wp1500R = ch_wp1500R . CopyTree(cut_sig);
      _wp1500R = t_wp1500R->CopyTree("","");
      _wp1500R->SetName("wp1500R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1500R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1500R_JESUP = ch_wp1500R_JESUP . CopyTree(cut_sys);
	_wp1500R_JESUP = t_wp1500R_JESUP->CopyTree("","");
	_wp1500R_JESUP->SetName("wp1500R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1500R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1500R_JESDOWN = ch_wp1500R_JESDOWN . CopyTree(cut_sys);
	_wp1500R_JESDOWN = t_wp1500R_JESDOWN->CopyTree("","");
	_wp1500R_JESDOWN->SetName("wp1500R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1500R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1500R_BTAGUP = ch_wp1500R_BTAGUP . CopyTree(cut_sys);
	_wp1500R_BTAGUP = t_wp1500R_BTAGUP->CopyTree("","");
	_wp1500R_BTAGUP->SetName("wp1500R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1500R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1500R_BTAGDOWN = ch_wp1500R_BTAGDOWN . CopyTree(cut_sys);
	_wp1500R_BTAGDOWN = t_wp1500R_BTAGDOWN->CopyTree("","");
	_wp1500R_BTAGDOWN->SetName("wp1500R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1500R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1500R_JERUP = ch_wp1500R_JERUP . CopyTree(cut_sys);
	_wp1500R_JERUP = t_wp1500R_JERUP->CopyTree("","");
	_wp1500R_JERUP->SetName("wp1500R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1500R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1500R_JERDOWN = ch_wp1500R_JERDOWN . CopyTree(cut_sys);
	_wp1500R_JERDOWN = t_wp1500R_JERDOWN->CopyTree("","");
	_wp1500R_JERDOWN->SetName("wp1500R_JERDOWN"); 

      }

      ch_wp1600R . SetBranchStatus("*",1); 
      TTree * t_wp1600R = ch_wp1600R . CopyTree(cut_sig);
      _wp1600R = t_wp1600R->CopyTree("","");
      _wp1600R->SetName("wp1600R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1600R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1600R_JESUP = ch_wp1600R_JESUP . CopyTree(cut_sys);
	_wp1600R_JESUP = t_wp1600R_JESUP->CopyTree("","");
	_wp1600R_JESUP->SetName("wp1600R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1600R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1600R_JESDOWN = ch_wp1600R_JESDOWN . CopyTree(cut_sys);
	_wp1600R_JESDOWN = t_wp1600R_JESDOWN->CopyTree("","");
	_wp1600R_JESDOWN->SetName("wp1600R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1600R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1600R_BTAGUP = ch_wp1600R_BTAGUP . CopyTree(cut_sys);
	_wp1600R_BTAGUP = t_wp1600R_BTAGUP->CopyTree("","");
	_wp1600R_BTAGUP->SetName("wp1600R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1600R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1600R_BTAGDOWN = ch_wp1600R_BTAGDOWN . CopyTree(cut_sys);
	_wp1600R_BTAGDOWN = t_wp1600R_BTAGDOWN->CopyTree("","");
	_wp1600R_BTAGDOWN->SetName("wp1600R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1600R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1600R_JERUP = ch_wp1600R_JERUP . CopyTree(cut_sys);
	_wp1600R_JERUP = t_wp1600R_JERUP->CopyTree("","");
	_wp1600R_JERUP->SetName("wp1600R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1600R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1600R_JERDOWN = ch_wp1600R_JERDOWN . CopyTree(cut_sys);
	_wp1600R_JERDOWN = t_wp1600R_JERDOWN->CopyTree("","");
	_wp1600R_JERDOWN->SetName("wp1600R_JERDOWN"); 

      }

      ch_wp1700R . SetBranchStatus("*",1); 
      TTree * t_wp1700R = ch_wp1700R . CopyTree(cut_sig);
      _wp1700R = t_wp1700R->CopyTree("","");
      _wp1700R->SetName("wp1700R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1700R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1700R_JESUP = ch_wp1700R_JESUP . CopyTree(cut_sys);
	_wp1700R_JESUP = t_wp1700R_JESUP->CopyTree("","");
	_wp1700R_JESUP->SetName("wp1700R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1700R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1700R_JESDOWN = ch_wp1700R_JESDOWN . CopyTree(cut_sys);
	_wp1700R_JESDOWN = t_wp1700R_JESDOWN->CopyTree("","");
	_wp1700R_JESDOWN->SetName("wp1700R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1700R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1700R_BTAGUP = ch_wp1700R_BTAGUP . CopyTree(cut_sys);
	_wp1700R_BTAGUP = t_wp1700R_BTAGUP->CopyTree("","");
	_wp1700R_BTAGUP->SetName("wp1700R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1700R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1700R_BTAGDOWN = ch_wp1700R_BTAGDOWN . CopyTree(cut_sys);
	_wp1700R_BTAGDOWN = t_wp1700R_BTAGDOWN->CopyTree("","");
	_wp1700R_BTAGDOWN->SetName("wp1700R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1700R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1700R_JERUP = ch_wp1700R_JERUP . CopyTree(cut_sys);
	_wp1700R_JERUP = t_wp1700R_JERUP->CopyTree("","");
	_wp1700R_JERUP->SetName("wp1700R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1700R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1700R_JERDOWN = ch_wp1700R_JERDOWN . CopyTree(cut_sys);
	_wp1700R_JERDOWN = t_wp1700R_JERDOWN->CopyTree("","");
	_wp1700R_JERDOWN->SetName("wp1700R_JERDOWN"); 

      }

      ch_wp1800R . SetBranchStatus("*",1); 
      TTree * t_wp1800R = ch_wp1800R . CopyTree(cut_sig);
      _wp1800R = t_wp1800R->CopyTree("","");
      _wp1800R->SetName("wp1800R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1800R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1800R_JESUP = ch_wp1800R_JESUP . CopyTree(cut_sys);
	_wp1800R_JESUP = t_wp1800R_JESUP->CopyTree("","");
	_wp1800R_JESUP->SetName("wp1800R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1800R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1800R_JESDOWN = ch_wp1800R_JESDOWN . CopyTree(cut_sys);
	_wp1800R_JESDOWN = t_wp1800R_JESDOWN->CopyTree("","");
	_wp1800R_JESDOWN->SetName("wp1800R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1800R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1800R_BTAGUP = ch_wp1800R_BTAGUP . CopyTree(cut_sys);
	_wp1800R_BTAGUP = t_wp1800R_BTAGUP->CopyTree("","");
	_wp1800R_BTAGUP->SetName("wp1800R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1800R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1800R_BTAGDOWN = ch_wp1800R_BTAGDOWN . CopyTree(cut_sys);
	_wp1800R_BTAGDOWN = t_wp1800R_BTAGDOWN->CopyTree("","");
	_wp1800R_BTAGDOWN->SetName("wp1800R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1800R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1800R_JERUP = ch_wp1800R_JERUP . CopyTree(cut_sys);
	_wp1800R_JERUP = t_wp1800R_JERUP->CopyTree("","");
	_wp1800R_JERUP->SetName("wp1800R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1800R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1800R_JERDOWN = ch_wp1800R_JERDOWN . CopyTree(cut_sys);
	_wp1800R_JERDOWN = t_wp1800R_JERDOWN->CopyTree("","");
	_wp1800R_JERDOWN->SetName("wp1800R_JERDOWN"); 

      }

      ch_wp1900R . SetBranchStatus("*",1); 
      TTree * t_wp1900R = ch_wp1900R . CopyTree(cut_sig);
      _wp1900R = t_wp1900R->CopyTree("","");
      _wp1900R->SetName("wp1900R");

      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp1900R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp1900R_JESUP = ch_wp1900R_JESUP . CopyTree(cut_sys);
	_wp1900R_JESUP = t_wp1900R_JESUP->CopyTree("","");
	_wp1900R_JESUP->SetName("wp1900R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp1900R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp1900R_JESDOWN = ch_wp1900R_JESDOWN . CopyTree(cut_sys);
	_wp1900R_JESDOWN = t_wp1900R_JESDOWN->CopyTree("","");
	_wp1900R_JESDOWN->SetName("wp1900R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp1900R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp1900R_BTAGUP = ch_wp1900R_BTAGUP . CopyTree(cut_sys);
	_wp1900R_BTAGUP = t_wp1900R_BTAGUP->CopyTree("","");
	_wp1900R_BTAGUP->SetName("wp1900R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp1900R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp1900R_BTAGDOWN = ch_wp1900R_BTAGDOWN . CopyTree(cut_sys);
	_wp1900R_BTAGDOWN = t_wp1900R_BTAGDOWN->CopyTree("","");
	_wp1900R_BTAGDOWN->SetName("wp1900R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp1900R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp1900R_JERUP = ch_wp1900R_JERUP . CopyTree(cut_sys);
	_wp1900R_JERUP = t_wp1900R_JERUP->CopyTree("","");
	_wp1900R_JERUP->SetName("wp1900R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp1900R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp1900R_JERDOWN = ch_wp1900R_JERDOWN . CopyTree(cut_sys);
	_wp1900R_JERDOWN = t_wp1900R_JERDOWN->CopyTree("","");
	_wp1900R_JERDOWN->SetName("wp1900R_JERDOWN"); 

      }


      ch_wp2000R . SetBranchStatus("*",1); 
      TTree * t_wp2000R = ch_wp2000R . CopyTree(cut_sig);
      _wp2000R = t_wp2000R->CopyTree("","");
      _wp2000R->SetName("wp2000R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2000R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2000R_JESUP = ch_wp2000R_JESUP . CopyTree(cut_sys);
	_wp2000R_JESUP = t_wp2000R_JESUP->CopyTree("","");
	_wp2000R_JESUP->SetName("wp2000R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2000R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2000R_JESDOWN = ch_wp2000R_JESDOWN . CopyTree(cut_sys);
	_wp2000R_JESDOWN = t_wp2000R_JESDOWN->CopyTree("","");
	_wp2000R_JESDOWN->SetName("wp2000R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2000R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2000R_BTAGUP = ch_wp2000R_BTAGUP . CopyTree(cut_sys);
	_wp2000R_BTAGUP = t_wp2000R_BTAGUP->CopyTree("","");
	_wp2000R_BTAGUP->SetName("wp2000R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2000R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2000R_BTAGDOWN = ch_wp2000R_BTAGDOWN . CopyTree(cut_sys);
	_wp2000R_BTAGDOWN = t_wp2000R_BTAGDOWN->CopyTree("","");
	_wp2000R_BTAGDOWN->SetName("wp2000R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2000R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2000R_JERUP = ch_wp2000R_JERUP . CopyTree(cut_sys);
	_wp2000R_JERUP = t_wp2000R_JERUP->CopyTree("","");
	_wp2000R_JERUP->SetName("wp2000R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2000R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2000R_JERDOWN = ch_wp2000R_JERDOWN . CopyTree(cut_sys);
	_wp2000R_JERDOWN = t_wp2000R_JERDOWN->CopyTree("","");
	_wp2000R_JERDOWN->SetName("wp2000R_JERDOWN"); 

      }

      ch_wp2100R . SetBranchStatus("*",1); 
      TTree * t_wp2100R = ch_wp2100R . CopyTree(cut_sig);
      _wp2100R = t_wp2100R->CopyTree("","");
      _wp2100R->SetName("wp2100R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2100R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2100R_JESUP = ch_wp2100R_JESUP . CopyTree(cut_sys);
	_wp2100R_JESUP = t_wp2100R_JESUP->CopyTree("","");
	_wp2100R_JESUP->SetName("wp2100R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2100R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2100R_JESDOWN = ch_wp2100R_JESDOWN . CopyTree(cut_sys);
	_wp2100R_JESDOWN = t_wp2100R_JESDOWN->CopyTree("","");
	_wp2100R_JESDOWN->SetName("wp2100R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2100R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2100R_BTAGUP = ch_wp2100R_BTAGUP . CopyTree(cut_sys);
	_wp2100R_BTAGUP = t_wp2100R_BTAGUP->CopyTree("","");
	_wp2100R_BTAGUP->SetName("wp2100R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2100R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2100R_BTAGDOWN = ch_wp2100R_BTAGDOWN . CopyTree(cut_sys);
	_wp2100R_BTAGDOWN = t_wp2100R_BTAGDOWN->CopyTree("","");
	_wp2100R_BTAGDOWN->SetName("wp2100R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2100R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2100R_JERUP = ch_wp2100R_JERUP . CopyTree(cut_sys);
	_wp2100R_JERUP = t_wp2100R_JERUP->CopyTree("","");
	_wp2100R_JERUP->SetName("wp2100R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2100R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2100R_JERDOWN = ch_wp2100R_JERDOWN . CopyTree(cut_sys);
	_wp2100R_JERDOWN = t_wp2100R_JERDOWN->CopyTree("","");
	_wp2100R_JERDOWN->SetName("wp2100R_JERDOWN"); 

      }

      ch_wp2200R . SetBranchStatus("*",1); 
      TTree * t_wp2200R = ch_wp2200R . CopyTree(cut_sig);
      _wp2200R = t_wp2200R->CopyTree("","");
      _wp2200R->SetName("wp2200R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2200R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2200R_JESUP = ch_wp2200R_JESUP . CopyTree(cut_sys);
	_wp2200R_JESUP = t_wp2200R_JESUP->CopyTree("","");
	_wp2200R_JESUP->SetName("wp2200R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2200R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2200R_JESDOWN = ch_wp2200R_JESDOWN . CopyTree(cut_sys);
	_wp2200R_JESDOWN = t_wp2200R_JESDOWN->CopyTree("","");
	_wp2200R_JESDOWN->SetName("wp2200R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2200R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2200R_BTAGUP = ch_wp2200R_BTAGUP . CopyTree(cut_sys);
	_wp2200R_BTAGUP = t_wp2200R_BTAGUP->CopyTree("","");
	_wp2200R_BTAGUP->SetName("wp2200R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2200R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2200R_BTAGDOWN = ch_wp2200R_BTAGDOWN . CopyTree(cut_sys);
	_wp2200R_BTAGDOWN = t_wp2200R_BTAGDOWN->CopyTree("","");
	_wp2200R_BTAGDOWN->SetName("wp2200R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2200R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2200R_JERUP = ch_wp2200R_JERUP . CopyTree(cut_sys);
	_wp2200R_JERUP = t_wp2200R_JERUP->CopyTree("","");
	_wp2200R_JERUP->SetName("wp2200R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2200R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2200R_JERDOWN = ch_wp2200R_JERDOWN . CopyTree(cut_sys);
	_wp2200R_JERDOWN = t_wp2200R_JERDOWN->CopyTree("","");
	_wp2200R_JERDOWN->SetName("wp2200R_JERDOWN"); 

      }
   
      ch_wp2300R . SetBranchStatus("*",1); 
      TTree * t_wp2300R = ch_wp2300R . CopyTree(cut_sig);
      _wp2300R = t_wp2300R->CopyTree("","");
      _wp2300R->SetName("wp2300R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2300R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2300R_JESUP = ch_wp2300R_JESUP . CopyTree(cut_sys);
	_wp2300R_JESUP = t_wp2300R_JESUP->CopyTree("","");
	_wp2300R_JESUP->SetName("wp2300R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2300R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2300R_JESDOWN = ch_wp2300R_JESDOWN . CopyTree(cut_sys);
	_wp2300R_JESDOWN = t_wp2300R_JESDOWN->CopyTree("","");
	_wp2300R_JESDOWN->SetName("wp2300R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2300R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2300R_BTAGUP = ch_wp2300R_BTAGUP . CopyTree(cut_sys);
	_wp2300R_BTAGUP = t_wp2300R_BTAGUP->CopyTree("","");
	_wp2300R_BTAGUP->SetName("wp2300R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2300R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2300R_BTAGDOWN = ch_wp2300R_BTAGDOWN . CopyTree(cut_sys);
	_wp2300R_BTAGDOWN = t_wp2300R_BTAGDOWN->CopyTree("","");
	_wp2300R_BTAGDOWN->SetName("wp2300R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2300R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2300R_JERUP = ch_wp2300R_JERUP . CopyTree(cut_sys);
	_wp2300R_JERUP = t_wp2300R_JERUP->CopyTree("","");
	_wp2300R_JERUP->SetName("wp2300R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2300R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2300R_JERDOWN = ch_wp2300R_JERDOWN . CopyTree(cut_sys);
	_wp2300R_JERDOWN = t_wp2300R_JERDOWN->CopyTree("","");
	_wp2300R_JERDOWN->SetName("wp2300R_JERDOWN"); 

      }
   
      ch_wp2400R . SetBranchStatus("*",1); 
      TTree * t_wp2400R = ch_wp2400R . CopyTree(cut_sig);
      _wp2400R = t_wp2400R->CopyTree("","");
      _wp2400R->SetName("wp2400R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2400R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2400R_JESUP = ch_wp2400R_JESUP . CopyTree(cut_sys);
	_wp2400R_JESUP = t_wp2400R_JESUP->CopyTree("","");
	_wp2400R_JESUP->SetName("wp2400R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2400R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2400R_JESDOWN = ch_wp2400R_JESDOWN . CopyTree(cut_sys);
	_wp2400R_JESDOWN = t_wp2400R_JESDOWN->CopyTree("","");
	_wp2400R_JESDOWN->SetName("wp2400R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2400R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2400R_BTAGUP = ch_wp2400R_BTAGUP . CopyTree(cut_sys);
	_wp2400R_BTAGUP = t_wp2400R_BTAGUP->CopyTree("","");
	_wp2400R_BTAGUP->SetName("wp2400R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2400R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2400R_BTAGDOWN = ch_wp2400R_BTAGDOWN . CopyTree(cut_sys);
	_wp2400R_BTAGDOWN = t_wp2400R_BTAGDOWN->CopyTree("","");
	_wp2400R_BTAGDOWN->SetName("wp2400R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2400R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2400R_JERUP = ch_wp2400R_JERUP . CopyTree(cut_sys);
	_wp2400R_JERUP = t_wp2400R_JERUP->CopyTree("","");
	_wp2400R_JERUP->SetName("wp2400R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2400R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2400R_JERDOWN = ch_wp2400R_JERDOWN . CopyTree(cut_sys);
	_wp2400R_JERDOWN = t_wp2400R_JERDOWN->CopyTree("","");
	_wp2400R_JERDOWN->SetName("wp2400R_JERDOWN"); 

      }
    
      ch_wp2500R . SetBranchStatus("*",1); 
      TTree * t_wp2500R = ch_wp2500R . CopyTree(cut_sig);
      _wp2500R = t_wp2500R->CopyTree("","");
      _wp2500R->SetName("wp2500R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2500R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2500R_JESUP = ch_wp2500R_JESUP . CopyTree(cut_sys);
	_wp2500R_JESUP = t_wp2500R_JESUP->CopyTree("","");
	_wp2500R_JESUP->SetName("wp2500R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2500R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2500R_JESDOWN = ch_wp2500R_JESDOWN . CopyTree(cut_sys);
	_wp2500R_JESDOWN = t_wp2500R_JESDOWN->CopyTree("","");
	_wp2500R_JESDOWN->SetName("wp2500R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2500R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2500R_BTAGUP = ch_wp2500R_BTAGUP . CopyTree(cut_sys);
	_wp2500R_BTAGUP = t_wp2500R_BTAGUP->CopyTree("","");
	_wp2500R_BTAGUP->SetName("wp2500R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2500R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2500R_BTAGDOWN = ch_wp2500R_BTAGDOWN . CopyTree(cut_sys);
	_wp2500R_BTAGDOWN = t_wp2500R_BTAGDOWN->CopyTree("","");
	_wp2500R_BTAGDOWN->SetName("wp2500R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2500R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2500R_JERUP = ch_wp2500R_JERUP . CopyTree(cut_sys);
	_wp2500R_JERUP = t_wp2500R_JERUP->CopyTree("","");
	_wp2500R_JERUP->SetName("wp2500R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2500R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2500R_JERDOWN = ch_wp2500R_JERDOWN . CopyTree(cut_sys);
	_wp2500R_JERDOWN = t_wp2500R_JERDOWN->CopyTree("","");
	_wp2500R_JERDOWN->SetName("wp2500R_JERDOWN"); 

      }
   
 
      ch_wp2600R . SetBranchStatus("*",1); 
      TTree * t_wp2600R = ch_wp2600R . CopyTree(cut_sig);
      _wp2600R = t_wp2600R->CopyTree("","");
      _wp2600R->SetName("wp2600R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2600R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2600R_JESUP = ch_wp2600R_JESUP . CopyTree(cut_sys);
	_wp2600R_JESUP = t_wp2600R_JESUP->CopyTree("","");
	_wp2600R_JESUP->SetName("wp2600R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2600R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2600R_JESDOWN = ch_wp2600R_JESDOWN . CopyTree(cut_sys);
	_wp2600R_JESDOWN = t_wp2600R_JESDOWN->CopyTree("","");
	_wp2600R_JESDOWN->SetName("wp2600R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2600R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2600R_BTAGUP = ch_wp2600R_BTAGUP . CopyTree(cut_sys);
	_wp2600R_BTAGUP = t_wp2600R_BTAGUP->CopyTree("","");
	_wp2600R_BTAGUP->SetName("wp2600R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2600R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2600R_BTAGDOWN = ch_wp2600R_BTAGDOWN . CopyTree(cut_sys);
	_wp2600R_BTAGDOWN = t_wp2600R_BTAGDOWN->CopyTree("","");
	_wp2600R_BTAGDOWN->SetName("wp2600R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2600R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2600R_JERUP = ch_wp2600R_JERUP . CopyTree(cut_sys);
	_wp2600R_JERUP = t_wp2600R_JERUP->CopyTree("","");
	_wp2600R_JERUP->SetName("wp2600R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2600R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2600R_JERDOWN = ch_wp2600R_JERDOWN . CopyTree(cut_sys);
	_wp2600R_JERDOWN = t_wp2600R_JERDOWN->CopyTree("","");
	_wp2600R_JERDOWN->SetName("wp2600R_JERDOWN"); 

      }

      ch_wp2700R . SetBranchStatus("*",1); 
      TTree * t_wp2700R = ch_wp2700R . CopyTree(cut_sig);
      _wp2700R = t_wp2700R->CopyTree("","");
      _wp2700R->SetName("wp2700R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2700R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2700R_JESUP = ch_wp2700R_JESUP . CopyTree(cut_sys);
	_wp2700R_JESUP = t_wp2700R_JESUP->CopyTree("","");
	_wp2700R_JESUP->SetName("wp2700R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2700R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2700R_JESDOWN = ch_wp2700R_JESDOWN . CopyTree(cut_sys);
	_wp2700R_JESDOWN = t_wp2700R_JESDOWN->CopyTree("","");
	_wp2700R_JESDOWN->SetName("wp2700R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2700R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2700R_BTAGUP = ch_wp2700R_BTAGUP . CopyTree(cut_sys);
	_wp2700R_BTAGUP = t_wp2700R_BTAGUP->CopyTree("","");
	_wp2700R_BTAGUP->SetName("wp2700R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2700R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2700R_BTAGDOWN = ch_wp2700R_BTAGDOWN . CopyTree(cut_sys);
	_wp2700R_BTAGDOWN = t_wp2700R_BTAGDOWN->CopyTree("","");
	_wp2700R_BTAGDOWN->SetName("wp2700R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2700R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2700R_JERUP = ch_wp2700R_JERUP . CopyTree(cut_sys);
	_wp2700R_JERUP = t_wp2700R_JERUP->CopyTree("","");
	_wp2700R_JERUP->SetName("wp2700R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2700R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2700R_JERDOWN = ch_wp2700R_JERDOWN . CopyTree(cut_sys);
	_wp2700R_JERDOWN = t_wp2700R_JERDOWN->CopyTree("","");
	_wp2700R_JERDOWN->SetName("wp2700R_JERDOWN"); 

      }
   
      ch_wp2800R . SetBranchStatus("*",1); 
      TTree * t_wp2800R = ch_wp2800R . CopyTree(cut_sig);
      _wp2800R = t_wp2800R->CopyTree("","");
      _wp2800R->SetName("wp2800R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2800R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2800R_JESUP = ch_wp2800R_JESUP . CopyTree(cut_sys);
	_wp2800R_JESUP = t_wp2800R_JESUP->CopyTree("","");
	_wp2800R_JESUP->SetName("wp2800R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2800R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2800R_JESDOWN = ch_wp2800R_JESDOWN . CopyTree(cut_sys);
	_wp2800R_JESDOWN = t_wp2800R_JESDOWN->CopyTree("","");
	_wp2800R_JESDOWN->SetName("wp2800R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2800R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2800R_BTAGUP = ch_wp2800R_BTAGUP . CopyTree(cut_sys);
	_wp2800R_BTAGUP = t_wp2800R_BTAGUP->CopyTree("","");
	_wp2800R_BTAGUP->SetName("wp2800R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2800R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2800R_BTAGDOWN = ch_wp2800R_BTAGDOWN . CopyTree(cut_sys);
	_wp2800R_BTAGDOWN = t_wp2800R_BTAGDOWN->CopyTree("","");
	_wp2800R_BTAGDOWN->SetName("wp2800R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2800R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2800R_JERUP = ch_wp2800R_JERUP . CopyTree(cut_sys);
	_wp2800R_JERUP = t_wp2800R_JERUP->CopyTree("","");
	_wp2800R_JERUP->SetName("wp2800R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2800R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2800R_JERDOWN = ch_wp2800R_JERDOWN . CopyTree(cut_sys);
	_wp2800R_JERDOWN = t_wp2800R_JERDOWN->CopyTree("","");
	_wp2800R_JERDOWN->SetName("wp2800R_JERDOWN"); 

      }
   
      ch_wp2900R . SetBranchStatus("*",1); 
      TTree * t_wp2900R = ch_wp2900R . CopyTree(cut_sig);
      _wp2900R = t_wp2900R->CopyTree("","");
      _wp2900R->SetName("wp2900R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp2900R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp2900R_JESUP = ch_wp2900R_JESUP . CopyTree(cut_sys);
	_wp2900R_JESUP = t_wp2900R_JESUP->CopyTree("","");
	_wp2900R_JESUP->SetName("wp2900R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp2900R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp2900R_JESDOWN = ch_wp2900R_JESDOWN . CopyTree(cut_sys);
	_wp2900R_JESDOWN = t_wp2900R_JESDOWN->CopyTree("","");
	_wp2900R_JESDOWN->SetName("wp2900R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp2900R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp2900R_BTAGUP = ch_wp2900R_BTAGUP . CopyTree(cut_sys);
	_wp2900R_BTAGUP = t_wp2900R_BTAGUP->CopyTree("","");
	_wp2900R_BTAGUP->SetName("wp2900R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp2900R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp2900R_BTAGDOWN = ch_wp2900R_BTAGDOWN . CopyTree(cut_sys);
	_wp2900R_BTAGDOWN = t_wp2900R_BTAGDOWN->CopyTree("","");
	_wp2900R_BTAGDOWN->SetName("wp2900R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp2900R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp2900R_JERUP = ch_wp2900R_JERUP . CopyTree(cut_sys);
	_wp2900R_JERUP = t_wp2900R_JERUP->CopyTree("","");
	_wp2900R_JERUP->SetName("wp2900R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp2900R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp2900R_JERDOWN = ch_wp2900R_JERDOWN . CopyTree(cut_sys);
	_wp2900R_JERDOWN = t_wp2900R_JERDOWN->CopyTree("","");
	_wp2900R_JERDOWN->SetName("wp2900R_JERDOWN"); 

      }
                
      ch_wp3000R . SetBranchStatus("*",1); 
      TTree * t_wp3000R = ch_wp3000R . CopyTree(cut_sig);
      _wp3000R = t_wp3000R->CopyTree("","");
      _wp3000R->SetName("wp3000R");
      if (ifsys && i==1) {
	std::cout << " set systematics _JESUP ======== " << std::endl;
	ch_wp3000R_JESUP . SetBranchStatus("*",1);
	TTree * t_wp3000R_JESUP = ch_wp3000R_JESUP . CopyTree(cut_sys);
	_wp3000R_JESUP = t_wp3000R_JESUP->CopyTree("","");
	_wp3000R_JESUP->SetName("wp3000R_JESUP"); 

	std::cout << " set systematics _JESDOWN ======== " << std::endl;
	ch_wp3000R_JESDOWN . SetBranchStatus("*",1);
	TTree * t_wp3000R_JESDOWN = ch_wp3000R_JESDOWN . CopyTree(cut_sys);
	_wp3000R_JESDOWN = t_wp3000R_JESDOWN->CopyTree("","");
	_wp3000R_JESDOWN->SetName("wp3000R_JESDOWN"); 

	std::cout << " set systematics _BTAGUP ======== " << std::endl;
	ch_wp3000R_BTAGUP . SetBranchStatus("*",1);
	TTree * t_wp3000R_BTAGUP = ch_wp3000R_BTAGUP . CopyTree(cut_sys);
	_wp3000R_BTAGUP = t_wp3000R_BTAGUP->CopyTree("","");
	_wp3000R_BTAGUP->SetName("wp3000R_BTAGUP"); 

	std::cout << " set systematics _BTAGDOWN ======== " << std::endl;
	ch_wp3000R_BTAGDOWN . SetBranchStatus("*",1);
	TTree * t_wp3000R_BTAGDOWN = ch_wp3000R_BTAGDOWN . CopyTree(cut_sys);
	_wp3000R_BTAGDOWN = t_wp3000R_BTAGDOWN->CopyTree("","");
	_wp3000R_BTAGDOWN->SetName("wp3000R_BTAGDOWN"); 

	std::cout << " set systematics _JERUP ======== " << std::endl;
	ch_wp3000R_JERUP . SetBranchStatus("*",1);
	TTree * t_wp3000R_JERUP = ch_wp3000R_JERUP . CopyTree(cut_sys);
	_wp3000R_JERUP = t_wp3000R_JERUP->CopyTree("","");
	_wp3000R_JERUP->SetName("wp3000R_JERUP"); 

	std::cout << " set systematics _JERDOWN ======== " << std::endl;
	ch_wp3000R_JERDOWN . SetBranchStatus("*",1);
	TTree * t_wp3000R_JERDOWN = ch_wp3000R_JERDOWN . CopyTree(cut_sys);
	_wp3000R_JERDOWN = t_wp3000R_JERDOWN->CopyTree("","");
	_wp3000R_JERDOWN->SetName("wp3000R_JERDOWN"); 

      }

   
      TFile * out_file = new TFile(outfile, "RECREATE");
      out_file->cd();
      std::cout << "writing " << outfile << std::endl;
      if (i==1)  { 
	_data->Write();
	std::cout << " wrote data ======== " << std::endl;
      }
      _ttbar->Write();
      std::cout << " wrote ttbar ======== " << std::endl;
      if (ifsys && i==1) {
	_ttbar_JESUP->Write();
	_ttbar_JESDOWN->Write();
	_ttbar_BTAGUP->Write();
	_ttbar_BTAGDOWN->Write();
	_ttbar_JERUP->Write();
	_ttbar_JERDOWN->Write();
      }
      _wjets->Write();
      std::cout << " wrote wjets ======== " << std::endl;
      if (ifsys && i==1) {
	_wjets_JESUP->Write();
	_wjets_JESDOWN->Write();
	_wjets_BTAGUP->Write();
	_wjets_BTAGDOWN->Write();
	_wjets_JERUP->Write();
	_wjets_JERDOWN->Write();
      }
      _s->Write();
      std::cout << " wrote s ======== " << std::endl;
      if (ifsys && i==1) {
	_s_JESUP->Write();
	_s_JESDOWN->Write();
	_s_BTAGUP->Write();
	_s_BTAGDOWN->Write();
	_s_JERUP->Write();
	_s_JERDOWN->Write();
      }
      _bs->Write();
      std::cout << " wrote bs ======== " << std::endl;
      if (ifsys && i==1) {
	_bs_JESUP->Write();
	_bs_JESDOWN->Write();
	_bs_BTAGUP->Write();
	_bs_BTAGDOWN->Write();
	_bs_JERUP->Write();
	_bs_JERDOWN->Write();
      }
      _t->Write();
      std::cout << " wrote t ======== " << std::endl;
      if (ifsys && i==1) {
	_t_JESUP->Write();
	_t_JESDOWN->Write();
	_t_BTAGUP->Write();
	_t_BTAGDOWN->Write();
	_t_JERUP->Write();
	_t_JERDOWN->Write();
      }
      _bt->Write();
      std::cout << " wrote bt ======== " << std::endl;
      if (ifsys && i==1) {
	_bt_JESUP->Write();
	_bt_JESDOWN->Write();
	_bt_BTAGUP->Write();
	_bt_BTAGDOWN->Write();
	_bt_JERUP->Write();
	_bt_JERDOWN->Write();
      }
      _tw->Write();
      std::cout << " wrote tw ======== " << std::endl;
      if (ifsys && i==1) {
	_tw_JESUP->Write();
	_tw_JESDOWN->Write();
	_tw_BTAGUP->Write();
	_tw_BTAGDOWN->Write();
	_tw_JERUP->Write();
	_tw_JERDOWN->Write();
      }
      _btw->Write();
      std::cout << " wrote btw ======== " << std::endl;
      if (ifsys && i==1) {
	_btw_JESUP->Write();
	_btw_JESDOWN->Write();
	_btw_BTAGUP->Write();
	_btw_BTAGDOWN->Write();
	_btw_JERUP->Write();
	_btw_JERDOWN->Write();
      }
      _zjets->Write();
      std::cout << " wrote zjets ======== " << std::endl;
      if (ifsys && i==1) {
	_zjets_JESUP->Write();
	_zjets_JESDOWN->Write();
	_zjets_BTAGUP->Write();
	_zjets_BTAGDOWN->Write();
	_zjets_JERUP->Write();
	_zjets_JERDOWN->Write();
      }
      _ww->Write();
      std::cout << " wrote ww ======== " << std::endl;
      if (ifsys && i==1) {
	_ww_JESUP->Write();
	_ww_JESDOWN->Write();
	_ww_BTAGUP->Write();
	_ww_BTAGDOWN->Write();
	_ww_JERUP->Write();
	_ww_JERDOWN->Write();
      }
      _wp1100R->Write();
      std::cout << " wrote wp1100R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1100R_JESUP->Write();
	_wp1100R_JESDOWN->Write();
	_wp1100R_BTAGUP->Write();
	_wp1100R_BTAGDOWN->Write();
	_wp1100R_JERUP->Write();
	_wp1100R_JERDOWN->Write();
      }
      _wp1200R->Write();
      std::cout << " wrote wp1200R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1200R_JESUP->Write();
	_wp1200R_JESDOWN->Write();
	_wp1200R_BTAGUP->Write();
	_wp1200R_BTAGDOWN->Write();
	_wp1200R_JERUP->Write();
	_wp1200R_JERDOWN->Write();
      }
      _wp1300R->Write();
      std::cout << " wrote wp1300R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1300R_JESUP->Write();
	_wp1300R_JESDOWN->Write();
	_wp1300R_BTAGUP->Write();
	_wp1300R_BTAGDOWN->Write();
	_wp1300R_JERUP->Write();
	_wp1300R_JERDOWN->Write();
      }
      _wp1400R->Write();
      std::cout << " wrote wp14000R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1400R_JESUP->Write();
	_wp1400R_JESDOWN->Write();
	_wp1400R_BTAGUP->Write();
	_wp1400R_BTAGDOWN->Write();
	_wp1400R_JERUP->Write();
	_wp1400R_JERDOWN->Write();
      }
      _wp1500R->Write();
      std::cout << " wrote wp1500R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1500R_JESUP->Write();
	_wp1500R_JESDOWN->Write();
	_wp1500R_BTAGUP->Write();
	_wp1500R_BTAGDOWN->Write();
	_wp1500R_JERUP->Write();
	_wp1500R_JERDOWN->Write();
      }
      _wp1600R->Write();
      std::cout << " wrote wp1600R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1600R_JESUP->Write();
	_wp1600R_JESDOWN->Write();
	_wp1600R_BTAGUP->Write();
	_wp1600R_BTAGDOWN->Write();
	_wp1600R_JERUP->Write();
	_wp1600R_JERDOWN->Write();
      }
      _wp1700R->Write();
      std::cout << " wrote wp1700R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1700R_JESUP->Write();
	_wp1700R_JESDOWN->Write();
	_wp1700R_BTAGUP->Write();
	_wp1700R_BTAGDOWN->Write();
	_wp1700R_JERUP->Write();
	_wp1700R_JERDOWN->Write();
      }
      _wp1800R->Write();
      std::cout << " wrote wp1800R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1800R_JESUP->Write();
	_wp1800R_JESDOWN->Write();
	_wp1800R_BTAGUP->Write();
	_wp1800R_BTAGDOWN->Write();
	_wp1800R_JERUP->Write();
	_wp1800R_JERDOWN->Write();
      }
      _wp1900R->Write();
      std::cout << " wrote wp1900R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp1900R_JESUP->Write();
	_wp1900R_JESDOWN->Write();
	_wp1900R_BTAGUP->Write();
	_wp1900R_BTAGDOWN->Write();
	_wp1900R_JERUP->Write();
	_wp1900R_JERDOWN->Write();
      }
      _wp2000R->Write();
      std::cout << " wrote wp2000R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2000R_JESUP->Write();
	_wp2000R_JESDOWN->Write();
	_wp2000R_BTAGUP->Write();
	_wp2000R_BTAGDOWN->Write();
	_wp2000R_JERUP->Write();
	_wp2000R_JERDOWN->Write();
      }
      _wp2100R->Write();
      std::cout << " wrote wp2100R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2100R_JESUP->Write();
	_wp2100R_JESDOWN->Write();
	_wp2100R_BTAGUP->Write();
	_wp2100R_BTAGDOWN->Write();
	_wp2100R_JERUP->Write();
	_wp2100R_JERDOWN->Write();
      }
      _wp2200R->Write();
      std::cout << " wrote wp2200R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2200R_JESUP->Write();
	_wp2200R_JESDOWN->Write();
	_wp2200R_BTAGUP->Write();
	_wp2200R_BTAGDOWN->Write();
	_wp2200R_JERUP->Write();
	_wp2200R_JERDOWN->Write();
      }
      _wp2300R->Write();
      std::cout << " wrote wp2300R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2300R_JESUP->Write();
	_wp2300R_JESDOWN->Write();
	_wp2300R_BTAGUP->Write();
	_wp2300R_BTAGDOWN->Write();
	_wp2300R_JERUP->Write();
	_wp2300R_JERDOWN->Write();
      }
      _wp2400R->Write();
      std::cout << " wrote wp2400R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2400R_JESUP->Write();
	_wp2400R_JESDOWN->Write();
	_wp2400R_BTAGUP->Write();
	_wp2400R_BTAGDOWN->Write();
	_wp2400R_JERUP->Write();
	_wp2400R_JERDOWN->Write();
      }
      _wp2500R->Write();
      std::cout << " wrote wp2500R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2500R_JESUP->Write();
	_wp2500R_JESDOWN->Write();
	_wp2500R_BTAGUP->Write();
	_wp2500R_BTAGDOWN->Write();
	_wp2500R_JERUP->Write();
	_wp2500R_JERDOWN->Write();
      }
      _wp2600R->Write();
      std::cout << " wrote wp2600R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2600R_JESUP->Write();
	_wp2600R_JESDOWN->Write();
	_wp2600R_BTAGUP->Write();
	_wp2600R_BTAGDOWN->Write();
	_wp2600R_JERUP->Write();
	_wp2600R_JERDOWN->Write();
      }
      _wp2700R->Write();
      std::cout << " wrote wp2700R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2700R_JESUP->Write();
	_wp2700R_JESDOWN->Write();
	_wp2700R_BTAGUP->Write();
	_wp2700R_BTAGDOWN->Write();
	_wp2700R_JERUP->Write();
	_wp2700R_JERDOWN->Write();
      }
      _wp2800R->Write();
      std::cout << " wrote wp2800R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2800R_JESUP->Write();
	_wp2800R_JESDOWN->Write();
	_wp2800R_BTAGUP->Write();
	_wp2800R_BTAGDOWN->Write();
	_wp2800R_JERUP->Write();
	_wp2800R_JERDOWN->Write();
      }
      _wp2900R->Write();
      std::cout << " wrote wp2900R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp2900R_JESUP->Write();
	_wp2900R_JESDOWN->Write();
	_wp2900R_BTAGUP->Write();
	_wp2900R_BTAGDOWN->Write();
	_wp2900R_JERUP->Write();
	_wp2900R_JERDOWN->Write();
      }
      _wp3000R->Write();
      std::cout << " wrote wp3000R ======== " << std::endl;
      if (ifsys && i==1) {
	_wp3000R_JESUP->Write();
	_wp3000R_JESDOWN->Write();
	_wp3000R_BTAGUP->Write();
	_wp3000R_BTAGDOWN->Write();
	_wp3000R_JERUP->Write();
	_wp3000R_JERDOWN->Write();
      }
      /*
	if (ifsys && i==1) {
	_ttbar_matchingup->Write();
	_ttbar_matchingdown->Write();
	_ttbar_scaleup->Write();
	_ttbar_scaledown->Write();
	}
      */
      out_file->Write();
      std::cout << " wrote out file  "<< outfile << std::endl ;
      out_file->Close();
      delete out_file;
    }
    std::cout << " done ... " << std::endl;
 
  }// train and yield 
}
