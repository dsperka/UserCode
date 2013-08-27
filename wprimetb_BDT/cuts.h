#include "TCut.h"

TCut jet_pt_cut = "jet_0_pt_WprimeCalc>120.0 && jet_1_pt_WprimeCalc>40.0";
TCut jet_eta_cut = "abs(jet_0_eta_WprimeCalc)<2.4 && abs(jet_1_eta_WprimeCalc)<2.4";

TCut electron_pt_cut = "elec_1_pt_WprimeCalc>50.0";
TCut electron_eta_cut = "abs(elec_1_eta_WprimeCalc)<2.5";
TCut muon_pt_cut = "muon_1_pt_WprimeCalc>50.0";
TCut muon_eta_cut = "abs(muon_1_eta_WprimeCalc)<2.1";

TCut met_cut = "corr_met_WprimeCalc > 20.0";

TCut deltar_cut = "Muon_DeltaR_LjetsTopoCalcNew > 0.3";

//-----------------cuts for BDT input--------------

TCut cut_mu =  jet_pt_cut && jet_eta_cut && met_cut && muon_pt_cut && muon_eta_cut && deltar_cut;
TCut cut_el =  jet_pt_cut && jet_eta_cut && met_cut && electron_pt_cut && electron_eta_cut && deltar_cut;

TCut wprime0btag = "(jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc)==0";
TCut wprime1btag = "(jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc)==1";
TCut wprime2btag = "(jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc)==2";
TCut wprimeGE1tags = "(jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc)>=1";
TCut wprimeGE2tags = "( (jet_0_tag_WprimeCalc==1 && (jet_1_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) || (jet_1_tag_WprimeCalc==1 && (jet_0_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) )";


TCut traineventbkg = "(event_CommonCalc % 10) == 0";
TCut testeventbkg = "(event_CommonCalc % 10) == 1";
TCut yieldeventbkg = !traineventbkg && !testeventbkg;
TCut yieldeventsig = "(event_CommonCalc % 2) == 0"; // to get a different training fraction for signal

// Electron Cuts //

// >=1 btags
TCut trainsampleBkgGE1tags_el = cut_el &&  wprimeGE1tags && !yieldeventbkg ;
TCut yieldsampleBkgGE1tags_el = cut_el &&  wprimeGE1tags && yieldeventbkg ;

TCut trainsampleSigGE1tags_el = cut_el &&  wprimeGE1tags && !yieldeventsig ;
TCut yieldsampleSigGE1tags_el = cut_el &&  wprimeGE1tags && yieldeventsig ;

TCut yieldsDataGE1tags_el = cut_el &&  wprimeGE1tags ;
TCut yieldsSysGE1tags_el = cut_el &&  wprimeGE1tags ;

// ==1 btags
TCut trainsampleBkg1tags_el = cut_el &&  wprime1btag && !yieldeventbkg ;
TCut yieldsampleBkg1tags_el = cut_el &&  wprime1btag && yieldeventbkg ;

TCut trainsampleSig1tags_el = cut_el &&  wprime1btag && !yieldeventsig ;
TCut yieldsampleSig1tags_el = cut_el &&  wprime1btag && yieldeventsig ;

TCut yieldsData1tags_el = cut_el &&  wprime1btag ;
TCut yieldsSys1tags_el = cut_el &&  wprime1btag  ;

// ==2 btags
TCut trainsampleBkg2tags_el = cut_el &&  wprime2btag && !yieldeventbkg ;
TCut yieldsampleBkg2tags_el = cut_el &&  wprime2btag && yieldeventbkg ;

TCut trainsampleSig2tags_el = cut_el &&  wprime2btag && !yieldeventsig ;
TCut yieldsampleSig2tags_el = cut_el &&  wprime2btag && yieldeventsig ;

TCut yieldsData2tags_el = cut_el &&  wprime2btag ;
TCut yieldsSys2tags_el = cut_el &&  wprime2btag ;


// Muon Cuts //

// >=1 btags
TCut trainsampleBkgGE1tags_mu = cut_mu &&  wprimeGE1tags && !yieldeventbkg ;
TCut yieldsampleBkgGE1tags_mu = cut_mu &&  wprimeGE1tags && yieldeventbkg ;

TCut trainsampleSigGE1tags_mu = cut_mu &&  wprimeGE1tags && !yieldeventsig ;
TCut yieldsampleSigGE1tags_mu = cut_mu &&  wprimeGE1tags && yieldeventsig ;

TCut yieldsDataGE1tags_mu = cut_mu &&  wprimeGE1tags ;
TCut yieldsSysGE1tags_mu = cut_mu &&  wprimeGE1tags ;

// ==1 btags
TCut trainsampleBkg1tags_mu = cut_mu &&  wprime1btag && !yieldeventbkg ;
TCut yieldsampleBkg1tags_mu = cut_mu &&  wprime1btag && yieldeventbkg ;

TCut trainsampleSig1tags_mu = cut_mu &&  wprime1btag && !yieldeventsig ;
TCut yieldsampleSig1tags_mu = cut_mu &&  wprime1btag && yieldeventsig ;

TCut yieldsData1tags_mu = cut_mu &&  wprime1btag ;
TCut yieldsSys1tags_mu = cut_mu &&  wprime1btag ;

// ==2 btags
TCut trainsampleBkg2tags_mu = cut_mu &&  wprime2btag && !yieldeventbkg ;
TCut yieldsampleBkg2tags_mu = cut_mu &&  wprime2btag && yieldeventbkg ;

TCut trainsampleSig2tags_mu = cut_mu &&  wprime2btag && !yieldeventsig ;
TCut yieldsampleSig2tags_mu = cut_mu &&  wprime2btag && yieldeventsig ;

TCut yieldsData2tags_mu = cut_mu &&  wprime2btag ;
TCut yieldsSys2tags_mu = cut_mu &&  wprime2btag ;

