import ROOT, sys, os, string, re
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack, TGraph, TGraphErrors, TColor
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array
import math
from math import *
import copy

from tdrStyle import *
setTDRStyle()

from LoadData_LPC import *


def plot_BDT(channel, var, massPoint, bin, low, high, ylabel, xlabel, save, nBtags = -1, setLog = False, finalcuts = False):

    if (channel == 'electron'):      
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && elec_1_pt_WprimeCalc > 32 && abs(elec_1_eta_WprimeCalc) < 2.5 && elec_1_RelIso_WprimeCalc < 0.1 && corr_met_WprimeCalc > 20' 
        #cut = 'jet_0_pt_WprimeCalc >= 100 && jet_1_pt_WprimeCalc >= 40 && elec_1_pt_WprimeCalc > 30 && abs(elec_1_eta_WprimeCalc) < 2.5 && elec_1_RelIso_WprimeCalc < 0.1 && corr_met_WprimeCalc > 35' 

    if (channel == 'muon'):      
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && muon_1_pt_WprimeCalc > 26 && abs(muon_1_eta_WprimeCalc) < 2.1 && muon_1_RelIso_WprimeCalc < 0.12 && corr_met_WprimeCalc > 20'
        #cut = 'jet_0_pt_WprimeCalc >= 100 && jet_1_pt_WprimeCalc >= 40 && muon_1_pt_WprimeCalc > 26 && abs(muon_1_eta_WprimeCalc) < 2.1 && muon_1_RelIso_WprimeCalc < 0.12 && corr_met_WprimeCalc > 35' 


    if finalcuts: cut+= '&& BestTop_LjetsTopoCalcNew > 130 && BestTop_LjetsTopoCalcNew < 210 &&  BestTop_Pt_LjetsTopoCalcNew > 75  && Jet1Jet2_Pt_LjetsTopoCalcNew > 100'   
    njets = ""

    if nBtags == -1:
        cutbtag = ''
        save = save     
    if nBtags == 0:
        cutbtag =  ' && ( (jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) == 0 )'
        save = save + '_0bTags'
        njets = "N_{b tags} = 0"
    if nBtags == 1:
        cutbtag =  ' && ( (jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc) == 1)'
        save = save + '_1bTags'
        njets = "N_{b tags} = 1"
    if nBtags == 2:
        cutbtag =  ' && ( (jet_0_tag_WprimeCalc + jet_1_tag_WprimeCalc) >= 1 ) '
        save = save + '_GE1bTags'
        njets = "N_{b tags} #geq 1"


    cutwbb = ' && n_Bjets_WprimeCalc > 0' # Wb(b)
    cutwcc = ' && n_Bjets_WprimeCalc==0 && n_Cjets_WprimeCalc>0' # Wc(c)
    cutwjj = ' && n_Bjets_WprimeCalc==0 && n_Cjets_WprimeCalc==0' # W+light
    #cutwbb = ' ' # Wb(b)
    #cutwcc = ' ' # Wc(c)
    #cutwjj = ' ' # W+light
                                                                                                                   
    SFWjmu = 1.08*0.85
    SFWcmu = 1.06*0.92*1.66
    SFWbmu = 1.06*0.92*1.21
    #SFWjmu = 1.0
    #SFWcmu = 1.0
    #SFWbmu = 1.0

    WjjHist = TH1D('WjjHist', 'WjjHist', bin,low,high)
    WccHist = TH1D('WccHist', 'WccHist', bin,low,high)
    WbbHist = TH1D('WbbHist', 'WbbHist', bin,low,high)

    Variables = {}
    efficiency = {}
   
    BkgList = []

    for Type in Samples:

        #print channel,' ',Type

        if (Type.endswith('_el') and channel == 'muon'): continue
        if (Type.endswith('_mu') and channel == 'electron'): continue
        if (not Type.startswith(massPoint) ): continue

        Variables[Type] = TH1D(Type+var+channel, Type+var+channel, bin, low, high)
        histName = Type+var+channel
     
        if (channel == 'electron'): chan = '_el'
        if (channel == 'muon'): chan = '_mu'

        if (channel == 'electron'): weight = 'weight_PU_ABC_PileUpCalc*weight_ElectronEff_WprimeCalc'
        if (channel == 'muon'): weight = 'weight_PU_ABC_PileUpCalc*weight_MuonEff_WprimeCalc'
        
        if ((not Type == massPoint+massPoint+chan) and (not Type == massPoint+'_data'+chan)): BkgList.extend([Type])

        if Type.endswith('wjets'+chan):
            #print 'Filling ',Type
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*(" + str(SFWjmu) + ")*(" + cut + cutbtag + cutwjj + ")", 'goff')
            Trees[Type].Draw(var + " >> " + "WbbHist","("+weight+")*(" + str(SFWbmu) + ")*(" + cut + cutbtag + cutwbb + ")", 'goff')
            Trees[Type].Draw(var + " >> " + "WccHist","("+weight+")*(" + str(SFWcmu) + ")*(" + cut + cutbtag + cutwcc + ")", 'goff')
            #print 'Raw Wjj ',Variables['WJets'].Integral()
            Variables[Type].Add(WbbHist)
            #print 'Raw Wjj + Wbb ',Variables['WJets'].Integral()
            Variables[Type].Add(WccHist) 
            #print 'Raw Wjj + Wbb + Wcc',Variables['WJets'].Integral()

        elif Type.endswith('data'+chan):
            #print 'Filling ',Type
            Trees[Type].Draw(var + " >> " + histName, "(" + cut + cutbtag + ")", 'goff')
        else:
            #print 'Filling ',Type
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*(" + cut + cutbtag + ")", 'goff')
            
        if (not Type.endswith('data'+chan)):

            SF = 1.0
            if (channel == 'electron'):
                lumi = lumi_el
            if (channel == 'muon'):
                lumi = lumi_mu

            if (Type.startswith(massPoint+'_'+massPoint)): SF *= 20
            #print 'EVENTS Before Scaling FOR ',Type,' = ',Variables[Type].Integral()
            #print 'Pre Events before scaling for ',Type,' = ',VariablesPre[Type].Integral()
            #print str(SF),' ',str(lumi),' ',str(xsec_norm[Type]),' ',str(Nevents[Type])

            if Variables[Type].Integral() != 0:
                #print Type,' Lumi scaling: ',str(SF*lumi*xsec[Type]/Nevents[Type])
                Variables[Type].Scale ( SF*Yield[Type]/Variables[Type].Integral() ) 
                efficiency[Type] = Variables[Type].Integral()/Nevents[Type]
            else:
                efficiency[Type] = 0

    
    Variables[massPoint+'_ttbar'+chan].SetFillColor(ROOT.kRed-7)
    Variables[massPoint+'_s'+chan].SetFillColor(ROOT.kRed-7)
    Variables[massPoint+'_bs'+chan].SetFillColor(ROOT.kRed-7)
    Variables[massPoint+'_t'+chan].SetFillColor(ROOT.kRed-7)
    Variables[massPoint+'_bt'+chan].SetFillColor(ROOT.kRed-7)
    Variables[massPoint+'_tw'+chan].SetFillColor(ROOT.kRed-7)
    Variables[massPoint+'_btw'+chan].SetFillColor(ROOT.kRed-7)

    Variables[massPoint+'_s'+chan].SetLineColor(ROOT.kRed-7)
    Variables[massPoint+'_bs'+chan].SetLineColor(ROOT.kRed-7)
    Variables[massPoint+'_t'+chan].SetLineColor(ROOT.kRed-7)
    Variables[massPoint+'_bt'+chan].SetLineColor(ROOT.kRed-7)
    Variables[massPoint+'_tw'+chan].SetLineColor(ROOT.kRed-7)
    Variables[massPoint+'_btw'+chan].SetLineColor(ROOT.kRed-7)

    Variables[massPoint+'_wjets'+chan].SetFillColor(ROOT.kGreen-3)
    Variables[massPoint+'_zjets'+chan].SetFillColor(ROOT.kGreen-3)
    Variables[massPoint+'_ww'+chan].SetFillColor(ROOT.kGreen-3)

    Variables[massPoint+'_zjets'+chan].SetLineColor(ROOT.kGreen-3)
    Variables[massPoint+'_ww'+chan].SetLineColor(ROOT.kGreen-3)
    
    Variables[massPoint+'_ttbar'+chan].SetLineWidth(2)
    Variables[massPoint+'_wjets'+chan].SetLineWidth(2)

    Variables[massPoint+'_'+massPoint+chan].SetLineColor(1)
    Variables[massPoint+'_'+massPoint+chan].SetLineWidth(2)
    Variables[massPoint+'_'+massPoint+chan].SetLineStyle(6)

    stack = THStack('a', 'a')
    added = TH1D('a', 'a',bin,low,high)
    topadded  = TH1D('topadded', 'topadded', bin, low, high)
    wjetsadded = TH1D('wjetsadded', 'wjetsadded',bin,low,high)

    wjetsadded = Variables[massPoint+'_wjets'+chan].Clone()
    wjetsadded.Add(Variables[massPoint+'_ww'+chan])
    wjetsadded.Add(Variables[massPoint+'_zjets'+chan])

    topadded = Variables[massPoint+'_ttbar'+chan].Clone()
    topadded.Add(Variables[massPoint+'_s'+chan])
    topadded.Add(Variables[massPoint+'_bs'+chan])
    topadded.Add(Variables[massPoint+'_t'+chan])
    topadded.Add(Variables[massPoint+'_bt'+chan])
    topadded.Add(Variables[massPoint+'_tw'+chan])
    topadded.Add(Variables[massPoint+'_btw'+chan])

    wjetsadded.SetFillColor(ROOT.kGreen-3)
    wjetsadded.SetLineColor(1)
    wjetsadded.SetLineWidth(2)
    topadded.SetFillColor(ROOT.kRed-7)
    topadded.SetLineColor(1)
    topadded.SetLineWidth(2)

    stack.Add(wjetsadded)
    stack.Add(topadded)
    added.Add(wjetsadded)  
    added.Add(topadded)

    print 'Data: ',Variables[massPoint+'_data'+chan].Integral(),' Background: ',added.Integral(),' Data/Background: ',Variables[massPoint+'_data'+chan].Integral()/added.Integral()

    lumi_error = 0.022
    ttbar_error = 0.15
    wjets_error = 0.20
    other_error = 0.20

    uncert_list = []
    lumiband = added.Clone();
    
    for hbin in range(0,lumiband.GetNbinsX()+1): 

        uncert_lumi = 0 
        uncert_xsec = 0
        uncert_stat = 0
 
        for i in BkgList:

            error = 0
             
            if i in xsec.keys(): 
                if (i.startswith(massPoint+'_t') or i.startswith(massPoint+'_b') or i.startswith(massPoint+'_s')): 
                    error = ttbar_error
                    uncert_lumi += (efficiency[i]*xsec[i])**2 
                    uncert_xsec += (Variables[i].GetBinContent(hbin+1)*error)**2
                    uncert_stat += Variables[i].GetBinError(hbin+1)**2
                elif (i.startswith(massPoint+'_w') or i.startswith(massPoint+'_z')):
                    error = wjets_error
                    uncert_lumi += (efficiency[i]*xsec[i])**2 
                    uncert_xsec += (Variables[i].GetBinContent(hbin+1)*error)**2         
                    uncert_stat += Variables[i].GetBinError(hbin+1)**2

        #print 'uncert_lumi: ',uncert_lumi,' uncert_xsec ',uncert_xsec,' uncert_stat ',uncert_stat
        uncert = sqrt( (lumi_error**2)*uncert_lumi + uncert_xsec + uncert_stat )

        if lumiband.GetBinContent(hbin+1) != 0:
            dummy = 1.0
            #print lumiband.GetBinContent(hbin+1),'+/-',uncert,'(',100*uncert/lumiband.GetBinContent(hbin+1),'%)'
        lumiband.SetBinError(hbin+1,uncert);
        added.SetBinError(hbin+1,uncert);
        uncert_list . append(uncert)
    
    #gStyle.SetHatchesSpacing(2.0);
    gStyle.SetHatchesLineWidth(1);
            
    lumiband.SetFillStyle(3344);
    #lumiband.SetFillStyle(3001);
    lumiband.SetFillColor(1);
      
    legend = TLegend(.60,.70,.90,.90)
    legend . AddEntry( Variables[massPoint+'_data'+chan], 'Data' , "lp")
    legend . AddEntry( Variables[massPoint+'_ttbar'+chan], "t#bar{t} + Single-Top", "f")
    legend . AddEntry( Variables[massPoint+'_wjets'+chan], "W#rightarrowl#nu + Z/#gamma*#rightarrowl^{+}l^{-} + VV" , "f")
 
    if (massPoint.endswith('R')): coupling = 'R'
    if (massPoint.endswith('L')): coupling = 'L'
    if (massPoint.endswith('RL')): coupling = 'RL'

    massval = copy.copy(massPoint)
    massval = massval.lstrip('wp')
    massval = massval.rstrip('00'+coupling)
    if (len(massval)==1): massval = '0'+massval
    massval = massval[0]+'.'+massval[1]

    legend . AddEntry( Variables[massPoint+'_'+massPoint+chan], "W'_{"+coupling+"} x 20, m="+massval+" TeV", "l")
    legend . AddEntry( lumiband , "Uncertainty" , "f")

    c4 = TCanvas("c4","c4", 1000, 800)
    
    c4.SetBottomMargin(0.3)
    c4.SetRightMargin(0.06)
    stack.SetMaximum( 2*stack.GetMaximum() ) 
    if setLog:
        c4.SetLogy()
        stack.SetMaximum( stack.GetMaximum()  +  30*stack.GetMaximum() ) 

    stack.SetMinimum(0.1 )
    #stack.SetMarkerSize(0)
    stack.Draw("") 
    stack.GetYaxis().CenterTitle() 
    stack.GetYaxis().SetTitle(ylabel)
    stack.GetXaxis().SetLabelSize(0)
    #stack.GetXaxis().SetTitle(xlabel)
    lumiband.Draw("samee2")
    #lumiband.Draw("esame")
    
    legend.SetShadowColor(0);
    legend.SetFillColor(0);
    legend.SetLineColor(0);
    legend.Draw("same")    

    if (Variables[massPoint+'_data'+chan].GetBinContent(bin+1)>0):
        print "Overflow for ",massPoint+"_"+channel," data "
    Variables[massPoint+'_data'+chan].SetMarkerStyle(20)
    Variables[massPoint+'_data'+chan].Draw('SAMES:E1')
 
    Variables[massPoint+'_'+massPoint+chan].Draw("same")

    latex2 = TLatex()
    latex2.SetNDC()
    latex2.SetTextSize(0.04)
    latex2.SetTextAlign(31) # align right
    if channel == ('electron'): 
        latex2.DrawLatex(0.87, 0.95, "CMS Preliminary, "+lumiPlot_el+" fb^{-1} at #sqrt{s} = 8 TeV");
    if channel == ('muon'): 
        latex2.DrawLatex(0.87, 0.95, "CMS Preliminary, "+lumiPlot_mu+" fb^{-1} at #sqrt{s} = 8 TeV");

    latex3 = TLatex()
    latex3.SetNDC()
    latex3.SetTextSize(0.04)
    latex3.SetTextAlign(31) # align right

    if (channel == 'electron'):
        latex3.DrawLatex(0.47, 0.85, "e+jets " + njets);   
    if (channel == 'muon'):
        latex3.DrawLatex(0.47, 0.85, "#mu+jets " + njets);   
 
    latex4 = TLatex()
    latex4.SetNDC()
    latex4.SetTextSize(0.03)
    latex4.SetTextAlign(22) # align right
    latex4.SetTextAngle(90) # align right
    #latex4.DrawLatex(0.905, 0.56, "overflow")
    
    Pull  = TH1D('Pull', 'Pull', bin, low, high)  
    Pull = Variables[massPoint+'_data'+chan].Clone();
    Pull.Add(added,-1)
    Pull.Divide(added)

    for i in range(bin):
        i += 1
        #print i+1,' ',added.GetBinContent(i+1)
        if (Pull.GetBinContent(i+1) != 0 and Pull.GetBinError(i+1) != 0):
            Pull.SetBinContent(i+1,Pull.GetBinContent(i+1)/Pull.GetBinError(i+1))
        else: Pull.SetBinContent(i+1,0)

    pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 1.0)
    pad.SetTopMargin(0.7)
    pad.SetFillColor(0)
    pad.SetGridy(1)
    pad.SetFillStyle(0)
    pad.Draw()
    pad.cd(0)
    pad.SetRightMargin(0.06)

    Pull.SetMarkerStyle(20)
    Pull.SetMaximum(3.0 )
    Pull.SetMinimum(-3.0)
    Pull.SetFillColor(2)
    Pull.GetXaxis().SetTitle(xlabel)
    Pull.GetYaxis().SetTitleSize(0.04)
    Pull.GetYaxis().SetTitle('#sigma(Data-MC)')
    Pull.SetMarkerSize(0.7)
    Pull.GetYaxis().SetNdivisions(5);
    Pull.Draw("HIST")
    
    c4.SaveAs('Wprime_Plots/StackedHisto_' + save + '.pdf')
      
    del c4
    #del pad
    del stack
    del Variables



######################
## electron channel ##
######################
channel = 'electron'
var = 'MVA_BDT'; bin = 50; low = -0.5; high = 1.0; xaxis = "BDT Discriminant"; yaxis = 'Events / 0.03'; setLog = True; nBtags = 2; finalcuts = False;

save = 'BDT_wp1500R_el'; massPoint = 'wp1500R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp1700R_el'; massPoint = 'wp1700R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp1900R_el'; massPoint = 'wp1900R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp2100R_el'; massPoint = 'wp2100R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp2300R_el'; massPoint = 'wp2300R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)


######################
## muon channel ##
######################
channel = 'muon'
var = 'MVA_BDT'; bin = 50; low = -0.5; high = 1.0; xaxis = "BDT Discriminant"; yaxis = 'Events / 0.03'; setLog = True; nBtags = 2; finalcuts = False;

save = 'BDT_wp1500R_mu'; massPoint = 'wp1500R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp1700R_mu'; massPoint = 'wp1700R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp1900R_mu'; massPoint = 'wp1900R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp2100R_mu'; massPoint = 'wp2100R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)

save = 'BDT_wp2300R_mu'; massPoint = 'wp2300R';
plot_BDT(channel, var, massPoint, bin, low, high, yaxis, xaxis , save, nBtags, setLog, finalcuts)


