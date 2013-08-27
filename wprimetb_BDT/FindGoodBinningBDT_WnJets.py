import ROOT, sys, os, re, string
from ROOT import *

from array import array
from math import *
import copy
import decimal


#from LoadDataBDT_LPC_minKS0pt1_minimal_allnewWjets import *
#from LoadDataBDT_WnJets_1and2BTags import *
from LoadDataBDT_WnJets_QCD_1and2BTags_AllVars import *

#from comb_yields_May16 import *
#from comb_yields_Jun06_ScaleGenTopPt import *
from comb_yields_19Jun import *

def Rebin(channel, varName, wprime, btags):

    List_Bkg = ['w1jets','w2jets','w3jets','w4jets','ww','ttbar','zjets','t','bt','tw','btw','s','bs']
    if (channel=='electron'): List_Bkg = ['w1jets','w2jets','w3jets','w4jets','qcd80to170','qcd170to250','qcd250to350','qcd350','ww','ttbar','zjets','t','bt','tw','btw','s','bs']


    if (channel == 'electron'): ch = '_el'
    if (channel == 'muon'): ch = '_mu'

    RootFilesBDT = {}
    Trees = {}
    for Type in List_Bkg:
        if btags == 'ge1btags':
            RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_GE1BTag_'+wprime+'_'+Type+ch+'.root')
            Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)
        if btags == 'onebtags':
            RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_1BTag_'+wprime+'_'+Type+ch+'.root')
            Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)
        if btags == 'twobtags':
            RootFilesBDT[wprime+'_'+Type+ch] = TFile(BDTDir+'BDT_2BTag_'+wprime+'_'+Type+ch+'.root')
            Trees[wprime+'_'+Type+ch] = RootFilesBDT[wprime+'_'+Type+ch].Get(Type)


    if (channel == 'electron'):
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && elec_1_pt_WprimeCalc > 50 && abs(elec_1_eta_WprimeCalc) < 2.5 && elec_1_RelIso_WprimeCalc < 0.1 && corr_met_WprimeCalc > 20 && Muon_DeltaR_LjetsTopoCalcNew > 0.3'

    if (channel == 'muon'):
        cut = 'jet_0_pt_WprimeCalc >= 120 && jet_1_pt_WprimeCalc >= 40 && muon_1_pt_WprimeCalc > 50 && abs(muon_1_eta_WprimeCalc) < 2.1 && muon_1_RelIso_WprimeCalc < 0.12 && corr_met_WprimeCalc > 20 && Muon_DeltaR_LjetsTopoCalcNew > 0.3'

    if btags == 'zerobtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==0) '
    if btags == 'onebtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==1) '
    if btags == 'ge1btags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)>=1) '
    if btags == 'twobtags': cutbtag = ' && ((jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc)==2) '
    if btags == 'ge2btags': cutbtag = ' && ( (jet_0_tag_WprimeCalc==1 && (jet_1_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) || (jet_1_tag_WprimeCalc==1 && (jet_0_tag_WprimeCalc + jet_2_tag_WprimeCalc + jet_3_tag_WprimeCalc + jet_4_tag_WprimeCalc + jet_5_tag_WprimeCalc + jet_6_tag_WprimeCalc + jet_7_tag_WprimeCalc + jet_8_tag_WprimeCalc + jet_9_tag_WprimeCalc) >= 1 ) ) '

    if btags == 'final': cutbtag = ' && ( (jet_0_tag_WprimeCalc+jet_1_tag_WprimeCalc ) >= 1 )'
    if btags == 'final': cut = cut + ' && BestTop_LjetsTopoCalcNew > 130 && BestTop_LjetsTopoCalcNew < 210 &&  BestTop_Pt_LjetsTopoCalcNew > 75  && Jet1Jet2_Pt_LjetsTopoCalcNew > 100 '


    var = varName
    print 'Rebinning of variable ',varName,' for wprime = ',wprime,' and ',btags

    global binfile
    binfile = open('bins_'+var+'_'+btags+'_WnJets_QCD_1and2_AllVars.txt', 'a')      
          
    minbkg = 1.0
    maxerrbkg = 9999.0  

    print 'min background prediction per bin is ',minbkg
               
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

        SFWjmuMinus = 1.0*1.13        ## myHF120lep50, scale ttbar 
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



    # This is the starting point for the binning search (smart choices speed up the initial bg search)
    xlowbg  = array('d',[-1.0,-0.95,-0.90,-0.85,-0.80,-0.75,-0.70,-0.65,-0.60,-0.55,-0.50,-0.45,-0.40,-0.35,-0.30,-0.25,-0.20,-0.15,-0.10,-0.05,-0.0,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.0])


    foundbinningbg = 'False'
    while (foundbinningbg=='False'):

        binningbadbg = 'False'  

        binbg = len(xlowbg)-1   

        Variables = {}
        bgadded = TH1D('bgadded', 'bgadded',binbg,xlowbg)
        wnjetsadded = TH1D('wnjetsadded', 'wnjetsadded',binbg,xlowbg)

        for Type in List_Bkg:
        
            Type = wprime+'_'+Type+ch

            Variables[Type] = TH1D(Type, Type, binbg, xlowbg) 
            Variables[Type].Sumw2()
        
            if (channel=='electron'):
                #weight = 'weight_PU_ABC_PileUpCalc*weight_ElectronEff_WprimeCalc'                                                                         
                weight = '( ((0.973*weight_PU_ABCD_PileUpCalc*weight_ElectronEff_53x_WprimeCalc)*(abs(elec_1_eta_WprimeCalc)<1.5)) + ((1.02*weight_PU_ABCD_PileUpCalc*weight_ElectronEff_53x_WprimeCalc)*(abs(elec_1_eta_WprimeCalc)>1.5 && abs(elec_1_eta_WprimeCalc)<2.5)) )'
                SF = 1.0
            if (channel=='muon'):
                weight = 'weight_PU_ABCD_PileUpCalc*weight_MuonEff_WprimeCalc'
                SF = 1.0

            if (Type == wprime+'_'+'w1jets'+ch):
                WccHist1 = TH1D('WccHist1', 'WccHist1', binbg,xlowbg)
                WbbHist1 = TH1D('WbbHist1', 'WbbHist1', binbg,xlowbg)
                WccHist1.Sumw2()
                WbbHist1.Sumw2()
            if (Type == wprime+'_'+'w2jets'+ch):
                WccHist2 = TH1D('WccHist2', 'WccHist2', binbg,xlowbg)
                WbbHist2 = TH1D('WbbHist2', 'WbbHist2', binbg,xlowbg)
                WccHist2.Sumw2()
                WbbHist2.Sumw2()
            if (Type == wprime+'_'+'w3jets'+ch):
                WccHist3 = TH1D('WccHist3', 'WccHist3', binbg,xlowbg)
                WbbHist3 = TH1D('WbbHist3', 'WbbHist3', binbg,xlowbg)
                WccHist3.Sumw2()
                WbbHist3.Sumw2()
            if (Type == wprime+'_'+'w4jets'+ch):
                WccHist4 = TH1D('WccHist4', 'WccHist4', binbg,xlowbg)
                WbbHist4 = TH1D('WbbHist4', 'WbbHist4', binbg,xlowbg)
                WccHist4.Sumw2()
                WbbHist4.Sumw2()

            if (Type.startswith(wprime+'_w1jets')):
                Trees[Type].Draw(var+" >> "+Type,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist1","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist1","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff')
                Variables[Type].Add(WbbHist1)
                Variables[Type].Add(WccHist1)
            elif (Type.startswith(wprime+'_w2jets')):
                Trees[Type].Draw(var+" >> "+Type,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist2","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist2","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff')
                Variables[Type].Add(WbbHist2)
                Variables[Type].Add(WccHist2)
            elif (Type.startswith(wprime+'_w3jets')):
                Trees[Type].Draw(var+" >> "+Type,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist3","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist3","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff')
                Variables[Type].Add(WbbHist3)
                Variables[Type].Add(WccHist3)
            elif (Type.startswith(wprime+'_w4jets')):
                Trees[Type].Draw(var+" >> "+Type,"("+weight+")*("+str(SFWjmu)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHist4","("+weight+")*("+str(SFWbmu)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHist4","("+weight+")*("+str(SFWcmu)+")*("+cut+cutwcc+cutbtag+")",'goff')
                Variables[Type].Add(WbbHist4)
                Variables[Type].Add(WccHist4)
            elif (Type.startswith(wprime+'_ttbar')):
                Trees[Type].Draw(var + " >> " + Type, "("+weight+")*("+weight_ttbar+")*("+cut+cutbtag+")", 'goff')
            else:
                Trees[Type].Draw(var + " >> " + Type, "("+weight+")*("+cut+cutbtag+")", 'goff')




            if re.match(wprime+"_w[1-4]jets", Type):
                Variables[Type].Scale(xsec[Type]/Nevents[Type])
                wnjetsadded.Add(Variables[Type])
            elif Variables[Type].Integral() != 0:
                Variables[Type].Scale ( yields[Type+'_'+btags]/Variables[Type].Integral() )
                bgadded.Add(Variables[Type])


            if (Type.startswith(wprime+'_w1jets')): del WccHist1; del WbbHist1;
            if (Type.startswith(wprime+'_w2jets')): del WccHist2; del WbbHist2;
            if (Type.startswith(wprime+'_w3jets')): del WccHist3; del WbbHist3;
            if (Type.startswith(wprime+'_w4jets')): del WccHist4; del WbbHist4;
            
        wnjetsadded.Scale(yields[wprime+'_wjets_'+chan+'_'+btags]/wnjetsadded.Integral())
        bgadded.Add(wnjetsadded)

        
        for x in range(1,binbg+1):  
            if ( (bgadded.GetBinContent(binbg+1-x) < minbkg or bgadded.GetBinError(binbg+1-x)/bgadded.GetBinContent(binbg+1-x) > maxerrbkg) and binningbadbg == 'False' ):
                binningbadbg = 'True'
                print 'B.G. for bin ',binbg+1-x,' is ',bgadded.GetBinContent(binbg+1-x),', So merging'
                if ((binbg+1-x)>1): xlowbg.pop(binbg-x)
                else: xlowbg.pop(1)
 
        #if (binningbadbg=='True'):
        #    print 'Had to merge so will start over with next xlow: '
        #    print '[',
        #    for b in range(len(xlowbg)):
        #        if (b == (len(xlowbg)-1)): print round(decimal.Decimal(str(float(xlowbg[b]))),2),
        #        else: print round(decimal.Decimal(str(float(xlowbg[b]))),2),',',
        #    print ']'
        if (binningbadbg=='False'): 
            foundbinningbg = 'True' 
            print 'Finished!!!!  xlowbg is '      
            print '[',
            for b in range(len(xlowbg)):
                if (b == (len(xlowbg)-1)): print round(decimal.Decimal(str(float(xlowbg[b]))),2),
                else: print round(decimal.Decimal(str(float(xlowbg[b]))),2),',',
            print ']'
            
        del Variables
        del bgadded
        del wnjetsadded
      
  

    binfile.write("# "+wprime+" "+varName+" "+channel+" \n")
    binfile.write("channel = '"+channel+"' \n")
    binfile.write("btags = '"+btags+"' \n")
    binfile.write("wprime = '"+wprime+"' \n")
    binfile.write("xlow = [")
    for b in range(len(xlowbg)):
        if (b == (len(xlowbg)-1)):binfile.write(str(round(decimal.Decimal(str(float(xlowbg[b]))),2)))
        else: binfile.write(str(round(decimal.Decimal(str(float(xlowbg[b]))),2))+",")
    binfile.write("] \n")
    binfile.write("bins = len(xlow)-1 \n")
    binfile.write("plot_DataVsMc(channel, var, bins, xlow, high, yaxis, xaxis, save, wprime, btags) ")
    binfile.write("\n")
    binfile.write("\n")
    binfile.close()
            
    del RootFilesBDT
    del Trees



#Rebin('electron', 'MVA_BDT', 'wp800R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp1000R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp1200R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp1400R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp1600R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp1800R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp2000R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp2200R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp2400R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp2600R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp2800R', 'ge1btags')
#Rebin('electron', 'MVA_BDT', 'wp3000R', 'ge1btags')

#Rebin('muon', 'MVA_BDT', 'wp800R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp1000R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp1200R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp1400R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp1600R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp1800R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp2000R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp2200R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp2400R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp2600R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp2800R', 'ge1btags')
#Rebin('muon', 'MVA_BDT', 'wp3000R', 'ge1btags')

Rebin('electron', 'MVA_BDT', 'wp800R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp1000R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp1200R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp1400R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp1600R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp1800R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp2000R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp2200R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp2400R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp2600R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp2800R', 'onebtags')
Rebin('electron', 'MVA_BDT', 'wp3000R', 'onebtags')

Rebin('muon', 'MVA_BDT', 'wp800R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp1000R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp1200R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp1400R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp1600R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp1800R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp2000R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp2200R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp2400R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp2600R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp2800R', 'onebtags')
Rebin('muon', 'MVA_BDT', 'wp3000R', 'onebtags')

Rebin('electron', 'MVA_BDT', 'wp800R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp1000R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp1200R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp1400R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp1600R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp1800R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp2000R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp2200R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp2400R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp2600R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp2800R', 'twobtags')
Rebin('electron', 'MVA_BDT', 'wp3000R', 'twobtags')

Rebin('muon', 'MVA_BDT', 'wp800R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp1000R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp1200R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp1400R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp1600R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp1800R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp2000R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp2200R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp2400R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp2600R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp2800R', 'twobtags')
Rebin('muon', 'MVA_BDT', 'wp3000R', 'twobtags')
