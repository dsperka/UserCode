// @(#)root/tmva $Id: TMVAnalysis_wjets.C,v 1.4 2010/01/06 20:20:46 kukartse Exp $
/**********************************************************************************
 * Project   : TMVA - a Root-integrated toolkit for multivariate data analysis    *
 * Package   : TMVA                                                               *
 * Root Macro: TMVAnalysis                                                        *
 *                                                                                *
 * This macro provides examples for the training and testing of all the           *
 * TMVA classifiers.                                                              *
 *                                                                                *
 * As input data is used a toy-MC sample consisting of four Gaussian-distributed  *
 * and linearly correlated input variables.                                       *
 *                                                                                *
 * The methods to be used can be switched on and off by means of booleans, or     *
 * via the prompt command, for example:                                           *
 *                                                                                *
 *    root -l TMVAnalysis.C\(\"Fisher,Likelihood\"\)                              *
 *                                                                                *
 * (note that the backslashes are mandatory)                                      *
 *                                                                                *
 * The output file "TMVA.root" can be analysed with the use of dedicated          *
 * macros (simply say: root -l <macro.C>), which can be conveniently              *
 * invoked through a GUI that will appear at the end of the run of this macro.    *
 **********************************************************************************/

#include <iostream>
#include <sstream>

#include "TMath.h"
#include "TCut.h"
#include "TFile.h"
#include "TSystem.h"
#include "TTree.h"
// requires links
#include "TStopwatch.h"
#include "TH1F.h"
#include "TList.h"
// requires links

#include "TMVA/Factory.h"
#if not defined(__CINT__) || defined(__MAKECINT__)

#include "TMVA/Tools.h"
#include "TMVA/Config.h"
#include "TMVA/Reader.h"
#endif
//#include "TMVA/IMethod.h"
#include "TMVAGui.C"

// ---------------------------------------------------------------
// choose MVA methods to be trained + tested
Bool_t Use_Cuts            = 0;
Bool_t Use_CutsD           = 0;
Bool_t Use_CutsGA          = 0;
// ---
Bool_t Use_Likelihood      = 1;
Bool_t Use_LikelihoodD     = 1; // the "D" extension indicates decorrelated input variables (see option strings)
Bool_t Use_LikelihoodPCA   = 1; // the "PCA" extension indicates PCA-transformed input variables (see option strings)
Bool_t Use_LikelihoodKDE   = 0;
Bool_t Use_LikelihoodMIX   = 0;
// ---
Bool_t Use_PDERS           = 0;
Bool_t Use_PDERSD          = 0;
Bool_t Use_PDERSPCA        = 0;
Bool_t Use_KNN             = 0;
// ---
Bool_t Use_HMatrix         = 0;
Bool_t Use_Fisher          = 1;
// ---
Bool_t Use_FDA_GA          = 0;
Bool_t Use_FDA_MC          = 0;
Bool_t Use_FDA_SA          = 0;
Bool_t Use_FDA_MT          = 1;
Bool_t Use_FDA_GAMT        = 0;
Bool_t Use_FDA_MCMT        = 0;
// ---
Bool_t Use_MLP             = 1; // this is the recommended ANN
Bool_t Use_CFMlpANN        = 0; 
Bool_t Use_TMlpANN         = 0; 
// ---
Bool_t Use_BDT             = 1;
Bool_t Use_BDTD            = 1;
// ---
Bool_t Use_RuleFitTMVA     = 1;
Bool_t Use_RuleFitJF       = 0;
// ---
Bool_t Use_SVM_Gauss       = 1;
Bool_t Use_SVM_Poly        = 0;
Bool_t Use_SVM_Lin         = 0;
// ---------------------------------------------------------------

// read input data file with ascii format (otherwise ROOT) ?
Bool_t ReadDataFromAsciiIFormat = kFALSE;

void TMVAnalysis( TString myMethodList = "" ,TString infname = "",TString tag = "", string sig = "", TString varlist = "", TString coupl = "", TString chan = "") 
{

  // explicit loading of the shared libTMVA is done in TMVAlogon.C, defined in .rootrc
  // if you use your private .rootrc, or run from a different directory, please copy the 
  // corresponding lines from .rootrc

  // methods to be processed can be given as an argument; use format:
  //
  // mylinux~> root -l TMVAnalysis.C\(\"myMethod1,myMethod2,myMethod3\"\)
  //

  TList* mlist = TMVA::gTools().ParseFormatLine( myMethodList, " :," );
  cout << " set mlist for   " << myMethodList <<  endl;
  if (mlist->GetSize()>0) {
    Use_CutsGA = Use_CutsD = Use_Cuts
      = Use_LikelihoodKDE = Use_LikelihoodMIX = Use_LikelihoodPCA = Use_LikelihoodD = Use_Likelihood
      = Use_PDERSPCA = Use_PDERSD = Use_PDERS 
      = Use_KNN
      = Use_MLP = Use_CFMlpANN = Use_TMlpANN
      = Use_HMatrix = Use_Fisher = Use_BDTD = Use_BDT
      = Use_RuleFitTMVA = Use_RuleFitJF
      = Use_SVM_Gauss = Use_SVM_Poly = Use_SVM_Lin 
      = Use_FDA_GA = Use_FDA_MC = Use_FDA_SA = Use_FDA_MT = Use_FDA_GAMT = Use_FDA_MCMT 
      = 0;

    if (mlist->FindObject( "Cuts"          ) != 0) Use_Cuts          = 1; 
    if (mlist->FindObject( "CutsD"         ) != 0) Use_CutsD         = 1; 
    if (mlist->FindObject( "CutsGA"        ) != 0) Use_CutsGA        = 1; 
    if (mlist->FindObject( "Likelihood"    ) != 0) Use_Likelihood    = 1; 
    if (mlist->FindObject( "LikelihoodD"   ) != 0) Use_LikelihoodD   = 1; 
    if (mlist->FindObject( "LikelihoodPCA" ) != 0) Use_LikelihoodPCA = 1; 
    if (mlist->FindObject( "LikelihoodKDE" ) != 0) Use_LikelihoodKDE = 1; 
    if (mlist->FindObject( "LikelihoodMIX" ) != 0) Use_LikelihoodMIX = 1; 
    if (mlist->FindObject( "PDERSPCA"      ) != 0) Use_PDERSPCA      = 1; 
    if (mlist->FindObject( "PDERSD"        ) != 0) Use_PDERSD        = 1; 
    if (mlist->FindObject( "PDERS"         ) != 0) Use_PDERS         = 1; 
    if (mlist->FindObject( "KNN"           ) != 0) Use_KNN           = 1; 
    if (mlist->FindObject( "HMatrix"       ) != 0) Use_HMatrix       = 1; 
    if (mlist->FindObject( "Fisher"        ) != 0) Use_Fisher        = 1; 
    if (mlist->FindObject( "MLP"           ) != 0) Use_MLP           = 1; 
    if (mlist->FindObject( "CFMlpANN"      ) != 0) Use_CFMlpANN      = 1; 
    if (mlist->FindObject( "TMlpANN"       ) != 0) Use_TMlpANN       = 1; 
    if (mlist->FindObject( "BDTD"          ) != 0) Use_BDTD          = 1; 
    if (mlist->FindObject( "BDT"           ) != 0) Use_BDT           = 1; 
    if (mlist->FindObject( "RuleFitJF"     ) != 0) Use_RuleFitJF     = 1; 
    if (mlist->FindObject( "RuleFitTMVA"   ) != 0) Use_RuleFitTMVA   = 1; 
    if (mlist->FindObject( "SVM_Gauss"     ) != 0) Use_SVM_Gauss     = 1; 
    if (mlist->FindObject( "SVM_Poly"      ) != 0) Use_SVM_Poly      = 1; 
    if (mlist->FindObject( "SVM_Lin"       ) != 0) Use_SVM_Lin       = 1; 
    if (mlist->FindObject( "FDA_MC"        ) != 0) Use_FDA_MC        = 1; 
    if (mlist->FindObject( "FDA_GA"        ) != 0) Use_FDA_GA        = 1; 
    if (mlist->FindObject( "FDA_SA"        ) != 0) Use_FDA_SA        = 1; 
    if (mlist->FindObject( "FDA_MT"        ) != 0) Use_FDA_MT        = 1; 
    if (mlist->FindObject( "FDA_GAMT"      ) != 0) Use_FDA_GAMT      = 1; 
    if (mlist->FindObject( "FDA_MCMT"      ) != 0) Use_FDA_MCMT      = 1; 

    delete mlist;
  }
  
  std::cout << "Start Test TMVAnalysis" << std::endl
	    << "======================" << std::endl
	    << std::endl;
  std::cout << "Testing all standard methods may take about 10 minutes of running..." << std::endl;
  /////***********************************************************/////
  TString outf = "Training_outfiles/BDTtrained_" + tag + "_" + sig +  "_" + chan + ".root"; 
  TFile* outputFile = TFile::Open( outf, "RECREATE" );
  //TFile* outputFile = new TFile( outf, "RECREATE" );

  // Create the factory object. Later you can choose the methods
  // whose performance you'd like to investigate. The factory will
  // then run the performance analysis for you.
  //
  // The first argument is the base of the name of all the
  // weightfiles in the directory weight/ 
  //
  // The second argument is the output file for the training results

  //TMVA::Factory *factory = new TMVA::Factory( "TMVAnalysis", outputFile, Form("V:%sColor", gROOT->IsBatch()?"!":"") ); olderversion
  //TMVA::Factory *factory = new TMVA::Factory( "TMVAnalysis", outputFile, "!V:!Silent:Color:DrawProgressBar:Transformations=I;D;P;G,D:AnalysisType=Classification" );

  TString factoryname = "TMVAnalysis_" + tag + "_" + sig +  "_" + chan ;
  TMVA::Factory *factory = new TMVA::Factory( factoryname , outputFile, "V:!Silent:Color:DrawProgressBar:AnalysisType=Classification" );
  cout << " set the factory   " << endl;
   
  TFile *input(0);
   
  std::cout << "--- TMVAnalysis  : Input filename is: " << infname << std::endl;

  if (!gSystem->AccessPathName( infname )) {
    std::cout << "--- TMVAnalysis  : accessing " << infname << std::endl;
    input = TFile::Open( infname );
  } 
  else { 
    std::cout << "--- TMVAnalysis  : could not find" << infname << std::endl;
  }
   
  if (!input) {
    std::cout << "ERROR: could not open data file" << std::endl;
    exit(1);
    return;
  }
  cout << " got the file  " << infname <<  endl;

  //
  //_____ input tree name ___________________________________________
  //
    
  char *signalt = (char*)sig.c_str();
  cout << "=====Signal for training ======" << signalt << endl;
  TTree *signal      = (TTree*)input->Get(signalt);

  int nTrainSignal = floor(0.50*signal->GetEntries());
  string string_nTrainSignal = static_cast<ostringstream*>( &(ostringstream() << nTrainSignal) )->str();
  std::cout <<"entries = "<< signal->GetEntries() <<", "<<string_nTrainSignal<<" for training "<< std::endl;

  TTree *bkgndwjets = (TTree*)input->Get("wjets");
  TTree *bkgndTtbar = (TTree*)input->Get("ttbar");
  TTree *bkgndTchan = (TTree*)input->Get("t");
  TTree *bkgndTchanb = (TTree*)input->Get("bt");
  TTree *bkgndSchan = (TTree*)input->Get("s");
  TTree *bkgndSchanb = (TTree*)input->Get("bs");
  TTree *bkgndTWchan = (TTree*)input->Get("tw");
  TTree *bkgndTWchanb = (TTree*)input->Get("btw");
  TTree *bkgndWW = (TTree*)input->Get("ww"); 
  TTree *bkgndZJets = (TTree*)input->Get("zjets"); 
  
  Double_t signalWeight     = 1.0;
   
  std::cout<<"coupling = "<<coupl<<std::endl;

  int nTrainBackground = bkgndwjets->GetEntries()+bkgndTtbar->GetEntries()+bkgndTchan->GetEntries()+bkgndTchanb->GetEntries()+bkgndTWchan->GetEntries()+bkgndTWchanb->GetEntries()+bkgndWW->GetEntries()+bkgndZJets->GetEntries(); 
  if (coupl == "R") nTrainBackground += (bkgndSchan->GetEntries()+bkgndSchanb->GetEntries());

  std::cout << "=====Total Background for training ======" << std::endl;
  string string_nTrainBackground = static_cast<ostringstream*>( &(ostringstream() << floor(0.50*nTrainBackground) ) )->str();
  std::cout <<"entries = "<< nTrainBackground <<", "<<string_nTrainBackground<<" for training "<< std::endl;

  Double_t bkgndwjetsWeight    = 1.0;
  Double_t bkgndTtbarWeight    = 1.0;
  Double_t bkgndTchanWeight    = 1.0;
  Double_t bkgndTchanWeightb   = 1.0;
  Double_t bkgndSchanWeight    = 1.0;
  Double_t bkgndSchanWeightb   = 1.0;
  Double_t bkgndTWchanWeight   = 1.0;
  Double_t bkgndTWchanWeightb  = 1.0;
  Double_t bkgndzjetsWeight    = 1.0;
  Double_t bkgndwwWeight      = 1.0; 
   
  //TSring bkgnd[]= {};
  double scalebk = 1000.0;

  if (chan == "mu"){
    bkgndwjetsWeight   = (1.0/bkgndwjets->GetEntries()) *scalebk*19062.;
    bkgndTtbarWeight   =   (1.0/bkgndTtbar->GetEntries())* scalebk*45491.;
    bkgndTchanWeight   =  (1.0/bkgndTchan->GetEntries()) * scalebk*2052.;
    bkgndTchanWeightb  =  (1.0/bkgndTchanb->GetEntries())* scalebk*1048.;
    bkgndSchanWeight   =  (1.0/bkgndSchan->GetEntries()) *scalebk*230.;
    bkgndSchanWeightb  =   (1.0/bkgndSchanb->GetEntries())*scalebk*108.;
    bkgndTWchanWeight  =  (1.0/bkgndTWchan->GetEntries()) *scalebk*1319.;
    bkgndTWchanWeightb =  (1.0/bkgndTWchanb->GetEntries())*scalebk*1357.;
    bkgndzjetsWeight   =  (1.0/bkgndZJets->GetEntries()) *scalebk*1547.;
    bkgndwwWeight      = (1.0/bkgndWW->GetEntries())* scalebk*192;
    cout << " weight " << bkgndTtbarWeight <<  " " << bkgndwjetsWeight << endl;
  }
  if (chan == "el"){
    bkgndwjetsWeight   = (1.0/bkgndwjets->GetEntries()) *scalebk*17288.;
    bkgndTtbarWeight   =   (1.0/bkgndTtbar->GetEntries())* scalebk*41389.;
    bkgndTchanWeight   =  (1.0/bkgndTchan->GetEntries()) * scalebk*1715.;
    bkgndTchanWeightb  =  (1.0/bkgndTchanb->GetEntries())* scalebk*848.;
    bkgndSchanWeight   =  (1.0/bkgndSchan->GetEntries()) *scalebk*204.;
    bkgndSchanWeightb  =   (1.0/bkgndSchanb->GetEntries())*scalebk*72.;
    bkgndTWchanWeight  =  (1.0/bkgndTWchan->GetEntries()) *scalebk*1202.;
    bkgndTWchanWeightb =  (1.0/bkgndTWchanb->GetEntries())*scalebk*1224.;
    bkgndzjetsWeight   =  (1.0/bkgndZJets->GetEntries()) *scalebk*1345.;
    bkgndwwWeight      = (1.0/bkgndWW->GetEntries())* scalebk*173.;
    cout << " weight " << bkgndTtbarWeight <<  " " << bkgndwjetsWeight << endl;
  }
   
  if (tag != "GE2BTag"){
    factory->AddBackgroundTree( bkgndwjets, bkgndwjetsWeight );
    factory->AddBackgroundTree( bkgndZJets, bkgndzjetsWeight);
    factory->AddBackgroundTree( bkgndWW, bkgndwwWeight);
  }
    
  factory->AddBackgroundTree( bkgndTtbar, bkgndTtbarWeight);
  factory->AddBackgroundTree( bkgndTchan, bkgndTchanWeight);
  factory->AddBackgroundTree( bkgndTchanb, bkgndTchanWeightb );
  if (coupl == "R") factory->AddBackgroundTree( bkgndSchan, bkgndSchanWeight);
  if (coupl == "R") factory->AddBackgroundTree( bkgndSchanb, bkgndSchanWeightb);
  factory->AddBackgroundTree( bkgndTWchan, bkgndTWchanWeight);
  factory->AddBackgroundTree( bkgndTWchanb, bkgndTWchanWeightb);
     
  signalWeight = (1./signal->GetEntries())*(bkgndwjetsWeight + bkgndzjetsWeight + bkgndwwWeight + bkgndTtbarWeight + bkgndTchanWeight + bkgndTchanWeightb + bkgndTWchanWeight + bkgndTWchanWeightb + bkgndSchanWeight + bkgndSchanWeightb);

  factory->AddSignalTree( signal, signalWeight );
  
  if (chan == "mu") {
    cout << "---- applying weights -------" << endl ;
    factory->SetWeightExpression("(1000.*weight_WJets_WprimeCalc*weight_PU_ABC_PileUpCalc*weight_MuonEff_WprimeCalc)");
  }
  if (chan == "el") {
    cout << "---- applying weights -------" << endl ;
    factory->SetWeightExpression("(1000.*weight_WJets_WprimeCalc*weight_PU_ABC_PileUpCalc*weight_ElectronEff_WprimeCalc)");
  }
   
  // Define the input variables that shall be used for the MVA training
  // note that you may also use variable expressions, such as: "3*var1/var2*abs(var3)"
  // [all types of expressions that can also be parsed by TTree::Draw( "expression" )]
   
   
  /////***********************************************************/////
  /////***********************************************************/////
  /////            Provide the list of variables here.            /////
  /////***********************************************************/////

  ifstream fvarname;
  fvarname.open(varlist);
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
    cout << "Could not open variable list: " << varlist << endl;
  }
   

  // Book the variables to be used in the training
  for (unsigned int i=0; i < varname.size(); i++) {
    cout << "adding " << vartype[i] << " " << varname[i] << " to the training " << endl;
    if (vartype[i] == 'D') factory->AddVariable( varname[i], varname[i], "", 'D' );
    else if (vartype[i] == 'I') factory->AddVariable( varname[i], varname[i], "", 'I' );
    else if (vartype[i] == 'F') factory->AddVariable( varname[i], varname[i], "", 'F' );

  }
   
  // Book the spectator variables not used in the training
  for (unsigned int i=0; i < specvarname.size(); i++) {
    cout << "adding spectator " << specvarname[i] << endl;
    factory->AddSpectator( specvarname[i] );
  }
   


  // Apply additional cuts on the signal and background sample. 
   
  TCut mycut = "jet_0_pt_WprimeCalc>120";
  TCut mycutb = "jet_0_pt_WprimeCalc>120"; 


  //TString paramfs = "nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=None:V";
  //TString paramfs = "nTrain_Signal="+string_nTrainSignal+":nTest_Signal=0:nTrain_Background="+string_nTrainBackground+":nTest_Background=0:SplitMode=Random:NormMode=None:V";                                                          
  //TString paramfs = "nTrain_Signal="+string_nTrainSignal+":nTest_Signal=0:nTrain_Background="+string_nTrainBackground+":nTest_Background=0:SplitMode=Random:NormMode=EqualNumEvents:V";
  TString paramfs = "nTrain_Signal="+string_nTrainSignal+":nTest_Signal=0:nTrain_Background="+string_nTrainBackground+":nTest_Background=0:SplitMode=Random:NormMode=EqualNumEvents:V";


  cout << "parameters are = " <<  paramfs << endl;
  factory->PrepareTrainingAndTestTree( mycut,  mycutb, paramfs );//signal and background weights equal - this works
   

  cout << "trees are prepared! " << endl;


  /////*********************************************************************/////
  /////*********************************************************************/////
  /////*********************************************************************/////
  /////***************** --- Book MVA methods --- **************************/////
  /////*********************************************************************/////
  /////*********************************************************************/////
  /////*********************************************************************/////

  // please lookup the various method configuration options in the corresponding cxx files, eg:
  // src/MethoCuts.cxx, etc.
  // it is possible to preset ranges in the option string in which the cut optimisation should be done:
  // "...:CutRangeMin[2]=-1:CutRangeMax[2]=1"...", where [2] is the third input variable

  // Cut optimisation
  //if (Use_Fisher)
  //     factory->BookMethod( TMVA::Types::kFisher, "Fisher", 
  //                           "H:!V:!Normalise:CreateMVAPdfs:Fisher:NbinsMVAPdf=50:NsmoothMVAPdf=1" );  
  //#$%//#$% factory->BookMethod( TMVA::Types::kFisher, "Fisher", "H:!V:Fisher:CreateMVAPdfs:PDFInterpolMVAPdf=Spline2:NbinsMVAPdf=50:NsmoothMVAPdf=10" );
 
  //if (Use_Likelihood)
  //#$%//#$% factory->BookMethod( TMVA::Types::kLikelihood, "Likelihood",
  //#$%//#$%		      "H:!V:!TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50" );
 
  //if (Use_LikelihoodD)
  //#$%//#$% factory->BookMethod( TMVA::Types::kLikelihood, "LikelihoodD",
  //#$%//#$%		      "!H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmooth=5:NAvEvtPerBin=50:VarTransform=Decorrelate" );
 
 
  if (Use_BDT){
      //factory->BookMethod( TMVA::Types::kBDT, "BDT","!H:!V:NTrees=400:nEventsMin=400:MaxDepth=3:BoostType=AdaBoost:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning" );
      //factory->BookMethod( TMVA::Types::kBDT, "BDT","H:V:NTrees=400:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.2:SeparationType=GiniIndex:nCuts=20:PruneMethod=NoPruning" );
      //factory->BookMethod( TMVA::Types::kBDT, "BDT","!H:V:NTrees=700:BoostType=AdaBoost:AdaBoostBeta=0.2:SeparationType=GiniIndex:nCuts=20"); // Shabnam
      factory->BookMethod( TMVA::Types::kBDT, "BDT","!H:V:NTrees=500:BoostType=AdaBoost:AdaBoostBeta=0.2:SeparationType=GiniIndex:nCuts=20:nEventsMin=10000");                 

  }

  // ---- Now you can tell the factory to train, test, and evaluate the MVAs

  // Train MVAs using the set of training events
  factory->TrainAllMethods();

  // ---- Evaluate all MVAs using the set of test events
  factory->TestAllMethods();

  // ----- Evaluate and compare performance of all configured MVAs
  factory->EvaluateAllMethods();    

  // --------------------------------------------------------------
   
  // Save the output
  outputFile->Close();

  std::cout << "==> wrote root file " << outf << std::endl;
  std::cout << "==> TMVAnalysis is done!" << std::endl;      

  // Clean up
  delete factory;

  // Launch the GUI for the root macros
  //if (!gROOT->IsBatch()) TMVAGui( outputFile );
}
