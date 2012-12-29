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
  bool ifdata = false;
  bool ifsys = false;

  TString indir = "/uscms_data/d2/dsperka/8TeV/Samples/16Nov_53X/";
  //TString indir = "/home/dsperka/CMS/Wprimetb/8TeV/plots_53x/";
  TString chan[2] = {"el", "mu"};
  
  for (int j=0; j<2; j++) {

    TString channel = chan[j];
     
    if (j==0) std::cout << "****Electron Channel*****" << std::endl;
    if (j==1) std::cout << "****Muon Channel*****" << std::endl;

    std::cout << " add nominal root files... " << std::endl;

    TChain ch_data("ljmet");

    TChain ch_ttbar("ljmet");
    TChain ch_ttbar_JES_UP("ljmet"); 
    TChain ch_ttbar_JES_DOWN("ljmet"); 
    TChain ch_ttbar_BTAG_UP("ljmet"); 
    TChain ch_ttbar_BTAG_DOWN("ljmet"); 
    TChain ch_ttbar_JER_UP("ljmet"); 
    TChain ch_ttbar_JER_DOWN("ljmet"); 

    TChain ch_wjets("ljmet");
    TChain ch_wjets_JES_UP("ljmet"); 
    TChain ch_wjets_JES_DOWN("ljmet"); 
    TChain ch_wjets_BTAG_UP("ljmet"); 
    TChain ch_wjets_BTAG_DOWN("ljmet"); 
    TChain ch_wjets_JER_UP("ljmet"); 
    TChain ch_wjets_JER_DOWN("ljmet"); 

    TChain ch_s("ljmet");
    TChain ch_s_JES_UP("ljmet"); 
    TChain ch_s_JES_DOWN("ljmet"); 
    TChain ch_s_BTAG_UP("ljmet"); 
    TChain ch_s_BTAG_DOWN("ljmet"); 
    TChain ch_s_JER_UP("ljmet"); 
    TChain ch_s_JER_DOWN("ljmet"); 

    TChain ch_bs("ljmet");
    TChain ch_bs_JES_UP("ljmet"); 
    TChain ch_bs_JES_DOWN("ljmet"); 
    TChain ch_bs_BTAG_UP("ljmet"); 
    TChain ch_bs_BTAG_DOWN("ljmet"); 
    TChain ch_bs_JER_UP("ljmet"); 
    TChain ch_bs_JER_DOWN("ljmet"); 

    TChain ch_t("ljmet");
    TChain ch_t_JES_UP("ljmet"); 
    TChain ch_t_JES_DOWN("ljmet"); 
    TChain ch_t_BTAG_UP("ljmet"); 
    TChain ch_t_BTAG_DOWN("ljmet"); 
    TChain ch_t_JER_UP("ljmet"); 
    TChain ch_t_JER_DOWN("ljmet"); 

    TChain ch_bt("ljmet");
    TChain ch_bt_JES_UP("ljmet"); 
    TChain ch_bt_JES_DOWN("ljmet"); 
    TChain ch_bt_BTAG_UP("ljmet"); 
    TChain ch_bt_BTAG_DOWN("ljmet"); 
    TChain ch_bt_JER_UP("ljmet"); 
    TChain ch_bt_JER_DOWN("ljmet"); 

    TChain ch_tw("ljmet");
    TChain ch_tw_JES_UP("ljmet"); 
    TChain ch_tw_JES_DOWN("ljmet"); 
    TChain ch_tw_BTAG_UP("ljmet"); 
    TChain ch_tw_BTAG_DOWN("ljmet"); 
    TChain ch_tw_JER_UP("ljmet"); 
    TChain ch_tw_JER_DOWN("ljmet"); 

    TChain ch_btw("ljmet");
    TChain ch_btw_JES_UP("ljmet"); 
    TChain ch_btw_JES_DOWN("ljmet"); 
    TChain ch_btw_BTAG_UP("ljmet"); 
    TChain ch_btw_BTAG_DOWN("ljmet"); 
    TChain ch_btw_JER_UP("ljmet"); 
    TChain ch_btw_JER_DOWN("ljmet"); 

    TChain ch_zjets("ljmet");
    TChain ch_zjets_JES_UP("ljmet"); 
    TChain ch_zjets_JES_DOWN("ljmet"); 
    TChain ch_zjets_BTAG_UP("ljmet"); 
    TChain ch_zjets_BTAG_DOWN("ljmet"); 
    TChain ch_zjets_JER_UP("ljmet"); 
    TChain ch_zjets_JER_DOWN("ljmet"); 

    TChain ch_ww("ljmet");
    TChain ch_ww_JES_UP("ljmet"); 
    TChain ch_ww_JES_DOWN("ljmet"); 
    TChain ch_ww_BTAG_UP("ljmet"); 
    TChain ch_ww_BTAG_DOWN("ljmet"); 
    TChain ch_ww_JER_UP("ljmet"); 
    TChain ch_ww_JER_DOWN("ljmet"); 

    TChain ch_wp1700R("ljmet");
    TChain ch_wp1700R_JES_UP("ljmet"); 
    TChain ch_wp1700R_JES_DOWN("ljmet"); 
    TChain ch_wp1700R_BTAG_UP("ljmet"); 
    TChain ch_wp1700R_BTAG_DOWN("ljmet"); 
    TChain ch_wp1700R_JER_UP("ljmet"); 
    TChain ch_wp1700R_JER_DOWN("ljmet"); 

    TChain ch_wp1900R("ljmet");
    TChain ch_wp1900R_JES_UP("ljmet"); 
    TChain ch_wp1900R_JES_DOWN("ljmet"); 
    TChain ch_wp1900R_BTAG_UP("ljmet"); 
    TChain ch_wp1900R_BTAG_DOWN("ljmet"); 
    TChain ch_wp1900R_JER_UP("ljmet"); 
    TChain ch_wp1900R_JER_DOWN("ljmet"); 

    TChain ch_wp2100R("ljmet");
    TChain ch_wp2100R_JES_UP("ljmet"); 
    TChain ch_wp2100R_JES_DOWN("ljmet"); 
    TChain ch_wp2100R_BTAG_UP("ljmet"); 
    TChain ch_wp2100R_BTAG_DOWN("ljmet"); 
    TChain ch_wp2100R_JER_UP("ljmet"); 
    TChain ch_wp2100R_JER_DOWN("ljmet"); 

    TChain ch_ttbar_matchingup("ljmet"); 
    TChain ch_ttbar_matchingdown("ljmet"); 
    TChain ch_ttbar_scaleup("ljmet"); 
    TChain ch_ttbar_scaledown("ljmet"); 

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

    TTree * _wp1700R;
    TTree * _wp1900R;
    TTree * _wp2100R;
  
    TTree * _ttbar_JES_UP;
    TTree * _ttbar_JES_DOWN;
    TTree * _ttbar_JER_UP;
    TTree * _ttbar_JER_DOWN;
    TTree * _ttbar_BTAG_UP;
    TTree * _ttbar_BTAG_DOWN;

    TTree * _wjets_JES_UP;
    TTree * _wjets_JES_DOWN;
    TTree * _wjets_JER_UP;
    TTree * _wjets_JER_DOWN;
    TTree * _wjets_BTAG_UP;
    TTree * _wjets_BTAG_DOWN;

    TTree * _s_JES_UP;
    TTree * _s_JES_DOWN;
    TTree * _s_JER_UP;
    TTree * _s_JER_DOWN;
    TTree * _s_BTAG_UP;
    TTree * _s_BTAG_DOWN;

    TTree * _bs_JES_UP;
    TTree * _bs_JES_DOWN;
    TTree * _bs_JER_UP;
    TTree * _bs_JER_DOWN;
    TTree * _bs_BTAG_UP;
    TTree * _bs_BTAG_DOWN;

    TTree * _t_JES_UP;
    TTree * _t_JES_DOWN;
    TTree * _t_JER_UP;
    TTree * _t_JER_DOWN;
    TTree * _t_BTAG_UP;
    TTree * _t_BTAG_DOWN;

    TTree * _bt_JES_UP;
    TTree * _bt_JES_DOWN;
    TTree * _bt_JER_UP;
    TTree * _bt_JER_DOWN;
    TTree * _bt_BTAG_UP;
    TTree * _bt_BTAG_DOWN;

    TTree * _tw_JES_UP;
    TTree * _tw_JES_DOWN;
    TTree * _tw_JER_UP;
    TTree * _tw_JER_DOWN;
    TTree * _tw_BTAG_UP;
    TTree * _tw_BTAG_DOWN;

    TTree * _btw_JES_UP;
    TTree * _btw_JES_DOWN;
    TTree * _btw_JER_UP;
    TTree * _btw_JER_DOWN;
    TTree * _btw_BTAG_UP;
    TTree * _btw_BTAG_DOWN;

    TTree * _zjets_JES_UP;
    TTree * _zjets_JES_DOWN;
    TTree * _zjets_JER_UP;
    TTree * _zjets_JER_DOWN;
    TTree * _zjets_BTAG_UP;
    TTree * _zjets_BTAG_DOWN;

    TTree * _ww_JES_UP;
    TTree * _ww_JES_DOWN;
    TTree * _ww_JER_UP;
    TTree * _ww_JER_DOWN;
    TTree * _ww_BTAG_UP;
    TTree * _ww_BTAG_DOWN;

    TTree * _ttbar_matchingup;
    TTree * _ttbar_matchingdown;
    TTree * _ttbar_scaleup;
    TTree * _ttbar_scaledown;

    TTree * _wp1700R_JES_UP;
    TTree * _wp1700R_JES_DOWN;
    TTree * _wp1700R_JER_UP;
    TTree * _wp1700R_JER_DOWN;
    TTree * _wp1700R_BTAG_UP;
    TTree * _wp1700R_BTAG_DOWN;
    TTree * _wp1900R_JES_UP;
    TTree * _wp1900R_JES_DOWN;
    TTree * _wp1900R_JER_UP;
    TTree * _wp1900R_JER_DOWN;
    TTree * _wp1900R_BTAG_UP;
    TTree * _wp1900R_BTAG_DOWN;
    TTree * _wp2100R_JES_UP;
    TTree * _wp2100R_JES_DOWN;
    TTree * _wp2100R_JER_UP;
    TTree * _wp2100R_JER_DOWN;
    TTree * _wp2100R_BTAG_UP;
    TTree * _wp2100R_BTAG_DOWN;


    std::cout << " add  root files... " << std::endl;
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
      
    ch_wp1700R . Add(indir + "Wprime1700Right/Wprime1700Right_1.root");
    ch_wp1900R . Add(indir + "Wprime1900Right/Wprime1900Right_1.root");
    ch_wp2100R . Add(indir + "Wprime2100Right/Wprime2100Right_1.root");

    if (ifsys) {
      std::cout << " add _JES_UP root files... " << std::endl;
      ch_ttbar_JES_UP . Add(indir + "TTbar_Madgraph_JES_UP_el.root");
      ch_wjets_JES_UP . Add(indir + "WJets_JES_UP_el.root");
      ch_s_JES_UP . Add(indir + "T_s_JES_UP_el.root");
      ch_bs_JES_UP . Add(indir + "Tbar_s_JES_UP_el.root");
      ch_t_JES_UP . Add(indir + "T_t_JES_UP_el.root");
      ch_bt_JES_UP . Add(indir + "Tbar_t_JES_UP_el.root");
      ch_tw_JES_UP . Add(indir + "T_tW_JES_UP_el.root");
      ch_btw_JES_UP . Add(indir + "Tbar_tW_JES_UP_el.root");
      ch_zjets_JES_UP . Add(indir + "ZJets_JES_UP_el.root");
      ch_ww_JES_UP . Add(indir + "WW_JES_UP_el.root");
      
      ch_wp1700R_JES_UP . Add(indir + "Wprime1700Right/Wprime1700Right_1_JES_UP.root");
      ch_wp1900R_JES_UP . Add(indir + "Wprime1700Right/Wprime1900Right_1_JES_UP.root");
      ch_wp2100R_JES_UP . Add(indir + "Wprime1700Right/Wprime2100Right_1_JES_UP.root");

      std::cout << " add _JES_DOWN root files... " << std::endl;
      ch_ttbar_JES_DOWN . Add(indir + "TTbar_Madgraph_JES_DOWN_el.root");
      ch_wjets_JES_DOWN . Add(indir + "WJets_JES_DOWN_el.root");
      ch_s_JES_DOWN . Add(indir + "T_s_JES_DOWN_el.root");
      ch_bs_JES_DOWN . Add(indir + "Tbar_s_JES_DOWN_el.root");
      ch_t_JES_DOWN . Add(indir + "T_t_JES_DOWN_el.root");
      ch_bt_JES_DOWN . Add(indir + "Tbar_t_JES_DOWN_el.root");
      ch_tw_JES_DOWN . Add(indir + "T_tW_JES_DOWN_el.root");
      ch_btw_JES_DOWN . Add(indir + "Tbar_tW_JES_DOWN_el.root");
      ch_zjets_JES_DOWN . Add(indir + "ZJets_JES_DOWN_el.root");
      ch_ww_JES_DOWN . Add(indir + "WW_JES_DOWN_el.root");
      
      ch_wp1700R_JES_DOWN . Add(indir + "Wprime1700Right/Wprime1700Right_1_JES_DOWN.root");
      ch_wp1900R_JES_DOWN . Add(indir + "Wprime1700Right/Wprime1900Right_1_JES_DOWN.root");
      ch_wp2100R_JES_DOWN . Add(indir + "Wprime1700Right/Wprime2100Right_1_JES_DOWN.root");


      std::cout << " add _BTAG_UP root files... " << std::endl;
      ch_ttbar_BTAG_UP . Add(indir + "TTbar_Madgraph_BTAG_UP_el.root");
      ch_wjets_BTAG_UP . Add(indir + "WJets_BTAG_UP_el.root");
      ch_s_BTAG_UP . Add(indir + "T_s_BTAG_UP_el.root");
      ch_bs_BTAG_UP . Add(indir + "Tbar_s_BTAG_UP_el.root");
      ch_t_BTAG_UP . Add(indir + "T_t_BTAG_UP_el.root");
      ch_bt_BTAG_UP . Add(indir + "Tbar_t_BTAG_UP_el.root");
      ch_tw_BTAG_UP . Add(indir + "T_tW_BTAG_UP_el.root");
      ch_btw_BTAG_UP . Add(indir + "Tbar_tW_BTAG_UP_el.root");
      ch_zjets_BTAG_UP . Add(indir + "ZJets_BTAG_UP_el.root");
      ch_ww_BTAG_UP . Add(indir + "WW_BTAG_UP_el.root");
            
      ch_wp1700R_BTAG_UP . Add(indir + "Wprime1700Right/Wprime1700Right_1_BTAG_UP.root");
      ch_wp1900R_BTAG_UP . Add(indir + "Wprime1700Right/Wprime1900Right_1_BTAG_UP.root");
      ch_wp2100R_BTAG_UP . Add(indir + "Wprime1700Right/Wprime2100Right_1_BTAG_UP.root");


      std::cout << " add _BTAG_DOWN root files... " << std::endl;
      ch_ttbar_BTAG_DOWN . Add(indir + "TTbar_Madgraph_BTAG_DOWN_el.root");
      ch_wjets_BTAG_DOWN . Add(indir + "WJets_BTAG_DOWN_el.root");
      ch_s_BTAG_DOWN . Add(indir + "T_s_BTAG_DOWN_el.root");
      ch_bs_BTAG_DOWN . Add(indir + "Tbar_s_BTAG_DOWN_el.root");
      ch_t_BTAG_DOWN . Add(indir + "T_t_BTAG_DOWN_el.root");
      ch_bt_BTAG_DOWN . Add(indir + "Tbar_t_BTAG_DOWN_el.root");
      ch_tw_BTAG_DOWN . Add(indir + "T_tW_BTAG_DOWN_el.root");
      ch_btw_BTAG_DOWN . Add(indir + "Tbar_tW_BTAG_DOWN_el.root");
      ch_zjets_BTAG_DOWN . Add(indir + "ZJets_BTAG_DOWN_el.root");
      ch_ww_BTAG_DOWN . Add(indir + "WW_BTAG_DOWN_el.root");
      
      ch_wp1700R_BTAG_DOWN . Add(indir + "Wprime1700Right/Wprime1700Right_1_BTAG_DOWN.root");
      ch_wp1900R_BTAG_DOWN . Add(indir + "Wprime1900Right/Wprime1900Right_1_BTAG_DOWN.root");
      ch_wp2100R_BTAG_DOWN . Add(indir + "Wprime2100Right/Wprime2100Right_1_BTAG_DOWN.root");


      std::cout << " add _JER_UP root files... " << std::endl;
      ch_ttbar_JER_UP . Add(indir + "TTbar_Madgraph_JER_UP_el.root");
      ch_wjets_JER_UP . Add(indir + "WJets_JER_UP_el.root");
      ch_s_JER_UP . Add(indir + "T_s_JER_UP_el.root");
      ch_bs_JER_UP . Add(indir + "Tbar_s_JER_UP_el.root");
      ch_t_JER_UP . Add(indir + "T_t_JER_UP_el.root");
      ch_bt_JER_UP . Add(indir + "Tbar_t_JER_UP_el.root");
      ch_tw_JER_UP . Add(indir + "T_tW_JER_UP_el.root");
      ch_btw_JER_UP . Add(indir + "Tbar_tW_JER_UP_el.root");
      ch_zjets_JER_UP . Add(indir + "ZJets_JER_UP_el.root");
      ch_ww_JER_UP . Add(indir + "WW_JER_UP_el.root");
      
      ch_wp1700R_JER_UP . Add(indir + "Wprime1700Right/Wprime1700Right_1_JER_UP.root");
      ch_wp1900R_JER_UP . Add(indir + "Wprime1900Right/Wprime1900Right_1_JER_UP.root");
      ch_wp2100R_JER_UP . Add(indir + "Wprime2100Right/Wprime2100Right_1_JER_UP.root");


      std::cout << " add _JER_DOWN root files... " << std::endl;
      ch_ttbar_JER_DOWN . Add(indir + "TTbar_Madgraph_JER_DOWN_el.root");
      ch_wjets_JER_DOWN . Add(indir + "WJets_JER_DOWN_el.root");
      ch_s_JER_DOWN . Add(indir + "T_s_JER_DOWN_el.root");
      ch_bs_JER_DOWN . Add(indir + "Tbar_s_JER_DOWN_el.root");
      ch_t_JER_DOWN . Add(indir + "T_t_JER_DOWN_el.root");
      ch_bt_JER_DOWN . Add(indir + "Tbar_t_JER_DOWN_el.root");
      ch_tw_JER_DOWN . Add(indir + "T_tW_JER_DOWN_el.root");
      ch_btw_JER_DOWN . Add(indir + "Tbar_tW_JER_DOWN_el.root");
      ch_zjets_JER_DOWN . Add(indir + "ZJets_JER_DOWN_el.root");
      ch_ww_JER_DOWN . Add(indir + "WW_JER_DOWN_el.root");
      
      ch_wp1700R_JER_DOWN . Add(indir + "Wprime1700Right/Wprime1700Right_1_JER_DOWN.root");
      ch_wp1900R_JER_DOWN . Add(indir + "Wprime1900Right/Wprime1900Right_1_JER_DOWN.root");
      ch_wp2100R_JER_DOWN . Add(indir + "Wprime2100Right/Wprime2100Right_1_JER_DOWN.root");


      //ch_ttbar_matchingdown . Add(indir + "TTbar_Madgraph_MATCHING_DOWN_el.root");
      //ch_ttbar_matchingup . Add(indir + "TTbar_Madgraph_MATCHING_UP_el.root");
      //ch_ttbar_scaledown . Add(indir + "TTbar_Madgraph_SCALE_DOWN_el.root");
      //ch_ttbar_scaleup . Add(indir + "TTbar_Madgraph_SCALE_UP_el.root");
    }
  
    TCut the_cut;
    TCut cut_data;
 
    for (int i=0; i<2; i++) {      

      std::cout<< channel << " " << i <<std::endl;
 
      ifdata = false;

      if (channel == "el"){
	if (i==0) {
	  the_cut = trainsampleGE1tags_el;
	  cut_data = yieldsDataGE1tags_el;
	  outfile = "TrainingSamples/TrainingTrees_GE1BTag_el.root";
	}      
	if (i==1){
	  the_cut = yieldsampleGE1tags_el;
	  cut_data = yieldsDataGE1tags_el;
	  ifdata = true;
	  outfile = "YieldSamples/YieldsTrees_GE1BTag_el.root";
	}
      }

      if (channel == "mu") {
	if (i==0) {
	  the_cut = trainsampleGE1tags_mu;
	  cut_data = yieldsDataGE1tags_mu;
	  outfile = "TrainingSamples/TrainingTrees_GE1BTag_mu.root";
	}      
	if (i==1){
	  the_cut = yieldsampleGE1tags_mu;
	  cut_data = yieldsDataGE1tags_mu;
	  ifdata = true;
	  outfile = "YieldSamples/YieldsTrees_GE1BTag_mu.root";
	}
      }

      std::cout << "ifdata? " << ifdata << std::endl;
      std::cout << "the_cut " << the_cut.GetTitle() << std::endl;
      std::cout << "cut_data " << cut_data.GetTitle() << std::endl;

      if (channel == "el"){
	if (ifdata){
	  ch_data . Add(indir + "Data_el_13JulAB06AugA24AugC.root");
	  ch_data . SetBranchStatus("*",1);
	  TTree * t_data = ch_data . CopyTree(cut_data);
	  _data = t_data->CopyTree("","");      
	  _data->SetName("data");
	}
      }

      if (channel == "mu"){
	if (ifdata){
	  ch_data . Add(indir + "Data_mu_13JulAB24AugC.root");
	  ch_data . SetBranchStatus("*",1);
	  TTree * t_data = ch_data . CopyTree(cut_data);
	  _data = t_data->CopyTree("","");
	  _data->SetName("data");
	}
      }
    
      std::cout << " set branches ======== " << std::endl;
      ch_ttbar . SetBranchStatus("*",1); 
      TTree * t_ttbar = ch_ttbar . CopyTree(the_cut);
      _ttbar = t_ttbar->CopyTree("","");
      _ttbar->SetName("ttbar");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_ttbar_JES_UP . SetBranchStatus("*",1);
	TTree * t_ttbar_JES_UP = ch_ttbar_JES_UP . CopyTree(the_cut);
        _ttbar_JES_UP = t_ttbar_JES_UP->CopyTree("","");
	_ttbar_JES_UP->SetName("ttbar_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_ttbar_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_ttbar_JES_DOWN = ch_ttbar_JES_DOWN . CopyTree(the_cut);
	_ttbar_JES_DOWN = t_ttbar_JES_DOWN->CopyTree("","");
	_ttbar_JES_DOWN->SetName("ttbar_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_ttbar_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_ttbar_BTAG_UP = ch_ttbar_BTAG_UP . CopyTree(the_cut);
	_ttbar_BTAG_UP = t_ttbar_BTAG_UP->CopyTree("","");
	_ttbar_BTAG_UP->SetName("ttbar_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_ttbar_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_ttbar_BTAG_DOWN = ch_ttbar_BTAG_DOWN . CopyTree(the_cut);
	_ttbar_BTAG_DOWN = t_ttbar_BTAG_DOWN->CopyTree("","");
	_ttbar_BTAG_DOWN->SetName("ttbar_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_ttbar_JER_UP . SetBranchStatus("*",1);
	TTree * t_ttbar_JER_UP = ch_ttbar_JER_UP . CopyTree(the_cut);
	_ttbar_JER_UP = t_ttbar_JER_UP->CopyTree("","");
	_ttbar_JER_UP->SetName("ttbar_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_ttbar_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_ttbar_JER_DOWN = ch_ttbar_JER_DOWN . CopyTree(the_cut);
	_ttbar_JER_DOWN = t_ttbar_JER_DOWN->CopyTree("","");
	_ttbar_JER_DOWN->SetName("ttbar_JER_DOWN"); 
      }

      ch_wjets . SetBranchStatus("*",1); 
      TTree * t_wjets = ch_wjets . CopyTree(the_cut);
      _wjets = t_wjets->CopyTree("","");
      _wjets->SetName("wjets");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_wjets_JES_UP . SetBranchStatus("*",1);
	TTree * t_wjets_JES_UP = ch_wjets_JES_UP . CopyTree(the_cut);
	_wjets_JES_UP = t_wjets_JES_UP->CopyTree("","");
	_wjets_JES_UP->SetName("wjets_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_wjets_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_wjets_JES_DOWN = ch_wjets_JES_DOWN . CopyTree(the_cut);
	_wjets_JES_DOWN = t_wjets_JES_DOWN->CopyTree("","");
	_wjets_JES_DOWN->SetName("wjets_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_wjets_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_wjets_BTAG_UP = ch_wjets_BTAG_UP . CopyTree(the_cut);
	_wjets_BTAG_UP = t_wjets_BTAG_UP->CopyTree("","");
	_wjets_BTAG_UP->SetName("wjets_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_wjets_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_wjets_BTAG_DOWN = ch_wjets_BTAG_DOWN . CopyTree(the_cut);
	_wjets_BTAG_DOWN = t_wjets_BTAG_DOWN->CopyTree("","");
	_wjets_BTAG_DOWN->SetName("wjets_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_wjets_JER_UP . SetBranchStatus("*",1);
	TTree * t_wjets_JER_UP = ch_wjets_JER_UP . CopyTree(the_cut);
	_wjets_JER_UP = t_wjets_JER_UP->CopyTree("","");
	_wjets_JER_UP->SetName("wjets_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_wjets_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_wjets_JER_DOWN = ch_wjets_JER_DOWN . CopyTree(the_cut);
	_wjets_JER_DOWN = t_wjets_JER_DOWN->CopyTree("","");
	_wjets_JER_DOWN->SetName("wjets_JER_DOWN"); 

      }

      ch_s . SetBranchStatus("*",1); 
      TTree * t_s = ch_s . CopyTree(the_cut);
      _s = t_s->CopyTree("","");
      _s->SetName("s");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_s_JES_UP . SetBranchStatus("*",1);
	TTree * t_s_JES_UP = ch_s_JES_UP . CopyTree(the_cut);
	_s_JES_UP = t_s_JES_UP->CopyTree("","");
	_s_JES_UP->SetName("s_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_s_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_s_JES_DOWN = ch_s_JES_DOWN . CopyTree(the_cut);
	_s_JES_DOWN = t_s_JES_DOWN->CopyTree("","");
	_s_JES_DOWN->SetName("s_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_s_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_s_BTAG_UP = ch_s_BTAG_UP . CopyTree(the_cut);
	_s_BTAG_UP = t_s_BTAG_UP->CopyTree("","");
	_s_BTAG_UP->SetName("s_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_s_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_s_BTAG_DOWN = ch_s_BTAG_DOWN . CopyTree(the_cut);
	_s_BTAG_DOWN = t_s_BTAG_DOWN->CopyTree("","");
	_s_BTAG_DOWN->SetName("s_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_s_JER_UP . SetBranchStatus("*",1);
	TTree * t_s_JER_UP = ch_s_JER_UP . CopyTree(the_cut);
	_s_JER_UP = t_s_JER_UP->CopyTree("","");
	_s_JER_UP->SetName("s_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_s_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_s_JER_DOWN = ch_s_JER_DOWN . CopyTree(the_cut);
	_s_JER_DOWN = t_s_JER_DOWN->CopyTree("","");
	_s_JER_DOWN->SetName("s_JER_DOWN"); 

      }

      ch_bs . SetBranchStatus("*",1); 
      TTree * t_bs = ch_bs . CopyTree(the_cut);
      _bs = t_bs->CopyTree("","");
      _bs->SetName("bs");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_bs_JES_UP . SetBranchStatus("*",1);
	TTree * t_bs_JES_UP = ch_bs_JES_UP . CopyTree(the_cut);
	_bs_JES_UP = t_bs_JES_UP->CopyTree("","");
	_bs_JES_UP->SetName("bs_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_bs_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_bs_JES_DOWN = ch_bs_JES_DOWN . CopyTree(the_cut);
	_bs_JES_DOWN = t_bs_JES_DOWN->CopyTree("","");
	_bs_JES_DOWN->SetName("bs_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_bs_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_bs_BTAG_UP = ch_bs_BTAG_UP . CopyTree(the_cut);
	_bs_BTAG_UP = t_bs_BTAG_UP->CopyTree("","");
	_bs_BTAG_UP->SetName("bs_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_bs_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_bs_BTAG_DOWN = ch_bs_BTAG_DOWN . CopyTree(the_cut);
	_bs_BTAG_DOWN = t_bs_BTAG_DOWN->CopyTree("","");
	_bs_BTAG_DOWN->SetName("bs_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_bs_JER_UP . SetBranchStatus("*",1);
	TTree * t_bs_JER_UP = ch_bs_JER_UP . CopyTree(the_cut);
	_bs_JER_UP = t_bs_JER_UP->CopyTree("","");
	_bs_JER_UP->SetName("bs_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_bs_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_bs_JER_DOWN = ch_bs_JER_DOWN . CopyTree(the_cut);
	_bs_JER_DOWN = t_bs_JER_DOWN->CopyTree("","");
	_bs_JER_DOWN->SetName("bs_JER_DOWN"); 

      }

      ch_t . SetBranchStatus("*",1); 
      TTree * t_t = ch_t . CopyTree(the_cut);
      _t = t_t->CopyTree("","");
      _t->SetName("t");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_t_JES_UP . SetBranchStatus("*",1);
	TTree * t_t_JES_UP = ch_t_JES_UP . CopyTree(the_cut);
	_t_JES_UP = t_t_JES_UP->CopyTree("","");
	_t_JES_UP->SetName("t_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_t_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_t_JES_DOWN = ch_t_JES_DOWN . CopyTree(the_cut);
	_t_JES_DOWN = t_t_JES_DOWN->CopyTree("","");
	_t_JES_DOWN->SetName("t_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_t_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_t_BTAG_UP = ch_t_BTAG_UP . CopyTree(the_cut);
	_t_BTAG_UP = t_t_BTAG_UP->CopyTree("","");
	_t_BTAG_UP->SetName("t_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_t_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_t_BTAG_DOWN = ch_t_BTAG_DOWN . CopyTree(the_cut);
	_t_BTAG_DOWN = t_t_BTAG_DOWN->CopyTree("","");
	_t_BTAG_DOWN->SetName("t_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_t_JER_UP . SetBranchStatus("*",1);
	TTree * t_t_JER_UP = ch_t_JER_UP . CopyTree(the_cut);
	_t_JER_UP = t_t_JER_UP->CopyTree("","");
	_t_JER_UP->SetName("t_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_t_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_t_JER_DOWN = ch_t_JER_DOWN . CopyTree(the_cut);
	_t_JER_DOWN = t_t_JER_DOWN->CopyTree("","");
	_t_JER_DOWN->SetName("t_JER_DOWN"); 

      }
 
      ch_bt . SetBranchStatus("*",1); 
      TTree * t_bt = ch_bt . CopyTree(the_cut);
      _bt = t_bt->CopyTree("","");
      _bt->SetName("bt");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_bt_JES_UP . SetBranchStatus("*",1);
	TTree * t_bt_JES_UP = ch_bt_JES_UP . CopyTree(the_cut);
	_bt_JES_UP = t_bt_JES_UP->CopyTree("","");
	_bt_JES_UP->SetName("bt_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_bt_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_bt_JES_DOWN = ch_bt_JES_DOWN . CopyTree(the_cut);
	_bt_JES_DOWN = t_bt_JES_DOWN->CopyTree("","");
	_bt_JES_DOWN->SetName("bt_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_bt_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_bt_BTAG_UP = ch_bt_BTAG_UP . CopyTree(the_cut);
	_bt_BTAG_UP = t_bt_BTAG_UP->CopyTree("","");
	_bt_BTAG_UP->SetName("bt_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_bt_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_bt_BTAG_DOWN = ch_bt_BTAG_DOWN . CopyTree(the_cut);
	_bt_BTAG_DOWN = t_bt_BTAG_DOWN->CopyTree("","");
	_bt_BTAG_DOWN->SetName("bt_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_bt_JER_UP . SetBranchStatus("*",1);
	TTree * t_bt_JER_UP = ch_bt_JER_UP . CopyTree(the_cut);
	_bt_JER_UP = t_bt_JER_UP->CopyTree("","");
	_bt_JER_UP->SetName("bt_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_bt_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_bt_JER_DOWN = ch_bt_JER_DOWN . CopyTree(the_cut);
	_bt_JER_DOWN = t_bt_JER_DOWN->CopyTree("","");
	_bt_JER_DOWN->SetName("bt_JER_DOWN"); 

      }

      ch_tw . SetBranchStatus("*",1); 
      TTree * t_tw = ch_tw . CopyTree(the_cut);
      _tw = t_tw->CopyTree("","");
      _tw->SetName("tw");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_tw_JES_UP . SetBranchStatus("*",1);
	TTree * t_tw_JES_UP = ch_tw_JES_UP . CopyTree(the_cut);
	_tw_JES_UP = t_tw_JES_UP->CopyTree("","");
	_tw_JES_UP->SetName("tw_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_tw_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_tw_JES_DOWN = ch_tw_JES_DOWN . CopyTree(the_cut);
	_tw_JES_DOWN = t_tw_JES_DOWN->CopyTree("","");
	_tw_JES_DOWN->SetName("tw_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_tw_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_tw_BTAG_UP = ch_tw_BTAG_UP . CopyTree(the_cut);
	_tw_BTAG_UP = t_tw_BTAG_UP->CopyTree("","");
	_tw_BTAG_UP->SetName("tw_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_tw_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_tw_BTAG_DOWN = ch_tw_BTAG_DOWN . CopyTree(the_cut);
	_tw_BTAG_DOWN = t_tw_BTAG_DOWN->CopyTree("","");
	_tw_BTAG_DOWN->SetName("tw_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_tw_JER_UP . SetBranchStatus("*",1);
	TTree * t_tw_JER_UP = ch_tw_JER_UP . CopyTree(the_cut);
	_tw_JER_UP = t_tw_JER_UP->CopyTree("","");
	_tw_JER_UP->SetName("tw_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_tw_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_tw_JER_DOWN = ch_tw_JER_DOWN . CopyTree(the_cut);
	_tw_JER_DOWN = t_tw_JER_DOWN->CopyTree("","");
	_tw_JER_DOWN->SetName("tw_JER_DOWN"); 

      }

      ch_btw . SetBranchStatus("*",1); 
      TTree * t_btw = ch_btw . CopyTree(the_cut);
      _btw = t_btw->CopyTree("","");
      _btw->SetName("btw");

      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_btw_JES_UP . SetBranchStatus("*",1);
	TTree * t_btw_JES_UP = ch_btw_JES_UP . CopyTree(the_cut);
	_btw_JES_UP = t_btw_JES_UP->CopyTree("","");
	_btw_JES_UP->SetName("btw_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_btw_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_btw_JES_DOWN = ch_btw_JES_DOWN . CopyTree(the_cut);
	_btw_JES_DOWN = t_btw_JES_DOWN->CopyTree("","");
	_btw_JES_DOWN->SetName("btw_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_btw_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_btw_BTAG_UP = ch_btw_BTAG_UP . CopyTree(the_cut);
	_btw_BTAG_UP = t_btw_BTAG_UP->CopyTree("","");
	_btw_BTAG_UP->SetName("btw_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_btw_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_btw_BTAG_DOWN = ch_btw_BTAG_DOWN . CopyTree(the_cut);
	_btw_BTAG_DOWN = t_btw_BTAG_DOWN->CopyTree("","");
	_btw_BTAG_DOWN->SetName("btw_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_btw_JER_UP . SetBranchStatus("*",1);
	TTree * t_btw_JER_UP = ch_btw_JER_UP . CopyTree(the_cut);
	_btw_JER_UP = t_btw_JER_UP->CopyTree("","");
	_btw_JER_UP->SetName("btw_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_btw_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_btw_JER_DOWN = ch_btw_JER_DOWN . CopyTree(the_cut);
	_btw_JER_DOWN = t_btw_JER_DOWN->CopyTree("","");
	_btw_JER_DOWN->SetName("btw_JER_DOWN"); 

      }

      ch_zjets . SetBranchStatus("*",1); 
      TTree * t_zjets = ch_zjets . CopyTree(the_cut);
      _zjets = t_zjets->CopyTree("","");
      _zjets->SetName("zjets");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_zjets_JES_UP . SetBranchStatus("*",1);
	TTree * t_zjets_JES_UP = ch_zjets_JES_UP . CopyTree(the_cut);
	_zjets_JES_UP = t_zjets_JES_UP->CopyTree("","");
	_zjets_JES_UP->SetName("zjets_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_zjets_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_zjets_JES_DOWN = ch_zjets_JES_DOWN . CopyTree(the_cut);
	_zjets_JES_DOWN = t_zjets_JES_DOWN->CopyTree("","");
	_zjets_JES_DOWN->SetName("zjets_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_zjets_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_zjets_BTAG_UP = ch_zjets_BTAG_UP . CopyTree(the_cut);
	_zjets_BTAG_UP = t_zjets_BTAG_UP->CopyTree("","");
	_zjets_BTAG_UP->SetName("zjets_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_zjets_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_zjets_BTAG_DOWN = ch_zjets_BTAG_DOWN . CopyTree(the_cut);
	_zjets_BTAG_DOWN = t_zjets_BTAG_DOWN->CopyTree("","");
	_zjets_BTAG_DOWN->SetName("zjets_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_zjets_JER_UP . SetBranchStatus("*",1);
	TTree * t_zjets_JER_UP = ch_zjets_JER_UP . CopyTree(the_cut);
	_zjets_JER_UP = t_zjets_JER_UP->CopyTree("","");
	_zjets_JER_UP->SetName("zjets_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_zjets_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_zjets_JER_DOWN = ch_zjets_JER_DOWN . CopyTree(the_cut);
	_zjets_JER_DOWN = t_zjets_JER_DOWN->CopyTree("","");
	_zjets_JER_DOWN->SetName("zjets_JER_DOWN"); 

      }

      ch_ww . SetBranchStatus("*",1); 
      TTree * t_ww = ch_ww . CopyTree(the_cut);
      _ww = t_ww->CopyTree("","");
      _ww->SetName("ww");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_ww_JES_UP . SetBranchStatus("*",1);
	TTree * t_ww_JES_UP = ch_ww_JES_UP . CopyTree(the_cut);
	_ww_JES_UP = t_ww_JES_UP->CopyTree("","");
	_ww_JES_UP->SetName("ww_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_ww_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_ww_JES_DOWN = ch_ww_JES_DOWN . CopyTree(the_cut);
	_ww_JES_DOWN = t_ww_JES_DOWN->CopyTree("","");
	_ww_JES_DOWN->SetName("ww_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_ww_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_ww_BTAG_UP = ch_ww_BTAG_UP . CopyTree(the_cut);
	_ww_BTAG_UP = t_ww_BTAG_UP->CopyTree("","");
	_ww_BTAG_UP->SetName("ww_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_ww_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_ww_BTAG_DOWN = ch_ww_BTAG_DOWN . CopyTree(the_cut);
	_ww_BTAG_DOWN = t_ww_BTAG_DOWN->CopyTree("","");
	_ww_BTAG_DOWN->SetName("ww_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_ww_JER_UP . SetBranchStatus("*",1);
	TTree * t_ww_JER_UP = ch_ww_JER_UP . CopyTree(the_cut);
	_ww_JER_UP = t_ww_JER_UP->CopyTree("","");
	_ww_JER_UP->SetName("ww_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_ww_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_ww_JER_DOWN = ch_ww_JER_DOWN . CopyTree(the_cut);
	_ww_JER_DOWN = t_ww_JER_DOWN->CopyTree("","");
	_ww_JER_DOWN->SetName("ww_JER_DOWN"); 

      }

      if (ifsys) {
	ch_ttbar_matchingup . SetBranchStatus("*",1);
	TTree * t_ttbar_matchingup = ch_ttbar_matchingup . CopyTree(the_cut);
	_ttbar_matchingup = t_ttbar_matchingup->CopyTree("","");
	_ttbar_matchingup->SetName("ttbar_matchingup"); 

	ch_ttbar_matchingdown . SetBranchStatus("*",1);
	TTree * t_ttbar_matchingdown = ch_ttbar_matchingdown . CopyTree(the_cut);
	_ttbar_matchingdown = t_ttbar_matchingdown->CopyTree("","");
	_ttbar_matchingdown->SetName("ttbar_matchingdown"); 

	ch_ttbar_scaleup . SetBranchStatus("*",1);
	TTree * t_ttbar_scaleup = ch_ttbar_scaleup . CopyTree(the_cut);
	_ttbar_scaleup = t_ttbar_scaleup->CopyTree("","");
	_ttbar_scaleup->SetName("ttbar_scaleup"); 

	ch_ttbar_scaledown . SetBranchStatus("*",1);
	TTree * t_ttbar_scaledown = ch_ttbar_scaledown . CopyTree(the_cut);
	_ttbar_scaledown = t_ttbar_scaledown->CopyTree("","");
	_ttbar_scaledown->SetName("ttbar_scaledown"); 

      }


      /// SIGNAL ///
      std::cout << " set signal branches ======== " << std::endl;
      ch_wp1700R . SetBranchStatus("*",1); 
      TTree * t_wp1700R = ch_wp1700R . CopyTree(the_cut);
      _wp1700R = t_wp1700R->CopyTree("","");
      _wp1700R->SetName("wp1700R");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_wp1700R_JES_UP . SetBranchStatus("*",1);
	TTree * t_wp1700R_JES_UP = ch_wp1700R_JES_UP . CopyTree(the_cut);
	_wp1700R_JES_UP = t_wp1700R_JES_UP->CopyTree("","");
	_wp1700R_JES_UP->SetName("wp1700R_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_wp1700R_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_wp1700R_JES_DOWN = ch_wp1700R_JES_DOWN . CopyTree(the_cut);
	_wp1700R_JES_DOWN = t_wp1700R_JES_DOWN->CopyTree("","");
	_wp1700R_JES_DOWN->SetName("wp1700R_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_wp1700R_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_wp1700R_BTAG_UP = ch_wp1700R_BTAG_UP . CopyTree(the_cut);
	_wp1700R_BTAG_UP = t_wp1700R_BTAG_UP->CopyTree("","");
	_wp1700R_BTAG_UP->SetName("wp1700R_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_wp1700R_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_wp1700R_BTAG_DOWN = ch_wp1700R_BTAG_DOWN . CopyTree(the_cut);
	_wp1700R_BTAG_DOWN = t_wp1700R_BTAG_DOWN->CopyTree("","");
	_wp1700R_BTAG_DOWN->SetName("wp1700R_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_wp1700R_JER_UP . SetBranchStatus("*",1);
	TTree * t_wp1700R_JER_UP = ch_wp1700R_JER_UP . CopyTree(the_cut);
	_wp1700R_JER_UP = t_wp1700R_JER_UP->CopyTree("","");
	_wp1700R_JER_UP->SetName("wp1700R_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_wp1700R_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_wp1700R_JER_DOWN = ch_wp1700R_JER_DOWN . CopyTree(the_cut);
	_wp1700R_JER_DOWN = t_wp1700R_JER_DOWN->CopyTree("","");
	_wp1700R_JER_DOWN->SetName("wp1700R_JER_DOWN"); 

      }

      ch_wp1900R . SetBranchStatus("*",1); 
      TTree * t_wp1900R = ch_wp1900R . CopyTree(the_cut);
      _wp1900R = t_wp1900R->CopyTree("","");
      _wp1900R->SetName("wp1900R");

      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_wp1900R_JES_UP . SetBranchStatus("*",1);
	TTree * t_wp1900R_JES_UP = ch_wp1900R_JES_UP . CopyTree(the_cut);
	_wp1900R_JES_UP = t_wp1900R_JES_UP->CopyTree("","");
	_wp1900R_JES_UP->SetName("wp1900R_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_wp1900R_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_wp1900R_JES_DOWN = ch_wp1900R_JES_DOWN . CopyTree(the_cut);
	_wp1900R_JES_DOWN = t_wp1900R_JES_DOWN->CopyTree("","");
	_wp1900R_JES_DOWN->SetName("wp1900R_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_wp1900R_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_wp1900R_BTAG_UP = ch_wp1900R_BTAG_UP . CopyTree(the_cut);
	_wp1900R_BTAG_UP = t_wp1900R_BTAG_UP->CopyTree("","");
	_wp1900R_BTAG_UP->SetName("wp1900R_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_wp1900R_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_wp1900R_BTAG_DOWN = ch_wp1900R_BTAG_DOWN . CopyTree(the_cut);
	_wp1900R_BTAG_DOWN = t_wp1900R_BTAG_DOWN->CopyTree("","");
	_wp1900R_BTAG_DOWN->SetName("wp1900R_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_wp1900R_JER_UP . SetBranchStatus("*",1);
	TTree * t_wp1900R_JER_UP = ch_wp1900R_JER_UP . CopyTree(the_cut);
	_wp1900R_JER_UP = t_wp1900R_JER_UP->CopyTree("","");
	_wp1900R_JER_UP->SetName("wp1900R_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_wp1900R_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_wp1900R_JER_DOWN = ch_wp1900R_JER_DOWN . CopyTree(the_cut);
	_wp1900R_JER_DOWN = t_wp1900R_JER_DOWN->CopyTree("","");
	_wp1900R_JER_DOWN->SetName("wp1900R_JER_DOWN"); 

      }

      ch_wp2100R . SetBranchStatus("*",1); 
      TTree * t_wp2100R = ch_wp2100R . CopyTree(the_cut);
      _wp2100R = t_wp2100R->CopyTree("","");
      _wp2100R->SetName("wp2100R");
      if (ifsys) {
	std::cout << " set systematics _JES_UP ======== " << std::endl;
	ch_wp2100R_JES_UP . SetBranchStatus("*",1);
	TTree * t_wp2100R_JES_UP = ch_wp2100R_JES_UP . CopyTree(the_cut);
	_wp2100R_JES_UP = t_wp2100R_JES_UP->CopyTree("","");
	_wp2100R_JES_UP->SetName("wp2100R_JES_UP"); 

	std::cout << " set systematics _JES_DOWN ======== " << std::endl;
	ch_wp2100R_JES_DOWN . SetBranchStatus("*",1);
	TTree * t_wp2100R_JES_DOWN = ch_wp2100R_JES_DOWN . CopyTree(the_cut);
	_wp2100R_JES_DOWN = t_wp2100R_JES_DOWN->CopyTree("","");
	_wp2100R_JES_DOWN->SetName("wp2100R_JES_DOWN"); 

	std::cout << " set systematics _BTAG_UP ======== " << std::endl;
	ch_wp2100R_BTAG_UP . SetBranchStatus("*",1);
	TTree * t_wp2100R_BTAG_UP = ch_wp2100R_BTAG_UP . CopyTree(the_cut);
	_wp2100R_BTAG_UP = t_wp2100R_BTAG_UP->CopyTree("","");
	_wp2100R_BTAG_UP->SetName("wp2100R_BTAG_UP"); 

	std::cout << " set systematics _BTAG_DOWN ======== " << std::endl;
	ch_wp2100R_BTAG_DOWN . SetBranchStatus("*",1);
	TTree * t_wp2100R_BTAG_DOWN = ch_wp2100R_BTAG_DOWN . CopyTree(the_cut);
	_wp2100R_BTAG_DOWN = t_wp2100R_BTAG_DOWN->CopyTree("","");
	_wp2100R_BTAG_DOWN->SetName("wp2100R_BTAG_DOWN"); 

	std::cout << " set systematics _JER_UP ======== " << std::endl;
	ch_wp2100R_JER_UP . SetBranchStatus("*",1);
	TTree * t_wp2100R_JER_UP = ch_wp2100R_JER_UP . CopyTree(the_cut);
	_wp2100R_JER_UP = t_wp2100R_JER_UP->CopyTree("","");
	_wp2100R_JER_UP->SetName("wp2100R_JER_UP"); 

	std::cout << " set systematics _JER_DOWN ======== " << std::endl;
	ch_wp2100R_JER_DOWN . SetBranchStatus("*",1);
	TTree * t_wp2100R_JER_DOWN = ch_wp2100R_JER_DOWN . CopyTree(the_cut);
	_wp2100R_JER_DOWN = t_wp2100R_JER_DOWN->CopyTree("","");
	_wp2100R_JER_DOWN->SetName("wp2100R_JER_DOWN"); 

      }

   
      TFile * out_file = new TFile(outfile, "RECREATE");
      out_file->cd();
      std::cout << "  writing " << outfile << std::endl;
      std::cout<< "ifdata? " << ifdata << std::endl;
      if (ifdata)  { 
	_data->Write();
	std::cout << " wrote data ======== " << std::endl;
      }
      _ttbar->Write();
      std::cout << " wrote ttbar ======== " << std::endl;
      if (ifsys) {
	_ttbar_JES_UP->Write();
	_ttbar_JES_DOWN->Write();
	_ttbar_BTAG_UP->Write();
	_ttbar_BTAG_DOWN->Write();
	_ttbar_JER_UP->Write();
	_ttbar_JER_DOWN->Write();
      }
      _wjets->Write();
      std::cout << " wrote wjets ======== " << std::endl;
      if (ifsys) {
	_wjets_JES_UP->Write();
	_wjets_JES_DOWN->Write();
	_wjets_BTAG_UP->Write();
	_wjets_BTAG_DOWN->Write();
	_wjets_JER_UP->Write();
	_wjets_JER_DOWN->Write();
      }
      _s->Write();
      std::cout << " wrote s ======== " << std::endl;
      if (ifsys) {
	_s_JES_UP->Write();
	_s_JES_DOWN->Write();
	_s_BTAG_UP->Write();
	_s_BTAG_DOWN->Write();
	_s_JER_UP->Write();
	_s_JER_DOWN->Write();
      }
      _bs->Write();
      std::cout << " wrote bs ======== " << std::endl;
      if (ifsys) {
	_bs_JES_UP->Write();
	_bs_JES_DOWN->Write();
	_bs_BTAG_UP->Write();
	_bs_BTAG_DOWN->Write();
	_bs_JER_UP->Write();
	_bs_JER_DOWN->Write();
      }
      _t->Write();
      std::cout << " wrote t ======== " << std::endl;
      if (ifsys) {
	_t_JES_UP->Write();
	_t_JES_DOWN->Write();
	_t_BTAG_UP->Write();
	_t_BTAG_DOWN->Write();
	_t_JER_UP->Write();
	_t_JER_DOWN->Write();
      }
      _bt->Write();
      std::cout << " wrote bt ======== " << std::endl;
      if (ifsys) {
	_bt_JES_UP->Write();
	_bt_JES_DOWN->Write();
	_bt_BTAG_UP->Write();
	_bt_BTAG_DOWN->Write();
	_bt_JER_UP->Write();
	_bt_JER_DOWN->Write();
      }
      _tw->Write();
      std::cout << " wrote tw ======== " << std::endl;
      if (ifsys) {
	_tw_JES_UP->Write();
	_tw_JES_DOWN->Write();
	_tw_BTAG_UP->Write();
	_tw_BTAG_DOWN->Write();
	_tw_JER_UP->Write();
	_tw_JER_DOWN->Write();
      }
      _btw->Write();
      std::cout << " wrote btw ======== " << std::endl;
      if (ifsys) {
	_btw_JES_UP->Write();
	_btw_JES_DOWN->Write();
	_btw_BTAG_UP->Write();
	_btw_BTAG_DOWN->Write();
	_btw_JER_UP->Write();
	_btw_JER_DOWN->Write();
      }
      _zjets->Write();
      std::cout << " wrote zjets ======== " << std::endl;
      if (ifsys) {
	_zjets_JES_UP->Write();
	_zjets_JES_DOWN->Write();
	_zjets_BTAG_UP->Write();
	_zjets_BTAG_DOWN->Write();
	_zjets_JER_UP->Write();
	_zjets_JER_DOWN->Write();
      }
      _ww->Write();
      std::cout << " wrote ww ======== " << std::endl;
      if (ifsys) {
	_ww_JES_UP->Write();
	_ww_JES_DOWN->Write();
	_ww_BTAG_UP->Write();
	_ww_BTAG_DOWN->Write();
	_ww_JER_UP->Write();
	_ww_JER_DOWN->Write();
      }
      _wp1700R->Write();
      std::cout << " wrote wp1700R ======== " << std::endl;
      if (ifsys) {
	_wp1700R_JES_UP->Write();
	_wp1700R_JES_DOWN->Write();
	_wp1700R_BTAG_UP->Write();
	_wp1700R_BTAG_DOWN->Write();
	_wp1700R_JER_UP->Write();
	_wp1700R_JER_DOWN->Write();
      }
      _wp1900R->Write();
      std::cout << " wrote wp1900R ======== " << std::endl;
      if (ifsys) {
	_wp1900R_JES_UP->Write();
	_wp1900R_JES_DOWN->Write();
	_wp1900R_BTAG_UP->Write();
	_wp1900R_BTAG_DOWN->Write();
	_wp1900R_JER_UP->Write();
	_wp1900R_JER_DOWN->Write();
      }
      _wp2100R->Write();
      std::cout << " wrote wp2100R ======== " << std::endl;
      if (ifsys) {
	_wp2100R_JES_UP->Write();
	_wp2100R_JES_DOWN->Write();
	_wp2100R_BTAG_UP->Write();
	_wp2100R_BTAG_DOWN->Write();
	_wp2100R_JER_UP->Write();
	_wp2100R_JER_DOWN->Write();
      }
      if (ifsys) {
	_ttbar_matchingup->Write();
	_ttbar_matchingdown->Write();
	_ttbar_scaleup->Write();
	_ttbar_scaledown->Write();
      }
      out_file->Write();
      std::cout << " wrote out file  "<< outfile << std::endl ;
      out_file->Close();
      delete out_file;
    }
    std::cout << " done ... " << std::endl;
 
  }// train and yield 
}
