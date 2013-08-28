import ROOT, sys, os, re, string
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array
import copy
import math


#from LoadDataBDT_LPC_minKS0pt1_minimal_allnewWjets import *
#from LoadDataBDT_WnJets_1and2BTags import *
from LoadDataBDT_WnJets_QCD_1and2BTags_AllVars import *

#from comb_yields_Jun06_ScaleGenTopPt import *
from comb_yields_19Jun import *

def plot_DataVsMc(channel, varName, bin, low, high, ylabel, xlabel, save, wprime, btags):


    scaleWjetsForQCD = True

    List_DataBg = ['data','w1jets','w2jets','w3jets','w4jets','qcd80to170','qcd170to250','qcd250to350','qcd350','ww','ttbar','zjets','t','bt','tw','btw','s','bs',
       'w1jets_JESUP','w2jets_JESUP','w3jets_JESUP','w4jets_JESUP','qcd80to170_JESUP','qcd170to250_JESUP','qcd250to350_JESUP','qcd350_JESUP','ww_JESUP','ttbar_JESUP','zjets_JESUP','t_JESUP','bt_JESUP','tw_JESUP','btw_JESUP','s_JESUP','bs_JESUP',
       'w1jets_JESDOWN','w2jets_JESDOWN','w3jets_JESDOWN','w4jets_JESDOWN','qcd80to170_JESDOWN','qcd170to250_JESDOWN','qcd250to350_JESDOWN','qcd350_JESDOWN','ww_JESDOWN','ttbar_JESDOWN','zjets_JESDOWN','t_JESDOWN','bt_JESDOWN','tw_JESDOWN','btw_JESDOWN','s_JESDOWN','bs_JESDOWN',
       'w1jets_JERUP','w2jets_JERUP','w3jets_JERUP','w4jets_JERUP','qcd80to170_JERUP','qcd170to250_JERUP','qcd250to350_JERUP','qcd350_JERUP','ww_JERUP','ttbar_JERUP','zjets_JERUP','t_JERUP','bt_JERUP','tw_JERUP','btw_JERUP','s_JERUP','bs_JERUP', 
       'w1jets_JERDOWN','w2jets_JERDOWN','w3jets_JERDOWN','w4jets_JERDOWN','qcd80to170_JERDOWN','qcd170to250_JERDOWN','qcd250to350_JERDOWN','qcd350_JERDOWN','ww_JERDOWN','ttbar_JERDOWN','zjets_JERDOWN','t_JERDOWN','bt_JERDOWN','tw_JERDOWN','btw_JERDOWN','s_JERDOWN','bs_JERDOWN',
       'w1jets_BTAGUP','w2jets_BTAGUP','w3jets_BTAGUP','w4jets_BTAGUP','qcd80to170_BTAGUP','qcd170to250_BTAGUP','qcd250to350_BTAGUP','qcd350_BTAGUP','ww_BTAGUP','ttbar_BTAGUP','zjets_BTAGUP','t_BTAGUP','bt_BTAGUP','tw_BTAGUP','btw_BTAGUP','s_BTAGUP','bs_BTAGUP',
       'w1jets_BTAGDOWN','w2jets_BTAGDOWN','w3jets_BTAGDOWN','w4jets_BTAGDOWN','qcd80to170_BTAGDOWN','qcd170to250_BTAGDOWN','qcd250to350_BTAGDOWN','qcd350_BTAGDOWN','ww_BTAGDOWN','ttbar_BTAGDOWN','zjets_BTAGDOWN','t_BTAGDOWN','bt_BTAGDOWN','tw_BTAGDOWN','btw_BTAGDOWN','s_BTAGDOWN','bs_BTAGDOWN',
       #'ttbar_MATCHING_UP','ttbar_MATCHING_DOWN','ttbar_SCALE_UP','ttbar_SCALE_DOWN','wjets_MATCHING_UP','wjets_MATCHING_DOWN','wjets_SCALE_UP','wjets_SCALE_DOWN',
    ]

    List_Sig = [wprime,wprime+'_JESUP',wprime+'_JESDOWN',wprime+'_JERUP',wprime+'_JERDOWN',wprime+'_BTAGUP',wprime+'_BTAGDOWN']

    List = copy.copy(List_DataBg)
    List.extend(List_Sig)
        
    if (channel == 'electron'): ch = '_el' 
    if (channel == 'muon'): ch = '_mu' 

    RootFilesBDT = {}
    Trees = {}
    for Type in List:

        if (channel == 'muon' and Type.startswith('qcd')): continue
        print Type
        
        if btags == 'ge1btags':
            RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_GE1BTag_'+wprime+'_'+Type+ch+'.root')
            Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)
        if btags == 'onebtags':
            RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_1BTag_'+wprime+'_'+Type+ch+'.root')
            Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)
        if btags == 'twobtags':
            RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_2BTag_'+wprime+'_'+Type+ch+'.root')
            Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)

    f = TFile("RootFiles_ForBDTLimits/"+channel+"_"+save+"_"+wprime+"_Histos-"+btags+".root","RECREATE")
    f.cd()
    
    if (channel == 'electron'):      
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && elec_1_pt_WprimeCalc > 50 && abs(elec_1_eta_WprimeCalc) < 2.5 && elec_1_RelIso_WprimeCalc < 0.1 && corr_met_WprimeCalc > 20'

    if (channel == 'muon'):      
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && muon_1_pt_WprimeCalc > 50 && abs(muon_1_eta_WprimeCalc) < 2.1 && muon_1_RelIso_WprimeCalc < 0.12 && corr_met_WprimeCalc > 20'
  
  
    print varName     

    #cut = cut + ' && nSelJets_CommonCalc>=3 && BestJetJet2W_M_LjetsTopoCalcNew > 400 && BestJetJet2W_M_LjetsTopoCalcNew < 750'

    if btags == 'zerobtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==0) '
    if btags == 'onebtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==1) '
    if btags == 'ge1btags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)>=1) '
    if btags == 'twobtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==2) '
    if btags == 'ge2btags': cutbtag = ' && ( (jet_0_tag_WprimeCalc==1 && (jet_1_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) || (jet_1_tag_WprimeCalc==1 && (jet_0_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) ) '
    if btags == 'final': cutbtag = ' && ( (jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc ) >= 1 )'
    
    if btags == 'final': cut = cut + ' && BestTop_LjetsTopoCalcNew > 130 && BestTop_LjetsTopoCalcNew < 210 &&  BestTop_Pt_LjetsTopoCalcNew > 75  && Jet1Jet2_Pt_LjetsTopoCalcNew > 100 '
 
    cutwbb = ' && n_Bjets_WprimeCalc > 0' # Wb(b)
    cutwcc = ' && n_Bjets_WprimeCalc==0 && n_Cjets_WprimeCalc>0' # Wc(c)
    cutwjj = ' && n_Bjets_WprimeCalc==0 && n_Cjets_WprimeCalc==0' # W+light

    doTTbarWeight = 'True'
    if (doTTbarWeight == 'True'):
        SFWjmu = 0.82        ## myHF120lep50, scale ttbar
        SFWcmu = 1.0*1.66   ## myHF120lep50, scale ttbar
        SFWbmu = 1.0*1.21   ## myHF120lep50, scale ttbar
        
        SFWjmuPlus = 0.82*0.87        ## myHF120lep50, scale ttbar
        SFWcmuPlus = 1.0*1.66*1.15   ## myHF120lep50, scale ttbar
        SFWbmuPlus = 1.0*1.21*1.15   ## myHF120lep50, scale ttbar
        
        SFWjmuMinus = 0.82*1.13        ## myHF120lep50, scale ttbar
        SFWcmuMinus = 1.0*1.66*0.85   ## myHF120lep50, scale ttbar
        SFWbmuMinus = 1.0*1.21*0.85   ## myHF120lep50, scale ttbar
        
        weight_ttbarminus = 'weight_TopPt_WprimeCalc'
        weight_ttbarplus = '1.0'
        weight_ttbar = 'weight_TopPt_WprimeCalc'
        
    if (doTTbarWeight == 'False'):
        SFWjmu = 0.82        ## myHF120lep50
        SFWcmu = 0.93*1.66   ## myHF120lep50
        SFWbmu = 0.93*1.21   ## myHF120lep50
        
        SFWjmuPlus = 0.82*0.87        ## myHF120lep50
        SFWcmuPlus = 0.93*1.66*1.15   ## myHF120lep50
        SFWbmuPlus = 0.93*1.21*1.15   ## myHF120lep50
        
        SFWjmuMinus = 0.82*1.13        ## myHF120lep50
        SFWcmuMinus = 0.93*1.66*0.85   ## myHF120lep50
        SFWbmuMinus = 0.93*1.21*0.85   ## myHF120lep50
        
        weight_ttbarminus = '1.0'
        weight_ttbarplus = '1.0'
        weight_ttbar = '1.0'
                                                                                                                                                                                    
    cutzerobtags = ' && ( (jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc+jet_2_tag_WprimeCalc+jet_3_tag_WprimeCalc+jet_4_tag_WprimeCalc+jet_5_tag_WprimeCalc+jet_6_tag_WprimeCalc+jet_7_tag_WprimeCalc+jet_8_tag_WprimeCalc+jet_9_tag_WprimeCalc) == 0 )'

    print wprime
    #print cut + cutbtag
 
    Variables = {}
    #VariablesPUup = {}
    #VariablesPUdown = {}
    VariablesHFup = {}
    VariablesHFdown = {}
    VariablesTTbarShapeUp = {}
    VariablesTTbarShapeDown = {}
    VariablesPre = {}

    VariablesSmooth = {}
    #VariablesSmoothPUup = {}
    #VariablesSmoothPUdown = {}
    VariablesSmoothHFup = {}
    VariablesSmoothHFdown = {}
    VariablesSmoothTTbarShapeUp = {}
    VariablesSmoothTTbarShapeDown = {}
    VariablesSmoothPre = {}

    background = 0
    j = 0

    for Type in List:

        if (channel == 'muon' and Type.startswith('qcd')): continue
        
        if (channel == 'electron'):
            prefix = 'elec_BDT_' + btags + '__'
        if (channel == 'muon'):
            prefix = 'mu_BDT_' + btags + '__'

        suffix = ''
        
        if (Type=='data'): suffix = 'DATA' + Type
        if (Type=='zjets' or Type=='ww' or Type=='w1jets' or Type=='w2jets' or Type=='w3jets' or Type=='w4jets'): suffix = 'wjets'+Type
        if (Type=='t' or Type=='bt' or Type=='tw' or Type=='btw'): suffix = 'scaledntb' + Type
        if (Type=='ttbar'): suffix = 'ttbar' + Type
        if (Type=='s' or Type=='bs'): suffix = 'tb' + Type


        if (Type=='zjets_JESUP' or Type=='ww_JESUP' or Type=='w1jets_JESUP' or Type=='w2jets_JESUP' or Type=='w3jets_JESUP' or Type=='w4jets_JESUP'): suffix = 'wjets_jesUp' + Type
        if (Type=='t_JESUP' or Type=='bt_JESUP' or Type=='tw_JESUP' or Type=='btw_JESUP'): suffix = 'scaledntb_jesUp' + Type
        if (Type=='ttbar_JESUP'): suffix = 'ttbar_jesUp' + Type
        if (Type=='s_JESUP' or Type=='bs_JESUP'): suffix = 'tb_jesUp' + Type
        
        if (Type=='zjets_JESDOWN' or Type=='ww_JESDOWN' or Type=='w1jets_JESDOWN' or Type=='w2jets_JESDOWN' or Type=='w3jets_JESDOWN' or Type=='w4jets_JESDOWN'): suffix = 'wjets_jesDown' + Type
        if (Type=='t_JESDOWN' or Type=='bt_JESDOWN' or Type=='tw_JESDOWN' or Type=='btw_JESDOWN'): suffix = 'scaledntb_jesDown' + Type
        if (Type=='ttbar_JESDOWN'): suffix = 'ttbar_jesDown' + Type
        if (Type=='s_JESDOWN' or Type=='bs_JESDOWN'): suffix = 'tb_jesDown' + Type
        

        if (Type=='zjets_JERUP' or Type=='ww_JERUP' or Type=='w1jets_JERUP' or Type=='w2jets_JERUP' or Type=='w3jets_JERUP' or Type=='w4jets_JERUP'): suffix = 'wjets_jerUp' + Type
        if (Type=='t_JERUP' or Type=='bt_JERUP' or Type=='tw_JERUP' or Type=='btw_JERUP'): suffix = 'scaledntb_jerUp' + Type
        if (Type=='ttbar_JERUP'): suffix = 'ttbar_jerUp' + Type
        if (Type=='s_JERUP' or Type=='bs_JERUP'): suffix = 'tb_jerUp' + Type
        
        if (Type=='zjets_JERDOWN' or Type=='ww_JERDOWN'  or Type=='w1jets_JERDOWN' or Type=='w2jets_JERDOWN' or Type=='w3jets_JERDOWN' or Type=='w4jets_JERDOWN'): suffix = 'wjets_jerDown' + Type
        if (Type=='t_JERDOWN' or Type=='bt_JERDOWN' or Type=='tw_JERDOWN' or Type=='btw_JERDOWN'): suffix = 'scaledntb_jerDown' + Type
        if (Type=='ttbar_JERDOWN'): suffix = 'ttbar_jerDown' + Type
        if (Type=='s_JERDOWN' or Type=='bs_JERDOWN'): suffix = 'tb_jerDown' + Type
        

        if (Type=='zjets_BTAGUP' or Type=='ww_BTAGUP' or Type=='w1jets_BTAGUP' or Type=='w2jets_BTAGUP' or Type=='w3jets_BTAGUP' or Type=='w4jets_BTAGUP'): suffix = 'wjets_btagUp' + Type
        if (Type=='t_BTAGUP' or Type=='bt_BTAGUP' or Type=='tw_BTAGUP' or Type=='btw_BTAGUP'): suffix = 'scaledntb_btagUp' + Type
        if (Type=='ttbar_BTAGUP'): suffix = 'ttbar_btagUp' + Type
        if (Type=='s_BTAGUP' or Type=='bs_BTAGUP'): suffix = 'tb_btagUp' + Type
        
        if (Type=='zjets_BTAGDOWN' or Type=='ww_BTAGDOWN' or Type=='w1jets_BTAGDOWN' or Type=='w2jets_BTAGDOWN' or Type=='w3jets_BTAGDOWN' or Type=='w4jets_BTAGDOWN'): suffix = 'wjets_btagDown' + Type
        if (Type=='t_BTAGDOWN' or Type=='bt_BTAGDOWN' or Type=='tw_BTAGDOWN' or Type=='btw_BTAGDOWN'): suffix = 'scaledntb_btagDown' + Type
        if (Type=='ttbar_BTAGDOWN'): suffix = 'ttbar_btagDown' + Type
        if (Type=='s_BTAGDOWN' or Type=='bs_BTAGDOWN'): suffix = 'tb_btagDown' + Type
        

        if (Type.startswith('qcd')): suffix = 'qcd' + Type
        if (Type.startswith('qcd') and Type.endswith('JESUP')): suffix = 'qcd_jesUp' + Type
        if (Type.startswith('qcd') and Type.endswith('JESDOWN')): suffix = 'qcd_jesDown' + Type
        if (Type.startswith('qcd') and Type.endswith('JERUP')): suffix = 'qcd_jerUp' + Type
        if (Type.startswith('qcd') and Type.endswith('JERDOWN')): suffix = 'qcd_jerDown' + Type
        if (Type.startswith('qcd') and Type.endswith('BTAGUP')): suffix = 'qcd_btagUp' + Type
        if (Type.startswith('qcd') and Type.endswith('BTAGDOWN')): suffix = 'qcd_btagDown' + Type

        if (Type == 'wjets_SCALEUP'): suffix = 'wjets_q2scaleUp'
        if (Type == 'wjets_SCALEDOWN'): suffix = 'wjets_q2scaleDown'
        if (Type == 'wjets_MATCHINGUP'): suffix = 'wjets_matchingUp'
        if (Type == 'wjets_MATCHINGDOWN'): suffix = 'wjets_matchingDown'
        if (Type == 'ttbar_SCALEUP'): suffix = 'ttbar_q2scaleUp'
        if (Type == 'ttbar_SCALEDOWN'): suffix = 'ttbar_q2scaleDown'
        if (Type == 'ttbar_MATCHINGUP'): suffix = 'ttbar_matchingUp'
        if (Type == 'ttbar_MATCHINGDOWN'): suffix = 'ttbar_matchingDown'

        w_suffix = 'wp'
        
        if (Type.startswith(wprime)): suffix = wprime
        if (Type.endswith('_JESUP')): suffix += '__jes__plus'
        if (Type.endswith('_JESDOWN')): suffix += '__jes__minus'
        if (Type.endswith('_JERUP')): suffix += '__jer__plus'
        if (Type.endswith('_JERDOWN')): suffix += '__jer__minus'
        if (Type.endswith('_BTAGUP')): suffix += '__btag__plus'
        if (Type.endswith('_BTAGDOWN')): suffix += '__btag__minus'
            
        histName = prefix+suffix+'varbin'
        histNamePUup = prefix+suffix+'varbin'+'_PileupUp'
        histNamePUdown = prefix+suffix+'varbin'+'_PileupDown'
        histNameHFup = prefix+suffix+'varbin'+'_hfUp'
        histNameHFdown = prefix+suffix+'varbin'+'_hfDown'
        histNameTTbarShapeUp = prefix+suffix+'varbin'+'__ttbarshape__plus'
        histNameTTbarShapeDown = prefix+suffix+'varbin'+'__ttbarshape__minus'
        histNamePre = prefix+suffix+'varbin'+'Pre'

        histNameSmooth = prefix+suffix
        histNameSmoothPUup = prefix+suffix+'_PileupUp'
        histNameSmoothPUdown = prefix+suffix+'_PileupDown'
        histNameSmoothHFup = prefix+suffix+'_hfUp'
        histNameSmoothHFdown = prefix+suffix+'_hfDown'
        histNameSmoothTTbarShapeUp = prefix+suffix+'__ttbarshape__plus'
        histNameSmoothTTbarShapeDown = prefix+suffix+'__ttbarshape__minus'
        histNameSmoothPre = prefix+suffix+'Pre'
          
        Type = wprime+'_'+Type+ch 

        Variables[Type] = TH1D(histName, histName, bin, array('d',xlow))  
        Variables[Type].Sumw2()
        VariablesPre[Type] = TH1D(histNamePre, histNamePre, bin, array('d',xlow))  
        VariablesPre[Type].Sumw2()
        VariablesSmooth[Type] = TH1D(histNameSmooth, histNameSmooth, bin, array('d',xlow) ) 
        VariablesSmooth[Type].Sumw2()
        VariablesSmoothPre[Type] = TH1D(histNameSmoothPre, histNameSmoothPre, bin, array('d',xlow) ) 
        VariablesSmoothPre[Type].Sumw2()

        if (channel=='electron'):
            #weight = 'weight_PU_ABC_PileUpCalc*weight_ElectronEff_WprimeCalc'
            weight = '( ((0.973*weight_PU_ABCD_PileUpCalc*weight_ElectronEff_53x_WprimeCalc)*(abs(elec_1_eta_WprimeCalc)<1.5)) + ((1.02*weight_PU_ABCD_PileUpCalc*weight_ElectronEff_53x_WprimeCalc)*(abs(elec_1_eta_WprimeCalc)>1.5 && abs(elec_1_eta_WprimeCalc)<2.5)) )'
            SF = 1.0
        if (channel=='muon'):
            weight = 'weight_PU_ABCD_PileUpCalc*weight_MuonEff_WprimeCalc'
            SF = 1.0

        if (Type == wprime+'_w1jets'+ch):
            WccHist1 = TH1D('WccHist1', 'WccHist1', bin,array('d',xlow))
            WbbHist1 = TH1D('WbbHist1', 'WbbHist1', bin,array('d',xlow))
            WccHist1.Sumw2()
            WbbHist1.Sumw2()
            WccHist1HFup = TH1D('WccHist1HFup', 'WccHist1HFup', bin,array('d',xlow))
            WbbHist1HFup = TH1D('WbbHist1HFup', 'WbbHist1HFup', bin,array('d',xlow))
            WccHist1HFup.Sumw2()
            WbbHist1HFup.Sumw2()
            WccHist1HFdown = TH1D('WccHist1HFdown', 'WccHist1HFdown', bin,array('d',xlow))
            WbbHist1HFdown = TH1D('WbbHist1HFdown', 'WbbHist1HFdown', bin,array('d',xlow))
            WccHist1HFdown.Sumw2()
            WbbHist1HFdown.Sumw2()
        if (Type == wprime+'_w2jets'+ch):
            WccHist2 = TH1D('WccHist2', 'WccHist2', bin,array('d',xlow))
            WbbHist2 = TH1D('WbbHist2', 'WbbHist2', bin,array('d',xlow))
            WccHist2.Sumw2()
            WbbHist2.Sumw2()
            WccHist2HFup = TH1D('WccHist2HFup', 'WccHist2HFup', bin,array('d',xlow))
            WbbHist2HFup = TH1D('WbbHist2HFup', 'WbbHist2HFup', bin,array('d',xlow))
            WccHist2HFup.Sumw2()
            WbbHist2HFup.Sumw2()
            WccHist2HFdown = TH1D('WccHist2HFdown', 'WccHist2HFdown', bin,array('d',xlow))
            WbbHist2HFdown = TH1D('WbbHist2HFdown', 'WbbHist2HFdown', bin,array('d',xlow))
            WccHist2HFdown.Sumw2()
            WbbHist2HFdown.Sumw2()
        if (Type == wprime+'_w3jets'+ch):
            WccHist3 = TH1D('WccHist3', 'WccHist3', bin,array('d',xlow))
            WbbHist3 = TH1D('WbbHist3', 'WbbHist3', bin,array('d',xlow))
            WccHist3.Sumw2()
            WbbHist3.Sumw2()
            WccHist3HFup = TH1D('WccHist3HFup', 'WccHist3HFup', bin,array('d',xlow))
            WbbHist3HFup = TH1D('WbbHist3HFup', 'WbbHist3HFup', bin,array('d',xlow))
            WccHist3HFup.Sumw2()
            WbbHist3HFup.Sumw2()
            WccHist3HFdown = TH1D('WccHist3HFdown', 'WccHist3HFdown', bin,array('d',xlow))
            WbbHist3HFdown = TH1D('WbbHist3HFdown', 'WbbHist3HFdown', bin,array('d',xlow))
            WccHist3HFdown.Sumw2()
            WbbHist3HFdown.Sumw2()
        if (Type == wprime+'_w4jets'+ch):
            WccHist4 = TH1D('WccHist4', 'WccHist4', bin,array('d',xlow))
            WbbHist4 = TH1D('WbbHist4', 'WbbHist4', bin,array('d',xlow))
            WccHist4.Sumw2()
            WbbHist4.Sumw2()
            WccHist4HFup = TH1D('WccHist4HFup', 'WccHist4HFup', bin,array('d',xlow))
            WbbHist4HFup = TH1D('WbbHist4HFup', 'WbbHist4HFup', bin,array('d',xlow))
            WccHist4HFup.Sumw2()
            WbbHist4HFup.Sumw2()
            WccHist4HFdown = TH1D('WccHist4HFdown', 'WccHist4HFdown', bin,array('d',xlow))
            WbbHist4HFdown = TH1D('WbbHist4HFdown', 'WbbHist4HFdown', bin,array('d',xlow))
            WccHist4HFdown.Sumw2()
            WbbHist4HFdown.Sumw2()

        if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):                      
            #VariablesPUup[Type] = TH1D(histNamePUup, histNamePUup, bin, array('d',xlow))
            #VariablesPUdown[Type] = TH1D(histNamePUdown, histNamePUdown, bin, array('d',xlow))
            VariablesHFup[Type] = TH1D(histNameHFup, histNameHFup, bin, array('d',xlow))
            VariablesHFdown[Type] = TH1D(histNameHFdown, histNameHFdown, bin, array('d',xlow))
            VariablesTTbarShapeUp[Type] = TH1D(histNameTTbarShapeUp, histNameTTbarShapeUp, bin, array('d',xlow))
            VariablesTTbarShapeDown[Type] = TH1D(histNameTTbarShapeDown, histNameTTbarShapeDown, bin, array('d',xlow))
            #VariablesPUup[Type].Sumw2()
            #VariablesPUdown[Type].Sumw2()
            VariablesHFup[Type].Sumw2()
            VariablesHFdown[Type].Sumw2()
            VariablesTTbarShapeUp[Type].Sumw2()
            VariablesTTbarShapeDown[Type].Sumw2()
            #VariablesSmoothPUup[Type] = TH1D(histNameSmoothPUup, histNameSmoothPUup, bin, array('d',xlow) )
            #VariablesSmoothPUdown[Type] = TH1D(histNameSmoothPUdown, histNameSmoothPUdown, bin, array('d',xlow) )
            VariablesSmoothHFup[Type] = TH1D(histNameSmoothHFup, histNameSmoothHFup, bin, array('d',xlow) )
            VariablesSmoothHFdown[Type] = TH1D(histNameSmoothHFdown, histNameSmoothHFdown, bin, array('d',xlow) )
            VariablesSmoothTTbarShapeUp[Type] = TH1D(histNameSmoothTTbarShapeUp, histNameSmoothTTbarShapeUp, bin, array('d',xlow))
            VariablesSmoothTTbarShapeDown[Type] = TH1D(histNameSmoothTTbarShapeDown, histNameSmoothTTbarShapeDown, bin, array('d',xlow))
            #VariablesSmoothPUup[Type].Sumw2()
            #VariablesSmoothPUdown[Type].Sumw2()
            VariablesSmoothHFup[Type].Sumw2()
            VariablesSmoothHFdown[Type].Sumw2()   
            VariablesSmoothTTbarShapeUp[Type].Sumw2()
            VariablesSmoothTTbarShapeDown[Type].Sumw2()

        #print Type
        if (Type.startswith(wprime+'_data')):
            Trees[Type].Draw(var + " >> " + histName, "(" + cut + cutbtag + ")", 'goff')
        elif (Type.startswith(wprime+'_w1jets')): 
            Trees[Type].Draw(var+" >> "+histName,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WbbHist1","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WccHist1","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff') 
            Variables[Type].Add(WbbHist1)
            Variables[Type].Add(WccHist1)
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                # Pile Up 
                #Trees[Type].Draw(var+" >> "+histNamePUup,"("+weightPUup+")*("+cut+cutbtag+")",'goff')
                #Trees[Type].Draw(var+" >> "+histNamePUdown,"("+weightPUdown+")*("+cut+cutbtag+")",'goff')
                # H.F. k-factor  
                Trees[Type].Draw(var+" >> "+histNameHFup,"("+weight+")*("+str(SFWjmuPlus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist1HFup","("+weight+")*("+str(SFWbmuPlus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist1HFup","("+weight+")*("+str(SFWcmuPlus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFup[Type].Add(WbbHist1HFup)
                VariablesHFup[Type].Add(WccHist1HFup)
                Trees[Type].Draw(var+" >> "+histNameHFdown,"("+weight+")*("+str(SFWjmuMinus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist1HFdown","("+weight+")*("+str(SFWbmuMinus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist1HFdown","("+weight+")*("+str(SFWcmuMinus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFdown[Type].Add(WbbHist1HFdown)
                VariablesHFdown[Type].Add(WccHist1HFdown)
        elif (Type.startswith(wprime+'_w2jets')): 
            Trees[Type].Draw(var+" >> "+histName,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WbbHist2","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WccHist2","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff') 
            Variables[Type].Add(WbbHist2)
            Variables[Type].Add(WccHist2)
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                # Pile Up 
                #Trees[Type].Draw(var+" >> "+histNamePUup,"("+weightPUup+")*("+cut+cutbtag+")",'goff')
                #Trees[Type].Draw(var+" >> "+histNamePUdown,"("+weightPUdown+")*("+cut+cutbtag+")",'goff')
                # H.F. k-factor  
                Trees[Type].Draw(var+" >> "+histNameHFup,"("+weight+")*("+str(SFWjmuPlus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist2HFup","("+weight+")*("+str(SFWbmuPlus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist2HFup","("+weight+")*("+str(SFWcmuPlus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFup[Type].Add(WbbHist2HFup)
                VariablesHFup[Type].Add(WccHist2HFup)
                Trees[Type].Draw(var+" >> "+histNameHFdown,"("+weight+")*("+str(SFWjmuMinus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist2HFdown","("+weight+")*("+str(SFWbmuMinus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist2HFdown","("+weight+")*("+str(SFWcmuMinus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFdown[Type].Add(WbbHist2HFdown)
                VariablesHFdown[Type].Add(WccHist2HFdown)
        elif (Type.startswith(wprime+'_w3jets')): 
            Trees[Type].Draw(var+" >> "+histName,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WbbHist3","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WccHist3","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff') 
            Variables[Type].Add(WbbHist3)
            Variables[Type].Add(WccHist3)
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                # Pile Up 
                #Trees[Type].Draw(var+" >> "+histNamePUup,"("+weightPUup+")*("+cut+cutbtag+")",'goff')
                #Trees[Type].Draw(var+" >> "+histNamePUdown,"("+weightPUdown+")*("+cut+cutbtag+")",'goff')
                # H.F. k-factor  
                Trees[Type].Draw(var+" >> "+histNameHFup,"("+weight+")*("+str(SFWjmuPlus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist3HFup","("+weight+")*("+str(SFWbmuPlus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist3HFup","("+weight+")*("+str(SFWcmuPlus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFup[Type].Add(WbbHist3HFup)
                VariablesHFup[Type].Add(WccHist3HFup)
                Trees[Type].Draw(var+" >> "+histNameHFdown,"("+weight+")*("+str(SFWjmuMinus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist3HFdown","("+weight+")*("+str(SFWbmuMinus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist3HFdown","("+weight+")*("+str(SFWcmuMinus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFdown[Type].Add(WbbHist3HFdown)
                VariablesHFdown[Type].Add(WccHist3HFdown)
        elif (Type.startswith(wprime+'_w4jets')): 
            Trees[Type].Draw(var+" >> "+histName,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WbbHist4","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WccHist4","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff') 
            Variables[Type].Add(WbbHist4)
            Variables[Type].Add(WccHist4)
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                # Pile Up 
                #Trees[Type].Draw(var+" >> "+histNamePUup,"("+weightPUup+")*("+cut+cutbtag+")",'goff')
                #Trees[Type].Draw(var+" >> "+histNamePUdown,"("+weightPUdown+")*("+cut+cutbtag+")",'goff')
                # H.F. k-factor  
                Trees[Type].Draw(var+" >> "+histNameHFup,"("+weight+")*("+str(SFWjmuPlus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist4HFup","("+weight+")*("+str(SFWbmuPlus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist4HFup","("+weight+")*("+str(SFWcmuPlus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFup[Type].Add(WbbHist4HFup)
                VariablesHFup[Type].Add(WccHist4HFup)
                Trees[Type].Draw(var+" >> "+histNameHFdown,"("+weight+")*("+str(SFWjmuMinus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist4HFdown","("+weight+")*("+str(SFWbmuMinus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist4HFdown","("+weight+")*("+str(SFWcmuMinus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFdown[Type].Add(WbbHist4HFdown)
                VariablesHFdown[Type].Add(WccHist4HFdown)
        elif ( (not Type.startswith(wprime+'_t')) and (not Type.startswith(wprime+'_qcd')) ):
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*("+cut+cutbtag+")", 'goff')
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):                      
                #Trees[Type].Draw(var + " >> " + histNamePUup, "("+weightPUup+")*("+cut+cutbtag+")", 'goff')
                #Trees[Type].Draw(var + " >> " + histNamePUdown, "("+weightPUdown+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFup, "("+weight+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "("+weight+")*("+cut+cutbtag+")", 'goff')
        elif (Type.startswith(wprime+'_ttbar')):
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*("+weight_ttbar+")*("+cut+cutbtag+")", 'goff')
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):
                Trees[Type].Draw(var + " >> " + histNameHFup, "("+weight+")*("+weight_ttbar+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "("+weight+")*("+weight_ttbar+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameTTbarShapeUp, "("+weight+")*("+weight_ttbarplus+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameTTbarShapeDown, "("+weight+")*("+weight_ttbarminus+")*("+cut+cutbtag+")", 'goff')
        else:
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*("+cut+cutbtag+")", 'goff')
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):                      
                #Trees[Type].Draw(var + " >> " + histNamePUup, "("+weightPUup+")*("+cut+cutbtag+")", 'goff')
                #Trees[Type].Draw(var + " >> " + histNamePUdown, "("+weightPUdown+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFup, "("+weight+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "("+weight+")*("+cut+cutbtag+")", 'goff')

        if (not Type.startswith(wprime+'_data') and Variables[Type].Integral()!=0):
                                    
            if (channel=='electron'): lumi = lumi_el
            if (channel=='muon'): lumi = lumi_mu

            if re.match(wprime+"_w[1-4]jets", Type):
                Variables[Type].Scale(xsec[Type]/Nevents[Type])
            else:
                Variables[Type].Scale ( yields[Type+'_'+btags]/Variables[Type].Integral() ) 

            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):
                if re.match(wprime+"_w[1-4]jets", Type):
                    VariablesHFup[Type].Scale(xsec[Type]/Nevents[Type])
                    VariablesHFdown[Type].Scale(xsec[Type]/Nevents[Type])
                    VariablesTTbarShapeUp[Type].Scale(xsec[Type]/Nevents[Type])
                    VariablesTTbarShapeDown[Type].Scale(xsec[Type]/Nevents[Type])
                else:
                    #if (VariablesPUup[Type].Integral() != 0):
                    #    VariablesPUup[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                    #if (VariablesPUdown[Type].Integral() != 0): 
                    #    VariablesPUdown[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) )
                    if (VariablesHFup[Type].Integral() != 0): 
                        VariablesHFup[Type].Scale ( yieldsHFup[Type+'_'+btags]/VariablesHFup[Type].Integral() ) 
                    if (VariablesHFdown[Type].Integral() != 0):                    
                        VariablesHFdown[Type].Scale ( yieldsHFdown[Type+'_'+btags]/VariablesHFdown[Type].Integral() ) 
                    if (VariablesTTbarShapeUp[Type].Integral() != 0):                    
                        VariablesTTbarShapeUp[Type].Scale ( yieldsTTbarShapeUp[Type+'_'+btags]/VariablesTTbarShapeUp[Type].Integral() ) 
                    if (VariablesTTbarShapeDown[Type].Integral() != 0):                    
                        VariablesTTbarShapeDown[Type].Scale ( yieldsTTbarShapeDown[Type+'_'+btags]/VariablesTTbarShapeDown[Type].Integral() ) 
                    
        ############################################## 
        ### REBIN TO HAVE EVEN SIZED BINS  
        ### If VariablesSmooth* have the same binning
        ### as Varibles*, this does nothing
        ##############################################
       
        for x in range(0,bin+1):       
            VariablesSmooth[Type].SetBinContent(x,Variables[Type].GetBinContent(x) )
            VariablesSmooth[Type].SetBinError(x,Variables[Type].GetBinError(x) )
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):
                #VariablesSmoothPUup[Type].SetBinContent(x,VariablesPUup[Type].GetBinContent(x) )
                #VariablesSmoothPUup[Type].SetBinError(x,VariablesPUup[Type].GetBinError(x) )
                #VariablesSmoothPUdown[Type].SetBinContent(x,VariablesPUdown[Type].GetBinContent(x) )
                #VariablesSmoothPUdown[Type].SetBinError(x,VariablesPUdown[Type].GetBinError(x) )
                VariablesSmoothHFup[Type].SetBinContent(x,VariablesHFup[Type].GetBinContent(x)  )
                VariablesSmoothHFdown[Type].SetBinContent(x,VariablesHFdown[Type].GetBinContent(x) )
                VariablesSmoothTTbarShapeUp[Type].SetBinContent(x,VariablesTTbarShapeUp[Type].GetBinContent(x)  )
                VariablesSmoothTTbarShapeDown[Type].SetBinContent(x,VariablesTTbarShapeDown[Type].GetBinContent(x) )
                VariablesSmoothHFup[Type].SetBinError(x,VariablesHFup[Type].GetBinError(x)  )
                VariablesSmoothHFdown[Type].SetBinError(x,VariablesHFdown[Type].GetBinError(x) )
                VariablesSmoothTTbarShapeUp[Type].SetBinError(x,VariablesTTbarShapeUp[Type].GetBinError(x)  )
                VariablesSmoothTTbarShapeDown[Type].SetBinError(x,VariablesTTbarShapeDown[Type].GetBinError(x) )

        VariablesSmooth[Type].SetEntries(Variables[Type].GetEntries() )
        if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):
            #VariablesSmoothPUup[Type].SetEntries(VariablesPUup[Type].GetEntries() )
            #VariablesSmoothPUdown[Type].SetEntries(VariablesPUdown[Type].GetEntries() )
            VariablesSmoothHFup[Type].SetEntries(VariablesHFup[Type].GetEntries() )
            VariablesSmoothHFdown[Type].SetEntries(VariablesHFdown[Type].GetEntries() )
            VariablesSmoothTTbarShapeUp[Type].SetEntries(VariablesTTbarShapeUp[Type].GetEntries() )
            VariablesSmoothTTbarShapeDown[Type].SetEntries(VariablesTTbarShapeDown[Type].GetEntries() )

        if (Type.startswith(wprime+'_data')):
            print 'EVENTS FOR  Data  = ',int(VariablesSmooth[Type].Integral())
            if VariablesSmooth[Type].GetBinContent(bin+1)!=0: print 'OVERFLOW!!!!!!'
            if VariablesSmooth[Type].GetBinContent(0)!=0: print 'UNDERFLOW!!!!!!'

        ######################################### 
        ### Set 0 B.G. Bins to something !=0 
        #########################################

        if (not (Type.startswith(wprime+'_data'))):
            if ( not Type.startswith(wprime+'_'+wprime) ):
                for x in range(1,bin+1):
                    if (VariablesSmooth[Type].GetBinContent(x) < 0.000001 ): 
                        #print 'Setting ',VariablesSmooth[Type].GetBinContent(x),' to 10E-6 for bin ',x,' of ',Type
                        VariablesSmooth[Type].SetBinContent(x,0.000001)
                    if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                        #if (VariablesSmoothPUup[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothPUup[Type].SetBinContent(x,0.00001)
                        #if (VariablesSmoothPUdown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothPUdown[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothHFup[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothHFup[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothHFdown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothHFdown[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothTTbarShapeUp[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothTTbarShapeUp[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothTTbarShapeDown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothTTbarShapeDown[Type].SetBinContent(x,0.00001)

            print 'SCALED EVENTS FOR ',Type,'  = ',Variables[Type].Integral()

            if ( (not Type.startswith(wprime+'_data')) and (not Type.startswith(wprime+'_'+wprime)) and (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch))):
                background = background + Variables[Type].Integral()


    if (channel == 'electron'):
        chan = 'elec_'
        VariablesSmooth[wprime+'_data_el'].SetName(chan+"BDT_"+btags+"__DATA")
        VariablesSmooth[wprime+'_data_el'].Write()
    if (channel == 'muon'):
        chan = 'mu_'
        VariablesSmooth[wprime+'_data_mu'].SetName(chan+"BDT_"+btags+"__DATA")
        VariablesSmooth[wprime+'_data_mu'].Write()
              
    if (channel == 'electron'):
         VariablesSmooth[wprime+'_qcd80to170'+ch].Add(VariablesSmooth[wprime+'_qcd80to170'+ch])
         VariablesSmooth[wprime+'_qcd80to170'+ch].Add(VariablesSmooth[wprime+'_qcd170to250'+ch])
         VariablesSmooth[wprime+'_qcd80to170'+ch].Add(VariablesSmooth[wprime+'_qcd250to350'+ch])
         VariablesSmooth[wprime+'_qcd80to170'+ch].Add(VariablesSmooth[wprime+'_qcd350'+ch])
         VariablesSmooth[wprime+'_qcd80to170'+ch].SetName(chan+"BDT_"+btags+"__qcd")
         #VariablesSmooth[wprime+'_qcd80to170'+ch].Write()

         VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].Add(VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].Add(VariablesSmooth[wprime+'_qcd170to250_JESUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].Add(VariablesSmooth[wprime+'_qcd250to350_JESUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].Add(VariablesSmooth[wprime+'_qcd350_JESUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].SetName(chan+"BDT_"+btags+"__qcd__jes__plus")
         #VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].Write()

         VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd170to250_JESDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd250to350_JESDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd350_JESDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].SetName(chan+"BDT_"+btags+"__qcd__jes__minus")
         #VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].Write()

         VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].Add(VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].Add(VariablesSmooth[wprime+'_qcd170to250_JERUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].Add(VariablesSmooth[wprime+'_qcd250to350_JERUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].Add(VariablesSmooth[wprime+'_qcd350_JERUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].SetName(chan+"BDT_"+btags+"__qcd__jer__plus")
         #VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].Write()

         VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd170to250_JERDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd250to350_JERDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd350_JERDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].SetName(chan+"BDT_"+btags+"__qcd__jer__minus")
         #VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].Write()
         
         VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_qcd170to250_BTAGUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_qcd250to350_BTAGUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_qcd350_BTAGUP'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].SetName(chan+"BDT_"+btags+"__qcd__btag__plus")
         #VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].Write()

         VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd170to250_BTAGDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd250to350_BTAGDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_qcd350_BTAGDOWN'+ch])
         VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].SetName(chan+"BDT_"+btags+"__qcd__btag__minus")
         #VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].Write()

    VariablesSmooth[wprime+'_w1jets'+ch].Add(VariablesSmooth[wprime+'_w2jets'+ch])
    VariablesSmooth[wprime+'_w1jets'+ch].Add(VariablesSmooth[wprime+'_w3jets'+ch])
    VariablesSmooth[wprime+'_w1jets'+ch].Add(VariablesSmooth[wprime+'_w4jets'+ch])
    VariablesSmooth[wprime+'_w1jets'+ch].Scale(yields[wprime+"_wjets"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets'+ch].Integral())

    VariablesSmooth[wprime+'_ww'+ch].Add(VariablesSmooth[wprime+'_zjets'+ch])
    VariablesSmooth[wprime+'_w1jets'+ch].Add(VariablesSmooth[wprime+'_ww'+ch])
    VariablesSmooth[wprime+'_w1jets'+ch].SetName(chan+"BDT_"+btags+"__wjets")

    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170'+ch].Integral()/VariablesSmooth[wprime+'_w1jets'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets'+ch].Write()

    VariablesSmooth[wprime+'_ttbar'+ch].SetName(chan+"BDT_"+btags+"__ttbar")
    VariablesSmooth[wprime+'_t'+ch].Add(VariablesSmooth[wprime+'_bt'+ch])
    VariablesSmooth[wprime+'_t'+ch].Add(VariablesSmooth[wprime+'_tw'+ch])
    VariablesSmooth[wprime+'_t'+ch].Add(VariablesSmooth[wprime+'_btw'+ch])
    VariablesSmooth[wprime+'_ttbar'+ch].Add( VariablesSmooth[wprime+'_t'+ch])
    VariablesSmooth[wprime+'_s'+ch].Add(VariablesSmooth[wprime+'_bs'+ch]) 
    VariablesSmooth[wprime+'_ttbar'+ch].Add(VariablesSmooth[wprime+'_s'+ch])
    VariablesSmooth[wprime+'_ttbar'+ch].Write()

    print channel,' data = ', VariablesSmooth[wprime+'_data'+ch].Integral()
    if (channel == 'muon'): print 'Total background = ', VariablesSmooth[wprime+'_ttbar'+ch].Integral()+VariablesSmooth[wprime+'_w1jets'+ch].Integral()
    else: print 'Total background = ', VariablesSmooth[wprime+'_ttbar'+ch].Integral()+VariablesSmooth[wprime+'_w1jets'+ch].Integral()+VariablesSmooth[wprime+'_qcd80to170'+ch].Integral()
    print 'wjets ',VariablesSmooth[wprime+'_w1jets'+ch].Integral()
    print 'TTbar ',VariablesSmooth[wprime+'_ttbar'+ch].Integral()
    if (channel == 'electron'): 
        print 'QCD ',VariablesSmooth[wprime+'_qcd80to170'+ch].Integral()
        print 'Background / Data = ', (VariablesSmooth[wprime+'_ttbar'+ch].Integral()+VariablesSmooth[wprime+'_w1jets'+ch].Integral()+VariablesSmooth[wprime+'_qcd80to170'+ch].Integral())/VariablesSmooth[wprime+'_data'+ch].Integral()
    else: 
        print 'Background / Data = ', (VariablesSmooth[wprime+'_ttbar'+ch].Integral()+VariablesSmooth[wprime+'_w1jets'+ch].Integral())/VariablesSmooth[wprime+'_data'+ch].Integral()
                 
    ##### JES UP ##### 
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Add(VariablesSmooth[wprime+'_w2jets_JESUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Add(VariablesSmooth[wprime+'_w3jets_JESUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Add(VariablesSmooth[wprime+'_w4jets_JESUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Scale(yields[wprime+"_wjets_JESUP"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Integral())

    VariablesSmooth[wprime+'_ww_JESUP'+ch].Add(VariablesSmooth[wprime+'_zjets_JESUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Add(VariablesSmooth[wprime+'_ww_JESUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].SetName(chan+"BDT_"+btags+"__wjets__jes__plus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170_JESUP'+ch].Integral()/VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets_JESUP'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jes__plus")
    VariablesSmooth[wprime+'_t_JESUP'+ch].Add(VariablesSmooth[wprime+'_bt_JESUP'+ch])
    VariablesSmooth[wprime+'_t_JESUP'+ch].Add(VariablesSmooth[wprime+'_tw_JESUP'+ch])
    VariablesSmooth[wprime+'_t_JESUP'+ch].Add(VariablesSmooth[wprime+'_btw_JESUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].Add( VariablesSmooth[wprime+'_t_JESUP'+ch])
    VariablesSmooth[wprime+'_s_JESUP'+ch].Add(VariablesSmooth[wprime+'_bs_JESUP'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].Add(VariablesSmooth[wprime+'_s_JESUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].Write()

    ##### JES DOWN #####
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_w2jets_JESDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_w3jets_JESDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_w4jets_JESDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Scale(yields[wprime+"_wjets_JESDOWN"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Integral())

    VariablesSmooth[wprime+'_ww_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_zjets_JESDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_ww_JESDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].SetName(chan+"BDT_"+btags+"__wjets__jes__minus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170_JESDOWN'+ch].Integral()/VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets_JESDOWN'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jes__minus")
    VariablesSmooth[wprime+'_t_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_bt_JESDOWN'+ch])
    VariablesSmooth[wprime+'_t_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_tw_JESDOWN'+ch])
    VariablesSmooth[wprime+'_t_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_btw_JESDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].Add( VariablesSmooth[wprime+'_t_JESDOWN'+ch])
    VariablesSmooth[wprime+'_s_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_bs_JESDOWN'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_s_JESDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].Write()

    ##### JER UP ##### 
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Add(VariablesSmooth[wprime+'_w2jets_JERUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Add(VariablesSmooth[wprime+'_w3jets_JERUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Add(VariablesSmooth[wprime+'_w4jets_JERUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Scale(yields[wprime+"_wjets_JERUP"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Integral())

    VariablesSmooth[wprime+'_ww_JERUP'+ch].Add(VariablesSmooth[wprime+'_zjets_JERUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Add(VariablesSmooth[wprime+'_ww_JERUP'+ch])
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].SetName(chan+"BDT_"+btags+"__wjets__jer__plus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170_JERUP'+ch].Integral()/VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets_JERUP'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jer__plus")
    VariablesSmooth[wprime+'_t_JERUP'+ch].Add(VariablesSmooth[wprime+'_bt_JERUP'+ch])
    VariablesSmooth[wprime+'_t_JERUP'+ch].Add(VariablesSmooth[wprime+'_tw_JERUP'+ch])
    VariablesSmooth[wprime+'_t_JERUP'+ch].Add(VariablesSmooth[wprime+'_btw_JERUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].Add( VariablesSmooth[wprime+'_t_JERUP'+ch])
    VariablesSmooth[wprime+'_s_JERUP'+ch].Add(VariablesSmooth[wprime+'_bs_JERUP'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].Add(VariablesSmooth[wprime+'_s_JERUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].Write()

    ##### JER DOWN #####
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_w2jets_JERDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_w3jets_JERDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_w4jets_JERDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Scale(yields[wprime+"_wjets_JERDOWN"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Integral())

    VariablesSmooth[wprime+'_ww_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_zjets_JERDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_ww_JERDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].SetName(chan+"BDT_"+btags+"__wjets__jer__minus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170_JERDOWN'+ch].Integral()/VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets_JERDOWN'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jer__minus")
    VariablesSmooth[wprime+'_t_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_bt_JERDOWN'+ch])
    VariablesSmooth[wprime+'_t_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_tw_JERDOWN'+ch])
    VariablesSmooth[wprime+'_t_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_btw_JERDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].Add( VariablesSmooth[wprime+'_t_JERDOWN'+ch])
    VariablesSmooth[wprime+'_s_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_bs_JERDOWN'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_s_JERDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].Write()

    ##### BTAG UP ##### 
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_w2jets_BTAGUP'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_w3jets_BTAGUP'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_w4jets_BTAGUP'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Scale(yields[wprime+"_wjets_BTAGUP"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Integral())

    VariablesSmooth[wprime+'_ww_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_zjets_BTAGUP'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_ww_BTAGUP'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].SetName(chan+"BDT_"+btags+"__wjets__btag__plus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170_BTAGUP'+ch].Integral()/VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets_BTAGUP'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].SetName(chan+"BDT_"+btags+"__ttbar__btag__plus")
    VariablesSmooth[wprime+'_t_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_bt_BTAGUP'+ch])
    VariablesSmooth[wprime+'_t_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_tw_BTAGUP'+ch])
    VariablesSmooth[wprime+'_t_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_btw_BTAGUP'+ch])
    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].Add( VariablesSmooth[wprime+'_t_BTAGUP'+ch])
    VariablesSmooth[wprime+'_s_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_bs_BTAGUP'+ch]) 
    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_s_BTAGUP'+ch])
    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].Write()

    ##### BTAG DOWN #####
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_w2jets_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_w3jets_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_w4jets_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Scale(yields[wprime+"_wjets_BTAGDOWN"+ch+'_'+btags]/VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Integral())

    VariablesSmooth[wprime+'_ww_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_zjets_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_ww_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].SetName(chan+"BDT_"+btags+"__wjets__btag__minus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170_BTAGDOWN'+ch].Integral()/VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Integral())
    VariablesSmooth[wprime+'_w1jets_BTAGDOWN'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_BTAGDOWN'+ch].SetName(chan+"BDT_"+btags+"__ttbar__btag__minus")
    VariablesSmooth[wprime+'_t_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_bt_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_t_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_tw_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_t_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_btw_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_BTAGDOWN'+ch].Add( VariablesSmooth[wprime+'_t_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_s_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_bs_BTAGDOWN'+ch]) 
    VariablesSmooth[wprime+'_ttbar_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_s_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_BTAGDOWN'+ch].Write()

    
    '''
    ##### PU Down ######
    VariablesSmoothPUdown['ww'].Add(VariablesSmoothPUdown['zjets'])
    VariablesSmoothPUdown['wjets'].Add(VariablesSmoothPUdown['ww'])
    VariablesSmoothPUdown['wjets'].SetName(chan+"BDT_"+btags+"__wjets_PileupDown")
    VariablesSmoothPUdown['wjets'].Write()

    VariablesSmoothPUdown['t'].Add(VariablesSmoothPUdown['bt'])
    VariablesSmoothPUdown['t'].Add(VariablesSmoothPUdown['tw'])
    VariablesSmoothPUdown['t'].Add(VariablesSmoothPUdown['btw'])
    VariablesSmoothPUdown['TTbar'].Add( VariablesSmoothPUdown['t'])
    VariablesSmoothPUdown['TTbar'].SetName(chan+"BDT_"+btags+"__ttbar_PileupDown")

    VariablesSmoothPUdown['s'].Add(VariablesSmoothPUdown['bs']) 

    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmoothPUdown['TTbar'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmoothPUdown['TTbar'].Write()
            VariablesSmoothPUdown['s'].SetName(chan+"BDT_"+btags+"__topstb_PileupDown")
            VariablesSmoothPUdown['s'].Write()
        elif (wprime == 'Right'):
            VariablesSmoothPUdown['TTbar'].Add(VariablesSmoothPUdown['s'])
            VariablesSmoothPUdown['TTbar'].Write()
  

    ##### PU Up#####
    VariablesSmoothPUup['ww'].Add(VariablesSmoothPUup['zjets'])
    VariablesSmoothPUup['wjets'].Add(VariablesSmoothPUup['ww'])
    VariablesSmoothPUup['wjets'].SetName(chan+"BDT_"+btags+"__wjets_PileupUp")
    VariablesSmoothPUup['wjets'].Write()

    VariablesSmoothPUup['t'].Add(VariablesSmoothPUup['bt'])
    VariablesSmoothPUup['t'].Add(VariablesSmoothPUup['tw'])
    VariablesSmoothPUup['t'].Add(VariablesSmoothPUup['btw'])
    VariablesSmoothPUup['TTbar'].Add( VariablesSmoothPUup['t'])
    VariablesSmoothPUup['TTbar'].SetName(chan+"BDT_"+btags+"__ttbar_PileupUp")

    VariablesSmoothPUup['s'].Add(VariablesSmoothPUup['bs']) 

    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmoothPUup['TTbar'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmoothPUup['TTbar'].Write()
            VariablesSmoothPUup['s'].SetName(chan+"BDT_"+btags+"__topstb_PileupUp")
            VariablesSmoothPUup['s'].Write()
        elif (wprime == 'Right'):
            VariablesSmoothPUup['TTbar'].Add(VariablesSmoothPUup['s'])
            VariablesSmoothPUup['TTbar'].Write()
    '''

    VariablesSmooth[wprime+'_'+wprime+ch].Write()
    VariablesSmooth[wprime+'_'+wprime+'_JESUP'+ch].Write()
    VariablesSmooth[wprime+'_'+wprime+'_JESDOWN'+ch].Write()
    VariablesSmooth[wprime+'_'+wprime+'_JERUP'+ch].Write()
    VariablesSmooth[wprime+'_'+wprime+'_JERDOWN'+ch].Write()
    VariablesSmooth[wprime+'_'+wprime+'_BTAGUP'+ch].Write()
    VariablesSmooth[wprime+'_'+wprime+'_BTAGDOWN'+ch].Write()
    #VariablesSmoothPUup[wprime+'_'+wprime+ch].Write()    
    #VariablesSmoothPUdown[wprime+'_'+wprime+ch].Write()
 
 
    '''
    VariablesSmooth[wprime+'_ttbar_MATCHING_DOWN'].Add(VariablesSmooth[wprime+'_t'])
    VariablesSmooth[wprime+'_ttbar_MATCHING_DOWN'].SetName(chan+"BDT_"+btags+"__ttbar__matching__minus")
    if (wprime == 'Left' or wprime == 'MixRL'):
        VariablesSmooth[wprime+'_ttbar_MATCHING_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth[wprime+'_ttbar_MATCHING_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth[wprime+'_ttbar_MATCHING_DOWN'].Add(VariablesSmooth[wprime+'_s'])
            VariablesSmooth[wprime+'_ttbar_MATCHING_DOWN'].Write()

    VariablesSmooth[wprime+'_ttbar_MATCHING_UP'].Add(VariablesSmooth[wprime+'_t'])
    VariablesSmooth[wprime+'_ttbar_MATCHING_UP'].SetName(chan+"BDT_"+btags+"__ttbar__matching__plus")
    if (wprime == 'Left' or wprime == 'MixRL'):
        VariablesSmooth[wprime+'_ttbar_MATCHING_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth[wprime+'_ttbar_MATCHING_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth[wprime+'_ttbar_MATCHING_UP'].Add(VariablesSmooth[wprime+'_s'])
            VariablesSmooth[wprime+'_ttbar_MATCHING_UP'].Write()

    VariablesSmooth[wprime+'_ttbar_SCALE_DOWN'].Add(VariablesSmooth[wprime+'_t'])
    VariablesSmooth[wprime+'_ttbar_SCALE_DOWN'].SetName(chan+"BDT_"+btags+"__ttbar__q2scale__minus")
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth[wprime+'_ttbar_SCALE_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth[wprime+'_ttbar_SCALE_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth[wprime+'_ttbar_SCALE_DOWN'].Add(VariablesSmooth[wprime+'_s'])
            VariablesSmooth[wprime+'_ttbar_SCALE_DOWN'].Write()

    VariablesSmooth[wprime+'_ttbar_SCALE_UP'].Add(VariablesSmooth[wprime+'_t'])
    VariablesSmooth[wprime+'_ttbar_SCALE_UP'].SetName(chan+"BDT_"+btags+"__ttbar__q2scale__plus")
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth[wprime+'_ttbar_SCALE_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth[wprime+'_ttbar_SCALE_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth[wprime+'_ttbar_SCALE_UP'].Add(VariablesSmooth[wprime+'_s'])
            VariablesSmooth[wprime+'_ttbar_SCALE_UP'].Write()

    VariablesSmooth[wprime+'_wjets_MATCHING_DOWN'].Add(VariablesSmooth[wprime+'_ww'])
    VariablesSmooth[wprime+'_wjets_MATCHING_DOWN'].SetName(chan+"BDT_"+btags+"__wjets__matching__minus")
    VariablesSmooth[wprime+'_wjets_MATCHING_DOWN'].Write()

    VariablesSmooth[wprime+'_wjets_MATCHING_UP'].Add(VariablesSmooth[wprime+'_ww'])
    VariablesSmooth[wprime+'_wjets_MATCHING_UP'].SetName(chan+"BDT_"+btags+"__wjets__matching__plus")
    VariablesSmooth[wprime+'_wjets_MATCHING_UP'].Write()

    VariablesSmooth[wprime+'_wjets_SCALE_DOWN'].Add(VariablesSmooth[wprime+'_ww'])
    VariablesSmooth[wprime+'_wjets_SCALE_DOWN'].SetName(chan+"BDT_"+btags+"__wjets__q2scale__minus")
    VariablesSmooth[wprime+'_wjets_SCALE_DOWN'].Write()

    VariablesSmooth[wprime+'_wjets_SCALE_UP'].Add(VariablesSmooth[wprime+'_ww'])
    VariablesSmooth[wprime+'_wjets_SCALE_UP'].SetName(chan+"BDT_"+btags+"__wjets__q2scale__plus")
    VariablesSmooth[wprime+'_wjets_SCALE_UP'].Write()
    '''

    VariablesSmoothHFup[wprime+'_w1jets'+ch].Add(VariablesSmoothHFup[wprime+'_w2jets'+ch])
    VariablesSmoothHFup[wprime+'_w1jets'+ch].Add(VariablesSmoothHFup[wprime+'_w3jets'+ch])
    VariablesSmoothHFup[wprime+'_w1jets'+ch].Add(VariablesSmoothHFup[wprime+'_w4jets'+ch])
    VariablesSmoothHFup[wprime+'_w1jets'+ch].Scale(yieldsHFup[wprime+"_wjets"+ch+'_'+btags]/VariablesSmoothHFup[wprime+'_w1jets'+ch].Integral())
    VariablesSmoothHFup[wprime+'_ww'+ch].Add(VariablesSmoothHFup[wprime+'_zjets'+ch])
    VariablesSmoothHFup[wprime+'_w1jets'+ch].Add(VariablesSmoothHFup[wprime+'_ww'+ch])
    VariablesSmoothHFup[wprime+'_w1jets'+ch].SetName(chan+"BDT_"+btags+"__wjets__hf__plus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmoothHFup[wprime+'_w1jets'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170'+ch].Integral()/VariablesSmoothHFup[wprime+'_w1jets'+ch].Integral())
    VariablesSmoothHFup[wprime+'_w1jets'+ch].Write()

    VariablesSmoothHFdown[wprime+'_w1jets'+ch].Add(VariablesSmoothHFdown[wprime+'_w2jets'+ch])
    VariablesSmoothHFdown[wprime+'_w1jets'+ch].Add(VariablesSmoothHFdown[wprime+'_w3jets'+ch])
    VariablesSmoothHFdown[wprime+'_w1jets'+ch].Add(VariablesSmoothHFdown[wprime+'_w4jets'+ch])
    VariablesSmoothHFdown[wprime+'_w1jets'+ch].Scale(yieldsHFdown[wprime+"_wjets"+ch+'_'+btags]/VariablesSmoothHFdown[wprime+'_w1jets'+ch].Integral())
    VariablesSmoothHFdown[wprime+'_ww'+ch].Add(VariablesSmoothHFdown[wprime+'_zjets'+ch])
    VariablesSmoothHFdown[wprime+'_w1jets'+ch].Add(VariablesSmoothHFdown[wprime+'_ww'+ch])
    VariablesSmoothHFdown[wprime+'_w1jets'+ch].SetName(chan+"BDT_"+btags+"__wjets__hf__minus")
    if (scaleWjetsForQCD and ch=='_el'): VariablesSmoothHFdown[wprime+'_w1jets'+ch].Scale( 1+VariablesSmooth[wprime+'_qcd80to170'+ch].Integral()/VariablesSmoothHFdown[wprime+'_w1jets'+ch].Integral())
    VariablesSmoothHFdown[wprime+'_w1jets'+ch].Write()

    VariablesSmoothTTbarShapeUp[wprime+'_ttbar'+ch].Add(VariablesSmooth[wprime+'_t'+ch])
    VariablesSmoothTTbarShapeUp[wprime+'_ttbar'+ch].SetName(chan+"BDT_"+btags+"__ttbar__shape__plus")
    VariablesSmoothTTbarShapeUp[wprime+'_ttbar'+ch].SetTitle(chan+"BDT_"+btags+"__ttbar__shape__plus")
    VariablesSmoothTTbarShapeDown[wprime+'_ttbar'+ch].Add(VariablesSmooth[wprime+'_t'+ch])
    VariablesSmoothTTbarShapeDown[wprime+'_ttbar'+ch].SetName(chan+"BDT_"+btags+"__ttbar__shape__minus")
    VariablesSmoothTTbarShapeDown[wprime+'_ttbar'+ch].SetTitle(chan+"BDT_"+btags+"__ttbar__shape__minus")
    VariablesSmoothTTbarShapeUp[wprime+'_ttbar'+ch].Write()
    VariablesSmoothTTbarShapeDown[wprime+'_ttbar'+ch].Write()

    del Variables
    del VariablesSmooth
    del VariablesSmoothHFup
    del VariablesSmoothHFdown
    del VariablesSmoothTTbarShapeUp
    del VariablesSmoothTTbarShapeDown
    del RootFilesBDT
    del Trees
  
#wprime = 'Right'
var = 'MVA_BDT'; high = 1.0; xaxis = "BDT Discriminant"; yaxis = 'Events'; save = 'BDT'

'''
#### minimal list, WnJets, QCD, separate 1and2 btag training 

# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.9,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
'''
# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.85,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT muon 
channel = 'muon' 
btags = 'onebtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.8,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT electron 
channel = 'electron' 
btags = 'twobtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp800R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1000R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1200R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1200R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1400R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1400R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1600R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1600R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp1800R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp1800R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2000R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2000R' 
xlow = [-1.0,-0.75,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2200R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2200R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.75,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2400R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2400R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2600R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2600R' 
xlow = [-1.0,-0.7,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp2800R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp2800R' 
xlow = [-1.0,-0.65,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

# wp3000R MVA_BDT muon 
channel = 'muon' 
btags = 'twobtags' 
wprime = 'wp3000R' 
xlow = [-1.0,-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.7,1.0] 
bins = len(xlow)-1 
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

