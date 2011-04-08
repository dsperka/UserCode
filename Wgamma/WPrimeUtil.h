#ifndef _wprime_util_h_
#define _wprime_util_h_

#include "FWCore/PythonParameterSet/interface/PythonProcessDesc.h"
#include "PhysicsTools/FWLite/interface/TFileService.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/FWLite/interface/Event.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "UserCode/CMGWPrimeGroup/interface/util.h"

#include <TVector2.h>
#include <TLorentzVector.h>

#include <fstream>
#include <iostream>

class TFileService;
class TH1D;
class TH2D;


class WPrimeUtil
{
 public:
  WPrimeUtil(const char * out_filename, edm::InputTag genParticles);

  ~WPrimeUtil();

  fwlite::TFileService * getFileService(){return fs;}

  // get input files (to be retrieved from samples_cross_sections.txt)
  void getInputFiles(std::vector<wprime::InputFile> & inputFiles);

  void setApplyMETCorrection(bool flag){applyMETCorrection_ = flag;}
  void setHadronicMETCalculated(bool flag){hadronicMETcalculated_ = flag;}

  bool shouldApplyMETCorrection(){return applyMETCorrection_;}

  void setSampleName(std::string samplename){samplename_ = samplename;}
  void setWeight(float weight){weight_ = weight;}

  std::string getSampleName(){return samplename_;}
  float getWeight(){return weight_;}

  static void getEff(float & eff, float & deff,float Num,float Denom);


  // integrated luminosity in pb^-1
  float getLumi_ipb(){return lumi_ipb;}

  //transverse mass with a given MET object (TVector2)
  static float TMass(const TLorentzVector& lv, const TVector2& themet)
    {
      //------------------------------------------------------------------------
      float tmass = 0;
      float cdphi = TMath::Cos(lv.Phi()-themet.Phi());
      float tmass_sqr = 2*lv.Pt()*themet.Mod()*(1-cdphi);
      tmass = (tmass_sqr>0) ? sqrt(tmass_sqr) : 0;
    return tmass;
    }

  // get hadronic MET component (that needs to be corrected 
  // if applyMETCorrection=true)from Z data; this will be done according to hadronic 
  // activity from Z->mumu reconstructed events
  TVector2 getHadronicMET(edm::EventBase const & event);
  
 private:
  fwlite::TFileService * fs;
  // directory containing all input samples
  std::string top_level_dir; 

  void setupZMETcorrection();
  void setRecoilProjections();
  
  TH1D * hRecoilPerp;
  TH2D * hRecoilParalvsVBPt;
  TH1D ** histRecoilParal;

  // keep track of input file name and weight (e.g. for scaling MC histograms);
  // values set at beginFile
  std::string samplename_;
  float weight_;

  float lumi_ipb; // in pb^-1, to be retrieved from samples_cross_sections.txt

  // used for the parsing of samples_cross_sections.txt
  void parseLine(const std::string & new_line, wprime::InputFile * in_file);

  bool applyMETCorrection_; // wether to apply hadronic recoil correction (aimed for W)
  bool hadronicMETcalculated_; // want to calculate this max. once per event

  TVector2 hadronicMETcached;

  edm::InputTag genParticles_;
 // Handle to GenParticleCollectiom>
  edm::Handle<reco::GenParticleCollection> genParticles;


};

#endif //#define _wprime_util_h_
