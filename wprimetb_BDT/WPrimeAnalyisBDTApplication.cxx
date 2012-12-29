/**********************************************************************************
 * Project   : TMVA - a Root-integrated toolkit for multivariate data analysis    *
 * Package   : TMVA                                                               *
 * Exectuable: TMVApplication                                                     *
 *                                                                                *
 * This macro provides a simple example on how to use the trained classifiers     *
 * within an analysis module                                                      *
 *                                                                                *
 * ------------------------------------------------------------------------------ *
 * see also the alternative (slightly faster) way to retrieve the MVA values in   *
 * examples/TMVApplicationAlternative.cxx  
 *                                       *
 * ------------------------------------------------------------------------------ *
 **********************************************************************************/
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"
#include "TH1F.h"

#if not defined(__CINT__) || defined(__MAKECINT__)
#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/Config.h"

#endif

using namespace TMVA;
using namespace std;

/*
  #include <iostream>

  #include "TCut.h"
  #include "TFile.h"
  #include "TSystem.h"
  #include "TTree.h"
  #include "TStopwatch.h"
  #include "TH1F.h"
  #include "TList.h"sssss// requires links
  #include "TMVA/Factory.h"
  #include "TMVA/Tools.h"
  #include "TMVA/Config.h"
  #include "TMVA/Reader.h"
*/
// ---------------------------------------------------------------
// choose MVA methods to be applied



Bool_t Use_Cuts            = 0;
Bool_t Use_CutsD           = 0;
Bool_t Use_CutsGA          = 0;
Bool_t Use_Likelihood      = 0;
Bool_t Use_LikelihoodD     = 0; // the "D" extension indicates decorrelated input variables (see option strings)
Bool_t Use_LikelihoodPCA   = 0; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
Bool_t Use_PDERS           = 0;
Bool_t Use_PDERSD          = 0;
Bool_t Use_PDERSPCA        = 0;
Bool_t Use_KNN             = 0;
Bool_t Use_HMatrix         = 0;
Bool_t Use_Fisher          = 1;
Bool_t Use_FDA_GA          = 0;
Bool_t Use_FDA_MT          = 0;
Bool_t Use_MLP             = 0; // this is the recommended ANN
Bool_t Use_CFMlpANN        = 0; 
Bool_t Use_TMlpANN         = 0; 
Bool_t Use_SVM_Gauss       = 0;
Bool_t Use_SVM_Poly        = 0;
Bool_t Use_SVM_Lin         = 0;
Bool_t Use_BDT             = 1;
Bool_t Use_BDTD            = 0;
Bool_t Use_RuleFit         = 0;


// ---------------------------------------------------------------

void TMVApplication( TString myMethodList = "", string treenm = "", TString tag  = "", TString sig = "", TString vlist = "", TString chan = "") 
{

 
  cout << "==> start TMVApplication" << endl;




  if (myMethodList != "") {
    Use_CutsGA = Use_CutsD = Use_Cuts
      = Use_LikelihoodPCA = Use_LikelihoodD = Use_Likelihood
      = Use_PDERSPCA = Use_PDERSD = Use_PDERS 
      = Use_KNN
      = Use_MLP = Use_CFMlpANN = Use_TMlpANN

      = Use_HMatrix = Use_Fisher = Use_BDTD = Use_BDT = Use_RuleFit 
      = Use_SVM_Gauss = Use_SVM_Poly = Use_SVM_Lin
      = Use_FDA_GA = Use_FDA_MT
      = 0;

    //TList* mlist = TMVA::Tools::ParseFormatLine( myMethodList, " :," );
    TList* mlist = TMVA::gTools().ParseFormatLine( myMethodList, " :," );

    if (mlist->FindObject( "Cuts"          ) != 0) Use_Cuts          = 1; 
    if (mlist->FindObject( "CutsD"         ) != 0) Use_CutsD         = 1; 
    if (mlist->FindObject( "CutsGA"        ) != 0) Use_CutsGA        = 1; 
    if (mlist->FindObject( "Likelihood"    ) != 0) Use_Likelihood    = 1; 
    if (mlist->FindObject( "LikelihoodD"   ) != 0) Use_LikelihoodD   = 1; 
    if (mlist->FindObject( "LikelihoodPCA" ) != 0) Use_LikelihoodPCA = 1; 
    if (mlist->FindObject( "PDERS"         ) != 0) Use_PDERS         = 1; 
    if (mlist->FindObject( "PDERSD"        ) != 0) Use_PDERSD        = 1; 
    if (mlist->FindObject( "PDERSPCA"      ) != 0) Use_PDERSPCA      = 1; 
    if (mlist->FindObject( "KNN"           ) != 0) Use_KNN           = 1; 
    if (mlist->FindObject( "HMatrix"       ) != 0) Use_HMatrix       = 1; 
    if (mlist->FindObject( "Fisher"        ) != 0) Use_Fisher        = 1; 
    if (mlist->FindObject( "MLP"           ) != 0) Use_MLP           = 1; 
    if (mlist->FindObject( "CFMlpANN"      ) != 0) Use_CFMlpANN      = 1; 
    if (mlist->FindObject( "TMlpANN"       ) != 0) Use_TMlpANN       = 1; 
    if (mlist->FindObject( "BDTD"          ) != 0) Use_BDTD          = 1; 
    if (mlist->FindObject( "BDT"           ) != 0) Use_BDT           = 1; 
    if (mlist->FindObject( "RuleFit"       ) != 0) Use_RuleFit       = 1; 
    if (mlist->FindObject( "SVM_Gauss"     ) != 0) Use_SVM_Gauss     = 1; 
    if (mlist->FindObject( "SVM_Poly"      ) != 0) Use_SVM_Poly      = 1; 
    if (mlist->FindObject( "SVM_Lin"       ) != 0) Use_SVM_Lin       = 1; 
    if (mlist->FindObject( "FDA_MT"        ) != 0) Use_FDA_MT        = 1; 
    if (mlist->FindObject( "FDA_GA"        ) != 0) Use_FDA_GA        = 1; 

    delete mlist;
  }
  
  /*
    std::cout << std::endl;
    std::cout << "==> Start TMVAMulticlassApplication" << std::endl; 
    if (myMethodList != "") {
    for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) it->second = 0;

    std::vector<TString> mlist = gTools().SplitString( myMethodList, ',' );
    for (UInt_t i=0; i<mlist.size(); i++) {
    std::string regMethod(mlist[i]);

    if (Use.find(regMethod) == Use.end()) {
    std::cout << "Method \"" << regMethod << "\" not known in TMVA under this name. Choose among the following:" << std::endl;
    for (std::map<std::string,int>::iterator it = Use.begin(); it != Use.end(); it++) std::cout << it->first << " " << std::endl;
    std::cout << std::endl;
    return;
    }
    Use[regMethod] = 1;
    }
    }
  */
  //
  // create the Reader object
  //
  TMVA::Reader *reader = new TMVA::Reader("!Color:!Silent");    

  ifstream fvarname;
  fvarname.open(vlist);
  string line;

  vector<string> varname;
  vector<string> vartype;

  vector<string> specvarname;
  vector<string> specvartype;

  if (fvarname.is_open())
    {
      while ( fvarname.good() )
	{
	  getline (fvarname,line);
          if(line.length() == 0) continue;
	  if(line[0] == '#') {
            string type_i = line.substr(2,2);   
	    string var_i = line.substr(5,line.length());
	    specvarname.push_back(var_i);
            specvartype.push_back(type_i);
	  } else {
            string type_i = line.substr(1,1);   
	    string var_i = line.substr(4,line.length());
	    varname.push_back(var_i);
            vartype.push_back(type_i);
	  }
	}
    } else {
    cout << "Could not open variable list: " << vlist << endl;
  }
   
   

  /////***********************************************************/////
  /////***********************************************************/////
  /////***********************************************************/////
  /////  create a set of variables and declare them to the reader /////
  ///// - the variable names must corresponds in name and type to /////
  ///// those given in the weight file(s) that you use            /////
  /////***********************************************************/////
  /////***********************************************************/////
  /////***********************************************************/////
   
  TFile *input(0);//input file
  //TString fname = "./YieldSamples/muon_Data_1BTag_1000_RightWprime.root";
  TString fname = "./YieldSamples/YieldsTrees_" +  tag + "_" +  chan + ".root";
  cout << fname << endl;
  input = TFile::Open( fname );
   
   
  if (!input) {
    std::cout << "ERROR: could not open data file: " << fname << std::endl;
    exit(1);
  }
   
  cout << "=========== booked the method =============" << endl;

  //_____ input tree name ______________________________________________   
  char *tnm = (char*)treenm.c_str();
  cout << "========getting the tree ======" << tnm << endl;
  TTree* theTree = (TTree*)input->Get(tnm);
   

  if (!theTree) {
    std::cout << "ERROR: could not get the tree: " << tnm << std::endl;
    exit(1);
  }

  cout << fname << " " << treenm  << endl;
      
  cout << "--- select signal sample=====" << endl;
    
  Double_t vardouble[varname.size()];
  Int_t varint[varname.size()];
  Float_t varfloat[varname.size()];

  Double_t specvardouble[specvarname.size()];
  Int_t specvarint[specvarname.size()];
  Float_t specvarfloat[specvarname.size()];

  Double_t _bdtc = -100.0;
   
  // Set branches for Training variables   
  for (unsigned int i=0; i < varname.size();i++){
    char *varn = (char*)varname[i].c_str();
    //cout << "==== setting BrAddress for ====" << varn << endl;
    if (vartype[i]=="D") theTree->SetBranchAddress(varn, &vardouble[i]);
    else if (vartype[i]=="I") theTree->SetBranchAddress(varn, &varint[i]);
  }

  // Set branches for Spectator variables
  for (unsigned int i=0; i < specvarname.size();i++){
    char *specvarn = (char*)specvarname[i].c_str();
    //cout << "==== setting BrAddress for ====" << varn << endl;
    if (specvartype[i]=="D") theTree->SetBranchAddress(specvarn, &specvardouble[i]);
    else if (specvartype[i]=="I") theTree->SetBranchAddress(specvarn, &specvarint[i]);
  }

  // Add Training variables to Reader
  for (unsigned int i=0; i < varname.size();i++){
    char *varn = (char*)varname[i].c_str();
    cout << "adding variable " << varname[i] << " to the reader " << i << endl;
    reader->AddVariable(varn, &varfloat[i]);
  }
   
  // Add Spectator variables to Reader
  for (unsigned int i=0; i < specvarname.size();i++){
    char *specvarn = (char*)specvarname[i].c_str();
    cout << "adding spectator " << specvarname[i] << "to the reader " << i << endl;
    reader->AddSpectator(specvarn, &specvarfloat[i]);
  }
   

  //
  // book the MVA methods
  //
  string dir    = "weights/";
  string prefix = "TMVAnalysis";
  cout << dir + prefix + "_" + tag + "_" + sig +  "_" + chan +  "_BDT.weights.xml" << endl;

  if (Use_Cuts)          reader->BookMVA( "Cuts method",          dir + prefix + "_Cuts.weights.txt" );
  if (Use_CutsD)         reader->BookMVA( "CutsD method",         dir + prefix + "_CutsD.weights.txt" );
  if (Use_Fisher)        reader->BookMVA( "Fisher method",        dir + prefix + "_Fisher.weights.txt" );
  if (Use_MLP)           reader->BookMVA( "MLP method",           dir + prefix + "_MLP.weights.txt" );
  if (Use_BDT)           reader->BookMVA( "BDT method",           dir + prefix + "_" + tag + "_" + sig +  "_" + chan +  "_BDT.weights.xml" );
  if (Use_BDTD)          reader->BookMVA( "BDTD method",          dir + prefix + "_BDTD.weights.txt" );
  if (Use_RuleFit)       reader->BookMVA( "RuleFit method",       dir + prefix + "_RuleFitTMVA.weights.txt" );
 

  TString noutfile= "BDTDone/BDT_" + tag + "_" + sig + "_" + treenm + "_" + chan + ".root";
  TFile *outfile  = new TFile( noutfile,"RECREATE" );//output file
     
   
  TTree * newtree = theTree->CloneTree();
   
  //TBranch *b_ll = theTree->Branch("MVA_Likelihood", &_ll, "MVA_Likelihood/F");
  //TBranch *b_ll = newtree->Branch("MVA_Likelihood", &_ll, "MVA_Likelihood/D");
  //TBranch * b_bdtc = theTree->Branch("MVA_BDT", &_bdtc, "MVA_BDT/F");
  TBranch * b_bdtc = newtree->Branch("MVA_BDT", &_bdtc, "MVA_BDT/D");
   
   
  cout << "--- after setting the branches" << endl;
   
  /////***********************************************************/////
   
  // book output histograms
  UInt_t nbin = 100;
  //TH1F *histLk;
  //TH1F  *histBdt, *histBdtD, *histRf;
  TH1F  *histBdt= new TH1F( "MVA_BDT",           "MVA_BDT",           nbin, -1.0, 1.0 );
   
  cout << "=========== booking output histograms ============== " << endl;
  //if (Use_Likelihood)    histLk    = new TH1F( "MVA_Likelihood",    "MVA_Likelihood",    nbin,  0, 1 );
  cout << "-------------------booked out histos ------" << endl;
  //if (Use_BDT)           histBdt   = new TH1F( "MVA_BDT",           "MVA_BDT",           nbin, -1.0, 1.0 );
  //if (Use_BDTD)          histBdtD  = new TH1F( "MVA_BDTD",          "MVA_BDTD",          nbin, -0.4, 0.6 );
  //if (Use_RuleFit)       histRf    = new TH1F( "MVA_RuleFitTMVA",   "MVA_RuleFitTMVA",   nbin, -2.0, 2.0 );
   
  // book examsple histogram for probability (the other methods are done similarly)
  //TH1F *probHistFi, *rarityHistFi;
  //if (Use_Fisher) {
  //   probHistFi   = new TH1F( "PROBA_MVA_Fisher",  "PROBA_MVA_Fisher",  nbin, 0, 1 );
  //   rarityHistFi = new TH1F( "RARITY_MVA_Fisher", "RARITY_MVA_Fisher", nbin, 0, 1 );
  //}
  
  
  // efficiency calculator for cut method
  Int_t    nSelCuts = 0, nSelCutsD = 0, nSelCutsGA = 0;
  Double_t effS     = 1.0;

  cout << "--- processing: " << theTree->GetEntries() << " events" << endl;
  TStopwatch sw;
  sw.Start();
  Int_t nEvent = theTree->GetEntries();

  cout << " events " << nEvent << endl;
   
   

  for (Long64_t ievt=0; ievt<nEvent;ievt++) {
    if (ievt%1000 == 0) cout << "--- ... processing event: " << ievt << endl;
     
    theTree->GetEntry(ievt);
     
    //vector<Double_t> vardouble;
    for (unsigned int i=0; i < varname.size();i++){
      varfloat[i] = (Float_t)vardouble[i];
      //cout <<" event " << ievt << " index " << i << " varname "  << varfloat[i] << endl;
       
    }
    //if (Use_Fisher       )   histFi    ->Fill( reader->EvaluateMVA( "Fisher method"        ) );
    if (Use_BDT          ){
      _bdtc =  (Double_t)(reader->EvaluateMVA("BDT method") );
      histBdt   ->Fill( reader->EvaluateMVA( "BDT method"           ) );
      b_bdtc    ->Fill();
      //cout <<  _bdtc << endl;
       
    }
    //if (Use_BDTD         )   histBdtD  ->Fill( reader->EvaluateMVA( "BDTD method"          ) );
     
    // retrieve probability instead of MVA output
    //if (Use_Fisher       )   {
    //   probHistFi  ->Fill( reader->GetProba ( "Fisher method" ) );
    //   rarityHistFi->Fill( reader->GetRarity( "Fisher method" ) );
    //}
  }
  sw.Stop();
  cout << "--- end of event loop: "; sw.Print();
  // get elapsed time
  if (Use_Cuts)   cout << "--- efficiency for Cuts method  : " << double(nSelCuts)/theTree->GetEntries()
		       << " (for a required signal efficiency of " << effS << ")" << endl;
  if (Use_CutsD)  cout << "--- efficiency for CutsD method : " << double(nSelCutsD)/theTree->GetEntries()
		       << " (for a required signal efficiency of " << effS << ")" << endl;
  if (Use_CutsGA) cout << "--- efficiency for CutsGA method: " << double(nSelCutsGA)/theTree->GetEntries()
		       << " (for a required signal efficiency of " << effS << ")" << endl;
   


  if (Use_BDT         )   histBdt  ->Write();
  /*************************
   //
   // write histograms
   //
   TFile *outfile  = new TFile( "TMVApp.root","RECREATE" );
   if (Use_Likelihood   )   histLk    ->Write();
   if (Use_LikelihoodD  )   histLkD   ->Write();
   if (Use_LikelihoodPCA)   histLkPCA ->Write();
   if (Use_PDERS        )   histPD    ->Write();
   if (Use_PDERSD       )   histPDD   ->Write();
   if (Use_PDERSPCA     )   histPDPCA ->Write();
   if (Use_KNN          )   histKNN   ->Write();
   if (Use_HMatrix      )   histHm    ->Write();
   if (Use_Fisher       )   histFi    ->Write();
   if (Use_MLP          )   histNn    ->Write();
   if (Use_CFMlpANN     )   histNnC   ->Write();
   if (Use_TMlpANN      )   histNnT   ->Write();
   if (Use_BDT          )   histBdt   ->Write();
   if (Use_BDTD         )   histBdtD  ->Write();
   if (Use_RuleFit      )   histRf    ->Write();
   if (Use_SVM_Gauss    )   histSVMG  ->Write();
   if (Use_SVM_Poly     )   histSVMP  ->Write();
   if (Use_SVM_Lin      )   histSVML  ->Write();
   if (Use_FDA_MT       )   histFDAMT ->Write();
   if (Use_FDA_GA       )   histFDAGA ->Write();

   if (Use_Fisher       ) { probHistFi->Write(); rarityHistFi->Write(); }

   outfile->Close();

       
  *******************************/


  
   
  outfile->cd();
  outfile->Write();
  delete outfile;

  cout << "--- created root file: \"TMVApp-XXX.root\" containing the MVA output histograms" << endl;
  
  delete reader;
  //  } //end loops
  // }
  //}

  cout << "==> TMVApplication is done!" << endl << endl;


} 
