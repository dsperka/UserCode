// 
// Limit calculation for W' -> tb analysis at CMS
// 

#include "TGraphErrors.h"
#include "TMultiGraph.h"
#include "RooStats/HypoTestInverterResult.h"

#include "StandardHypoTestInvDemo.5.32.C"


void limit( void ){

  std::string sWsFile  = "results/wprime_mujets_wprimeCrossSection_model.root";
  std::string sChannel = "mujets";
  std::string sSbHypo  = "ModelConfig"; // name of the S+B model config object
  std::string sBHypo   = ""; // name of the bg-only model config, optional
  std::string sData    = "obsData";
  std::string sClsPlotName    = "clsScanPlot.pdf";
  int iCalcType = 2;    // 2 for asymptotic, 0 for frequentist, 1 for hybrid
  int iTestStatType = 3; // 3 for one-sided profile likelihood aka LHC style
  bool doCls = true;
  int iNScan = 20;
  double poiMin = 0;
  double poiMax = 2;
  int iNToys = 1000; // for full CLs only
  

  RooStats::HypoTestInverterResult * 
    res = StandardHypoTestInvDemo( sWsFile.c_str(),
				   sChannel.c_str(),
				   sSbHypo.c_str(),
				   sBHypo.c_str(),
				   sData.c_str(),
				   iCalcType,
				   iTestStatType,
				   doCls,
				   iNScan,
				   poiMin,
				   poiMax,
				   iNToys,
				   false,"",
				   sClsPlotName );

  // print the observed limit
  std::cout << "Observed limit: " << res->UpperLimit() << std::endl;

  // get the CLs scan plot out of the result
  // the resulting TGraphErrors contains all points
  std::string sClsPlotTitle = "CLs scan";
  RooStats:: HypoTestInverterPlot 
    * pPlot = new HypoTestInverterPlot("cls_scan_plot",
				       sClsPlotTitle.c_str(),
				       res);

  // these graph objects contain all the observed 
  // and expected points
  // (these are not plotted, they are just containers)
  // 
  TGraphErrors * pObsPlot = pPlot->MakePlot();
  TMultiGraph * pExpPlot = pPlot->MakeExpectedPlot();

    return;
}
