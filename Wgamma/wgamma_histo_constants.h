#ifndef _mumet_histo_constants_h__
#define _mumet_histo_constants_h__

#include <string>

  // ++++++++++++++++++++++++++++++++Useful constants

  const int Num_trkAlgos = 7; // global, tracker, tpfms, cocktail, picky, tmr, dyt
  const std::string algo_desc_short[Num_trkAlgos] = {"gbl","trk","tpfms","ckt","pic","def","dyt"};
  // use this for histogram descriptions
  const std::string algo_desc_long[Num_trkAlgos] = {"global", "tracker", "TPFMS","cocktail","picky","default", "DYT"};

  const int Num_mumet_cuts = 5; // one new set of histograms after each cut
  // use this for histogram names
  const std::string mumet_cuts_desc_short[Num_mumet_cuts] = {"hlt","qual","1mu","iso", "met"};
  const std::string mumet_cuts_desc_long[Num_mumet_cuts] = {"Single-muon HLT", "Quality", "1 muon only","Isolation", "MET kinematic cuts"};
 
  const int Num_photon_cuts = 5; // one new set of histograms after each cut
  // use this for histogram names
  const std::string photon_cuts_desc_short[Num_photon_cuts] = {"pt","isolation","hovere", "etawidth","trackveto"};
 
  // use this for histogram descriptions
  const std::string photon_cuts_desc_long[Num_photon_cuts]= {"Photon above Threshold", "Photon Isolation", "Hadronic/EM", "Eta Width", "Track Veto"};

  // +++++++++++++++++++++++++++++++muon-pt histogram parameters
  const unsigned  nBinPtMu = 140;//45; // 400; // 45; // 18; 200; 380; 
  const float minPtMu = 0;
  const float  maxPtMu = 800; // 800; 2000;
  // +++++++++++++++++++++++++++++++muon-eta histogram parameters
  const unsigned nBinEtaMu = 28;
  const float minEtaMu = -2.4;
  const float maxEtaMu = 2.4;
  // +++++++++++++++++++++++++++++++muon-phi histogram parameters 
  const unsigned nBinPhiMu = 18;
  const float minPhiMu = -3.6;
  const float maxPhiMu = 3.6;
  // +++++++++++++++++++++++++++++++muon-jet delphi histogram parameters
  const unsigned nBinDPhiMu = 35;
  const float minDPhiMu = 0;
  const float maxDPhiMu = 3.5;
  // +++++++++++++++++++++++++++++++muon  iso histogram parameters
  const unsigned nBinIsoMu = 25;
  const float minIsoMu = 0;
  const float maxIsoMu = 0.5;
  // +++++++++++++++++++++++++++++++tmass histogram parameters
  const unsigned nBinWTmMu = 680;
  const float minWTmMu = 0;
  const float maxWTmMu = 1700;

  // +++++++++++++++++++++++++++++++++photon pt histogram parameters
  const unsigned nBinPhoPt = 140;
  const float minPhotonPt = 0;
  const float maxPhotonPt = 800;

  // +++++++++++++++++++++++++++++++++photon eta histogram parameters
  const unsigned nBinPhoEta = 28;
  const float minPhotonEta = -2.4;
  const float maxPhotonEta = 2.4;

  // +++++++++++++++++++++++++++++++++photon phi histogram parameters
  const unsigned nBinPhoPhi = 18;
  const float minPhotonPhi = -3.6;
  const float maxPhotonPhi = 3.6;

  // +++++++++++++++++++++++++++++++++photon phi histogram parameters
  const unsigned nBinMWgamma = 680;
  const float minMWgamma = 0;
  const float maxMWgamma = 1700;

 

#endif // #ifndef _mumet_histo_constants_h__
