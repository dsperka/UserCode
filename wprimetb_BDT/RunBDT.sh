#!/bin/sh

DoTraining(){

for tag in GE1BTag  ; do
for coupl in R  ; do
for sig in wp800$coupl wp1000$coupl wp1200$coupl wp1400$coupl wp1600$coupl wp1800$coupl wp2000$coupl wp2200$coupl wp2400$coupl wp2600$coupl wp2800$coupl wp3000$coupl  ; do

#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011_Minimal.txt
#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011.txt
#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011_Fix.txt
#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2012_minKS0pt1.txt
vlist=VarLists/minimal_${chan}.list

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
   echo make effciency plot .................................
   `root -l -b -q  'efficiencies.C("Training_outfiles/BDTtrained_'${tag}'_'${sig}'_'${chan}'.root", 0)'`
   echo make correlation plot .................................
   `root -l -b -q  'correlations.C("Training_outfiles/BDTtrained_'${tag}'_'${sig}'_'${chan}'.root")'`
   echo make ranking file .................................
   `grep -A 100 "Ranking input variables (method specific)..." Training_outfiles/Training_${tag}_${sig}_${chan}.log > Training_outfiles/RankedVars_${tag}_${sig}_${chan}.list`
   echo clean ...............................................
   `rm ${tag}_${sig}_${chan}.C`

cat >${tag}_${sig}_${chan}_testtrain.C <<EOF2
{ 
TFile *_file0 = TFile::Open("Training_outfiles/BDTtrained_${tag}_${sig}_${chan}.root");   
  
_file0->cd();
_file0->cd("Method_BDT/BDT");
TH1F *_h_sig = (TH1F*)gDirectory->Get("MVA_BDT_S");
TH1F *_h_bkg = (TH1F*)gDirectory->Get("MVA_BDT_B");

_h_sig->SetLineColor(2);
_h_sig->SetMarkerColor(2);
_h_sig->SetTitle("");
_h_sig->SetName("");
_h_sig->GetXaxis()->SetTitle("BDT Discriminant");
_h_sig->GetYaxis()->SetTitle("Entries");
_h_sig->SetMaximum(20*_h_sig->GetMaximum());
_h_sig->SetMarkerStyle(20);
_h_sig->SetMarkerSize(0.8);
_h_sig->Draw("e");
_h_bkg->SetMarkerStyle(20);
_h_bkg->SetMarkerSize(0.8);
_h_bkg->Draw("esame");

TH1F *_h_sigt = (TH1F*)gDirectory->Get("MVA_BDT_Train_S");
TH1F *_h_bkgt = (TH1F*)gDirectory->Get("MVA_BDT_Train_B");
_h_sigt->SetLineColor(2);
_h_sigt->SetMarkerColor(2);
_h_sigt->Draw("histsame");
_h_bkgt->Draw("histsame");

TLegend *legend = new TLegend(0.70,0.75,0.95,0.95,"${sig}_${chan}");
legend->AddEntry(_h_sig,"Signal (Test)","elp");
legend->AddEntry(_h_sigt,"Signal (Train)","l");
legend->AddEntry(_h_bkg,"Background (Test)","elp");  
legend->AddEntry(_h_bkgt,"Background (Train)","l");
legend->Draw("same");

TLatex *latex = new TLatex();
latex->SetNDC();
latex->SetTextSize(0.04);
latex->SetTextAlign(31);
latex->DrawLatex(0.47, 0.92, "CMS Simulation, #sqrt{s} = 8 TeV");

c1->SetLogy();

c1->Print("BDTDone/TestTrainBDT_${tag}_${sig}_${chan}.png");
_h_sigt->KolmogorovTest(_h_sig,"ND");
_h_bkgt->KolmogorovTest(_h_bkg,"ND");

}
EOF2

root -l -b -q ${tag}_${sig}_${chan}_testtrain.C > Training_outfiles/TestTrainKS_${tag}_${sig}_${chan}.txt
rm ${tag}_${sig}_${chan}_testtrain.C

done
done
done
}

ApplyBDT(){

for tag in  GE1BTag  ; do
for coupl in R  ; do
#for sig in  wp1500$coupl wp1700$coupl wp1900$coupl wp2100$coupl wp2300$coupl  ; do
for sig in wp800$coupl wp1000$coupl wp1200$coupl wp1400$coupl wp1600$coupl wp1800$coupl wp2000$coupl wp2200$coupl wp2400$coupl wp2600$coupl wp2800$coupl wp3000$coupl  ; do
for sys in '' '_JESUP' '_JESDOWN' '_JERUP' '_JERDOWN' '_BTAGUP' '_BTAGDOWN'  ; do
#for sys in ''  ; do
#for trenm in data wjets${sys} ww${sys} ttbar${sys} zjets${sys} t${sys} s${sys} tw${sys} bt${sys} bs${sys} btw${sys} $sig${sys}  ; do
for trenm in data w1jets${sys} w2jets${chan} w3jets${chan} w4jets${chan} ww${sys} ttbar${sys} zjets${sys} t${sys} s${sys} tw${sys} bt${sys} bs${sys} btw${sys} $sig${sys}  ; do

#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011_Minimal.txt
#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011.txt
#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2011_Fix.txt
#vlist=VarLists/Variables_${tag}_${chan}_${coupl}_2012_minKS0pt1.txt
vlist=VarLists/minimal_${chan}.list

echo $tag $sig $trenm  
cat > ${tag}_${sig}_${chan}_apply.C <<EOF
{   
   gROOT.ProcessLine(".x TMVAlogon.C"); 
   gROOT.ProcessLine(".L WPrimeAnalyisBDTApplication.cxx+");
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

#`rm plots/*.* BDTDone/*.* Training_outfiles/*.* weights/*.*` 

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