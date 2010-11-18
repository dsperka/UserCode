// -*- C++ -*-
//
// Package:    WprimeMuValidation_v2
// Class:      WprimeMuValidation_v2
// 

// Fills histograms which are used to calculate Muon Trigger efficiencies ( L1 and HLT )

// Original Author:  David Sperka

// system include files
#include <memory>
#include <vector>

// user include files, not really sure whats needed
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoChargedCandidateFwd.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticle.h"
#include "DataFormats/L1Trigger/interface/L1MuonParticleFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/Particle.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"

#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "HLTriggerOffline/Muon/interface/L1MuonMatcherAlgo.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/MuonReco/interface/MuonCocktails.h"

#include "FWCore/Utilities/interface/RegexMatch.h"
#include <boost/foreach.hpp>

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"

#include "TMath.h"

//
// class declaration
//

class WprimeMuValidation_v2 : public edm::EDAnalyzer {
    HLTConfigProvider hltConfig;
    public:
    explicit WprimeMuValidation_v2(const edm::ParameterSet&);
    ~WprimeMuValidation_v2();
    private:
    virtual void beginJob() ;
    virtual void beginRun(edm::Run const &, edm::EventSetup const &);
    virtual void endRun(edm::Run const &, edm::EventSetup const &);
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;

    // ----------member data ---------------------------
    edm::InputTag HLTTag_;
    const std::vector<std::string> expressions;
    std::map<unsigned int, std::string> m_triggers;

    // All eta
    TH1 *reco_pt;
    // Pt > 25
    TH1 *reco_eta_25;  

    // All eta
    TH1 *l1mu7_pt;
    TH1 *hltmu9_pt; 
    TH1 *hltmu11_pt;  
    TH1 *hltmu13_pt;  
    TH1 *hltmu15_pt; 
    TH1 *hltmuFinalOR_pt; 
    TH1 *l1andhltmu9_pt; 
    TH1 *l1andhltmu11_pt;  
    TH1 *l1andhltmu13_pt;  
    TH1 *l1andhltmu15_pt; 
    TH1 *l1andhltmuFinalOR_pt; 

    // Pt > 25
    TH1 *l1mu7_eta_25; 
    TH1 *hltmu9_eta_25; 
    TH1 *hltmu11_eta_25; 
    TH1 *hltmu13_eta_25; 
    TH1 *hltmu15_eta_25; 
    TH1 *hltmuFinalOR_eta_25; 
    TH1 *l1andhltmu9_eta_25; 
    TH1 *l1andhltmu11_eta_25; 
    TH1 *l1andhltmu13_eta_25; 
    TH1 *l1andhltmu15_eta_25; 
    TH1 *l1andhltmuFinalOR_eta_25; 

    // Barrel
    TH1 *reco_pt_b; 
    TH1 *l1muopen_pt_b;  
    TH1 *l1mu7_pt_b;  
    TH1 *hltmu9_pt_b; 
    TH1 *hltmu11_pt_b; 
    TH1 *hltmu13_pt_b; 
    TH1 *hltmu15_pt_b; 
    TH1 *hltmuFinalOR_pt_b; 
    TH1 *l1andhltmu9_pt_b; 
    TH1 *l1andhltmu11_pt_b;  
    TH1 *l1andhltmu13_pt_b;  
    TH1 *l1andhltmu15_pt_b; 
    TH1 *l1andhltmuFinalOR_pt_b; 

    // Overlap
    TH1 *reco_pt_o; 
    TH1 *l1mu7_pt_o; 
    TH1 *hltmu9_pt_o; 
    TH1 *hltmu11_pt_o; 
    TH1 *hltmu13_pt_o; 
    TH1 *hltmu15_pt_o; 
    TH1 *hltmuFinalOR_pt_o; 
    TH1 *l1andhltmu9_pt_o; 
    TH1 *l1andhltmu11_pt_o;  
    TH1 *l1andhltmu13_pt_o;  
    TH1 *l1andhltmu15_pt_o; 
    TH1 *l1andhltmuFinalOR_pt_o; 

    // Endcap
    TH1 *reco_pt_e;
    TH1 *l1mu7_pt_e;  
    TH1 *hltmu9_pt_e; 
    TH1 *hltmu11_pt_e; 
    TH1 *hltmu13_pt_e; 
    TH1 *hltmu15_pt_e; 
    TH1 *hltmuFinalOR_pt_e; 
    TH1 *l1andhltmu9_pt_e; 
    TH1 *l1andhltmu11_pt_e;  
    TH1 *l1andhltmu13_pt_e;  
    TH1 *l1andhltmu15_pt_e; 
    TH1 *l1andhltmuFinalOR_pt_e; 

    bool firstEventInRun;
    void check_trigger(const edm::Event & iEvent);

    PropagateToMuon propagator_;
  
    std::string tevMuonLabel_;
  
    const reco::TrackToTrackMap * tevMap_default;
    const reco::TrackToTrackMap * tevMap_1stHit;
    const reco::TrackToTrackMap * tevMap_picky;
    const reco::TrackToTrackMap * tevMap_dyt;

};

WprimeMuValidation_v2::WprimeMuValidation_v2(const edm::ParameterSet& iConfig) :
    HLTTag_ ( iConfig.getParameter<edm::InputTag>("HLTriggerResults")),
    expressions(iConfig.getParameter<std::vector<std::string> >("triggerConditions")), 
    propagator_ (iConfig),
    tevMuonLabel_ (iConfig.getParameter<std::string> ("tevMuonLabel"))
{
    //now do what ever initialization is needed

    //Float_t etabins[] = {-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0.0,0.3,0.6,0.9,1.2,1.5,1.8};
    Float_t etabins[] = {-2.1,-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0.0,0.3,0.6,0.9,1.2,1.5,1.8,2.1};
    Float_t ptbins[] = {0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0,21.0,22.0,23.0,24.0,25.0,30.0,35.0,40.0,45.0,50.0,75.0,100.0,200.0,300.0};

    edm::Service<TFileService> fs;

    // All eta
    reco_pt = fs->make<TH1D>("reco_pt", "",34, ptbins);
    l1mu7_pt = fs->make<TH1D>("l1mu7_pt", "",34, ptbins);
    hltmu9_pt = fs->make<TH1D>("hltmu9_pt", "",34, ptbins);
    hltmu11_pt = fs->make<TH1D>("hltmu11_pt", "",34, ptbins);
    hltmu13_pt = fs->make<TH1D>("hltmu13_pt", "",34, ptbins);
    hltmu15_pt = fs->make<TH1D>("hltmu15_pt", "",34, ptbins);
    hltmuFinalOR_pt = fs->make<TH1D>("hltmuFinalOR_pt", "",34, ptbins);
    l1andhltmu9_pt = fs->make<TH1D>("l1andhltmu9_pt", "",34, ptbins);
    l1andhltmu11_pt = fs->make<TH1D>("l1andhltmu11_pt", "",34, ptbins);
    l1andhltmu13_pt = fs->make<TH1D>("l1andhltmu13_pt", "",34, ptbins);
    l1andhltmu15_pt = fs->make<TH1D>("l1andhltmu15_pt", "",34, ptbins);
    l1andhltmuFinalOR_pt = fs->make<TH1D>("l1andhltmuFinalOR_pt", "",34, ptbins);

    // Pt > 25 GeV
    reco_eta_25 = fs->make<TH1D>("reco_eta_25", "", 12, etabins);
    l1mu7_eta_25 = fs->make<TH1D>("l1mu7_eta_25", "", 12, etabins);
    hltmu9_eta_25 = fs->make<TH1D>("hltmu9_eta_25", "", 12, etabins);
    hltmu11_eta_25 = fs->make<TH1D>("hltmu11_eta_25", "", 12, etabins);
    hltmu13_eta_25 = fs->make<TH1D>("hltmu13_eta_25", "", 12, etabins);
    hltmu15_eta_25 = fs->make<TH1D>("hltmu15_eta_25", "", 12, etabins);
    hltmuFinalOR_eta_25 = fs->make<TH1D>("hltmuFinalOR_eta_25", "", 12, etabins);
    l1andhltmu9_eta_25 = fs->make<TH1D>("l1andhltmu9_eta_25", "", 12, etabins);
    l1andhltmu11_eta_25 = fs->make<TH1D>("l1andhltmu11_eta_25", "", 12, etabins);
    l1andhltmu13_eta_25 = fs->make<TH1D>("l1andhltmu13_eta_25", "", 12, etabins);
    l1andhltmu15_eta_25 = fs->make<TH1D>("l1andhltmu15_eta_25", "", 12, etabins);
    l1andhltmuFinalOR_eta_25 = fs->make<TH1D>("1landhltmuFinalOR_eta_25", "", 12, etabins);

    // Barrel
    reco_pt_b = fs->make<TH1D>("reco_pt_b", "",34, ptbins);
    l1mu7_pt_b = fs->make<TH1D>("l1mu7_pt_b", "",34, ptbins);
    hltmu9_pt_b = fs->make<TH1D>("hltmu9_pt_b", "",34, ptbins);
    hltmu11_pt_b = fs->make<TH1D>("hltmu11_pt_b", "",34, ptbins);
    hltmu13_pt_b = fs->make<TH1D>("hltmu13_pt_b", "",34, ptbins);
    hltmu15_pt_b = fs->make<TH1D>("hltmu15_pt_b", "",34, ptbins);
    hltmuFinalOR_pt_b = fs->make<TH1D>("hltmuFinalOR_pt_b", "",34, ptbins);
    l1andhltmu9_pt_b = fs->make<TH1D>("l1andhltmu9_pt_b", "",34, ptbins);
    l1andhltmu11_pt_b = fs->make<TH1D>("l1andhltmu11_pt_b", "",34, ptbins);
    l1andhltmu13_pt_b = fs->make<TH1D>("l1andhltmu13_pt_b", "",34, ptbins);
    l1andhltmu15_pt_b = fs->make<TH1D>("l1andhltmu15_pt_b", "",34, ptbins);
    l1andhltmuFinalOR_pt_b = fs->make<TH1D>("l1andhltmuFinalOR_pt_b", "",34, ptbins);

    // Overlap
    reco_pt_o = fs->make<TH1D>("reco_pt_o", "",34, ptbins);
    l1mu7_pt_o = fs->make<TH1D>("l1mu7_pt_o", "",34, ptbins);
    hltmu9_pt_o = fs->make<TH1D>("hltmu9_pt_o", "",34, ptbins);
    hltmu11_pt_o = fs->make<TH1D>("hltmu11_pt_o", "",34, ptbins);
    hltmu13_pt_o = fs->make<TH1D>("hltmu13_pt_o", "",34, ptbins);
    hltmu15_pt_o = fs->make<TH1D>("hltmu15_pt_o", "",34, ptbins);
    hltmuFinalOR_pt_o = fs->make<TH1D>("hltmuFinalOR_pt_o", "",34, ptbins);
    l1andhltmu9_pt_o = fs->make<TH1D>("l1andhltmu9_pt_o", "",34, ptbins);
    l1andhltmu11_pt_o = fs->make<TH1D>("l1andhltmu11_pt_o", "",34, ptbins);
    l1andhltmu13_pt_o = fs->make<TH1D>("l1andhltmu13_pt_o", "",34, ptbins);
    l1andhltmu15_pt_o = fs->make<TH1D>("l1andhltmu15_pt_o", "",34, ptbins);
    l1andhltmuFinalOR_pt_o = fs->make<TH1D>("l1andhltmuFinalOR_pt_o", "",34, ptbins);

    // Endcap
    reco_pt_e = fs->make<TH1D>("reco_pt_e", "",34, ptbins);
    l1mu7_pt_e = fs->make<TH1D>("l1mu7_pt_e", "",34, ptbins);
    hltmu9_pt_e = fs->make<TH1D>("hltmu9_pt_e", "",34, ptbins);
    hltmu11_pt_e = fs->make<TH1D>("hltmu11_pt_e", "",34, ptbins);
    hltmu13_pt_e = fs->make<TH1D>("hltmu13_pt_e", "",34, ptbins);
    hltmu15_pt_e = fs->make<TH1D>("hltmu15_pt_e", "",34, ptbins);
    hltmuFinalOR_pt_e = fs->make<TH1D>("hltmuFinalOR_pt_e", "",34, ptbins);
    l1andhltmu9_pt_e = fs->make<TH1D>("l1andhltmu9_pt_e", "",34, ptbins);
    l1andhltmu11_pt_e = fs->make<TH1D>("l1andhltmu11_pt_e", "",34, ptbins);
    l1andhltmu13_pt_e = fs->make<TH1D>("l1andhltmu13_pt_e", "",34, ptbins);
    l1andhltmu15_pt_e = fs->make<TH1D>("l1andhltmu15_pt_e", "",34, ptbins);
    l1andhltmuFinalOR_pt_e = fs->make<TH1D>("l1andhltmuFinalOR_pt_e", "",34, ptbins);

    firstEventInRun = false;

}


WprimeMuValidation_v2::~WprimeMuValidation_v2()
{
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
}

void
WprimeMuValidation_v2::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

   using namespace edm;
   using namespace reco;
   using namespace std;
   using namespace l1extra;
   using namespace trigger;

   if(firstEventInRun) {
       check_trigger(iEvent);
       firstEventInRun = false;
    }

   Handle<BeamSpot> beamSpotHandle;
   iEvent.getByLabel("offlineBeamSpot", beamSpotHandle);

   //Reconstructed Muons
   Handle<MuonCollection> recomuons;
   iEvent.getByLabel("muons", recomuons);

   //Trigger Filters/Objects
   Handle<TriggerEvent> aodTriggerEvent;
   iEvent.getByLabel("hltTriggerSummaryAOD",aodTriggerEvent);

   Handle<L1MuonParticleCollection> l1Muons;
   iEvent.getByLabel("l1extraParticles", l1Muons);
  
   TriggerObjectCollection allObjects = aodTriggerEvent->getObjects();

   Handle<TrackToTrackMap> tevMapH_default;
   Handle<TrackToTrackMap> tevMapH_1stHit;
   Handle<TrackToTrackMap> tevMapH_picky;
   Handle<TrackToTrackMap> tevMapH_dyt; 

   iEvent.getByLabel(tevMuonLabel_, "default", tevMapH_default);
   tevMap_default = tevMapH_default.product();

   iEvent.getByLabel(tevMuonLabel_, "firstHit", tevMapH_1stHit);
   tevMap_1stHit = tevMapH_1stHit.product();

   iEvent.getByLabel(tevMuonLabel_, "picky", tevMapH_picky);
   tevMap_picky = tevMapH_picky.product();

   iEvent.getByLabel(tevMuonLabel_, "dyt", tevMapH_dyt);
   tevMap_dyt = tevMapH_dyt.product();

   //Handle<TriggerResults> hltresults;
   //iEvent.getByLabel(HLTTag_,hltresults);

   if (!recomuons.isValid()) cout<<"Bad Reco Muons"<<endl;
   if (!l1Muons.isValid()) cout<<"Bad L1muons"<<endl;
   if (!aodTriggerEvent.isValid()) cout<<"Bad AOD trigger event"<<endl;
   if (!beamSpotHandle.isValid()) cout<<"Bad beam spot"<<endl;

   if (recomuons.isValid() && l1Muons.isValid() && aodTriggerEvent.isValid() && beamSpotHandle.isValid() ) {

       for(MuonCollection::const_iterator mu=recomuons->begin(); mu!=recomuons->end(); mu++ ) {

           if (!mu->isGlobalMuon()) continue;
           TrackRef gm = mu->globalTrack();

           // Build the Cocktail
           TrackToTrackMap::const_iterator iTeV_default;
           TrackToTrackMap::const_iterator iTeV_1stHit;
           TrackToTrackMap::const_iterator iTeV_picky;
           TrackToTrackMap::const_iterator iTeV_dyt;

           iTeV_default = tevMap_default->find(mu->globalTrack());
           iTeV_1stHit = tevMap_1stHit->find(mu->globalTrack());
           iTeV_picky = tevMap_picky->find(mu->globalTrack());
           iTeV_dyt = tevMap_dyt->find(mu->globalTrack());

           TrackRef cocktail = muon::tevOptimized(mu->combinedMuon(), mu->track(), 
			   *tevMap_default, *tevMap_1stHit, *tevMap_picky);
           
           // Make some quality cuts on the offline muon/cocktail
           // Exotica Muon ID Reccomended cuts
           if (!mu->isTrackerMuon()) continue;
           if (!(mu->numberOfMatches()>1)) continue;
           if (!(gm->hitPattern().numberOfValidTrackerHits()>10)) continue;
           if (!(gm->hitPattern().numberOfValidPixelHits()>0)) continue; 
           if (!(gm->hitPattern().numberOfValidMuonHits()>0)) continue;
           if (!(gm->normalizedChi2()<10)) continue;
           if (!(fabs(gm->dxy(beamSpotHandle->position()))<0.2)) continue;  
           // This isolation is different than our analysis, but its the simplest
           // and should be enough for the purpose of trigger efficiency.
           if (!(mu->isolationR03().sumPt<3)) continue;

           TrajectoryStateOnSurface prop = propagator_.extrapolate(*mu);
           if (!prop.isValid()) continue; 
       
           // We now have a good offline reconstructed muon. Fill the denominator.
           if (abs(mu->eta())<2.1 ) { // All eta
               reco_pt->Fill(cocktail->pt());
               if (cocktail->pt()>25.0) reco_eta_25->Fill(mu->eta());
           }
           if (abs(mu->eta())<0.9) { // Barrel
               reco_pt_b->Fill(cocktail->pt());
           }
           if (abs(mu->eta())>0.9 && abs(mu->eta())<1.2){ // Overlap
               reco_pt_o->Fill(cocktail->pt()); 
           }
           if (abs(mu->eta())>1.2 && abs(mu->eta())<2.1){ // Overlap
               reco_pt_e->Fill(cocktail->pt());
           }

           // Check if it fired the trigger.
           // First, loop over l1muons and check if any match this reco muon.
           // Use the extrapolated position to do the matching

           bool l1matched=false;
           bool firedL1Mu7=false;
 
           for ( size_t im=0; im<l1Muons->size(); im++) {

               L1MuonParticleRef l1muon(l1Muons, im);

               if ( !(l1muon->gmtMuonCand().quality() > 3.0) )  continue;     
               double dR = deltaR(l1muon->eta(),(l1muon->phi()+1.25*TMath::Pi()/180.),prop.globalPosition().eta(),prop.globalPosition().phi());
               if ( dR < 0.5 ) l1matched = true;
               if ( l1muon->pt() >= 7.0 ) firedL1Mu7=true;
           }
           if (l1matched) {
               if ( abs(mu->eta())<2.1 ) { // All eta
                   if (firedL1Mu7) {
                       l1mu7_pt->Fill(cocktail->pt());
                       if (cocktail->pt()>=25.0) l1mu7_eta_25->Fill(mu->eta());
                   }
               }
               if ( abs(mu->eta())<0.9 ) { // Barrel
                   if (firedL1Mu7) {
                       l1mu7_pt_b->Fill(cocktail->pt());
                   }       
               }
               if (abs(mu->eta())>0.9 && abs(mu->eta())<1.2){ //Overlap
                   if (firedL1Mu7) {
                       l1mu7_pt_o->Fill(cocktail->pt());
                   }                   
               }
               if (abs(mu->eta())>1.2 && abs(mu->eta())<2.1){ // Endcap
                   if (firedL1Mu7) {
                       l1mu7_pt_e->Fill(cocktail->pt());
                   }                          
               }
           }

           // Now, try and match to an HLT L3 filter object.
           bool firedHLTMu9=false;
           bool firedHLTMu11=false;
           bool firedHLTMu13=false;
           bool firedHLTMu15=false;
           bool firedHLTMuFinalOR=false;

           // Loop over all the filters
           for(int i=0; i<aodTriggerEvent->sizeFilters(); i++){       
               // The keys label the objects from a given filter
               // Loop over all the objects in this filter, and match it to the reco::Muon
               Keys keys = aodTriggerEvent->filterKeys(i);
               bool hltmatched = false;         
               for(size_t j=0; j<keys.size(); j++){
                   // Match the object to this reco muon
                   double dR = deltaR(allObjects[keys[j]].eta(),allObjects[keys[j]].phi(),mu->eta(),cocktail->phi());
                   //double dpt = (cocktail->pt()-allObjects[keys[j]].pt())/(cocktail->pt());
                   //if ( (dR < 0.3) && (abs(dpt)<0.1) ) hltmatched = true; 
                   if ( (dR < 0.2) ) hltmatched = true; 
               }
               if (hltmatched) {
                   if(aodTriggerEvent->filterTag(i).label()=="hltSingleMu9L3Filtered9") firedHLTMu9=true;
                   if(aodTriggerEvent->filterTag(i).label()=="hltSingleMu11L3Filtered11") firedHLTMu11=true;  
                   if(aodTriggerEvent->filterTag(i).label()=="hltSingleMu13L3Filtered13") firedHLTMu13=true;     
                   if(aodTriggerEvent->filterTag(i).label()=="hltSingleMu15L3Filtered15") firedHLTMu15=true;     
                   // See if it matches to any of the triggers in the logical OR we use for the final analysis
                   string finalFilter = "NOTHINGYET";
                   for(size_t pathNr=0; pathNr<hltConfig.size(); pathNr++){
                       const std::string& pathName = hltConfig.triggerName(pathNr);
                       //loop over the triggers used for the analysis
                       for(std::map<unsigned int,std::string>::const_iterator itinfo = m_triggers.begin(), itinfoend = m_triggers.end(); 
                           itinfo != itinfoend;++itinfo) {
                           string muTrigName = itinfo->second; 
                           if (pathName.compare(muTrigName) != 0 ) continue;
                           // This path matches one of the paths we want!!!
                           unsigned int hlt_prescale = hltConfig.prescaleValue(iEvent, iSetup, pathName);
                           if ( hlt_prescale != 1 ) continue;
                           // We found an unprescaled Muon Trigger which is used in the analysis.  
                           // Now we need the label of the final filter to do the matching.
                           const std::vector<std::string>& filters = hltConfig.moduleLabels(pathNr);
                           if(!filters.empty()){
                               if(filters.back()=="hltBoolEnd" && filters.size()>=2) {
                                   finalFilter = filters[filters.size()-2]; //2nd to last element is the last filter, except for ES bits
                               } else {
                                   finalFilter = filters.back();
                               }
                           }
                           if(aodTriggerEvent->filterTag(i).label() == finalFilter) firedHLTMuFinalOR=true;     
                       }// Paths in the Analysis
                   }// Paths in the Menu
               }// Filters with objects matching our reco::Muon
           }// All Filters
            
           if ( abs(mu->eta())<2.1 ) { // All eta
               if (firedHLTMu9) {
                   l1andhltmu9_pt->Fill(cocktail->pt());
                   if (cocktail->pt()>=25.0) l1andhltmu9_eta_25->Fill(mu->eta());
                   if (firedL1Mu7 && l1matched) {
                       hltmu9_pt->Fill(cocktail->pt());
                       if (cocktail->pt()>=25.0) hltmu9_eta_25->Fill(mu->eta());
                   }
               }
               if (firedHLTMu11) {
                   l1andhltmu11_pt->Fill(cocktail->pt());
                   if (cocktail->pt()>=25.0) l1andhltmu11_eta_25->Fill(mu->eta());                   
                   if (firedL1Mu7 && l1matched) { 
                       hltmu11_pt->Fill(cocktail->pt());
                       if (cocktail->pt()>=25.0) hltmu11_eta_25->Fill(mu->eta());
                   }
               }
               if (firedHLTMu13) {
                   l1andhltmu13_pt->Fill(cocktail->pt());
                   if (cocktail->pt()>=25.0) l1andhltmu13_eta_25->Fill(mu->eta());                   
                   if (firedL1Mu7 && l1matched) { 
                       hltmu13_pt->Fill(cocktail->pt());
                       if (cocktail->pt()>=25.0) hltmu13_eta_25->Fill(mu->eta());
                   }
               }
               if (firedHLTMu15) {
                   l1andhltmu15_pt->Fill(cocktail->pt());
                   if (cocktail->pt()>=25.0) l1andhltmu15_eta_25->Fill(mu->eta());                   
                   if (firedL1Mu7 && l1matched) { 
                       hltmu15_pt->Fill(cocktail->pt());
                       if (cocktail->pt()>=25.0) hltmu15_eta_25->Fill(mu->eta());
                   }
               }
               if (firedHLTMuFinalOR) {
                   l1andhltmuFinalOR_pt->Fill(cocktail->pt());
                   if (cocktail->pt()>=25.0) l1andhltmuFinalOR_eta_25->Fill(mu->eta());                   
                   if (firedL1Mu7 && l1matched) { 
                       hltmuFinalOR_pt->Fill(cocktail->pt());
                       if (cocktail->pt()>=25.0) hltmuFinalOR_eta_25->Fill(mu->eta());
                   }
               }
           }
           if ( abs(mu->eta())<0.9 ) { // Barrel  
               if (firedHLTMu9) {
                   l1andhltmu9_pt_b->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) {
                       hltmu9_pt_b->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu11) {
                   l1andhltmu11_pt_b->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu11_pt_b->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu13) {
                   l1andhltmu13_pt_b->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu13_pt_b->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu15) {
                   l1andhltmu15_pt_b->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu15_pt_b->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMuFinalOR) {
                   l1andhltmuFinalOR_pt_b->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmuFinalOR_pt_b->Fill(cocktail->pt());
                   }
               }
           }
           if (abs(mu->eta())>0.9 && abs(mu->eta())<1.2){ //Overlap
                if (firedHLTMu9) {
                   l1andhltmu9_pt_o->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) {
                       hltmu9_pt_o->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu11) {
                   l1andhltmu11_pt_o->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu11_pt_o->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu13) {
                   l1andhltmu13_pt_o->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu13_pt_o->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu15) {
                   l1andhltmu15_pt_o->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu15_pt_o->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMuFinalOR) {
                   l1andhltmuFinalOR_pt_o->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmuFinalOR_pt_o->Fill(cocktail->pt());
                   }
               }
           }
           if (abs(mu->eta())>1.2 && abs(mu->eta())<2.1){ // Endcap
                if (firedHLTMu9) {
                   l1andhltmu9_pt_e->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) {
                       hltmu9_pt_e->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu11) {
                   l1andhltmu11_pt_e->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu11_pt_e->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu13) {
                   l1andhltmu13_pt_e->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu13_pt_e->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMu15) {
                   l1andhltmu15_pt_e->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmu15_pt_e->Fill(cocktail->pt());
                   }
               }
               if (firedHLTMuFinalOR) {
                   l1andhltmuFinalOR_pt_e->Fill(cocktail->pt());
                   if (firedL1Mu7 && l1matched) { 
                       hltmuFinalOR_pt_e->Fill(cocktail->pt());
                   }
               }
           }
      
       }//reco muons
   }//valid collections
}//analyze

void WprimeMuValidation_v2::beginRun(edm::Run const & iRun, 
			       edm::EventSetup const & iSetup)
{
  firstEventInRun = true;

  propagator_.init(iSetup);

  bool changed(true);
  if(! hltConfig.init(iRun, iSetup, HLTTag_.process(), changed) )
    {
      std::cout << "  -- Failed to init HLT Config" << std::endl; 
      abort(); // what is the proper way of handling this??? skip run?
    }

  // collect the triggers of interest according to config input
  m_triggers.clear();
  for (unsigned int i = 0; i < expressions.size(); ++i){
    
      const std::vector< std::vector<std::string>::const_iterator > & matches = 
          edm::regexMatch(hltConfig.triggerNames(), expressions[i]);
    
      BOOST_FOREACH(const std::vector<std::string>::const_iterator & match, matches){
          unsigned int index = hltConfig.triggerIndex(*match);
          assert(index < hltConfig.size());
          std::map<unsigned int, std::string>::const_iterator mit = m_triggers.find(index);
          if (mit != m_triggers.end()) { 
              std::cout << " Trigger " << *match
                        << " was already considered (your wildcarding is overlapping)\n"
                        << " don't panic, it's ok, I will skip the double entry..."<<std::endl;
              continue;
          }
          m_triggers.insert( std::make_pair(index , *match) );
      }
  }// collect triggers of interest

}

void WprimeMuValidation_v2::endRun(edm::Run const &, edm::EventSetup const &)
{
}


// ------------ method called once each job just before starting event loop  ------------
void 
WprimeMuValidation_v2::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
WprimeMuValidation_v2::endJob() {
}

void WprimeMuValidation_v2::check_trigger(const edm::Event & iEvent)
{
  edm::Handle<edm::TriggerResults> hltresults;
  iEvent.getByLabel(HLTTag_,hltresults);
  
  if (! hltresults.isValid() ) 
  { 
      std::cout << "  -- No HLTRESULTS" << std::endl; 
      abort(); // what is the proper way of handling this??? skip run?
  }
    
  const edm::Provenance & prov = iEvent.getProvenance(hltresults.id());
  std::cout << " CMSSW release used to produce trigger decisions: "<<std::endl;
  std::cout<< prov.releaseVersion() << std::endl;
}


//define this as a plug-in
DEFINE_FWK_MODULE(WprimeMuValidation_v2);
