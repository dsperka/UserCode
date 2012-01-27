import ROOT, sys, os, string, re
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack, TGraph, TGraphErrors, TGraphAsymmErrors, TVectorD
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
 
    mass = array('d')
    exp = array('d')
    obs = array('d')
    exp68H = array('d')
    exp68L = array('d')
    exp95H = array('d')
    exp95L = array('d')
 
    masserr = array('d')
    obserr = array('d')
    experr = array('d')
   
    m = 0
    for entry in xrange(Nentries):

        Trees[Type].GetEntry(entry)            

        thismass=Trees[Type].mh
        thisquantile=Trees[Type].quantileExpected
        thislimit=Trees[Type].limit
        thislimiterr=Trees[Type].limitErr

        print thisquantile

        if (abs(thisquantile + 1.000 ) < 0.0001 ):
            mass.append(thismass)
            obs.append(thislimit)
            obserr.append(0)
            masserr.append(0)
        elif (abs(thisquantile - 0.025 ) < 0.0001 ):
            exp95L.append(thislimit)
        elif (abs(thisquantile - 0.160 ) < 0.0001 ):
            exp68L.append(thislimit)
        elif (abs(thisquantile - 0.500 ) < 0.0001 ):
            exp.append(thislimit)
            experr.append(thislimiterr)
        elif (abs(thisquantile - 0.840 ) < 0.0001 ):
            exp68H.append(thislimit)
        elif (abs(thisquantile - 0.975 ) < 0.0001 ):
            exp95H.append(thislimit) 
    
    massv = TVectorD(len(mass),mass)
    expv = TVectorD(len(mass),exp)
    obsv = TVectorD(len(mass),obs)
    exp68Hv = TVectorD(len(mass),exp68H)
    exp68Lv = TVectorD(len(mass),exp68L)
    exp95Hv = TVectorD(len(mass),exp95H)
    #exp95Lv = TVectorD(len(mass),exp95L)
 
    masserrv = TVectorD(len(mass),masserr)
    obserrv = TVectorD(len(mass),obserr)
    experrv = TVectorD(len(mass),experr)
       

    observed = TGraphAsymmErrors(massv,obsv,masserrv,masserrv,obserrv,obserrv)
    observed.SetLineColor(ROOT.kBlack)    
    observed.SetLineWidth(2)    
    observed.SetMarkerStyle(20)    
    expected = TGraphAsymmErrors(massv,expv,masserrv,masserrv,experrv,experrv)
    expected.SetLineColor(ROOT.kBlack)    
    expected.SetLineWidth(2)    
    expected.SetLineStyle(2)    
    expected68 = TGraphAsymmErrors(massv,expv,masserrv,masserrv,exp68Lv,exp68Hv)
    expected68.SetFillColor(ROOT.kGreen)
    #expected95 = TGraphAsymmErrors(massv,expv,masserrv,masserrv,exp95Lv,exp95Hv)
    #expected95.SetFillColor(ROOT.kYellow)

    c4 = TCanvas("c4","W' tb Limits", 1000, 800)

    c4.SetBottomMargin(0.15)
    c4.SetRightMargin(0.06)
    
    #expected95.Draw("a4") 
    #expected95.GetYaxis().SetTitle("W'_{"+Type+"} mass [GeV/c^{2}]")
    #expected95.GetXaxis().SetTitle("#sigma #cdot BR(t#rightarrow Wb,W#rightarrow #ell #nu)")
    #expected68.Draw("4same") 
    #expected.Draw("lcsame") 
    #observed.Draw("lpsame") 
 
    expected68.Draw("a3") 
    expected68.GetXaxis().SetTitle("W'_{"+Type+"} mass [GeV/c^{2}]")
    expected68.GetYaxis().SetTitle("#sigma#timesB.R.(t#rightarrowWb,W#rightarrowl#nu)")
    expected.Draw("csame") 
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
    latex2.DrawLatex(0.87, 0.95, str(lumiPlot) + " fb^{-1} at #sqrt{s} = 7 TeV")

    latex4 = TLatex()
    latex4.SetNDC()
    latex4.SetTextSize(0.04)
    latex4.SetTextAlign(31) # align right
    latex4.DrawLatex(0.80, 0.87, "e+jets N_{b tags} #geq 1 ");

    legend = TLegend(.566,.684,.84,.84)
    legend . AddEntry(observed , '95% C.L. Observed', "lp")
    legend . AddEntry(expected , '95% C.L. Expected', "l")
    legend . AddEntry(expected68 , '#pm 1#sigma Expected', "f")
    #legend . AddEntry(expected95 , '#pm 1#sigma Expected', "f")

    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);
    legend.Draw()        

    c4.SaveAs('Wprime_'+Type+'_Limits.root')
    c4.SaveAs('Wprime_'+Type+'_Limits.png')

PlotLimits('Right')

