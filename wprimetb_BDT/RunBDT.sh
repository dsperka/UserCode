#!/bin/sh

DoTraining(){

for tag in GE1BTag  ; do
for coupl in R  ; do
for sig in wp1500$coupl wp1700$coupl wp1900$coupl wp2100$coupl wp2300$coupl  ; do
#for sig in wp1700$coupl  ; do

#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011_Minimal.txt
vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011.txt


echo $vlist $chan $tag $sig

cat > ${tag}_${sig}_${chan}.C <<EOF
{              
   gROOT.ProcessLine(".x TMVAlogon.C");         
   gROOT.ProcessLine(".L WPrimeAnalyisTraining.cxx+");
   gROOT.ProcessLine("TMVAnalysis(\"BDT\",\"TrainingSamples/TrainingTrees_${tag}_${chan}.root\",\"$tag\", \"$sig\",  \"$vlist\", \"$coupl\",\"$chan\")");
}
EOF
    
   echo Do the training .................................  
   `root -l -b -q ${tag}_${sig}_${chan}.C > Training_outfiles/Training_${tag}_${sig}_${chan}.log` 
   #echo Rename the weight file .................................
   #`mv weights/TMVAnalysis_BDT.weights.xml weights/TMVAnalysis_BDT_${tag}_${sig}_${chan}.weights.xml`    
   echo make effciency plot .................................
   `root -l -b -q  'efficiencies.C("Training_outfiles/BDTtrained_'${tag}'_'${sig}'_'${chan}'.root", 0)'`
   echo make correlation plot .................................
   `root -l -b -q  'correlations.C("Training_outfiles/BDTtrained_'${tag}'_'${sig}'_'${chan}'.root")'`
   echo make ranking file .................................
   `grep -A 100 "Ranking input variables (method specific)..." Training_outfiles/Training_${tag}_${sig}_${chan}.log > Training_outfiles/RankedVars_${tag}_${sig}_${chan}.list`
   #echo clean ...............................................
   #`rm ${tag}_${sig}_${chan}.C`

cat >${tag}_${sig}_${chan}_testtrain.C <<EOF2
{ 

 TFile *_file0 = TFile::Open("Training_outfiles/BDTtrained_${tag}_${sig}_${chan}.root");
 gROOT->ProcessLine(".x ~/rootlogon.C");
  
_file0->cd();
_file0->cd("Method_BDT/BDT");
TH1F *_h_sig = (TH1F*)gDirectory->Get("MVA_BDT_S");
TH1F *_h_bkg = (TH1F*)gDirectory->Get("MVA_BDT_B");
_h_sig->Add(_h_bkg);

_h_sig->SetLineColor(2);
_h_sig->SetLineWidth(2);
_h_sig->SetMarkerColor(2);
//_h_sig->SetMarkerStyle(3);
_h_sig->GetXaxis()->SetTitle("BDT Discriminant");
_h_sig->Draw("e");

TH1F *_h_sigt = (TH1F*)gDirectory->Get("MVA_BDT_Train_S");
TH1F *_h_bkgt = (TH1F*)gDirectory->Get("MVA_BDT_Train_B");
_h_sigt->Add(_h_bkg);
_h_sigt->Draw("esame");

TLegend *legend = new TLegend(0.4,0.2,0.55,0.4);
legend->AddEntry(_h_sig,"S+B (Test)","lp");
legend->AddEntry(_h_sigt,"S+B (Train)","lp");
legend->Draw("same");


c1->Print("Training_outfiles/TestTrainBDT_${tag}_${sig}_${chan}.png");
_h_sigt->KolmogorovTest(_h_sig,"ND");

}
EOF2

root -l -b -q ${tag}_${sig}_${chan}_testtrain.C > Training_outfiles/TestTrainKS_${tag}_${sig}_${chan}.txt
#rm ${tag}_${sig}_${chan}_testtrain.C

done
done
done
}

ApplyBDT(){

for tag in  GE1BTag  ; do
for coupl in R  ; do
for sig in  wp1500$coupl wp1700$coupl wp1900$coupl wp2100$coupl wp2300$coupl  ; do
#for sig in  wp1700$coupl  ; do
#for sys in '' '_JESUP' '_JESDOWN' '_JERUP' '_JERDOWN' '_BTAGUP' '_BTAGDOWN'  ; do
for sys in ''  ; do
for trenm in data wjets${sys} ww${sys} ttbar${sys} zjets${sys} t${sys} s${sys} tw${sys} bt${sys} bs${sys} btw${sys} $sig${sys}  ; do

#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011_Minimal.txt
vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011.txt


echo $tag $sig $trenm  
cat > ${tag}_${sig}_${chan}_apply.C <<EOF
{   
   gROOT.ProcessLine(".x TMVAlogon.C"); 
   gROOT.ProcessLine(".L WPrimeAnalyisBDTApplication.cxx+");
   //gSystem->Load("/uscms_data/d2/jabeen/work/.c/CMSSW_5_0_0_pre2/src/BDT/WPrimeAnalyisBDTApplication_batch_cxx.so");
   gROOT.ProcessLine("TMVApplication(\"BDT\",\"$trenm\", \"$tag\", \"$sig\", \"$vlist\",\"$chan\")");
}
EOF
    `root -l -b -q  ${tag}_${sig}_${chan}_apply.C  > BDTDone/BDT_${trenm}_${tag}_${sig}_${chan}.log` 
    `rm ${tag}_${sig}_${chan}_apply.C`

done 
done  
done 
done 
done   
}

`rm plots/* BDTDone/* Training_outfiles/* weights/*` 

`rm WPrimeAnalyisTraining_cxx.so  WPrimeAnalyisTraining_cxx.d`
`rm WPrimeAnalyisBDTApplication_cxx.so WPrimeAnalyisBDTApplication_cxx.d`
chan=mu
DoTraining
ApplyBDT

`rm WPrimeAnalyisTraining_cxx.so  WPrimeAnalyisTraining_cxx.d`
`rm WPrimeAnalyisBDTApplication_cxx.so WPrimeAnalyisBDTApplication_cxx.d`
chan=el
DoTraining
ApplyBDT