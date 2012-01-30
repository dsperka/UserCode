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
RootFiles['Right'] = TFile("CLs_RootFiles/WprimeRight_AsymptoticCLs_30Jan.root")

Trees = {}
Trees['Right']  = RootFiles['Right'].Get("limit")

def PlotLimits(Type):

    theory_x = array('d' , [800,900,1000,1100,1200,1300,1400,1500,1600,1700,1900,2100,2300,2500] )
    if Type == 'Right':
          theory_y = array('d', [1.2*1.6997,1.2*0.97609,1.2*0.58782,1.2*0.36266,1.2*0.22815,1.2*0.14584,1.2*0.09445,1.2*0.06195,1.2*0.04102,1.2*0.027453,1.2*0.012585,1.2*0.005984,1.2*0.0029719,1.2*0.0015585] )
    theory_xv = TVectorD(len(theory_x),theory_x)
    theory_yv = TVectorD(len(theory_y),theory_y)

    theory = TGraph(theory_xv,theory_yv)
    theory.SetLineColor(2)
    theory.SetLineWidth(2)

         
    Nentries = Trees[Type].GetEntriesFast()        
 
    mass = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    exp = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    obs = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    exp68H = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    exp68L = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    exp95H = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    exp95L = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
 
    masserr = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    obserr = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    experr = array('d', [0,0,0,0,0,0,0,0,0,0,0,0,0,0])
   
    m = 0
    for entry in xrange(Nentries):

        Trees[Type].GetEntry(entry)            

        thismass=Trees[Type].mh
        thisquantile=Trees[Type].quantileExpected
        thislimit=Trees[Type].limit
        thislimiterr=Trees[Type].limitErr

        if thismass == 800.0: i = 0
        elif thismass == 900.0: i = 1 
        elif thismass == 1000.0: i = 2 
        elif thismass == 1100.0: i = 3 
        elif thismass == 1200.0: i = 4 
        elif thismass == 1300.0: i = 5 
        elif thismass == 1400.0: i = 6 
        elif thismass == 1500.0: i = 7 
        elif thismass == 1600.0: i = 8 
        elif thismass == 1700.0: i = 9 
        elif thismass == 1900.0: i = 10 
        elif thismass == 2100.0: i = 11 
        elif thismass == 2300.0: i = 12
        elif thismass == 2500.0: i = 13 


        #if thismass < 1000: continue
        
        if (abs(thisquantile + 1.000 ) < 0.01 ):
            mass[i] = thismass
            obs[i] = thislimit
            obserr[i] = 0
            masserr[i] = 0
        elif (abs(thisquantile - 0.025 ) < 0.01 ):
            exp95L[i] = thislimit
            print '95L ',thislimit
        elif (abs(thisquantile - 0.160 ) < 0.01 ):
            exp68L[i] = thislimit
        elif (abs(thisquantile - 0.500 ) < 0.01 ):
            exp[i] = thislimit
            experr[i] = thislimiterr
        elif (abs(thisquantile - 0.840 ) < 0.01 ):
            exp68H[i] = thislimit
        elif (abs(thisquantile - 0.975 ) < 0.01 ):
            exp95H[i] = thislimit

        print str(thismass)+' '+str(thisquantile)+' '+str(thislimit)


    print 'exp95L',exp95L
    print 'exp95H',exp95H
    print 'exp68L',exp68L
    print 'exp68H',exp68H

    massv = TVectorD(len(mass),mass)
    expv = TVectorD(len(mass),exp)
    obsv = TVectorD(len(mass),obs)
    exp68Hv = TVectorD(len(mass),exp68H)
    exp68Lv = TVectorD(len(mass),exp68L)
    exp95Hv = TVectorD(len(mass),exp95H)
    exp95Lv = TVectorD(len(mass),exp95L)
    #exp95Lv = TVectorD(len(mass),exp68L)

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
    ## I'm confused, somehow this is the way that works
    expected68 = TGraphAsymmErrors(massv,expv,masserrv,masserrv,exp95Lv,exp68Hv)
    #expected68 = TGraphAsymmErrors(massv,expv,masserrv,masserrv,exp68Lv,exp68Hv)
    expected68.SetFillColor(ROOT.kGreen)
    expected95 = TGraphAsymmErrors(massv,expv,masserrv,masserrv,exp68Lv,exp95Hv)
    #expected95 = TGraphAsymmErrors(massv,expv,masserrv,masserrv,exp95Lv,exp95Hv)
    expected95.SetFillColor(ROOT.kYellow)

    c4 = TCanvas("c4","W' tb Limits", 1000, 800)

    c4.SetBottomMargin(0.15)
    c4.SetRightMargin(0.06)

    expected95.Draw("a3") 
    expected95.GetXaxis().SetTitle("W'_{"+Type+"} mass [GeV/c^{2}]")
    expected95.GetYaxis().SetTitle("#sigma(pp#rightarrowW/W'_{"+str(Type)+"}#rightarrowtb) [pb]")
    expected68.Draw("3same")
    expected.Draw("csame") 
    observed.Draw("cpsame") 
    theory.Draw("csame")

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
    legend . AddEntry(expected95 , '#pm 2#sigma Expected', "f")

    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);
    legend.Draw()        

    c4.SaveAs('Wprime_'+Type+'_Limits.root')
    c4.SaveAs('Wprime_'+Type+'_Limits.png')

PlotLimits('Right')

