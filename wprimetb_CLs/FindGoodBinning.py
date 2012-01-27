import ROOT, sys, os, re, string
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array
from math import *
import copy

#from LoadData import *
from LoadData_ForLPC import *

List_databg = ['Data','WJets', 'WW', 'TTbar', 'ZJets', 'QCD_80to170', 'T_t', 'Tbar_t', 'T_tW', 'Tbar_tW', 'T_s', 'Tbar_s']

List_wprime = [           'Wprime_800_RightWprime',
                         'Wprime_900_RightWprime',
                         'Wprime_1000_RightWprime',
                         'Wprime_1100_RightWprime',
                         'Wprime_1200_RightWprime',
                         'Wprime_1300_RightWprime',
                         'Wprime_1400_RightWprime',
                         'Wprime_1500_RightWprime',
                         'Wprime_1600_RightWprime',
                         'Wprime_1700_RightWprime',
                         'Wprime_1900_RightWprime',
                         'Wprime_2100_RightWprime',
                         'Wprime_2300_RightWprime',
                         'Wprime_2500_RightWprime',
                        #'Wprime_800_LeftWprime',
                        #'Wprime_900_LeftWprime',
                        #'Wprime_1000_LeftWprime',
                        #'Wprime_1100_LeftWprime',
                        #'Wprime_1200_LeftWprime',
                        #'Wprime_1300_LeftWprime',
                        #'Wprime_1400_LeftWprime',
                        #'Wprime_1500_LeftWprime',
                        #'Wprime_1600_LeftWprime',
                        #'Wprime_1700_LeftWprime',
                        #'Wprime_1900_LeftWprime',
                        #'Wprime_2100_LeftWprime',
                        #'Wprime_2300_LeftWprime',
                        #'Wprime_2500_LeftWprime',
                       #'Wprime_800_MixRLWprime',
                       #'Wprime_900_MixRLWprime',
                       #'Wprime_1000_MixRLWprime',
                       #'Wprime_1100_MixRLWprime',
                       #'Wprime_1200_MixRLWprime',
                       #'Wprime_1300_MixRLWprime',
                       #'Wprime_1400_MixRLWprime',
                       #'Wprime_1500_MixRLWprime',
                       #'Wprime_1600_MixRLWprime',
                       #'Wprime_1700_MixRLWprime',
                       #'Wprime_1900_MixRLWprime',
                       #'Wprime_2100_MixRLWprime',
                       #'Wprime_2300_MixRLWprime',
                       #'Wprime_2500_MixRLWprime',
]

def Rebin(letter,varName,btags,List_to_use):

    cut = 'electron0_pt_el > 35 && electron0_Iso_el < 0.125 && electron0_IDHyperTight1_el == 1 && fabs(PFjet0_eta_el) < 2.4 && fabs(PFjet1_eta_el) < 2.4 && PF_met_pt_el > 35 && fabs(electron0_eleConvDcot_el) > 0.02 && fabs(electron0_eleConvDist_el) > 0.02'

    if letter == 'J':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40'
    if letter == 'M':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 100'

    if letter == 'M_aa':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 55  && Pt_Jet1Jet2_bestTop_el > 80'
    if letter == 'M_ab':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 55  && Pt_Jet1Jet2_bestTop_el > 90'
    if letter == 'M_ac':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 55  && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'M_ad':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 55  && Pt_Jet1Jet2_bestTop_el > 110'
    if letter == 'M_ae':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 55  && Pt_Jet1Jet2_bestTop_el > 120'
 
    if letter == 'M_ba':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 65  && Pt_Jet1Jet2_bestTop_el > 80'
    if letter == 'M_bb':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 65  && Pt_Jet1Jet2_bestTop_el > 90'
    if letter == 'M_bc':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 65  && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'M_bd':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 65  && Pt_Jet1Jet2_bestTop_el > 110'
    if letter == 'M_be':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 65  && Pt_Jet1Jet2_bestTop_el > 120'
 
    if letter == 'M_ca':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 80'
    if letter == 'M_cb':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 90'
    if letter == 'M_cc':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'M_cd':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 110'
    if letter == 'M_ce':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 120'
 
    if letter == 'M_da':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 85  && Pt_Jet1Jet2_bestTop_el > 80'
    if letter == 'M_db':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 85  && Pt_Jet1Jet2_bestTop_el > 90'
    if letter == 'M_dc':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 85  && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'M_dd':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 85  && Pt_Jet1Jet2_bestTop_el > 110'
    if letter == 'M_de':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 85  && Pt_Jet1Jet2_bestTop_el > 120'
 
    if letter == 'M_ea':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 95  && Pt_Jet1Jet2_bestTop_el > 80'
    if letter == 'M_eb':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 95  && Pt_Jet1Jet2_bestTop_el > 90'
    if letter == 'M_ec':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 95  && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'M_ed':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 95  && Pt_Jet1Jet2_bestTop_el > 110'
    if letter == 'M_ee':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopPt_Best_bestTop_el > 95  && Pt_Jet1Jet2_bestTop_el > 120'
 
    if letter == 'N':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210'
    if letter == 'O':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 100'
 
    if letter == 'A':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210 && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'B':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210 && TopPt_BTag_bestTop_el > 50  && Pt_Jet1Jet2_bestTop_el > 100'

       
    if btags == 1:
        btag = '1b'
        cut = cut + ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el ) == 1 )'

    if btags == 2:
        btag = '2b'
        cut = cut + ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el ) >= 2 )'

    if btags == 3:
        btag = 'ge1b'
        cut = cut + ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el ) >= 1 )'

    if btags == 4:
        btag = 'ge1btop3'
        cut = cut + ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el + weight_BTag_jet2_medium_el  ) >= 1 )'

    if btags == -1:
        btag = 'Nob'

    var = varName
    print 'Rebinning of variable ',varName,' for cut letter',letter,' and ',btag,' , which means the cut is: '
    print cut

    global binfile
    binfile = open('bins_'+var+'_'+letter+'_el.txt', 'w')      
          
    precision = 0.1
    precisiondata = 1.0

    print 'min statistcal uncertainty per bin for sig and bg is ',precision
    print 'min statistcal uncertainty per bin for data is ',precisiondata
               
    cutwbb = ' &&  n_Bjets_el > 0' # Wb(b)
    cutwcc = ' && n_Bjets_el==0 && n_Cjets_el>0' # Wc(c)
    cutwjj = ' && n_Bjets_el==0 && n_Cjets_el==0' # W+light

    SFWjmu = 0.91
    SFWcmu = 1.07
    SFWbmu = 1.07

    Variables = {}

    # This is the starting point for the binning search (smart choices speed up the initial bg search)
    xlowbg  = [170, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225, 1275, 1300, 1325, 1375, 1425, 1475, 1550, 1700, 3500]

    foundbinningbg = 'False'
    while (foundbinningbg=='False'):

        binningbadbg = 'False'  

        binbg = len(xlowbg)-1   
        bgadded = TH1D('bgadded', 'bgadded',binbg,array('d',xlowbg))
 
        for Type in List_databg:

            Variables[Type] = TH1D(Type, Type, binbg, array('d',xlowbg)) 
            Variables[Type].Sumw2()

            if (Type == 'WJets'):
                WccHist = TH1D('WccHist', 'WccHist', binbg,array('d',xlowbg))
                WbbHist = TH1D('WbbHist', 'WbbHist', binbg,array('d',xlowbg))
                WccHist.Sumw2()
                WbbHist.Sumw2()
                        
            #print Type
            if (Type == 'Data'):
                Trees[Type].Draw(var + " >> " + Type, "(" + cut + ")", 'goff')
            elif (Type == 'WJets'):
                Trees[Type].Draw(var + " >> " + Type, "(weight_WxsecNoLight_comb)*(" + str(SFWjmu) + ")*(" + cut + cutwjj + ")", 'goff')
                Trees[Type].Draw(var + " >> " + "WbbHist", "(weight_WxsecNoLight_comb)*(" + str(SFWbmu) + ")*(" + cut + cutwbb + ")", 'goff')
                Trees[Type].Draw(var + " >> " + "WccHist", "(weight_WxsecNoLight_comb)*(" + str(SFWcmu) + ")*(" + cut + cutwcc + ")", 'goff')
                Variables[Type].Add(WbbHist)
                Variables[Type].Add(WccHist)                 
            else:
                Trees[Type].Draw(var + " >> " + Type,"("+cut+ ")", 'goff')
          
            if (Type!='Data'): bgadded.Add(Variables[Type])

        for x in range(1,binbg+1):  
            if ( bgadded.GetBinContent(binbg+1-x) < 0.00001 and binningbadbg == 'False' ):
                binningbadbg = 'True'
                print 'B.G. for bin ',binbg+1-x,' is ',bgadded.GetBinContent(binbg+1-x),', So popping'
                if ((binbg+1-x)>1): xlowbg.pop(binbg-x)
                else: xlowbg.pop(1)
            elif (bgadded.GetBinContent(binbg+1-x) > 0.00001 and 1/sqrt(bgadded.GetBinContent(binbg+1-x)) > precision and binningbadbg == 'False' ): 
                binningbadbg = 'True'
                print 'B.G. for bin ',binbg+1-x,' is ',bgadded.GetBinContent(binbg+1-x),', So popping'
                if ((binbg+1-x)>1): xlowbg.pop(binbg-x)
                else: xlowbg.pop(1)

        for x in range(1,binbg+1):  
            if ( Variables['Data'].GetBinContent(binbg+1-x) < 0.00001 and binningbadbg == 'False' ):
                binningbadbg = 'True'
                print 'Data for bin ',binbg+1-x,' is ',Variables['Data'].GetBinContent(binbg+1-x),', So popping'
                if ((binbg+1-x)>1): xlowbg.pop(binbg-x)
                else: xlowbg.pop(1)
            elif (Variables['Data'].GetBinContent(binbg+1-x) > 0.00001 and 1/sqrt(Variables['Data'].GetBinContent(binbg+1-x)) > precisiondata and binningbadbg == 'False' ): 
                binningbadbg = 'True'
                print 'Data for bin ',binbg+1-x,' is ',Variables['Data'].GetBinContent(binbg+1-x),', So popping'
                if ((binbg+1-x)>1): xlowbg.pop(binbg-x)
                else: xlowbg.pop(1)
 
        if (binningbadbg=='True'):
            print 'Had to pop so will start over with next xlow: '
            print xlowbg  
        if (binningbadbg=='False'): 
            foundbinningbg = 'True' 
            print 'Finished!!!!  xlowbg is '              
            print xlowbg
            print 'Now for signal...'


    for Type in List_to_use:

        print Type    
        # Start with the bg bins for each W'
        #xlowsig  = xlowbg
        xlowsig = copy.copy(xlowbg)
 
        print 'starting with xlowbg: ' 
        print xlowsig

        foundbinningsig='False'
        while (foundbinningsig=='False'):

            binningbadsig = 'False' 
            binsig = len(xlowsig)-1
 
            Variables[Type] = TH1D(Type, Type, binsig, array('d',xlowsig)) 
            Variables[Type].Sumw2()
                
            # nothing fancy here, only looking at W'
            Trees[Type].Draw(var + " >> " + Type,"("+cut+ ")", 'goff')
 
            for x in range(1,binsig+1):
                if (Variables[Type].GetBinContent(binsig+1-x) < 0.00001 and binningbadsig == 'False'  ):
                    binningbadsig = 'True'
                    print 'Bin ',binsig+1-x,' for ',Type,' is ',Variables[Type].GetBinContent(binsig+1-x),', So popping'
                    if ((binsig+1-x)>1): xlowsig.pop(binsig-x) 
                    else: xlowsig.pop(1) 
                elif (Variables[Type].GetBinContent(binsig+1-x) > 0.00001 and 1/sqrt(Variables[Type].GetBinContent(binsig+1-x)) > precision and binningbadsig == 'False'  ): 
                    binningbadsig = 'True'
                    print 'Bin ',binsig+1-x,' for ',Type,' is ',Variables[Type].GetBinContent(binsig+1-x),', So popping'
                    if ((binsig+1-x)>1): xlowsig.pop(binsig-x) 
                    else: xlowsig.pop(1) 

            if (binningbadsig=='True'):
                print 'Had to pop so will start over with next xlowsig: '
                print xlowsig  
            if (binningbadsig=='False'): 
                foundbinningsig = 'True' 
                print 'Finished!!!!  xlowsig is '              
                print xlowsig 

        maxbins = 15
        while (len(xlowsig)-1 > maxbins):
            indextpop = 0
            for x in range(1,binsig+1):
                binn = bgadded.GetBinContent(x)
                if (binn < minn): 
                    minn = binn 
                    indextopop = x-1
            xlowsig.pop(indextopop) 
       
        binfile.write('# '+Type+' '+var+'\n')
        binfile.write('xlow = '+str(xlowsig)+'\n')
        binfile.write('bins = len(xlow)-1 \n')
        binfile.write('List_DataBg_'+Type+' = copy.copy(List_DataBg) \n')
        binfile.write('List_DataBg_'+Type+'.extend(List_'+Type+') \n')
        binfile.write("f.cd('..') \n")
        binfile.write("f.mkdir('"+Type+"') \n")
        binfile.write("f.cd('"+Type+"') \n")
        binfile.write('plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_'+Type+') \n')
        binfile.write('\n')
        binfile.write('\n')
      
Rebin('O','BestJetJet2W_M_bestTop_el',3,List_wprime)


