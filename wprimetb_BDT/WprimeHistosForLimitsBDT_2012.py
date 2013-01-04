import ROOT, sys, os, re, string
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array
import copy
import math

#from LoadData import *
from LoadDataBDT_LPC import *



def plot_DataVsMc(channel, varName, bin, low, high, ylabel, xlabel, save, wprime, btags):

    List_DataBg = ['data','wjets','ww','ttbar','zjets','t','bt','tw','btw','s','bs',
       'wjets_JESUP','ww_JESUP','ttbar_JESUP','zjets_JESUP','t_JESUP','bt_JESUP','tw_JESUP','btw_JESUP','s_JESUP','bs_JESUP',
       'wjets_JESDOWN','ww_JESDOWN','ttbar_JESDOWN','zjets_JESDOWN','t_JESDOWN','bt_JESDOWN','tw_JESDOWN','btw_JESDOWN','s_JESDOWN','bs_JESDOWN',
       'wjets_JERUP','ww_JERUP','ttbar_JERUP','zjets_JERUP','t_JERUP','bt_JERUP','tw_JERUP','btw_JERUP','s_JERUP','bs_JERUP', 
       'wjets_JERDOWN','ww_JERDOWN','ttbar_JERDOWN','zjets_JERDOWN','t_JERDOWN','bt_JERDOWN','tw_JERDOWN','btw_JERDOWN','s_JERDOWN','bs_JERDOWN',
       'wjets_BTAGUP','ww_BTAGUP','ttbar_BTAGUP','zjets_BTAGUP','t_BTAGUP','bt_BTAGUP','tw_BTAGUP','btw_BTAGUP','s_BTAGUP','bs_BTAGUP',
       'wjets_BTAGDOWN','ww_BTAGDOWN','ttbar_BTAGDOWN','zjets_BTAGDOWN','t_BTAGDOWN','bt_BTAGDOWN','tw_BTAGDOWN','btw_BTAGDOWN','s_BTAGDOWN','bs_BTAGDOWN',
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
        RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_GE1BTag_'+wprime+'_'+Type+ch+'.root')
        Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)

    f = TFile("RootFiles_ForBDTLimits/"+channel+"_"+save+"_"+wprime+"_Histos-"+btags+".root","RECREATE")
    f.cd()
    
    if (channel == 'electron'):      
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && elec_1_pt_WprimeCalc > 32 && abs(elec_1_eta_WprimeCalc) < 2.5 && elec_1_RelIso_WprimeCalc < 0.1 && corr_met_WprimeCalc > 20' 

    if (channel == 'muon'):      
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && muon_1_pt_WprimeCalc > 26 && abs(muon_1_eta_WprimeCalc) < 2.1 && muon_1_RelIso_WprimeCalc < 0.12 && corr_met_WprimeCalc > 20'
  
  
    print varName     

    if btags == 'zerobtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==0) '
    if btags == 'onebtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==1) '
    if btags == 'ge1btags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)>=1) '
    if btags == 'ge2btags': cutbtag = ' && ( (jet_0_tag_WprimeCalc==1 && (jet_1_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) || (jet_1_tag_WprimeCalc==1 && (jet_0_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) ) '
    if btags == 'final': cutbtag = ' && ( (jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc ) >= 1 )'
    
    if btags == 'final': cut = cut + ' && BestTop_LjetsTopoCalcNew > 130 && BestTop_LjetsTopoCalcNew < 210 &&  BestTop_Pt_LjetsTopoCalcNew > 75  && Jet1Jet2_Pt_LjetsTopoCalcNew > 100 '
 
    cutwbb = ' && n_Bjets_WprimeCalc > 0' # Wb(b)
    cutwcc = ' && n_Bjets_WprimeCalc==0 && n_Cjets_WprimeCalc>0' # Wc(c)
    cutwjj = ' && n_Bjets_WprimeCalc==0 && n_Cjets_WprimeCalc==0' # W+light

    SFWjmu = 1.08*0.85      ## myHF120
    SFWcmu = 1.06*0.92*1.66  ## myHF120
    SFWbmu = 1.06*0.92*1.21  ## myHF120

    SFWjmuPlus = 1.08*0.85*0.8
    SFWcmuPlus = 1.06*0.92*1.66*1.27
    SFWbmuPlus = 1.06*0.92*1.21*1.27

    SFWjmuMinus = 1.08*0.85*1.2
    SFWcmuMinus = 1.06*0.92*1.66*0.73
    SFWbmuMinus = 1.06*0.92*1.21*0.73
                       
    cutzerobtags = ' && ( (jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc+jet_2_tag_WprimeCalc+jet_3_tag_WprimeCalc+jet_4_tag_WprimeCalc+jet_5_tag_WprimeCalc+jet_6_tag_WprimeCalc+jet_7_tag_WprimeCalc+jet_8_tag_WprimeCalc+jet_9_tag_WprimeCalc) == 0 )'

    print wprime
    #print cut + cutbtag
 
    Variables = {}
    #VariablesPUup = {}
    #VariablesPUdown = {}
    VariablesHFup = {}
    VariablesHFdown = {}
    VariablesPre = {}

    VariablesSmooth = {}
    #VariablesSmoothPUup = {}
    #VariablesSmoothPUdown = {}
    VariablesSmoothHFup = {}
    VariablesSmoothHFdown = {}
    VariablesSmoothPre = {}

    background = 0
    j = 0

    nominalwprime = 'False'

    for Type in List:

        if (channel == 'electron'):
            prefix = 'elec_BDT_' + btags + '__'
        if (channel == 'muon'):
            prefix = 'mu_BDT_' + btags + '__'

        suffix = ''
        
        if (Type=='data'): suffix = 'DATA' + Type
        if (Type=='wjets'): suffix = 'wjets' + Type
        if (Type=='ww'): suffix = 'scaledntb' + Type
        if (Type=='zjets' or Type=='ww' or Type=='t' or Type=='bt' or Type=='tw' or Type=='btw'): suffix = 'scaledntb' + Type
        if (Type=='ttbar'): suffix = 'ttbar' + Type
        if (Type=='s' or Type=='bs'): suffix = 'tb' + Type

        if (Type== 'wjets_JESUP'): suffix = 'wjets_jesUp' + Type
        if (Type=='ttbar_JESUP' or Type=='ww_JESUP' or Type=='zjets_JESUP' or Type=='t_JESUP' or Type=='bt_JESUP' or Type=='tw_JESUP' or Type=='btw_JESUP'): suffix = 'scaledntb_jesUp' + Type
        if (Type=='ttbar_JESUP'): suffix = 'scaledall_jesUp' + Type
        if (Type=='s_JESUP' or Type=='bs_JESUP'): suffix = 'tb_jesUp' + Type

        if (Type== 'wjets_JESDOWN'): suffix = 'wjets_jesDown' + Type
        if (Type=='ttbar_JESDOWN' or Type=='ww_JESDOWN' or Type=='zjets_JESDOWN' or Type=='t_JESDOWN' or Type=='bt_JESDOWN' or Type=='tw_JESDOWN' or Type=='btw_JESDOWN'): suffix = 'scaledntb_jesDown' + Type
        if (Type=='ttbar_JESDOWN'): suffix = 'scaledall_jesDown' + Type
        if (Type=='s_JESDOWN' or Type=='bs_JESDOWN'): suffix = 'tb_jesDown' + Type

        if (Type== 'wjets_JERUP'): suffix = 'wjets_jerUp' + Type
        if (Type=='ttbar_JERUP' or Type=='ww_JERUP' or Type=='zjets_JERUP' or Type=='t_JERUP' or Type=='bt_JERUP' or Type=='tw_JERUP' or Type=='btw_JERUP'): suffix = 'scaledntb_jerUp' + Type
        if (Type=='ttbar_JERUP'): suffix = 'scaledall_jerUp' + Type
        if (Type=='s_JERUP' or Type=='bs_JERUP'): suffix = 'tb_jerUp' + Type

        if (Type== 'wjets_JERDOWN'): suffix = 'wjets_jerDown' + Type
        if (Type=='ttbar_JERDOWN' or Type=='ww_JERDOWN' or Type=='zjets_JERDOWN' or Type=='t_JERDOWN' or Type=='bt_JERDOWN' or Type=='tw_JERDOWN' or Type=='btw_JERDOWN'): suffix = 'scaledntb_jerDown' + Type
        if (Type=='ttbar_JERDOWN'): suffix = 'scaledall_jerDown' + Type
        if (Type=='s_JERDOWN' or Type=='bs_JERDOWN'): suffix = 'tb_jerDown' + Type

        if (Type== 'wjets_BTAGUP'): suffix = 'wjets_btagUp' + Type
        if (Type=='ttbar_BTAGUP' or Type=='ww_BTAGUP' or Type=='zjets_BTAGUP' or Type=='t_BTAGUP' or Type=='bt_BTAGUP' or Type=='tw_BTAGUP' or Type=='btw_BTAGUP'): suffix = 'scaledntb_btagUp' + Type
        if (Type=='ttbar_BTAGUP'): suffix = 'scaledall_btagUp' + Type
        if (Type=='s_BTAGUP' or Type=='bs_BTAGUP'): suffix = 'tb_btagUp' + Type

        if (Type== 'wjets_BTAGDOWN'): suffix = 'wjets_btagDown' + Type
        if (Type=='ttbar_BTAGDOWN' or Type=='ww_BTAGDOWN' or Type=='zjets_BTAGDOWN' or Type=='t_BTAGDOWN' or Type=='bt_BTAGDOWN' or Type=='tw_BTAGDOWN' or Type=='btw_BTAGDOWN'): suffix = 'scaledntb_btagDown' + Type
        if (Type=='ttbar_BTAGDOWN'): suffix = 'scaledall_btagDown' + Type
        if (Type=='s_BTAGDOWN' or Type=='bs_BTAGDOWN'): suffix = 'tb_btagDown' + Type


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
        histNamePre = prefix+suffix+'varbin'+'Pre'

        histNameSmooth = prefix+suffix
        histNameSmoothPUup = prefix+suffix+'_PileupUp'
        histNameSmoothPUdown = prefix+suffix+'_PileupDown'
        histNameSmoothHFup = prefix+suffix+'_hfUp'
        histNameSmoothHFdown = prefix+suffix+'_hfDown'
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
            weight = 'weight_PU_ABC_PileUpCalc*weight_ElectronEff_WprimeCalc'
            SF = 0.977
        if (channel=='muon'):
            weight = 'weight_PU_ABC_PileUpCalc*weight_MuonEff_WprimeCalc'
            SF = 1.0

        if (Type == wprime+'_'+'wjets'+ch):
            WccHist = TH1D('WccHist', 'WccHist', bin,array('d',xlow))
            WbbHist = TH1D('WbbHist', 'WbbHist', bin,array('d',xlow))
            WccHist.Sumw2()
            WbbHist.Sumw2()
            WccHistHFup = TH1D('WccHistHFup', 'WccHistHFup', bin,array('d',xlow))
            WbbHistHFup = TH1D('WbbHistHFup', 'WbbHistHFup', bin,array('d',xlow))
            WccHistHFup.Sumw2()
            WbbHistHFup.Sumw2()
            WccHistHFdown = TH1D('WccHistHFdown', 'WccHistHFdown', bin,array('d',xlow))
            WbbHistHFdown = TH1D('WbbHistHFdown', 'WbbHistHFdown', bin,array('d',xlow))
            WccHistHFdown.Sumw2()
            WbbHistHFdown.Sumw2()

        if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):                      
            #VariablesPUup[Type] = TH1D(histNamePUup, histNamePUup, bin, array('d',xlow))
            #VariablesPUdown[Type] = TH1D(histNamePUdown, histNamePUdown, bin, array('d',xlow))
            VariablesHFup[Type] = TH1D(histNameHFup, histNameHFup, bin, array('d',xlow))
            VariablesHFdown[Type] = TH1D(histNameHFdown, histNameHFdown, bin, array('d',xlow))
            #VariablesPUup[Type].Sumw2()
            #VariablesPUdown[Type].Sumw2()
            VariablesHFup[Type].Sumw2()
            VariablesHFdown[Type].Sumw2()
            #VariablesSmoothPUup[Type] = TH1D(histNameSmoothPUup, histNameSmoothPUup, bin, array('d',xlow) )
            #VariablesSmoothPUdown[Type] = TH1D(histNameSmoothPUdown, histNameSmoothPUdown, bin, array('d',xlow) )
            VariablesSmoothHFup[Type] = TH1D(histNameSmoothHFup, histNameSmoothHFup, bin, array('d',xlow) )
            VariablesSmoothHFdown[Type] = TH1D(histNameSmoothHFdown, histNameSmoothHFdown, bin, array('d',xlow) )
            #VariablesSmoothPUup[Type].Sumw2()
            #VariablesSmoothPUdown[Type].Sumw2()
            VariablesSmoothHFup[Type].Sumw2()
            VariablesSmoothHFdown[Type].Sumw2()   

        #print Type
        if (Type.startswith(wprime+'_data')):
            Trees[Type].Draw(var + " >> " + histName, "(" + cut + cutbtag + ")", 'goff')
        elif (Type.startswith(wprime+'_wjets')): # Here we go...

            ############################################
            ############################################
            Trees[Type].Draw(var+" >> "+histName,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WbbHist","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
            Trees[Type].Draw(var+" >> "+"WccHist","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff') 
            Variables[Type].Add(WbbHist)
            Variables[Type].Add(WccHist)

            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                # Pile Up 
                #Trees[Type].Draw(var+" >> "+histNamePUup,"("+weightPUup+")*("+cut+cutbtag+")",'goff')
                #Trees[Type].Draw(var+" >> "+histNamePUdown,"("+weightPUdown+")*("+cut+cutbtag+")",'goff')
                # H.F. k-factor  
                Trees[Type].Draw(var+" >> "+histNameHFup,"("+weight+")*("+str(SFWjmuPlus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHistHFup","("+weight+")*("+str(SFWbmuPlus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHistHFup","("+weight+")*("+str(SFWcmuPlus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFup[Type].Add(WbbHistHFup)
                VariablesHFup[Type].Add(WccHistHFup)
                Trees[Type].Draw(var+" >> "+histNameHFdown,"("+weight+")*("+str(SFWjmuMinus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHistHFdown","("+weight+")*("+str(SFWbmuMinus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHistHFdown","("+weight+")*("+str(SFWcmuMinus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFdown[Type].Add(WbbHistHFdown)
                VariablesHFdown[Type].Add(WccHistHFdown)
        elif (not Type.startswith(wprime+'_t')):
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*("+cut+cutbtag+")", 'goff')
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):                      
                #Trees[Type].Draw(var + " >> " + histNamePUup, "("+weightPUup+")*("+cut+cutbtag+")", 'goff')
                #Trees[Type].Draw(var + " >> " + histNamePUdown, "("+weightPUdown+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFup, "("+weight+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "("+weight+")*("+cut+cutbtag+")", 'goff')
        else:
            #print 'cut = ',cut+cutbtag
            Trees[Type].Draw(var + " >> " + histName, "("+weight+")*("+cut+cutbtag+")", 'goff')
            if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):                      
                #Trees[Type].Draw(var + " >> " + histNamePUup, "("+weightPUup+")*("+cut+cutbtag+")", 'goff')
                #Trees[Type].Draw(var + " >> " + histNamePUdown, "("+weightPUdown+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFup, "("+weight+")*("+cut+cutbtag+")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "("+weight+")*("+cut+cutbtag+")", 'goff')

        if (not Type.startswith(wprime+'_data')):
            #print 'EVENTS Before Scaling FOR ',Type,' = ',Variables[Type].Integral()
            #print 'Pre Events before scaling for ',Type,' = ',VariablesPre[Type].Integral()
            #print str(SF),' ',str(lumi),' ',str(xsec_norm[Type]),' ',str(Nevents[Type])
                                    
            if (channel=='electron'): lumi = lumi_el
            if (channel=='muon'): lumi = lumi_mu

            if (Type == (wprime+'_'+wprime+ch)):
                splitfraction = 2.
            elif ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):
                splitfraction = 2.
            else:
                splitfraction = 2.
   
            if Variables[Type].Integral() != 0:
                Variables[Type].Scale ( (SF*lumi*splitfraction*xsec_norm[Type]/Nevents[Type]) ) 
                if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                    #VariablesPUup[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                    #VariablesPUdown[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) )
                    VariablesHFup[Type].Scale ( (SF*lumi*splitfraction*xsec_norm[Type]/Nevents[Type]) ) 
                    VariablesHFdown[Type].Scale ( (SF*lumi*splitfraction*xsec_norm[Type]/Nevents[Type]) )

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
                VariablesSmoothHFup[Type].SetBinError(x,VariablesHFup[Type].GetBinError(x)  )
                VariablesSmoothHFdown[Type].SetBinError(x,VariablesHFdown[Type].GetBinError(x) )
        VariablesSmooth[Type].SetEntries(Variables[Type].GetEntries() )
        if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ):
            #VariablesSmoothPUup[Type].SetEntries(VariablesPUup[Type].GetEntries() )
            #VariablesSmoothPUdown[Type].SetEntries(VariablesPUdown[Type].GetEntries() )
            VariablesSmoothHFup[Type].SetEntries(VariablesHFup[Type].GetEntries() )
            VariablesSmoothHFdown[Type].SetEntries(VariablesHFdown[Type].GetEntries() )

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
                        print 'Setting ',VariablesSmooth[Type].GetBinContent(x),' to 10E-6 for bin ',x,' of ',Type
                        VariablesSmooth[Type].SetBinContent(x,0.000001)
                    if ( (not Type.endswith('UP'+ch)) and (not Type.endswith('DOWN'+ch)) ): 
                        #if (VariablesSmoothPUup[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothPUup[Type].SetBinContent(x,0.00001)
                        #if (VariablesSmoothPUdown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothPUdown[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothHFup[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothHFup[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothHFdown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothHFdown[Type].SetBinContent(x,0.00001)

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

    VariablesSmooth[wprime+'_ww'+ch].Add(VariablesSmooth[wprime+'_zjets'+ch])
    VariablesSmooth[wprime+'_wjets'+ch].Add(VariablesSmooth[wprime+'_ww'+ch])

    VariablesSmooth[wprime+'_wjets'+ch].SetName(chan+"BDT_"+btags+"__wjets")
    VariablesSmooth[wprime+'_wjets'+ch].Write()

    VariablesSmooth[wprime+'_ttbar'+ch].SetName(chan+"BDT_"+btags+"__ttbar")
    VariablesSmooth[wprime+'_t'+ch].Add(VariablesSmooth[wprime+'_bt'+ch])
    VariablesSmooth[wprime+'_t'+ch].Add(VariablesSmooth[wprime+'_tw'+ch])
    VariablesSmooth[wprime+'_t'+ch].Add(VariablesSmooth[wprime+'_btw'+ch])
    VariablesSmooth[wprime+'_ttbar'+ch].Add( VariablesSmooth[wprime+'_t'+ch])
    VariablesSmooth[wprime+'_s'+ch].Add(VariablesSmooth[wprime+'_bs'+ch]) 
    VariablesSmooth[wprime+'_ttbar'+ch].Add(VariablesSmooth[wprime+'_s'+ch])
    VariablesSmooth[wprime+'_ttbar'+ch].Write()

    print channel,' data = ', VariablesSmooth[wprime+'_data'+ch].Integral()
    print 'Total background = ', VariablesSmooth[wprime+'_ttbar'+ch].Integral()+VariablesSmooth[wprime+'_wjets'+ch].Integral()
    print 'wjets ',VariablesSmooth[wprime+'_wjets'+ch].Integral()
    print 'TTbar ',VariablesSmooth[wprime+'_ttbar'+ch].Integral()
    print 'Background / Data = ', (VariablesSmooth[wprime+'_ttbar'+ch].Integral()+VariablesSmooth[wprime+'_wjets'+ch].Integral())/VariablesSmooth[wprime+'_data'+ch].Integral()
    totaln=0
    for i in range(bin):
        totaln+=VariablesSmooth[wprime+'_ttbar'+ch].GetBinContent(i+1)+VariablesSmooth[wprime+'_wjets'+ch].GetBinContent(i+1)
    print 'total b.g. again: ',totaln
                
    ##### JES UP ##### 
    VariablesSmooth[wprime+'_ww_JESUP'+ch].Add(VariablesSmooth[wprime+'_zjets_JESUP'+ch])
    VariablesSmooth[wprime+'_wjets_JESUP'+ch].Add(VariablesSmooth[wprime+'_ww_JESUP'+ch])

    VariablesSmooth[wprime+'_wjets_JESUP'+ch].SetName(chan+"BDT_"+btags+"__wjets__jes__plus")
    VariablesSmooth[wprime+'_wjets_JESUP'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jes__plus")
    VariablesSmooth[wprime+'_t_JESUP'+ch].Add(VariablesSmooth[wprime+'_bt_JESUP'+ch])
    VariablesSmooth[wprime+'_t_JESUP'+ch].Add(VariablesSmooth[wprime+'_tw_JESUP'+ch])
    VariablesSmooth[wprime+'_t_JESUP'+ch].Add(VariablesSmooth[wprime+'_btw_JESUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].Add( VariablesSmooth[wprime+'_t_JESUP'+ch])
    VariablesSmooth[wprime+'_s_JESUP'+ch].Add(VariablesSmooth[wprime+'_bs_JESUP'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].Add(VariablesSmooth[wprime+'_s_JESUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JESUP'+ch].Write()

    ##### JES DOWN #####
    VariablesSmooth[wprime+'_ww_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_zjets_JESDOWN'+ch])
    VariablesSmooth[wprime+'_wjets_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_ww_JESDOWN'+ch])

    VariablesSmooth[wprime+'_wjets_JESDOWN'+ch].SetName(chan+"BDT_"+btags+"__wjets__jes__minus")
    VariablesSmooth[wprime+'_wjets_JESDOWN'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jes__minus")
    VariablesSmooth[wprime+'_t_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_bt_JESDOWN'+ch])
    VariablesSmooth[wprime+'_t_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_tw_JESDOWN'+ch])
    VariablesSmooth[wprime+'_t_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_btw_JESDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].Add( VariablesSmooth[wprime+'_t_JESDOWN'+ch])
    VariablesSmooth[wprime+'_s_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_bs_JESDOWN'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].Add(VariablesSmooth[wprime+'_s_JESDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JESDOWN'+ch].Write()

    ##### JER UP ##### 
    VariablesSmooth[wprime+'_ww_JERUP'+ch].Add(VariablesSmooth[wprime+'_zjets_JERUP'+ch])
    VariablesSmooth[wprime+'_wjets_JERUP'+ch].Add(VariablesSmooth[wprime+'_ww_JERUP'+ch])

    VariablesSmooth[wprime+'_wjets_JERUP'+ch].SetName(chan+"BDT_"+btags+"__wjets__jer__plus")
    VariablesSmooth[wprime+'_wjets_JERUP'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jer__plus")
    VariablesSmooth[wprime+'_t_JERUP'+ch].Add(VariablesSmooth[wprime+'_bt_JERUP'+ch])
    VariablesSmooth[wprime+'_t_JERUP'+ch].Add(VariablesSmooth[wprime+'_tw_JERUP'+ch])
    VariablesSmooth[wprime+'_t_JERUP'+ch].Add(VariablesSmooth[wprime+'_btw_JERUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].Add( VariablesSmooth[wprime+'_t_JERUP'+ch])
    VariablesSmooth[wprime+'_s_JERUP'+ch].Add(VariablesSmooth[wprime+'_bs_JERUP'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].Add(VariablesSmooth[wprime+'_s_JERUP'+ch])
    VariablesSmooth[wprime+'_ttbar_JERUP'+ch].Write()

    ##### JER DOWN #####
    VariablesSmooth[wprime+'_ww_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_zjets_JERDOWN'+ch])
    VariablesSmooth[wprime+'_wjets_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_ww_JERDOWN'+ch])

    VariablesSmooth[wprime+'_wjets_JERDOWN'+ch].SetName(chan+"BDT_"+btags+"__wjets__jer__minus")
    VariablesSmooth[wprime+'_wjets_JERDOWN'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].SetName(chan+"BDT_"+btags+"__ttbar__jer__minus")
    VariablesSmooth[wprime+'_t_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_bt_JERDOWN'+ch])
    VariablesSmooth[wprime+'_t_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_tw_JERDOWN'+ch])
    VariablesSmooth[wprime+'_t_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_btw_JERDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].Add( VariablesSmooth[wprime+'_t_JERDOWN'+ch])
    VariablesSmooth[wprime+'_s_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_bs_JERDOWN'+ch]) 
    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].Add(VariablesSmooth[wprime+'_s_JERDOWN'+ch])
    VariablesSmooth[wprime+'_ttbar_JERDOWN'+ch].Write()

    ##### BTAG UP ##### 
    VariablesSmooth[wprime+'_ww_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_zjets_BTAGUP'+ch])
    VariablesSmooth[wprime+'_wjets_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_ww_BTAGUP'+ch])

    VariablesSmooth[wprime+'_wjets_BTAGUP'+ch].SetName(chan+"BDT_"+btags+"__wjets__btag__plus")
    VariablesSmooth[wprime+'_wjets_BTAGUP'+ch].Write()

    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].SetName(chan+"BDT_"+btags+"__ttbar__btag__plus")
    VariablesSmooth[wprime+'_t_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_bt_BTAGUP'+ch])
    VariablesSmooth[wprime+'_t_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_tw_BTAGUP'+ch])
    VariablesSmooth[wprime+'_t_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_btw_BTAGUP'+ch])
    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].Add( VariablesSmooth[wprime+'_t_BTAGUP'+ch])
    VariablesSmooth[wprime+'_s_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_bs_BTAGUP'+ch]) 
    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].Add(VariablesSmooth[wprime+'_s_BTAGUP'+ch])
    VariablesSmooth[wprime+'_ttbar_BTAGUP'+ch].Write()

    ##### BTAG DOWN #####
    VariablesSmooth[wprime+'_ww_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_zjets_BTAGDOWN'+ch])
    VariablesSmooth[wprime+'_wjets_BTAGDOWN'+ch].Add(VariablesSmooth[wprime+'_ww_BTAGDOWN'+ch])

    VariablesSmooth[wprime+'_wjets_BTAGDOWN'+ch].SetName(chan+"BDT_"+btags+"__wjets__btag__minus")
    VariablesSmooth[wprime+'_wjets_BTAGDOWN'+ch].Write()

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

    VariablesSmoothHFup[wprime+'_ww'+ch].Add(VariablesSmoothHFup[wprime+'_zjets'+ch])
    VariablesSmoothHFup[wprime+'_wjets'+ch].Add(VariablesSmoothHFup[wprime+'_ww'+ch])
    VariablesSmoothHFup[wprime+'_wjets'+ch].SetName(chan+"BDT_"+btags+"__wjets__hf__plus")
    VariablesSmoothHFup[wprime+'_wjets'+ch].Write()
    VariablesSmoothHFdown[wprime+'_ww'+ch].Add(VariablesSmoothHFdown[wprime+'_zjets'+ch])
    VariablesSmoothHFdown[wprime+'_wjets'+ch].Add(VariablesSmoothHFdown[wprime+'_ww'+ch])
    VariablesSmoothHFdown[wprime+'_wjets'+ch].SetName(chan+"BDT_"+btags+"__wjets__hf__minus")
    VariablesSmoothHFdown[wprime+'_wjets'+ch].Write()

    del Variables
    del VariablesSmooth
    del VariablesSmoothHFup
    del VariablesSmoothHFdown
    del RootFilesBDT
    del Trees
  
#wprime = 'Right'
var = 'MVA_BDT'; high = 1.0; xaxis = "BDT Discriminant"; yaxis = 'Events'; save = 'BDT'

btags = 'ge1btags'
xlow  = [-0.8,-0.5,-0.45,-0.4,-0.35,-0.3,-0.25,-0.2,-0.15,-0.1,-0.05,0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.5,1.0]
bins = len(xlow)-1 

channel = 'electron'

wprime = 'wp1100R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1300R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1500R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1700R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1900R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2100R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2300R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2500R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2700R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 

channel = 'muon'

wprime = 'wp1100R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1300R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1500R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1700R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp1900R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2100R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2300R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2500R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
wprime = 'wp2700R'
plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) 
