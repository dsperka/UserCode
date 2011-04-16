// -*- C++ -*-
//
// Package:    WprimeMuValidation_v3
// Class:      WprimeMuValidation_v3
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

#include "DataFormats/JetReco/interface/CaloJet.h"

#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/RecoCandidate/interface/IsoDepositFwd.h"

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

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"

#include "TMath.h"

#include "CommonTools/Utils/interface/PtComparator.h"


//
// class declaration
//

class WprimeMuValidation_v3 : public edm::EDAnalyzer {
    HLTConfigProvider hltConfig;
    public:
    explicit WprimeMuValidation_v3(const edm::ParameterSet&);
    ~WprimeMuValidation_v3();
    private:
    virtual void beginJob() ;
    virtual void beginRun(edm::Run const &, edm::EventSetup const &);
    virtual void endRun(edm::Run const &, edm::EventSetup const &);
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob() ;

    // ----------member data ---------------------------
    edm::InputTag HLTTag_;

    // All eta
    TH1 *reco_pt;
    TH1 *l1mu7_pt;
    TH1 *hltmu15_pt; 
    TH1 *l1andhltmu15_pt; 

    // Pt > 25
    TH1 *reco_eta_20;
    TH1 *l1mu7_eta_20; 
    TH1 *hltmu15_eta_20; 
    TH1 *l1andhltmu15_eta_20; 

    // Barrel
    TH1 *reco_pt_b; 
    TH1 *l1mu7_pt_b;   
    TH1 *hltmu15_pt_b;  
    TH1 *l1andhltmu15_pt_b; 

    // Overlap
    TH1 *reco_pt_o; 
    TH1 *l1mu7_pt_o; 
    TH1 *hltmu15_pt_o;  
    TH1 *l1andhltmu15_pt_o; 
   
    // Isolation stuff
    TH1 *reco_drmujet1_pt20;
    TH1 *l1mu7_drmujet1_pt20;
    TH1 *hltmu15_drmujet1_pt20;
    TH1 *l1andhltmu15_drmujet1_pt20;
 
    TH1 *reco_drmujet2_pt20;
    TH1 *l1mu7_drmujet2_pt20;
    TH1 *hltmu15_drmujet2_pt20;
    TH1 *l1andhltmu15_drmujet2_pt20;

    TH1 *reco_ptdR1_pt20;
    TH1 *l1mu7_ptdR1_pt20;
    TH1 *hltmu15_ptdR1_pt20;
    TH1 *l1andhltmu15_ptdR1_pt20;

    TH1 *reco_ptdR2_pt20;
    TH1 *l1mu7_ptdR2_pt20;
    TH1 *hltmu15_ptdR2_pt20;
    TH1 *l1andhltmu15_ptdR2_pt20;

    TH1 *reco_iso_pt20;
    TH1 *l1mu7_iso_pt20;
    TH1 *hltmu15_iso_pt20;
    TH1 *l1andhltmu15_iso_pt20;

    bool firstEventInRun;
    void check_trigger(const edm::Event & iEvent);

    PropagateToMuon propagator_;
  
    std::string tevMuonLabel_;
  
    const reco::TrackToTrackMap * tevMap_default;
    const reco::TrackToTrackMap * tevMap_1stHit;
    const reco::TrackToTrackMap * tevMap_picky;
    const reco::TrackToTrackMap * tevMap_dyt;

};

WprimeMuValidation_v3::WprimeMuValidation_v3(const edm::ParameterSet& iConfig) :
    HLTTag_ ( iConfig.getParameter<edm::InputTag>("HLTriggerResults")),
    propagator_ (iConfig),
    tevMuonLabel_ (iConfig.getParameter<std::string> ("tevMuonLabel"))
{
    //now do what ever initialization is needed

    Float_t etabins[] = {-2.4,-2.1,-1.5,-1.2,-0.9,-0.6,-0.3,-0.2,0.2,0.3,0.6,0.9,1.2,1.5,2.1,2.4};
    Float_t ptbins[] = {1.0,3.0,5.0,7.0,9.0,11.0,13.0,15.0,17.0,20.0,25.0,30.0,35.0,40.0,45.0,50.0,75.0,100.0,200.0,300.0,460.0};

    edm::Service<TFileService> fs;

    // All eta
    reco_pt = fs->make<TH1D>("reco_pt", "",20, ptbins);
    l1mu7_pt = fs->make<TH1D>("l1mu7_pt", "",20, ptbins);
    hltmu15_pt = fs->make<TH1D>("hltmu15_pt", "",20, ptbins);
    l1andhltmu15_pt = fs->make<TH1D>("l1andhltmu15_pt", "",20, ptbins);

    reco_drmujet1_pt20 = fs->make<TH1D>("reco_drmujet1_pt20", "", 80, 0.0, 2.0);
    l1mu7_drmujet1_pt20 = fs->make<TH1D>("l1mu7_drmujet1_pt20", "", 80, 0.0, 2.0);
    hltmu15_drmujet1_pt20 = fs->make<TH1D>("hltmu15_drmujet1_pt20", "", 80, 0.0, 2.0);
    l1andhltmu15_drmujet1_pt20 = fs->make<TH1D>("l1andhltmu15_drmujet1_pt20", "", 80, 0.0, 2.0);
  
    reco_drmujet2_pt20 = fs->make<TH1D>("reco_drmujet2_pt20", "", 80, 0.0, 2.0);
    l1mu7_drmujet2_pt20 = fs->make<TH1D>("l1mu7_drmujet2_pt20", "", 80, 0.0, 2.0);
    hltmu15_drmujet2_pt20 = fs->make<TH1D>("hltmu15_drmujet2_pt20", "", 80, 0.0, 2.0);
    l1andhltmu15_drmujet2_pt20 = fs->make<TH1D>("l1andhltmu15_drmujet2_pt20", "", 80, 0.0, 2.0);

    reco_ptdR1_pt20 = fs->make<TH1D>("reco_ptdR1_pt20", "", 50, 0.0, 5.0);
    l1mu7_ptdR1_pt20 = fs->make<TH1D>("l1mu7_ptdR1_pt20", "", 50, 0.0, 5.0);
    hltmu15_ptdR1_pt20 = fs->make<TH1D>("hltmu15_ptdR1_pt20", "", 50, 0.0, 5.0);
    l1andhltmu15_ptdR1_pt20 = fs->make<TH1D>("l1andhltmu15_ptdR1_pt20", "", 50, 0.0, 5.0);
 
    reco_ptdR2_pt20 = fs->make<TH1D>("reco_ptdR2_pt20", "", 50, 0.0, 5.0);
    l1mu7_ptdR2_pt20 = fs->make<TH1D>("l1mu7_ptdR2_pt20", "", 50, 0.0, 5.0);
    hltmu15_ptdR2_pt20 = fs->make<TH1D>("hltmu15_ptdR2_pt20", "", 50, 0.0, 5.0);
    l1andhltmu15_ptdR2_pt20 = fs->make<TH1D>("l1andhltmu15_ptdR2_pt20", "", 50, 0.0, 5.0);
 
    reco_iso_pt20 = fs->make<TH1D>("reco_iso_pt20", "", 80, 0.0, 4.0);
    l1mu7_iso_pt20 = fs->make<TH1D>("l1mu7_iso_pt20", "", 80, 0.0, 4.0);
    hltmu15_iso_pt20 = fs->make<TH1D>("hltmu15_iso_pt20", "", 80, 0.0, 4.0);
    l1andhltmu15_iso_pt20 = fs->make<TH1D>("l1andhltmu15_iso_pt20", "", 80, 0.0, 4.0);


    // Pt > 20 GeV
    reco_eta_20 = fs->make<TH1D>("reco_eta_20", "", 15, etabins);
    l1mu7_eta_20 = fs->make<TH1D>("l1mu7_eta_20", "", 15, etabins);
    hltmu15_eta_20 = fs->make<TH1D>("hltmu15_eta_20", "", 15, etabins);
    l1andhltmu15_eta_20 = fs->make<TH1D>("l1andhltmu15_eta_20", "", 15, etabins);

    // Barrel
    reco_pt_b = fs->make<TH1D>("reco_pt_b", "",20, ptbins);
    l1mu7_pt_b = fs->make<TH1D>("l1mu7_pt_b", "",20, ptbins);
    hltmu15_pt_b = fs->make<TH1D>("hltmu15_pt_b", "",20, ptbins);
    l1andhltmu15_pt_b = fs->make<TH1D>("l1andhltmu15_pt_b", "",20, ptbins);

    // Overlap
    reco_pt_o = fs->make<TH1D>("reco_pt_o", "",20, ptbins);
    l1mu7_pt_o = fs->make<TH1D>("l1mu7_pt_o", "",20, ptbins);
    hltmu15_pt_o = fs->make<TH1D>("hltmu15_pt_o", "",20, ptbins);
    l1andhltmu15_pt_o = fs->make<TH1D>("l1andhltmu15_pt_o", "",20, ptbins);
   
    firstEventInRun = false;

}


WprimeMuValidation_v3::~WprimeMuValidation_v3()
{
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
}

void
WprimeMuValidation_v3::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

   Handle<IsoDepositMap> tkMapH;
   Handle<IsoDepositMap> ecalMapH;
   Handle<IsoDepositMap> hcalMapH;
   iEvent.getByLabel("muIsoDepositTk", tkMapH);
   iEvent.getByLabel("muIsoDepositCalByAssociatorTowers","ecal", ecalMapH);
   iEvent.getByLabel("muIsoDepositCalByAssociatorTowers","hcal", hcalMapH);

   Handle<CaloJetCollection> jetCaloCollection;
   iEvent.getByLabel("ak7CaloJets", jetCaloCollection);

   if (!recomuons.isValid()) cout<<"Bad Reco Muons"<<endl;
   if (!l1Muons.isValid()) cout<<"Bad L1muons"<<endl;
   if (!aodTriggerEvent.isValid()) cout<<"Bad AOD trigger event"<<endl;
   if (!beamSpotHandle.isValid()) cout<<"Bad beam spot"<<endl;
   if (!tkMapH.isValid()) cout<<"Bad tkMapH"<<endl;
   if (!ecalMapH.isValid()) cout<<"Bad ecalMapH"<<endl;
   if (!hcalMapH.isValid()) cout<<"Bad hcalMapH"<<endl;
   if (!jetCaloCollection.isValid()) cout<<"Bad Jets"<<endl;
   

   if (recomuons.isValid() && l1Muons.isValid() && aodTriggerEvent.isValid() && beamSpotHandle.isValid() ) {

       int nglobal=0;
       for (unsigned i=0; i!=recomuons->size(); i++) {
           reco::MuonRef mu(recomuons, i);
           if (mu->isGlobalMuon()) nglobal++;
       }

       for (unsigned i=0; i!=recomuons->size(); i++) {

           if (nglobal>1) continue;
           reco::MuonRef mu(recomuons, i);
           TrackRef gm = mu->globalTrack();

           if (!mu->isGlobalMuon()) continue;


           // Isolation
           const reco::IsoDeposit tkDep((*tkMapH)[mu]);
           const reco::IsoDeposit ecalDep((*ecalMapH)[mu]);
           const reco::IsoDeposit hcalDep((*hcalMapH)[mu]);
           double ptsum_cone=tkDep.depositWithin(0.3);
           double ecetsum_cone=ecalDep.depositWithin(0.3); 
           double hcetsum_cone=hcalDep.depositWithin(0.3); 

           double CombRelIso = (ptsum_cone+ecetsum_cone+hcetsum_cone)/(mu->innerTrack()->pt());

           // Make some quality cuts on the offline muon/cocktail
           if (!(mu->numberOfMatchedStations()>1)) continue;
           if (!(gm->hitPattern().numberOfValidTrackerHits()>10)) continue;
           if (!(gm->hitPattern().numberOfValidPixelHits()>0)) continue; 
           if (!(gm->hitPattern().numberOfValidMuonHits()>0)) continue;
           if (!(gm->normalizedChi2()<10)) continue;
           if (!(fabs(gm->dxy(beamSpotHandle->position()))<0.02)) continue;

           TrajectoryStateOnSurface prop = propagator_.extrapolate(*mu);
           if (!prop.isValid()) continue; 
    
           //get the closest two calo jets
           double thisdRmujet;
           double dRmujet2 = 9999.9;
           double dRmujet1 = 9999.9;
           double ptdR1 = -999.0;
           double ptdR2 = -999.0;

           for (CaloJetCollection::const_iterator jet_ = jetCaloCollection->begin(); 
                jet_ !=jetCaloCollection->end(); ++jet_) { // loop over jets
               
               thisdRmujet = deltaR(mu->eta(),mu->phi(),jet_->eta(),jet_->phi());

               if ( (thisdRmujet < dRmujet2) && (thisdRmujet > dRmujet1 )) {
                        dRmujet2 = thisdRmujet;
                        ptdR2 = 1000*dRmujet2/jet_->pt();
                    }
                    if (  thisdRmujet < dRmujet1 ) {
                        dRmujet2 = dRmujet1;
                        ptdR2 = ptdR1;

                        dRmujet1 = thisdRmujet;
                        ptdR1 = 1000*dRmujet1/jet_->pt();
                    }
           } // loop over calojets

           // Apply isolation, fill the denominator.
           if (CombRelIso < 0.15) {
               if (abs(mu->eta())<2.4) {
                   if (mu->pt()>20.0) reco_eta_20->Fill(mu->eta());
               }
               if (abs(mu->eta())<2.1 ) { // All eta
                   reco_pt->Fill(mu->pt());
               }
               if (abs(mu->eta())<0.9) { // Barrel
                   reco_pt_b->Fill(mu->pt());
               }
               if (abs(mu->eta())>0.9 && abs(mu->eta())<2.1){ // Overlap
                   reco_pt_o->Fill(mu->pt()); 
               }
           }
           // For these plots, don't apply the isolation
           if (abs(mu->eta())<2.1) {
               if (mu->pt()>20.0) {
                   reco_drmujet1_pt20->Fill(dRmujet1);
                   reco_drmujet2_pt20->Fill(dRmujet2);
                   reco_ptdR1_pt20->Fill(ptdR1);
                   reco_ptdR2_pt20->Fill(ptdR2);
                   reco_iso_pt20->Fill(CombRelIso);
               }
           }
           // Check if it fired the trigger.
           // First, loop over l1muons and check if any match this reco muon.
           // Use the extrapolated position to do the matching

           bool l1matched=false;
           bool firedL1Mu7=false;

           for ( size_t im=0; im<l1Muons->size(); im++) {

               L1MuonParticleRef l1muon(l1Muons, im);

               if ( !(l1muon->gmtMuonCand().quality() > 3.0) )  continue;               
               double dR = deltaR(l1muon->eta(),l1muon->phi(),prop.globalPosition().eta(),prop.globalPosition().phi());
               if ( dR < 0.5 ) l1matched = true;
               if ( l1muon->pt() >= 7.0 ) firedL1Mu7=true;
           }
           if (l1matched) {
               if (CombRelIso < 0.15) {
                   if ( abs(mu->eta())<2.4) {
                       if (firedL1Mu7 && mu->pt()>20.0) l1mu7_eta_20->Fill(mu->eta());
                   }
                   if ( abs(mu->eta())<2.1 ) { // All eta
                       if (firedL1Mu7) {
                           l1mu7_pt->Fill(mu->pt());
                       }
                   }
                   if ( abs(mu->eta())<0.9 ) { // Barrel
                       if (firedL1Mu7) {
                           l1mu7_pt_b->Fill(mu->pt());
                       }       
                   }
                   if (abs(mu->eta())>0.9 && abs(mu->eta())<2.1){ //Overlap+Endcap
                       if (firedL1Mu7) {
                           l1mu7_pt_o->Fill(mu->pt());
                       }                   
                   }
               } // CombRelIso
               if (abs(mu->eta())<2.1 && firedL1Mu7) {
                   if (mu->pt()>20.0 ) {
                       l1mu7_drmujet1_pt20->Fill(dRmujet1);
                       l1mu7_drmujet2_pt20->Fill(dRmujet2);
                       l1mu7_ptdR1_pt20->Fill(ptdR1);
                       l1mu7_ptdR2_pt20->Fill(ptdR2);
                       l1mu7_iso_pt20->Fill(CombRelIso);
                   }
               }
           }

           // Now, try and match to an HLT L3 filter object.
           bool firedHLTMu15=false;

           // Loop over all the filters
           for(int i=0; i<aodTriggerEvent->sizeFilters(); i++){       
               // The keys label the objects from a given filter
               // Loop over all the objects in this filter, and match it to the reco::Muon
               Keys keys = aodTriggerEvent->filterKeys(i);
               bool hltmatched = false;         
               double objpt = 0.0;
               for(size_t j=0; j<keys.size(); j++){
                   // Match the object to this reco muon
                   double dR = deltaR(allObjects[keys[j]].eta(),allObjects[keys[j]].phi(),mu->eta(),mu->phi());
                   if ( (dR < 0.5) ) { 
                       hltmatched = true;
                       objpt = allObjects[keys[j]].pt(); 
                   }
               }
               if (hltmatched) {
                   if( aodTriggerEvent->filterTag(i).label()=="hltSingleMu15L3Filtered15") firedHLTMu15=true;
                   if( (aodTriggerEvent->filterTag(i).label()=="hltSingleMu9L3Filtered9") && (objpt >= 15.0) ) firedHLTMu15=true;    
               }// Filters with objects matching our reco::Muon
           }// All Filters
            
           if ( abs(mu->eta())<2.4 ) {
               if ( CombRelIso < 0.15 ) {
                   if ( firedHLTMu15 && mu->pt()>20.0) {
                       l1andhltmu15_eta_20->Fill(mu->eta());
                       if ( firedL1Mu7 && l1matched) hltmu15_eta_20->Fill(mu->eta());
                   }
                   if ( abs(mu->eta())<2.1 ) { // All eta
                       if (firedHLTMu15) {
                           l1andhltmu15_pt->Fill(mu->pt());
                           if (firedL1Mu7 && l1matched) { 
                               hltmu15_pt->Fill(mu->pt());
                           }
                       }
                   }
                   if ( abs(mu->eta())<0.9 ) { // Barrel  
                       if (firedHLTMu15) {
                           l1andhltmu15_pt_b->Fill(mu->pt());
                           if (firedL1Mu7 && l1matched) { 
                               hltmu15_pt_b->Fill(mu->pt());
                           }
                       }
                   }
                   if (abs(mu->eta())>0.9 && abs(mu->eta())<2.1){ //Overlap+Endcap
                       if (firedHLTMu15) {
                           l1andhltmu15_pt_o->Fill(mu->pt());
                           if (firedL1Mu7 && l1matched) { 
                               hltmu15_pt_o->Fill(mu->pt());
                           }
                       }
                   }   
               } // CombRelIso
               if (abs(mu->eta())<2.1) {
                   if (firedHLTMu15) {
                       if (mu->pt()>20.0 ) {
                           l1andhltmu15_drmujet1_pt20->Fill(dRmujet1);
                           l1andhltmu15_drmujet2_pt20->Fill(dRmujet2);
                           l1andhltmu15_ptdR1_pt20->Fill(ptdR1);
                           l1andhltmu15_ptdR2_pt20->Fill(ptdR2);
                           l1andhltmu15_iso_pt20->Fill(CombRelIso);
                       }
            
                       if (firedL1Mu7 && l1matched) {
                           if (mu->pt()>20.0 ) {
                               hltmu15_drmujet1_pt20->Fill(dRmujet1);
                               hltmu15_drmujet2_pt20->Fill(dRmujet2);
                               hltmu15_ptdR1_pt20->Fill(ptdR1);
                               hltmu15_ptdR2_pt20->Fill(ptdR2);
                               hltmu15_iso_pt20->Fill(CombRelIso);
                           }
                       }
                   }
               }
           }
         
           // Print event info for high pt muons
           if (mu->pt()>300 ) {
               cout <<"pt: "<<mu->pt()<<" "<<iEvent.id().run()<<":"<<iEvent.id().luminosityBlock()<<":"<<iEvent.id().event()<<" Mu15: "<<firedHLTMu15<<endl<<" Iso: "<<CombRelIso<<endl;
           }

       }//reco muons
   }//valid collections
}//analyze

void WprimeMuValidation_v3::beginRun(edm::Run const & iRun, 
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

}

void WprimeMuValidation_v3::endRun(edm::Run const &, edm::EventSetup const &)
{
}


// ------------ method called once each job just before starting event loop  ------------
void 
WprimeMuValidation_v3::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
WprimeMuValidation_v3::endJob() {
}

void WprimeMuValidation_v3::check_trigger(const edm::Event & iEvent)
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
DEFINE_FWK_MODULE(WprimeMuValidation_v3);
