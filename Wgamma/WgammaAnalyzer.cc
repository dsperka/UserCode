#include "UserCode/CMGWPrimeGroup/interface/WgammaAnalyzer.h"
#include "DataFormats/PatCandidates/interface/PFParticle.h"
//#include "ElectroWeakAnalysis/MultiBosons/interface/VGammaPhotonSelector.h"
//#include "UserCode/CMGWPrimeGroup/interface/MuMETAnalyzer.h"

#include <TH1F.h>
#include <TLorentzVector.h>
#include "FWCore/Framework/interface/ESHandle.h"
#include "DataFormats/Common/interface/View.h"

#include "UserCode/CMGWPrimeGroup/interface/AnglesUtil.h"

typedef math::XYZTLorentzVector LorentzVector;

using std::string; using std::cout; using std::endl;

WgammaAnalyzer::WgammaAnalyzer(const edm::ParameterSet& cfg,WPrimeUtil * wprimeUtil)
{
  wprimeUtil_ = wprimeUtil;
  assert(wprimeUtil_);

  muons_       = cfg.getParameter<edm::InputTag>("muons"  );
  met_       = cfg.getParameter<edm::InputTag>("mets"  );
  metLabel_ = cfg.getParameter<edm::InputTag>("patMET" );
  particleFlow_ = cfg.getParameter<edm::InputTag>("particleFlow" );
  photons_ = cfg.getParameter<edm::InputTag>("photons" );
  muReconstructor_   = cfg.getParameter<int>("muonReconstructor");
  muonPtThreshold_   = cfg.getParameter<double>("muonPtThreshold");
  chi2Cut_           = cfg.getParameter<double>("chi2Cut");
  muonEtaCut_        = cfg.getParameter<double>("muonEtaCut");
  oneMuPtTrackCut_   = cfg.getParameter<double>("oneMuPtTrackCut");
  combRelCut_        = cfg.getParameter<double>("combRelCut");
  highestPtMuonOnly_ = cfg.getParameter<bool>("highestPtMuonOnly");
  dumpHighPtMuons_   = cfg.getParameter<bool>("dumpHighPtMuons");
  dumpHighPtMuonThreshold_ = cfg.getParameter<double>("dumpHighPtMuonThreshold");
  highestPtPhotonOnly_ = cfg.getParameter<bool>("highestPtPhotonOnly");
  dumpHighPtPhotons_   = cfg.getParameter<bool>("dumpHighPtPhotons");
  dumpHighPtPhotonThreshold_ = cfg.getParameter<double>("dumpHighPtPhotonThreshold");
  barJurECALIsoConst_  = cfg.getParameter<double>("BarrelJurrasicECALIsoConst");
  barJurECALIsoSlope_  = cfg.getParameter<double>("BarrelJurrasicECALIsoSlope");
  barTowHCALIsoConst_  = cfg.getParameter<double>("BarrelTowerHCALIsoConst");	
  barTowHCALIsoSlope_  = cfg.getParameter<double>("BarrelTowerHCALIsoSlope");	
  barMaxHOverE_        = cfg.getParameter<double>("BarrelMaxHadronicOverEm");
  barHConeTrkIsoConst_ = cfg.getParameter<double>("BarrelHollowConeTrkIsoConst");
  barHConeTrkIsoSlope_ = cfg.getParameter<double>("BarrelHollowConeTrkIsoSlope");
  barMaxEtaWidth_   = cfg.getParameter<double>("BarrelMaxSigmaIetaIeta");
  endJurECALIsoConst_  = cfg.getParameter<double>("EndcapJurrasicECALIsoConst");
  endJurECALIsoSlope_  = cfg.getParameter<double>("EndcapJurrasicECALIsoSlope");
  endTowHCALIsoConst_  = cfg.getParameter<double>("EndcapTowerHCALIsoConst");
  endTowHCALIsoSlope_  = cfg.getParameter<double>("EndcapTowerHCALIsoSlope");	
  endMaxHOverE_        = cfg.getParameter<double>("EndcapMaxHadronicOverEm");
  endHConeTrkIsoConst_ = cfg.getParameter<double>("EndcapHollowConeTrkIsoConst");
  endHConeTrkIsoSlope_ = cfg.getParameter<double>("EndcapHollowConeTrkIsoSlope");
  endMaxEtaWidth_   = cfg.getParameter<double>("EndcapMaxSigmaIetaIeta");
  applyTrackVeto_ = cfg.getParameter<bool>("ApplyTrackVeto");
  minPhotonPt_         = cfg.getParameter<double>("minPt");
  maxPhotonEta_        = cfg.getParameter<double>("maxEta");


  assert( muReconstructor_ >= 0 );
  assert( muReconstructor_ < Num_trkAlgos);

  setupCutOrderMuons();
  setupCutOrderPhotons();

}

WgammaAnalyzer::~WgammaAnalyzer()
{
}

void WgammaAnalyzer::defineHistos(TFileDirectory & dir)
{
  for(int i = 0; i != Num_mumet_cuts; ++i)
      hPT[i] = hETA[i] = hPHI[i] = hMUMETDPHI[i] = hWTM[i] = 0;
 
  for(int j = 0; j != Num_photon_cuts; ++j)
      hPHOPT[j] = hPHOETA[j] = hPHOPHI[j] = hMWG[j] = 0;      

  defineHistos_MuonPt(dir);
  defineHistos_MuonEta(dir);
  defineHistos_MuonPhi(dir);
  defineHistos_MuonIso(dir);
  defineHistos_MuonMETDPhi(dir);
  defineHistos_WTMass(dir);
  defineHistos_PhotonPt(dir);
  defineHistos_PhotonEta(dir);
  defineHistos_PhotonPhi(dir);
  defineHistos_MWgamma(dir);


}

// Get the hardest muon (based on tracker-pt) in event
// (returns index in pat::MuonCollection)
int WgammaAnalyzer::getTheHardestMuon()
{
  int nmuons = muons->size();
  float temp_muPT = -999;
  int ret = -1;
  for(int j = 0; j != nmuons; ++j)
    {
      float current_muPT = (*muons)[j].innerTrack()->pt();
      if (current_muPT > temp_muPT) 
	{
	  temp_muPT = current_muPT;
	  ret = j;
	}
    }
  return ret;
}

void WgammaAnalyzer::eventLoop(edm::EventBase const & event)
{
  event.getByLabel(muons_, muons);
  event.getByLabel(met_, met);
  //event.getByLabel(photons_, photons);

  edm::Handle< edm::View<pat::MET> > metHandle;
  event.getByLabel (metLabel_, metHandle);
  edm::View<pat::MET> PatMETs = *metHandle;

  pat::MET patMET;
  patMET = PatMETs[0];
  recMet = MetStruct (&patMET);

  edm::Handle< edm::View<pat::Photon> >  photonHandle;
  event.getByLabel(photons_, photonHandle);
  edm::View<pat::Photon> photons = *photonHandle;



  // switch to help us keep track of whether a muon has already
  // been found in current event surviving the ith-cut;
  // this will ensure that we increase Num_surv_cut maximum once per evet
  // whereas we nevertheless fill the histograms 
  // for every muon surviving the i-th cut
  bool accountMe[Num_mumet_cuts];
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    accountMe[cut] = true;

  int iMuMin = 0; int iMuMax = muons->size();
  if(highestPtMuonOnly_ == 1) // if true, will only consider highest-pt muon in event
    {
      int iMu = getTheHardestMuon();
      if(iMu >=0) // there is at least one muon in the event
          {
              iMuMin = iMu;
              iMuMax = iMu + 1;
          }
    }

  int iPhotonMin = 0; int iPhotonMax = photons.size();
  if(highestPtPhotonOnly_) // if true, will only consider highest-pt muon in event
    {
        int iPho=-1.0;
        int nphotons = photons.size();
        float temp_phoPT = -999;
 
        for(int j = 0; j != nphotons; ++j)
        {
            pat::Photon currentPhoton = photons.at(j);
            float current_phoPT = currentPhoton.pt();
            if (current_phoPT > temp_phoPT) 
            {
                temp_phoPT = current_phoPT;
                iPho = j;
            }
        }

        if(iPho >=0) // there is at least one muon in the event
        {
            iPhotonMin = iPho;
            iPhotonMax = iPho + 1;
        }
    }



  //loop over muons
  for (int theMu = iMuMin; theMu != iMuMax; ++theMu){

      bool fill_entry = true; // if true, will histogram muon
      
      isInvalidMuon_ = false;
      pfMETwithoutMuCalculated_ = false;
      
      setMuonMomentum(theMu);
      if (isInvalidMuon_) continue;

      for(int cut_index = 0; cut_index != Num_mumet_cuts; ++cut_index) { // loop over selection cuts
          
          // call to function [as implemented in setupCutOder]
          string arg = mumet_cuts_desc_short[cut_index];
          pat::Photon dummyPhoton = photons.at(iPhotonMin);
          bool survived_cut = (this->*cuts[arg])(&fill_entry, theMu, event,dummyPhoton);
          if (!survived_cut) break; // skip rest of selection cuts
	
          if(fill_entry) {

              tabulateMu(cut_index, accountMe, event, theMu);
	
              if(dumpHighPtMuons_ && fill_entry 
                 && cut_index == Num_mumet_cuts-1
                 && wprimeUtil_->getSampleName()=="data" 
                 && (*muons)[theMu].innerTrack()->pt() > dumpHighPtMuonThreshold_ ) printHighPtMuon(event);
              
              // Start looking at photons if the muon passed all the cuts
              if (cut_index == Num_photon_cuts-1) {
                  //loop over photons
                  for (int thePhoton = iPhotonMin; thePhoton != iPhotonMax; ++thePhoton){
                      
                      pat::Photon currentPhoton = photons.at(thePhoton);
      
                      LorentzVector PhotonP4 = currentPhoton.p4();

                      for(int pho_cut_index = 0; pho_cut_index != Num_photon_cuts; ++pho_cut_index) {

                          // call to function [as implemented in setupCutOder]
                          string arg = photon_cuts_desc_short[cut_index];
                          bool survived_cut = (this->*cuts[arg])(&fill_entry, thePhoton, event, currentPhoton);
                          if (!survived_cut) break; // skip rest of selection cuts
                          double invMass = -999.999;
                          if (fill_entry) {
                              LorentzVector neutrinoP4 = calculateNeutrinoP4((*muons)[theMu].p4(), patMET.p4() );
                              if (neutrinoP4.E() > 0) {
                                  LorentzVector wP4   =  (*muons)[theMu].p4() + neutrinoP4;
                                  LorentzVector totalP4 = wP4+PhotonP4;
                                  invMass = totalP4.M();
                              }
                              tabulatePho(pho_cut_index, accountMe, event, currentPhoton, invMass);
	
                          }
                          if(dumpHighPtPhotons_ && fill_entry 
                             && cut_index == Num_photon_cuts-1
                             && wprimeUtil_->getSampleName()=="data" 
                             && currentPhoton.pt() > dumpHighPtPhotonThreshold_ ) printHighPtPhoton(event,&currentPhoton);
                  
                         
                      } // loop over photon cuts
                  } // loop over photons
              } // muon passing final cut
          } // muon still good
      } // loop over muon cuts
  } // loop over muons
}// events

void WgammaAnalyzer::setMuLorentzVector(TLorentzVector& P, const reco::TrackRef & trk)
{
  if(trk.isNull())
    {
      isInvalidMuon_ = true;
      return;
    }
  TVector3 p3(trk->px(), trk->py(), trk->pz());
  P.SetVectM(p3, wprime::MUON_MASS);
}

// set muon 4-d momentum according to muonReconstructor_ value (sets mu4D)
void WgammaAnalyzer::setMuonMomentum(int theMu)
{
  switch(muReconstructor_)
    {
    case 0:
      setMuLorentzVector(mu4D, (*muons)[theMu].globalTrack());
      break;
    case 1:
      setMuLorentzVector(mu4D, (*muons)[theMu].innerTrack());
      break;
    case 2:
      setMuLorentzVector(mu4D, (*muons)[theMu].tpfmsMuon());
      break;
    case 3:
      setMuLorentzVector(mu4D, (*muons)[theMu].cocktailMuon());
      break;
    case 4:
      setMuLorentzVector(mu4D, (*muons)[theMu].pickyMuon());
      break;
    case 5:
      setMuLorentzVector(mu4D, (*muons)[theMu].defaultTeVMuon());
      break;
    case 6:
      setMuLorentzVector(mu4D, (*muons)[theMu].dytMuon());
      break;
    }

}

LorentzVector
WgammaAnalyzer::calculateNeutrinoP4(LorentzVector mu4D, LorentzVector metP4) 
{

  double dPhi         = kinem::delta_phi (mu4D.phi(), metP4.phi());
  double wMass        = 80.398;
  double g            = wMass * wMass / 2. + 
                        mu4D.Pt() * metP4.Pt() * cos (dPhi);
  double a            = - pow (mu4D.Pt(), 2);
  double b            = 2 * g * mu4D.Pz();
  double c            = pow (g,2) - pow (mu4D.P(),2) * pow (metP4.Pt(),2);

  double discriminant = (b * b) - (4 * a * c);
  double neutrinoPz   = 0;

  if (discriminant < 0) return LorentzVector (0., 0., 0., -999.);

  TVector3 leptonP3(mu4D.px(), mu4D.py(), mu4D.pz());

  double   pz1     = -b/(2*a) + sqrt (discriminant)/(2*a);
  TVector3 p1      (metP4.px(), metP4.py(), pz1);
  double   deltaR1 = p1.DeltaR (leptonP3);

  double   pz2     = -b/(2*a) + sqrt (discriminant)/(2*a);
  TVector3 p2      (metP4.px(), metP4.py(), pz2);
  double   deltaR2 = p2.DeltaR (leptonP3);
  
  // Choose the smaller opening angle between the lepton and neutrino
  neutrinoPz = (deltaR1 < deltaR2 ) ? pz1 : pz2;
  
  double E = sqrt (pow (metP4.px(),2) + pow (metP4.py(),2) + pow (neutrinoPz,2));
  LorentzVector neutrinoP4(metP4.px(), metP4.py(), neutrinoPz, E);
  
  return neutrinoP4;
  
}




// fill histograms for muon if fill_entry=true; update book-keeping 
// (via private member: stats); make sure stats gets updated maximum once per event
void WgammaAnalyzer::tabulateMu(int cut_index, bool accountMe[], 
                                edm::EventBase const& event, int theMu)
{
  // if the accountMe switch is on, increase the number of events passing the cuts
  // and turn the switch off so we don't count more than once per event
  if(accountMe[cut_index])
    {
      wprime::SampleStat::iterator it;
      it = stats.find(wprimeUtil_->getSampleName());
      if(it == stats.end())abort();
      ++((it->second)[cut_index].Nsurv_evt_cut);
      accountMe[cut_index] = false;
    }
  float weight = wprimeUtil_->getWeight();
  // fill the histograms
  hPT[cut_index]->Fill(mu4D.Pt(), weight);
  hETA[cut_index]->Fill(mu4D.Eta(), weight);
  hPHI[cut_index]->Fill(mu4D.Phi(), weight);
  //  hMJDPHI[cut_index]->Fill( XJetDPhi(mu4D, event), weight);
  hWTM[cut_index]->Fill(WPrimeUtil::TMass(mu4D, getNewMET(event, mu4D)), weight);
  hISO[cut_index]->Fill(combRelIsolation(theMu),weight);

}

void WgammaAnalyzer::tabulatePho(int pho_cut_index, bool accountMe[], 
                                 edm::EventBase const& event, pat::Photon & currentPhoton, double & InvMass)
{
  // if the accountMe switch is on, increase the number of events passing the cuts
  // and turn the switch off so we don't count more than once per event
  if(accountMe[pho_cut_index])
    {
      wprime::SampleStat::iterator it;
      it = stats.find(wprimeUtil_->getSampleName());
      if(it == stats.end())abort();
      ++((it->second)[pho_cut_index].Nsurv_evt_cut);
      accountMe[pho_cut_index] = false;
    }
  float weight = wprimeUtil_->getWeight();
  // fill the histograms
  hPHOPT[pho_cut_index]->Fill(currentPhoton.pt(),weight);
  hPHOETA[pho_cut_index]->Fill(currentPhoton.superCluster()->eta());
  hPHOPHI[pho_cut_index]->Fill(currentPhoton.phi());
  hMWG[pho_cut_index]->Fill(InvMass, weight);
}



// operations to be done when changing input file (e.g. create new histograms)
void WgammaAnalyzer::beginFile(std::vector<wprime::InputFile>::const_iterator fi)
{
  wprime::FilterEff tmp; 
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    stats[fi->samplename].push_back(tmp);

  // add channel/analysis name here?
  TFileDirectory dir= wprimeUtil_->getFileService()->mkdir(fi->samplename); 
  defineHistos(dir); // one set of histograms per input file

}

// operations to be done when closing input file 
// (e.g. print summary)
void WgammaAnalyzer::endFile(std::vector<wprime::InputFile>::const_iterator fi,
			    ofstream & out)
{
  printFileSummary(fi, out);
}

// print summary of efficiencies
void WgammaAnalyzer::printFileSummary(std::vector<wprime::InputFile>::const_iterator fi, ofstream & out)
{
  string sample = fi->samplename;
  float weight = fi->weight;
  wprime::SampleStat::iterator it;
  it = stats.find(sample);
  if(it == stats.end())abort();  

  float eff, deff;
  out << "\n Sample: " << sample << endl;
  out << " Total # of produced events for " << wprimeUtil_->getLumi_ipb() 
       << " ipb = " << fi->Nprod_evt*weight << endl;
  out << " Total # of events after pre-selection for " 
       << wprimeUtil_->getLumi_ipb() << " ipb = " << fi->Nact_evt*weight 
       << endl;

  WPrimeUtil::getEff(eff, deff, fi->Nact_evt, fi->Nprod_evt);
  out << " Preselection efficiency = " << eff << " +- " << deff << endl;

  for(int cut_index = 0; cut_index != Num_mumet_cuts; ++cut_index){
    
    (it->second)[cut_index].Nsurv_evt_cut_w = 
      (it->second)[cut_index].Nsurv_evt_cut*weight;
    
    out << " Cut # " << cut_index << ": " << mumet_cuts_desc_long[cut_index] 
	 <<", expected # of evts = " 
	 << (it->second)[cut_index].Nsurv_evt_cut_w;
    
    //calculate efficiencies
    if(cut_index == 0)
      WPrimeUtil::getEff(eff, deff, (it->second)[cut_index].Nsurv_evt_cut,
	     fi->Nact_evt);
    else
      WPrimeUtil::getEff(eff, deff, (it->second)[cut_index].Nsurv_evt_cut,
	     (it->second)[cut_index-1].Nsurv_evt_cut);
    out << ", Relative eff = "<<eff << " +- " << deff;
    WPrimeUtil::getEff(eff, deff, (it->second)[cut_index].Nsurv_evt_cut, 
	   fi->Nprod_evt);
    out << ", Absolute eff = "<< eff << " +- " << deff
	 << endl;
    
    (it->second)[cut_index].eff = eff;
    (it->second)[cut_index].deff = deff;
    
  } // loop over different cuts
	
}

// e.g. print summmary of expected events for all samples
void WgammaAnalyzer::endAnalysis(ofstream & out)
{
  float N_SM = 0; 
  std::map<std::string, std::vector<wprime::FilterEff> >::const_iterator it;

  int index = Num_mumet_cuts-1; // get # of events after last cut

  out << endl;
  for(it = stats.begin(); it != stats.end(); ++it)
    { // loop over samples
      string sample = it->first;
      float N_evt = (it->second)[index].Nsurv_evt_cut_w;
      out<< " "<< sample << ": " << N_evt
	 << " evts (eff = " << 100.*(it->second)[index].eff
	 << " +- " << 100.*(it->second)[index].deff
	 << " %) " << endl;
      
      if(sample == "W" || sample == "Wlowpt" || sample == "QCD" 
	 || sample == "Z" || sample == "Top")
	N_SM += N_evt;
      
    } // loop over samples

  out << " Total # of SM (W + QCD + Z + Top) events: " 
      << N_SM << endl;
  
}

WgammaAnalyzer::MetStruct::MetStruct (pat::MET* p) : ParticleStruct() {
  isValid   = true;
  et        = p->et();
  pt        = p->pt();
  phi       = p->phi();
}


void WgammaAnalyzer::defineHistos_MuonPt(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    {
      string name = "hPT" + algo_desc_short[muReconstructor_] + "_" + 
	mumet_cuts_desc_short[cut];
      string title = algo_desc_long[muReconstructor_]+ " muon p_{T} with " + 
	mumet_cuts_desc_long[cut];
      
      hPT[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinPtMu,
			    minPtMu, maxPtMu);
    }
}

void WgammaAnalyzer::defineHistos_MuonEta(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    {
      string name = "hETA" + algo_desc_short[muReconstructor_] + "_" 
	+ mumet_cuts_desc_short[cut];
      string title = algo_desc_long[muReconstructor_] + " muon #eta with " 
	+ mumet_cuts_desc_long[cut];
      hETA[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinEtaMu,
			   minEtaMu,maxEtaMu);
    }

}

void WgammaAnalyzer::defineHistos_MuonPhi(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    {
      string name = "hPHI" + algo_desc_short[muReconstructor_] + "_" + 
	mumet_cuts_desc_short[cut];
      string title = algo_desc_long[muReconstructor_] + " muon #phi with " + 
	mumet_cuts_desc_long[cut];
      hPHI[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinPhiMu,
				 minPhiMu,maxPhiMu);
    }

}

void WgammaAnalyzer::defineHistos_MuonMETDPhi(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    {
      string name = "hMUMETDPHI" + algo_desc_short[muReconstructor_] + "_" + 
	mumet_cuts_desc_short[cut];
      string title = algo_desc_long[muReconstructor_] + " muon-#slash{E_{T}} #Delta#phi " + 
	mumet_cuts_desc_long[cut];
      hMUMETDPHI[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), 
			      nBinDPhiMu,minDPhiMu,maxDPhiMu);
    }

}

void WgammaAnalyzer::defineHistos_MuonIso(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    {
      string name = "hISO" + algo_desc_short[muReconstructor_] + "_" + 
	mumet_cuts_desc_short[cut];
      string title = algo_desc_long[muReconstructor_] + " muon isol with " + 
	mumet_cuts_desc_long[cut];
      hISO[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinIsoMu,
			   minIsoMu,maxIsoMu);
    }

}

void WgammaAnalyzer::defineHistos_WTMass(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_mumet_cuts; ++cut)
    {
      string name = "hWTM" + algo_desc_short[muReconstructor_] + "_" 
	+ mumet_cuts_desc_short[cut];
      string title = algo_desc_long[muReconstructor_]+ " W Transv. Mass with " 
	+ mumet_cuts_desc_long[cut];
      hWTM[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinWTmMu,
			  minWTmMu,maxWTmMu);
    } 
}

void WgammaAnalyzer::defineHistos_PhotonPt(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_photon_cuts; ++cut)
    {
      string name = "hPHOPT" + photon_cuts_desc_short[cut];
      string title =" Photon P_{T} With "+ photon_cuts_desc_long[cut];
      hPHOPT[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinPhoPt,
			  minPhotonPt,maxPhotonPt);
    } 
}

void WgammaAnalyzer::defineHistos_PhotonEta(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_photon_cuts; ++cut)
    {
      string name = "hPHOETA" + photon_cuts_desc_short[cut];
      string title =" Photon #eta With "+ photon_cuts_desc_long[cut];
      hPHOETA[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinPhoEta,
			  minPhotonEta,maxPhotonEta);
    } 
}

void WgammaAnalyzer::defineHistos_PhotonPhi(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_photon_cuts; ++cut)
    {
      string name = "hPHOPHI" + photon_cuts_desc_short[cut];
      string title =" Photon #phi With "+ photon_cuts_desc_long[cut];
      hPHOPHI[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinPhoPhi,
			  minPhotonPhi,maxPhotonPhi);
    } 
}

void WgammaAnalyzer::defineHistos_MWgamma(TFileDirectory & dir)
{
  for(int cut = 0; cut != Num_photon_cuts; ++cut)
    {
      string name = "hMWG" + photon_cuts_desc_short[cut];
      string title =" M_{W #gamma} "+ photon_cuts_desc_long[cut];
      hMWG[cut] = dir.make<TH1F>(name.c_str(), title.c_str(), nBinMWgamma,
			  minMWgamma,maxMWgamma);
    } 
}


void WgammaAnalyzer::setupCutOrderMuons()
{
  cuts.clear();
#if debugme
  cout << "\n Mu+MET cuts will be applied in this order: " << endl;
#endif

  for(int cut_i = 0; cut_i != Num_mumet_cuts; ++cut_i)
    { // loop over selection cuts
      string arg = mumet_cuts_desc_short[cut_i];
#if debugme
      cout << " Cut #" << (cut_i+1) << ": " << mumet_cuts_desc_long[cut_i]
	   << " (" << arg << ") " << endl;
#endif
      if(arg == "hlt")cuts[arg] = &WgammaAnalyzer::passedHLT;
      else if(arg.find("thr") != string::npos)
	cuts[arg] = &WgammaAnalyzer::muonMinimumPt;
      else if(arg == "qual")cuts[arg] = &WgammaAnalyzer::goodQualityMuon;
      else if(arg == "1mu")cuts[arg] = &WgammaAnalyzer::onlyOneHighTrackPtMuon;
      else if(arg == "iso")cuts[arg] = &WgammaAnalyzer::isolatedMuon;
      else if(arg == "met")cuts[arg] = &WgammaAnalyzer::kinematicCuts;
      else
	{
	  cout << " Oops! Don't understand how to prepare for cut nicknamed as "
	       << arg << endl;
	  abort();
	}
    } // loop over selection cuts

#if debugme
  cout << endl;
#endif

}


void WgammaAnalyzer::setupCutOrderPhotons()
{
  cuts.clear();
#if debugme
  cout << "\n Photon cuts will be applied in this order: " << endl;
#endif

  for(int cut_i = 0; cut_i != Num_photon_cuts; ++cut_i)
    { // loop over selection cuts
      string arg = photon_cuts_desc_short[cut_i];
#if debugme
      cout << " Cut #" << (cut_i+1) << ": " << mumet_cuts_desc_long[cut_i]
	   << " (" << arg << ") " << endl;
#endif
      if(arg == "pt")cuts[arg] = &WgammaAnalyzer::photonPt;
      else if(arg == "isolation")cuts[arg] = &WgammaAnalyzer::photonIsolation;
      else if(arg == "hovere")cuts[arg] = &WgammaAnalyzer::photonHOverE;
      else if(arg == "etawidth")cuts[arg] = &WgammaAnalyzer::photonEtaWidth;
      else if(arg == "trackveto")cuts[arg] = &WgammaAnalyzer::photonTrackVeto;
      else
	{
	  cout << " Oops! Don't understand how to prepare for cut nicknamed as "
	       << arg << endl;
	  abort();
	}
    } // loop over selection cuts

#if debugme
  cout << endl;
#endif

}

// dump on screen info about high-pt muon
void WgammaAnalyzer::printHighPtMuon(edm::EventBase const & event)
{
  cout << " Run # = " << event.id().run() << " Event # = " 
       << event.id().event() << " LS = " << event.id().luminosityBlock() 
       << endl;

  cout << " Muon eta = " << mu4D.Eta() << "  phi = " << mu4D.Phi()
       << " pt = " << mu4D.Pt() << endl;
  pat::METCollection::const_iterator oldMET = met->begin();
  TVector2 oldMETv(oldMET->px(), oldMET->py());
  TVector2 newMET = getNewMET(event, mu4D);
  cout << " default pfMET = " << oldMET->pt();
  cout << " muTeV-adjusted pfMET = " << newMET.Mod() << endl;

  cout << " default TM = " << WPrimeUtil::TMass(mu4D, oldMETv);
  cout << " muTeV-adjusted TM = " << WPrimeUtil::TMass(mu4D, newMET) << endl;

#if 0
  cout << " P = " << 

  printMe("  pt = ", theMu);
  printMe(" dpt = ", theMu);
  cout << " # of layers: (strip, pixel) " << endl;
  printMe("layers", theMu);
  cout << " # of layers w/o measurement: (strip, pixel) " << endl;
  printMe("layersNoMeas", theMu);
  cout << " # of hits (strip, pixel, muon) " << endl;
  printMe("hits", theMu);
  cout << " Chi2/Ndof " << endl;
  printMe("chi2", theMu);
  cout << " Tracker eta =  " << theMu->tracker.p.Eta()
       << ", Tracker phi = " << theMu->tracker.p.Phi() << endl;
  cout << " # of standalone muon hits = " << theMu->Nmu_hits << endl;
  cout << " Global: " << theMu->AllGlobalMuons
       << " Tracker: " << theMu->AllTrackerMuons
       << " Standalone: " << theMu->AllStandAloneMuons
       << " Global prompt tight: " << theMu->GlobalMuonPromptTight << endl;
#endif
}

// dump on screen info about high-pt muon
void WgammaAnalyzer::printHighPtPhoton(edm::EventBase const & event, pat::Photon* currentPhoton)
{
  cout << " Run # = " << event.id().run() << " Event # = " 
       << event.id().event() << " LS = " << event.id().luminosityBlock() 
       << endl;

  cout << " Photon eta = " << currentPhoton->eta() << "  phi = " << currentPhoton->phi()
       << " pt = " << currentPhoton->pt() << endl;

 
}

// Get new MET: there are two corrections to be made:
// (a) the hadronic MET component (that needs to be corrected 
// if applyMETCorrection=true)from Z data; this will be done according to hadronic 
// activity from Z->mumu reconstructed events
// (b) the muon-pt component that needs to be updated if we switch to one
// of the dedicated high-pt muon reconstructors
TVector2 WgammaAnalyzer::getNewMET(edm::EventBase const & event, const TLorentzVector & mu_p)
{
  if(wprimeUtil_->shouldApplyMETCorrection())
    return wprimeUtil_->getHadronicMET(event) - TVector2(mu_p.Px(), mu_p.Py());

  return getPFMETwithoutMu(event) - TVector2(mu_p.Px(), mu_p.Py());
}

// get (PF) MET without the default-pt for the running muon in event (mu4D);
// this is done so that we can adjust the muon-pt component of the MET by 
// switching to one of the dedicated high-pt muon reconstructors
TVector2 WgammaAnalyzer::getPFMETwithoutMu(edm::EventBase const & event)
{
  if(pfMETwithoutMuCalculated_)
    return pfMETwithoutMuCached_;

  pat::METCollection::const_iterator oldMET = met->begin();
  float met_x = oldMET->px(); float met_y = oldMET->py();

  //----Loop over PFCandidates to get the hardest muon and put its
  //pT back to the MET TVector2; create a new object
  edm::Handle<pat::PFParticleCollection > PFCandidates;
  event.getByLabel(particleFlow_,PFCandidates);
  int nmuon = 0;
  pat::PFParticleCollection::const_iterator iParticle;
  pat::PFParticleCollection::const_iterator icorrespondingPFMu;
  for( iParticle = (PFCandidates.product())->begin() ; 
       iParticle != (PFCandidates.product())->end() ; ++iParticle ){
    
    const reco::Candidate* candidate = &(*iParticle);
    if (candidate) {
      const reco::PFCandidate* pfCandidate = 
	dynamic_cast<const reco::PFCandidate*> (candidate);
      if (pfCandidate){
	//check that it is a muon
	if (!(pfCandidate->particleId() == 3)) continue;
	double deta = mu4D.Eta() - pfCandidate->eta();
	double dphi = mu4D.Phi() - pfCandidate->phi();
	double dR = TMath::Sqrt(deta*deta + dphi*dphi);
	if(dR < 0.01)
	  {
	    icorrespondingPFMu = iParticle;
	    ++nmuon;
	    break;
	  }
         
      }//pfCandidate
    }//if candidate
  }//loop over PFCandidates
  
  //Add back the pT for the hardest muon if found.
  if (nmuon > 0){
    const reco::Candidate* mycandidate = &(*icorrespondingPFMu);
    const reco::PFCandidate* mypfCandidate = 
      dynamic_cast<const reco::PFCandidate*> (mycandidate);
    met_x += mypfCandidate->px();
    met_y += mypfCandidate->py();
  }//if nmuon >0
  pfMETwithoutMuCached_.Set(met_x,met_y);
  pfMETwithoutMuCalculated_ = true;
  return pfMETwithoutMuCached_;
}

//computes the combined rel isolation value
float WgammaAnalyzer::combRelIsolation(int theMu)
{
  // maybe we should divide by the pt of the high-pt muon reconstructor
  // and not always use the tracker-only pt measurement
  return ( (*muons)[theMu].ecalIso() + (*muons)[theMu].hcalIso() + 
	   (*muons)[theMu].trackIso() ) / mu4D.Pt();
}

// whether HLT accepted the event
bool WgammaAnalyzer::passedHLT(bool *, int, edm::EventBase const &, pat::Photon & pho)
{
  // needs implementation
  return true;
}

// check if muon has minimum pt, fill isThere accordingly
// always returns true
bool WgammaAnalyzer::muonMinimumPt(bool * isThere, int, edm::EventBase const &, pat::Photon & pho)
{
  if(mu4D.Pt() <= muonPtThreshold_)
    *isThere = false;

  return true;
}

// check if muon satisfies quality requirements
// fill goodQual; always returns true
bool WgammaAnalyzer::goodQualityMuon(bool * goodQual, int theMu, edm::EventBase const &, pat::Photon & pho)
{
  //See twiki: https://twiki.cern.ch/twiki/bin/view/CMS/ExoticaWprime
  //for the latest quality cuts

  bool muonID = (*muons)[theMu].isGood("AllGlobalMuons") &&
    (*muons)[theMu].isGood("AllTrackerMuons");

  reco::TrackRef glb = (*muons)[theMu].globalTrack();
  if(glb.isNull())
    {
      *goodQual = false;
      return true;
    }

  bool muon_hits = glb->hitPattern().numberOfValidTrackerHits() > 10
    && glb->hitPattern().numberOfValidMuonHits() > 0
    && glb->hitPattern().numberOfValidPixelHits() > 0;

  // NB: also need to implement reco::Muon::numberOfMatches() > 1
  // how do I do this?
  
  TVector3 p3(glb->px(), glb->py(), glb->pz());

  bool checkqual = (glb->chi2()/glb->ndof() / chi2Cut_)
    && TMath::Abs(p3.Eta()) < muonEtaCut_
    // is this d0 wrt to the beamspot???
    && TMath::Abs((*muons)[theMu].dB()) < 0.02;
   
  if(!muonID || !muon_hits || !checkqual)
    *goodQual = false;

   return true;
}

bool WgammaAnalyzer::photonPt(bool * goodQual, int theMu, edm::EventBase const &, pat::Photon & pho)
{
    //See twiki: https://twiki.cern.ch/twiki/bin/view/CMS/PhotonID

    double pt = pho.et();
    double eta = fabs(pho.superCluster()->eta());
    bool passPt = ( pt > minPhotonPt_ && eta < maxPhotonEta_   );

    if(!passPt)
        *goodQual = false;

   return true;
}

bool WgammaAnalyzer::photonIsolation(bool * goodQual,int theMu, edm::EventBase const &, pat::Photon & pho)
{
    //See twiki: https://twiki.cern.ch/twiki/bin/view/CMS/ExoticaPhotons

    //pat::Photon pho = photons.at(thePhoton);

    double pt = pho.et();
    double eta = fabs(pho.superCluster()->eta());
    double ecaliso = pho.ecalRecHitSumEtConeDR04();
    double hcaliso = pho.hcalTowerSumEtConeDR04();
    double trkiso = pho.trkSumPtHollowConeDR04();
    double hovere = pho.hadronicOverEm();
  
    double maxecaliso = 0.0;
    double maxhcaliso = 0.0;
    double maxtrkiso = 0.0;
    double maxhovere = 0.0;

    //should fill some histograms here

    if(eta < 1.442) {
        maxecaliso = barJurECALIsoConst_ + barJurECALIsoSlope_*pt;
        maxhcaliso = barTowHCALIsoConst_ + barTowHCALIsoSlope_*pt;
        maxtrkiso  = barHConeTrkIsoConst_ + barHConeTrkIsoSlope_*pt;
        maxhovere   = barMaxHOverE_;
    }
    if(eta > 1.650) {
        maxecaliso = endJurECALIsoConst_ + endJurECALIsoSlope_*pt;
        maxhcaliso = endTowHCALIsoConst_ + endTowHCALIsoSlope_*pt;
        maxtrkiso  = endHConeTrkIsoConst_ + endHConeTrkIsoSlope_*pt;
        maxhovere   = endMaxHOverE_;
    }

  bool passJurassicECALIso = ( ecaliso < maxecaliso );
  bool passTowerHCALIso = ( hcaliso < maxhcaliso );
  bool passHadronicOverEm = ( hovere < maxhovere   );
  bool passHollowConeTrkIso = ( trkiso < maxtrkiso   );

if(!passJurassicECALIso || !passTowerHCALIso || !passHadronicOverEm ||!passHollowConeTrkIso)
    *goodQual = false;

   return true;
}


bool WgammaAnalyzer::photonHOverE(bool * goodQual, int theMu, edm::EventBase const &, pat::Photon & pho)
{
    //See twiki: https://twiki.cern.ch/twiki/bin/view/CMS/PhotonID

    //pat::Photon pho = photons.at(thePhoton);

  
    double hovere = pho.hadronicOverEm();
    double eta = fabs(pho.superCluster()->eta());
    double maxhovere = 0.0;

    //should fill some histograms here

    if(eta < 1.442) {
     
        maxhovere   = barMaxHOverE_;
    }
    if(eta > 1.650) {
       
        maxhovere   = endMaxHOverE_;
    }
    bool passHadronicOverEm = ( hovere < maxhovere   );

    if(!passHadronicOverEm)
        *goodQual = false;

   return true;
}
    

  
bool WgammaAnalyzer::photonEtaWidth(bool * goodQual, int theMu , edm::EventBase const &, pat::Photon & pho)
{
    //See twiki: https://twiki.cern.ch/twiki/bin/view/CMS/PhotonID

    //pat::Photon pho = photons.at(thePhoton);

  
    double etawidth = pho.sigmaIetaIeta();
    double eta = fabs(pho.superCluster()->eta());
    double maxetawidth = 0.0;

    //should fill some histograms here
    if(eta < 1.442) {
     
        maxetawidth   = barMaxEtaWidth_;
    }
    if(eta > 1.650) {
       
        maxetawidth   = endMaxEtaWidth_;
    }

  bool passEtaWidth = ( etawidth < maxetawidth   );

    if(!passEtaWidth)
        *goodQual = false;

   return true;
}


bool WgammaAnalyzer::photonTrackVeto(bool * goodQual, int theMu , edm::EventBase const &, pat::Photon & pho)
{
    //See twiki: https://twiki.cern.ch/twiki/bin/view/CMS/PhotonID
    if (applyTrackVeto_ && pho.hasPixelSeed())
        *goodQual = false;
   return true;
}
    


// true if only one muon with track pt > the threshold
bool WgammaAnalyzer::onlyOneHighTrackPtMuon(bool *, int, edm::EventBase const &, pat::Photon & pho)
{
  return (nMuAboveThresh(oneMuPtTrackCut_) == 1);
}

// returns # of (global) muons with tracker-pt above <tracker_muon_pt>
unsigned WgammaAnalyzer::nMuAboveThresh(float tracker_muon_pt)
{
  unsigned N = 0;
  int iMuMin = 0; int iMuMax = muons->size();
  //loop over muons
  for (int theMu = iMuMin; theMu != iMuMax; ++theMu){//loop over muons
    // consider only global muons
    if(!(*muons)[theMu].isGood("AllGlobalMuons"))continue;
    
    reco::TrackRef trk = (*muons)[theMu].innerTrack();
    if(trk.isNull())continue;
    if(trk->pt() > tracker_muon_pt)
      ++N;
  }
 
  return N;
}

// set bool flag to true if muon isolated
// always returns true
bool WgammaAnalyzer::isolatedMuon(bool * goodQual, int theMu, 
                                  edm::EventBase const &, pat::Photon & pho)
{
  if(combRelIsolation(theMu) > combRelCut_)
    *goodQual = false;

  return true;
}

// check if muon, MET, and Photon pass kinematic cuts, updated goodQual
// always returns true
bool WgammaAnalyzer::kinematicCuts(bool * goodQual, int, 
                                   edm::EventBase const & event, pat::Photon & pho)
{
  TVector2 MET = getNewMET(event, mu4D);
  float ratio = mu4D.Pt()/MET.Mod();
  
  TVector2 muon_T(mu4D.Px(), mu4D.Py());
  float delta_phi = MET.DeltaPhi(muon_T);
  
  // calculate w trans mass
  // W transverse mass calculation from doi:10.1016/j.physletb.2003.10.071
  //double dPhi = kinem::delta_phi (mu4D.Phi(), patMET->phi());
  //double mt2  = 2 * patMET.et() * mu4D.Et() - 
  //      		  2 * patMET.pt() * mu4D.Pt() * cos (dPhi);
  //double WtransMass = sqrt (mt2);

  double WtransMass = WPrimeUtil::TMass(mu4D, getNewMET(event, mu4D));

   if (debugme) cout << "Found with transverse mass " << WtransMass << endl;

 

  if(ratio < 0.4 || ratio > 1.5 || TMath::Abs(delta_phi) < 2.5)
    *goodQual = false;

  return true;
}
