import ROOT, sys, os, string, re
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack, TGraph, TGraphErrors, TGraphAssymErrors
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array

import math
from math import *

from tdrStyle import *
setTDRStyle()

lumiPlot = 4.68

RootFiles = {}
RootFiles['Right'] = TFile("CLs_RootFiles/WprimeRight_CLs_All.root")

Trees = {}
Trees['Right']  = RootFiles['Right'].Get("limit")

def PlotLimits(Type):

    Nentries = Trees[Type].GetEntriesFast()        
 
    mass = {}
    exp = {}
    obs = {}
    exp68H = {}
    exp68L = {}
    exp95H = {}
    exp95L = {}
 
    masserr = {}
    obserr = {}
   
    for entry in xrange(Nentries):

        Trees[Type].GetEntry(entry)            

        thismass=Trees[Type].mh
        thisquantile=Trees[Type].quantileExpected
        thislimit=Trees[Type].limit
        thislimiterr=Trees[Type].limitErr

        if (quantileExpected == -1.000):
            mass.append(int(thismass))
            obs.append(float(thislimit))
            obserr.append(float(thislimit))
        elif (quantileExpected == 0.025):
            exp95L.append(float(thislimit))
        elif (quantileExpected == 0.160):
            exp68L.append(float(thislimit))
        elif (quantileExpected == 0.500):
            exp.append(float(thislimit))
            experr.append(float(thislimiterr))
        elif (quantileExpected == 0.840):
            exp68H.append(float(thislimit))
        elif (quantileExpected == 0.975):
            exp95H.append(float(thislimit)) 
    
    observed = TGraphAsymmErrors(len(mass),mass,obs,masserr,masserr,obserr,obserr)
    observed.SetLineColor(ROOT.kBlack)    
    observed.SetLineWidth(2)    
    expected = TGraphAsymmErrors(len(mass),mass,exp,masserr,masserr,experr,experr)
    expected.SetLineColor(ROOT.kBlack)    
    expected.SetLineWidth(2)    
    expected.SetLineStyle(2)    
    expected68 = TGraphAsymmErrors(len(mass),mass,exp,masserr,masserr,exp68L,exp68H)
    expected68.SetFillColor(ROOT.kGreen)
    expected95 = TGraphAsymmErrors(len(mass),mass,exp,masserr,masserr,exp95L,exp95H)
    expected95.SetFillColor(ROOT.kYellow)

    c4 = TCanvas("c4","W' tb Limits", 1000, 800)

    c4.SetBottomMargin(0.3)
    c4.SetRightMargin(0.06)
    
    expected95.Draw("a4") 
    expected95.GetYaxis().SetTitle("W'_{"+Type+"} mass [GeV/c^{2}]")
    expected95.GetXaxis().SetTitle("#sigma #cdot BR(t#rightarrow Wb,W#rightarrow #ell #nu)")
    expected68.Draw("4same") 
    expected.Draw("lcsame") 
    observed.Draw("lpsame") 

    latex = TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.04)
    latex.SetTextAlign(31) # align right
    latex.DrawLatex(0.45, 0.95, "CMS Preliminary");
    
    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.04)
    latex2.SetTextAlign(31) # align right
    latex2.DrawLatex(0.87, 0.95, str(lumiPlot) + " fb^{-1} at #sqrt{s} = 7 TeV");

    legend = TLegend(.74,.60,.90,.90,'e+jets '+njets)
    legend . AddEntry(observed , '95% C.L. Observed', "lp")
    legend . AddEntry(expected , '95% C.L. Expected', "l")
    legend . AddEntry(expected68 , '#pm 1#sigma Expected', "lf")
    legend . AddEntry(expected95 , '#pm 1#sigma Expected', "lf")

    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);
    legend.Draw()        

    c4.SaveAs('Wprime_'+Typo+'_Limits.root')

PlotLimits('Right')

