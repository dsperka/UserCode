import ROOT, sys, os, re, string
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array
import copy
import math

#from LoadData import *
from LoadData_ForLPC import *

List_DataBg = ['Data', 'WJets', 'WW', 'TTbar', 'ZJets', 'QCD_80to170', 'T_t', 'Tbar_t', 'T_tW', 'Tbar_tW', 'T_s', 'Tbar_s',
              'WJets_JES_UP',
              'WW_JES_UP',
              'TTbar_JES_UP',
              'ZJets_JES_UP',
              'QCD_80to170_JES_UP',
              'T_t_JES_UP',
              'Tbar_t_JES_UP',
              'T_tW_JES_UP',
              'Tbar_tW_JES_UP',
              'T_s_JES_UP',
              'Tbar_s_JES_UP',
              'WJets_JES_DOWN',
              'WW_JES_DOWN',
              'TTbar_JES_DOWN',
              'ZJets_JES_DOWN',
              'QCD_80to170_JES_DOWN',
              'T_t_JES_DOWN',
              'Tbar_t_JES_DOWN',
              'T_tW_JES_DOWN',
              'Tbar_tW_JES_DOWN',
              'T_s_JES_DOWN',
              'Tbar_s_JES_DOWN',
              'WJets_BTAG_UP',
              'WW_BTAG_UP',
              'TTbar_BTAG_UP',
              'ZJets_BTAG_UP',
              'QCD_80to170_BTAG_UP',
              'T_t_BTAG_UP',
              'Tbar_t_BTAG_UP',
              'T_tW_BTAG_UP',
              'Tbar_tW_BTAG_UP',
              'T_s_BTAG_UP',
              'Tbar_s_BTAG_UP',
              'WJets_BTAG_DOWN',
              'WW_BTAG_DOWN',
              'TTbar_BTAG_DOWN',
              'ZJets_BTAG_DOWN',
              'QCD_80to170_BTAG_DOWN',
              'T_t_BTAG_DOWN',
              'Tbar_t_BTAG_DOWN',
              'T_tW_BTAG_DOWN',
              'Tbar_tW_BTAG_DOWN',
              'T_s_BTAG_DOWN',
              'Tbar_s_BTAG_DOWN',
              'WJets_JER_UP',
              'WW_JER_UP',
              'TTbar_JER_UP',
              'ZJets_JER_UP',
              'QCD_80to170_JER_UP',
              'T_t_JER_UP',
              'Tbar_t_JER_UP',
              'T_tW_JER_UP',
              'Tbar_tW_JER_UP',
              'T_s_JER_UP',
              'Tbar_s_JER_UP',
              'WJets_JER_DOWN',
              'WW_JER_DOWN',
              'TTbar_JER_DOWN',
              'ZJets_JER_DOWN',
              'QCD_80to170_JER_DOWN',
              'T_t_JER_DOWN',
              'Tbar_t_JER_DOWN',
              'T_tW_JER_DOWN',
              'Tbar_tW_JER_DOWN',
              'T_s_JER_DOWN',
              'Tbar_s_JER_DOWN',
              'TTbar_MATCHING_UP',
              'TTbar_MATCHING_DOWN',
              'TTbar_SCALE_UP',
              'TTbar_SCALE_DOWN',
              'WJets_MATCHING_UP',
              'WJets_MATCHING_DOWN',
              'WJets_SCALE_UP',
              'WJets_SCALE_DOWN',
]

List_Wprime_800_RightWprime = ['Wprime_800_RightWprime', 'Wprime_800_RightWprime_JES_UP','Wprime_800_RightWprime_JES_DOWN', 'Wprime_800_RightWprime_BTAG_UP', 'Wprime_800_RightWprime_BTAG_DOWN','Wprime_800_RightWprime_JER_UP','Wprime_800_RightWprime_JER_DOWN']
List_Wprime_900_RightWprime = ['Wprime_900_RightWprime', 'Wprime_900_RightWprime_JES_UP','Wprime_900_RightWprime_JES_DOWN', 'Wprime_900_RightWprime_BTAG_UP', 'Wprime_900_RightWprime_BTAG_DOWN','Wprime_900_RightWprime_JER_UP','Wprime_900_RightWprime_JER_DOWN']
List_Wprime_1000_RightWprime = ['Wprime_1000_RightWprime', 'Wprime_1000_RightWprime_JES_UP','Wprime_1000_RightWprime_JES_DOWN', 'Wprime_1000_RightWprime_BTAG_UP', 'Wprime_1000_RightWprime_BTAG_DOWN','Wprime_1000_RightWprime_JER_UP','Wprime_1000_RightWprime_JER_DOWN']
List_Wprime_1100_RightWprime = ['Wprime_1100_RightWprime', 'Wprime_1100_RightWprime_JES_UP','Wprime_1100_RightWprime_JES_DOWN', 'Wprime_1100_RightWprime_BTAG_UP', 'Wprime_1100_RightWprime_BTAG_DOWN','Wprime_1100_RightWprime_JER_UP','Wprime_1100_RightWprime_JER_DOWN']
List_Wprime_1200_RightWprime = ['Wprime_1200_RightWprime', 'Wprime_1200_RightWprime_JES_UP','Wprime_1200_RightWprime_JES_DOWN', 'Wprime_1200_RightWprime_BTAG_UP', 'Wprime_1200_RightWprime_BTAG_DOWN','Wprime_1200_RightWprime_JER_UP','Wprime_1200_RightWprime_JER_DOWN']
List_Wprime_1300_RightWprime = ['Wprime_1300_RightWprime', 'Wprime_1300_RightWprime_JES_UP','Wprime_1300_RightWprime_JES_DOWN', 'Wprime_1300_RightWprime_BTAG_UP', 'Wprime_1300_RightWprime_BTAG_DOWN','Wprime_1300_RightWprime_JER_UP','Wprime_1300_RightWprime_JER_DOWN']
List_Wprime_1400_RightWprime = ['Wprime_1400_RightWprime', 'Wprime_1400_RightWprime_JES_UP','Wprime_1400_RightWprime_JES_DOWN', 'Wprime_1400_RightWprime_BTAG_UP', 'Wprime_1400_RightWprime_BTAG_DOWN','Wprime_1400_RightWprime_JER_UP','Wprime_1400_RightWprime_JER_DOWN']
List_Wprime_1500_RightWprime = ['Wprime_1500_RightWprime', 'Wprime_1500_RightWprime_JES_UP','Wprime_1500_RightWprime_JES_DOWN', 'Wprime_1500_RightWprime_BTAG_UP', 'Wprime_1500_RightWprime_BTAG_DOWN','Wprime_1500_RightWprime_JER_UP','Wprime_1500_RightWprime_JER_DOWN']
List_Wprime_1600_RightWprime = ['Wprime_1600_RightWprime', 'Wprime_1600_RightWprime_JES_UP','Wprime_1600_RightWprime_JES_DOWN', 'Wprime_1600_RightWprime_BTAG_UP', 'Wprime_1600_RightWprime_BTAG_DOWN','Wprime_1600_RightWprime_JER_UP','Wprime_1600_RightWprime_JER_DOWN']
List_Wprime_1700_RightWprime = ['Wprime_1700_RightWprime', 'Wprime_1700_RightWprime_JES_UP','Wprime_1700_RightWprime_JES_DOWN', 'Wprime_1700_RightWprime_BTAG_UP', 'Wprime_1700_RightWprime_BTAG_DOWN','Wprime_1700_RightWprime_JER_UP','Wprime_1700_RightWprime_JER_DOWN']
List_Wprime_1900_RightWprime = ['Wprime_1900_RightWprime', 'Wprime_1900_RightWprime_JES_UP','Wprime_1900_RightWprime_JES_DOWN', 'Wprime_1900_RightWprime_BTAG_UP', 'Wprime_1900_RightWprime_BTAG_DOWN','Wprime_1900_RightWprime_JER_UP','Wprime_1900_RightWprime_JER_DOWN']
List_Wprime_2100_RightWprime = ['Wprime_2100_RightWprime', 'Wprime_2100_RightWprime_JES_UP','Wprime_2100_RightWprime_JES_DOWN', 'Wprime_2100_RightWprime_BTAG_UP', 'Wprime_2100_RightWprime_BTAG_DOWN','Wprime_2100_RightWprime_JER_UP','Wprime_2100_RightWprime_JER_DOWN']
List_Wprime_2300_RightWprime = ['Wprime_2300_RightWprime', 'Wprime_2300_RightWprime_JES_UP','Wprime_2300_RightWprime_JES_DOWN', 'Wprime_2300_RightWprime_BTAG_UP', 'Wprime_2300_RightWprime_BTAG_DOWN','Wprime_2300_RightWprime_JER_UP','Wprime_2300_RightWprime_JER_DOWN']
List_Wprime_2500_RightWprime = ['Wprime_2500_RightWprime', 'Wprime_2500_RightWprime_JES_UP','Wprime_2500_RightWprime_JES_DOWN', 'Wprime_2500_RightWprime_BTAG_UP', 'Wprime_2500_RightWprime_BTAG_DOWN','Wprime_2500_RightWprime_JER_UP','Wprime_2500_RightWprime_JER_DOWN']


fitParms = {} 

### SOME 'O' RATIOS ####
# wjets ge1b/pre =  0.09654
# wjets jerUp ge1b/pre = 0.09533
# wjets jerDown ge1b/pre = 0.09639
# wjets jesUp ge1b/pre = 0.09659
# wjets jesDown ge1b/pre = 0.09758
# wjets nominal / btagDown = 1.099
# wjets nominal / btagUp =  0.9162 

############## FOR ELECTRONS 'O' Cuts (RATIO = 0.0991) 
##### FOR NOMINAL DEF OF Wprime
fitParms['Wets'] = [790.004, 0.701211, 1.15353, 1.08324]
##### FOR NOMINAL DEF OF Wprime with pre-tag 
#fitParms['WJets'] = [7465.14, 0.720158, 1.33349, 1.01165]
##### FOR OLD DEF OF Wprime
#fitParms['WJets'] = [559.012, 0.959283, 1.89679, 0.943898]
##### FOR OLD DEF OF Wprime with pretag sample
#fitParms['WJets'] = [7611.6, 0.750674, 1.31823, 1.20564]

#def ExtractValue(MC, val):
def ExtractValue(MC, low, high):
    
    par0 = fitParms[MC][0]
    par1 = fitParms[MC][1]
    par2 = fitParms[MC][2]
    par3 = fitParms[MC][3]

    value = par0*ROOT.TMath.LogNormal(val/200.0, par1, par2, par3)
    #print 'FROM FIT value = ',value

    #lognorm =  TF1("lognorm", "TMath::LogNormal(x/200, [0], [1], [2])");
    #lognorm.SetParameters(par1, par2, par3);      
    #value = par0*lognorm.Integral(low,high)
    #print 'FROM FIT value = ',value
 
    return value


def plot_DataVsMc(letter,varName, bin, low, high, ylabel, xlabel, save, wprime, btags, List_to_use):

    cut = 'electron0_pt_el > 35 && electron0_Iso_el < 0.125 && electron0_IDHyperTight1_el == 1 && fabs(PFjet0_eta_el) < 2.4 && fabs(PFjet1_eta_el) < 2.4 && PF_met_pt_el > 35 && fabs(electron0_eleConvDcot_el) > 0.02 && fabs(electron0_eleConvDist_el) > 0.02 '
 
    print varName

    if letter == 'J_a':
        cut = cut + ' && PFjet0_pt_el >= 80 && PFjet1_pt_el >= 40'
    if letter == 'J_b':
        cut = cut + ' && PFjet0_pt_el >= 90 && PFjet1_pt_el >= 40'
    if letter == 'J_c':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40'
    if letter == 'J_d':
        cut = cut + ' && PFjet0_pt_el >= 110 && PFjet1_pt_el >= 40'
    if letter == 'J_e':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 40'
    if letter == 'J_f':
        cut = cut + ' && PFjet0_pt_el >= 130 && PFjet1_pt_el >= 40'

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
    if letter == 'P':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35'
    if letter == 'Q':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && nPFjet < 5 && TransverseMass_W_el > 40'
    if letter == 'R':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && nPFjet < 5 && TransverseMass_W_el > 40 && TopPt_Best_el > 75  && Pt_Jet1Jet2_el > 100'
    if letter == 'S':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && nPFjet < 5 && TopPt_Best_el > 75  && Pt_Jet1Jet2_el > 100'
    if letter == 'T':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'U':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && nPFjet < 5 && TransverseMass_W_el > 40'
    if letter == 'V':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && nPFjet < 5 && TransverseMass_W_el > 40 && TopPt_Best_el > 75  && Pt_Jet1Jet2_el > 100'
    if letter == 'W':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && TopPt_Best_el > 75  && Pt_Jet1Jet2_el > 100 && nPFjet < 5'
    if letter == 'X':
        cut = cut + '&& PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && nPFjet < 5 && TransverseMass_W_el > 40 &&  TopMass_Best_el > 130 && TopMass_Best_el < 210'
    if letter == 'Y':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210'
    if letter == 'Z':
        cut = cut + ' && PFjet0_pt_el >= 120 && PFjet1_pt_el >= 35 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210 && TopPt_Best_bestTop_el > 75  && Pt_Jet1Jet2_bestTop_el > 100'  

    if letter == 'A':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210 && Pt_Jet1Jet2_bestTop_el > 100'
    if letter == 'B':
        cut = cut + ' && PFjet0_pt_el >= 100 && PFjet1_pt_el >= 40 && TopMass_Best_bestTop_el > 130 && TopMass_Best_bestTop_el < 210 && TopPt_BTag_bestTop_el > 50  && Pt_Jet1Jet2_bestTop_el > 100'

    if btags == 0:
        btag = '0b'
        cutbtag = ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el +  weight_BTag_jet2_medium_el + weight_BTag_jet3_medium_el +  weight_BTag_jet4_medium_el +   weight_BTag_jet5_medium_el +  weight_BTag_jet6_medium_el +  weight_BTag_jet7_medium_el ) == 0 )'         
    if btags == 1:
        btag = '1b'
        cutbtag = ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el ) == 1 )'
    if btags == 2:
        btag = '2b'
        cutbtag = ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el ) >= 2 )'
    if btags == 3:
        btag = 'ge1b'
        cutbtag = ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el ) >= 1 )'
    if btags == 4:
        btag = 'ge1btop3'
        cutbtag = ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el + weight_BTag_jet2_medium_el  ) >= 1 )'
    if btags == -1:
        btag = 'Nob'
        cutbtag = ''

                        
    cutwbb = ' &&  n_Bjets_el > 0' # Wb(b)
    cutwcc = ' && n_Bjets_el==0 && n_Cjets_el>0' # Wc(c)
    cutwjj = ' && n_Bjets_el==0 && n_Cjets_el==0' # W+light

    SFWjmu = 0.91
    SFWcmu = 1.07
    SFWbmu = 1.07

    SFWjmuPlus = 0.91*0.8
    SFWcmuPlus = 1.07*1.27
    SFWbmuPlus = 1.07*1.27

    SFWjmuMinus = 0.91*1.2
    SFWcmuMinus = 1.07*0.73
    SFWbmuMinus = 1.07*0.73
   
    cutzerobtags = ' && ( (weight_BTag_jet0_medium_el +  weight_BTag_jet1_medium_el +  weight_BTag_jet2_medium_el + weight_BTag_jet3_medium_el +  weight_BTag_jet4_medium_el +   weight_BTag_jet5_medium_el +  weight_BTag_jet6_medium_el +  weight_BTag_jet7_medium_el ) == 0 )'

    print wprime
    print cut + cutbtag
 
    List = List_to_use
    
    Variables = {}
    #VariablesPUup = {}
    #VariablesPUdown = {}
    Variables0tag = {}
    VariablesHFup = {}
    VariablesHFdown = {}

    VariablesSmooth = {}
    #VariablesSmoothPUup = {}
    #VariablesSmoothPUdown = {}
    VariablesSmooth0tag = {}
    VariablesSmoothHFup = {}
    VariablesSmoothHFdown = {}

    background = 0
    j = 0

    nominalwprime = 'False'

    for Type in List:
    
        if Type.startswith('Wprime'):
           if (nominalwprime == 'False'): binname = copy.copy(Type) 
           nominalwprime = 'True'
    
        prefix = ''
        suffix = ''
        
        if (Type == 'Data'): suffix = 'DATA'
        if (Type == 'WJets'): suffix = 'wjets'
        if (Type == 'WW'): suffix = 'scaledntb'
        if (Type == 'ZJets' or Type == 'QCD_80to170' or Type == 'T_t' or Type == 'Tbar_t' or Type == 'T_tW' or Type == 'Tbar_tW'): suffix = 'scaledntb' + Type
        if (Type == 'TTbar'): suffix = 'ttbar' + Type
        if (Type == 'T_s'): suffix = 'tb'
        if (Type == 'Tbar_s'): suffix = 'tb' + Type 

        if (Type == 'WJets_JES_UP'): suffix = 'wjets_jesUp'
        if (Type == 'WW_JES_UP'): suffix = 'scaledntb_jesUp'
        if (Type == 'TTbar_JES_UP' or Type == 'ZJets_JES_UP' or Type == 'QCD_80to170_JES_UP' or Type == 'T_t_JES_UP' or Type == 'Tbar_t_JES_UP' or Type == 'T_tW_JES_UP' or Type == 'Tbar_tW_JES_UP'): suffix = 'scaledntb_jesUp' + Type
        if (Type == 'TTbar_JES_UP'): suffix = 'scaledall_jesUp' + Type
        if (Type == 'T_s_JES_UP'): suffix = 'tb_jesUp'
        if (Type == 'Tbar_s_JES_UP'): suffix = 'tb_jesUp' + Type 

        if (Type == 'WJets_JES_DOWN'): suffix = 'wjets_jesDown'
        if (Type == 'WW_JES_DOWN'): suffix = 'scaledntb_jesDown'
        if (Type == 'TTbar_JES_DOWN' or Type == 'ZJets_JES_DOWN' or Type == 'QCD_80to170_JES_DOWN' or Type == 'T_t_JES_DOWN' or Type == 'Tbar_t_JES_DOWN' or Type == 'T_tW_JES_DOWN' or Type == 'Tbar_tW_JES_DOWN'): suffix = 'scaledntb_jesDown' + Type
        if (Type == 'TTbar_JES_DOWN'): suffix = 'scaledall_jesDown' + Type
        if (Type == 'T_s_JES_DOWN'): suffix = 'tb_jesDown'
        if (Type == 'Tbar_s_JES_DOWN'): suffix = 'tb_jesDown' + Type 

        if (Type == 'WJets_JER_UP'): suffix = 'wjets_jerUp'
        if (Type == 'WW_JER_UP'): suffix = 'scaledntb_jerUp'
        if (Type == 'TTbar_JER_UP' or Type == 'ZJets_JER_UP' or Type == 'QCD_80to170_JER_UP' or Type == 'T_t_JER_UP' or Type == 'Tbar_t_JER_UP' or Type == 'T_tW_JER_UP' or Type == 'Tbar_tW_JER_UP'): suffix = 'scaledntb_jerUp' + Type
        if (Type == 'TTbar_JER_UP'): suffix = 'scaledall_jerUp' + Type
        if (Type == 'T_s_JER_UP'): suffix = 'tb_jerUp'
        if (Type == 'Tbar_s_JER_UP'): suffix = 'tb_jerUp' + Type 

        if (Type == 'WJets_JER_DOWN'): suffix = 'wjets_jerDown'
        if (Type == 'WW_JER_DOWN'): suffix = 'scaledntb_jerDown'
        if (Type == 'TTbar_JER_DOWN' or Type == 'ZJets_JER_DOWN' or Type == 'QCD_80to170_JER_DOWN' or Type == 'T_t_JER_DOWN' or Type == 'Tbar_t_JER_DOWN' or Type == 'T_tW_JER_DOWN' or Type == 'Tbar_tW_JER_DOWN'): suffix = 'scaledntb_jerDown' + Type
        if (Type == 'TTbar_JER_DOWN'): suffix = 'scaledall_jerDown' + Type
        if (Type == 'T_s_JER_DOWN'): suffix = 'tb_jerDown'
        if (Type == 'Tbar_s_JER_DOWN'): suffix = 'tb_jerDown' + Type 

        if (Type == 'WJets_BTAG_UP'): suffix = 'wjets_btagUp'
        if (Type == 'WW_BTAG_UP'): suffix = 'scaledntb_btagUp'
        if (Type == 'ZJets_BTAG_UP' or Type == 'QCD_80to170_BTAG_UP' or Type == 'T_t_BTAG_UP' or Type == 'Tbar_t_BTAG_UP' or Type == 'T_tW_BTAG_UP' or Type == 'Tbar_tW_BTAG_UP'): suffix = 'scaledntb_btagUp' + Type
        if (Type == 'TTbar_BTAG_UP'): suffix = 'scaledall_btagUp' + Type
        if (Type == 'T_s_BTAG_UP'): suffix = 'tb_btagUp'
        if (Type == 'Tbar_s_BTAG_UP'): suffix = 'tb_btagUp' + Type 

        if (Type == 'WJets_BTAG_DOWN'): suffix = 'wjets_btagDown'
        if (Type == 'WW_BTAG_DOWN'): suffix = 'scaledntb_btagDown'
        if (Type == 'ZJets_BTAG_DOWN' or Type == 'QCD_80to170_BTAG_DOWN' or Type == 'T_t_BTAG_DOWN' or Type == 'Tbar_t_BTAG_DOWN' or Type == 'T_tW_BTAG_DOWN' or Type == 'Tbar_tW_BTAG_DOWN'): suffix = 'scaledntb_btagDown' + Type
        if (Type == 'TTbar_BTAG_DOWN'): suffix = 'scaledall_btagDown' + Type
        if (Type == 'T_s_BTAG_DOWN'): suffix = 'tb_btagDown'
        if (Type == 'Tbar_s_BTAG_DOWN'): suffix = 'tb_btagDown' + Type 

        if (Type == 'WJets_SCALE_UP'): suffix = 'wjets_q2scaleUp'
        if (Type == 'WJets_SCALE_DOWN'): suffix = 'wjets_q2scaleDown'
        if (Type == 'WJets_MATCHING_UP'): suffix = 'wjets_matchingUp'
        if (Type == 'WJets_MATCHING_DOWN'): suffix = 'wjets_matchingDown'
        if (Type == 'TTbar_SCALE_UP'): suffix = 'ttbar_q2scaleUp'
        if (Type == 'TTbar_SCALE_DOWN'): suffix = 'ttbar_q2scaleDown'
        if (Type == 'TTbar_MATCHING_UP'): suffix = 'ttbar_matchingUp'
        if (Type == 'TTbar_MATCHING_DOWN'): suffix = 'ttbar_matchingDown'

        w_suffix = 'wp'

        if (wprime != 'ModRight'):
            if (Type == 'Wprime_800_' + wprime + 'Wprime'): suffix = w_suffix+'800'
            if (Type == 'Wprime_900_' + wprime + 'Wprime'): suffix = w_suffix+'900'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime'): suffix = w_suffix+'1000'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime'): suffix = w_suffix+'1100'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime'): suffix = w_suffix+'1200'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime'): suffix = w_suffix+'1300'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime'): suffix = w_suffix+'1400'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime'): suffix = w_suffix+'1500'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime'): suffix = w_suffix+'1600'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime'): suffix = w_suffix+'1700'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime'): suffix = w_suffix+'1900'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime'): suffix = w_suffix+'2100'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime'): suffix = w_suffix+'2300'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime'): suffix = w_suffix+'2500'

            if (Type == 'Wprime_800_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'800_jesUp'
            if (Type == 'Wprime_900_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'900_jesUp'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1000_jesUp'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1100_jesUp'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1200_jesUp'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1300_jesUp'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1400_jesUp'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1500_jesUp'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1600_jesUp'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1700_jesUp'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'1900_jesUp'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'2100_jesUp'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'2300_jesUp'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime_JES_UP'): suffix = w_suffix+'2500_jesUp'
        
            if (Type == 'Wprime_800_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'800_jesDown'
            if (Type == 'Wprime_900_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'900_jesDown'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1000_jesDown'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1100_jesDown'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1200_jesDown'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1300_jesDown'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1400_jesDown'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1500_jesDown'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1600_jesDown'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1700_jesDown'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'1900_jesDown'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'2100_jesDown'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'2300_jesDown'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime_JES_DOWN'): suffix = w_suffix+'2500_jesDown'

            if (Type == 'Wprime_800_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'800_jerUp'
            if (Type == 'Wprime_900_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'900_jerUp'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1000_jerUp'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1100_jerUp'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1200_jerUp'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1300_jerUp'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1400_jerUp'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1500_jerUp'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1600_jerUp'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1700_jerUp'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'1900_jerUp'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'2100_jerUp'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'2300_jerUp'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime_JER_UP'): suffix = w_suffix+'2500_jerUp'
        
            if (Type == 'Wprime_800_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'800_jerDown'
            if (Type == 'Wprime_900_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'900_jerDown'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1000_jerDown'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1100_jerDown'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1200_jerDown'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1300_jerDown'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1400_jerDown'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1500_jerDown'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1600_jerDown'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1700_jerDown'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'1900_jerDown'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'2100_jerDown'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'2300_jerDown'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime_JER_DOWN'): suffix = w_suffix+'2500_jerDown'

            if (Type == 'Wprime_800_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'800_btagUp'
            if (Type == 'Wprime_900_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'900_btagUp'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1000_btagUp'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1100_btagUp'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1200_btagUp'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1300_btagUp'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1400_btagUp'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1500_btagUp'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1600_btagUp'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1700_btagUp'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'1900_btagUp'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'2100_btagUp'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'2300_btagUp'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime_BTAG_UP'): suffix = w_suffix+'2500_btagUp'
        
            if (Type == 'Wprime_800_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'800_btagDown'
            if (Type == 'Wprime_900_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'900_btagDown'
            if (Type == 'Wprime_1000_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1000_btagDown'
            if (Type == 'Wprime_1100_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1100_btagDown'
            if (Type == 'Wprime_1200_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1200_btagDown'
            if (Type == 'Wprime_1300_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1300_btagDown'
            if (Type == 'Wprime_1400_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1400_btagDown'
            if (Type == 'Wprime_1500_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1500_btagDown'
            if (Type == 'Wprime_1600_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1600_btagDown'
            if (Type == 'Wprime_1700_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1700_btagDown'
            if (Type == 'Wprime_1900_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1900_btagDown'
            if (Type == 'Wprime_2100_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'2100_btagDown'
            if (Type == 'Wprime_2300_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'2300_btagDown'
            if (Type == 'Wprime_2500_' + wprime + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'2500_btagDown'
        else:
            if (Type == 'Wprime_800_' + 'Right' + 'Wprime'): suffix = w_suffix+'800'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime'): suffix = w_suffix+'900'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime'): suffix = w_suffix+'1000'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime'): suffix = w_suffix+'1100'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime'): suffix = w_suffix+'1200'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime'): suffix = w_suffix+'1300'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime'): suffix = w_suffix+'1400'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime'): suffix = w_suffix+'1500'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime'): suffix = w_suffix+'1600'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime'): suffix = w_suffix+'1700'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime'): suffix = w_suffix+'1900'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime'): suffix = w_suffix+'2100'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime'): suffix = w_suffix+'2300'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime'): suffix = w_suffix+'2500'

            if (Type == 'Wprime_800_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'800_jesUp'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'900_jesUp'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1000_jesUp'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1100_jesUp'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1200_jesUp'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1300_jesUp'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1400_jesUp'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1500_jesUp'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1600_jesUp'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1700_jesUp'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'1900_jesUp'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'2100_jesUp'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'2300_jesUp'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime_JES_UP'): suffix = w_suffix+'2500_jesUp'
        
            if (Type == 'Wprime_800_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'800_jesDown'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'900_jesDown'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1000_jesDown'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1100_jesDown'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1200_jesDown'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1300_jesDown'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1400_jesDown'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1500_jesDown'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1600_jesDown'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1700_jesDown'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'1900_jesDown'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'2100_jesDown'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'2300_jesDown'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime_JES_DOWN'): suffix = w_suffix+'2500_jesDown'

            if (Type == 'Wprime_800_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'800_jerUp'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'900_jerUp'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1000_jerUp'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1100_jerUp'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1200_jerUp'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1300_jerUp'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1400_jerUp'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1500_jerUp'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1600_jerUp'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1700_jerUp'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'1900_jerUp'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'2100_jerUp'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'2300_jerUp'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime_JER_UP'): suffix = w_suffix+'2500_jerUp'
        
            if (Type == 'Wprime_800_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'800_jerDown'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'900_jerDown'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1000_jerDown'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1100_jerDown'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1200_jerDown'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1300_jerDown'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1400_jerDown'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1500_jerDown'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1600_jerDown'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1700_jerDown'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'1900_jerDown'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'2100_jerDown'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'2300_jerDown'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime_JER_DOWN'): suffix = w_suffix+'2500_jerDown'

            if (Type == 'Wprime_800_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'800_btagUp'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'900_btagUp'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1000_btagUp'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1100_btagUp'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1200_btagUp'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1300_btagUp'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1400_btagUp'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1500_btagUp'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1600_btagUp'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1700_btagUp'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'1900_btagUp'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'2100_btagUp'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'2300_btagUp'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime_BTAG_UP'): suffix = w_suffix+'2500_btagUp'
        
            if (Type == 'Wprime_800_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'800_btagDown'
            if (Type == 'Wprime_900_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'900_btagDown'
            if (Type == 'Wprime_1000_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1000_btagDown'
            if (Type == 'Wprime_1100_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1100_btagDown'
            if (Type == 'Wprime_1200_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1200_btagDown'
            if (Type == 'Wprime_1300_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1300_btagDown'
            if (Type == 'Wprime_1400_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1400_btagDown'
            if (Type == 'Wprime_1500_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1500_btagDown'
            if (Type == 'Wprime_1600_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1600_btagDown'
            if (Type == 'Wprime_1700_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1700_btagDown'
            if (Type == 'Wprime_1900_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'1900_btagDown'
            if (Type == 'Wprime_2100_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'2100_btagDown'
            if (Type == 'Wprime_2300_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'2300_btagDown'
            if (Type == 'Wprime_2500_' + 'Right' + 'Wprime_BTAG_DOWN'): suffix = w_suffix+'2500_btagDown'
      
        histName = prefix+suffix+'varbin'
        histNamePUup = prefix+suffix+'varbin'+'_PileupUp'
        histNamePUdown = prefix+suffix+'varbin'+'_PileupDown'
        histName0tag = prefix+suffix+'varbin'+'_0tag'
        histNameHFup = prefix+suffix+'varbin'+'_hfUp'
        histNameHFdown = prefix+suffix+'varbin'+'_hfDown'

        histNameSmooth = prefix+suffix
        histNameSmoothPUup = prefix+suffix+'_PileupUp'
        histNameSmoothPUdown = prefix+suffix+'_PileupDown'
        histNameSmooth0tag = prefix+suffix+'0tag'
        histNameSmoothHFup = prefix+suffix+'_hfUp'
        histNameSmoothHFdown = prefix+suffix+'_hfDown'

        SF = 0.985
        Variables[Type] = TH1D(histName, histName, bin, array('d',xlow))  
        Variables[Type].Sumw2()
        #VariablesSmooth[Type] = TH1D(histNameSmooth, histNameSmooth, bin, 0, bin) 
        VariablesSmooth[Type] = TH1D(histNameSmooth, histNameSmooth, bin, array('d',xlow) ) 
        VariablesSmooth[Type].Sumw2()
       
        if (Type == 'WJets'):
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

        if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
            #VariablesPUup[Type] = TH1D(histNamePUup, histNamePUup, bin, array('d',xlow))
            #VariablesPUdown[Type] = TH1D(histNamePUdown, histNamePUdown, bin, array('d',xlow))
            Variables0tag[Type] = TH1D(histName0tag, histName0tag, bin, array('d',xlow))
            VariablesHFup[Type] = TH1D(histNameHFup, histNameHFup, bin, array('d',xlow))
            VariablesHFdown[Type] = TH1D(histNameHFdown, histNameHFdown, bin, array('d',xlow))
            #VariablesPUup[Type].Sumw2()
            #VariablesPUdown[Type].Sumw2()
            Variables0tag[Type].Sumw2()
            VariablesHFup[Type].Sumw2()
            VariablesHFdown[Type].Sumw2()
            #VariablesSmoothPUup[Type] = TH1D(histNameSmoothPUup, histNameSmoothPUup, bin, 0, bin)
            #VariablesSmoothPUdown[Type] = TH1D(histNameSmoothPUdown, histNameSmoothPUdown, bin, 0, bin)
            #VariablesSmooth0tag[Type] = TH1D(histNameSmooth0tag, histNameSmooth0tag, bin, 0, bin)
            #VariablesSmoothHFup[Type] = TH1D(histNameSmoothHFup, histNameSmoothHFup, bin, 0, bin)
            #VariablesSmoothHFdown[Type] = TH1D(histNameSmoothHFdown, histNameSmoothHFdown, bin, 0, bin)
            #VariablesSmoothPUup[Type] = TH1D(histNameSmoothPUup, histNameSmoothPUup, bin, array('d',xlow) )
            #VariablesSmoothPUdown[Type] = TH1D(histNameSmoothPUdown, histNameSmoothPUdown, bin, array('d',xlow) )
            VariablesSmooth0tag[Type] = TH1D(histNameSmooth0tag, histNameSmooth0tag, bin, array('d',xlow) )
            VariablesSmoothHFup[Type] = TH1D(histNameSmoothHFup, histNameSmoothHFup, bin, array('d',xlow) )
            VariablesSmoothHFdown[Type] = TH1D(histNameSmoothHFdown, histNameSmoothHFdown, bin, array('d',xlow) )
            #VariablesSmoothPUup[Type].Sumw2()
            #VariablesSmoothPUdown[Type].Sumw2()
            VariablesSmooth0tag[Type].Sumw2()
            VariablesSmoothHFup[Type].Sumw2()
            VariablesSmoothHFdown[Type].Sumw2()   

        #print Type
        if (Type == 'Data'):
            Trees[Type].Draw(var + " >> " + histName, "(" + cut + cutbtag + ")", 'goff')
            # 0 tag for data-driven shape
            Trees[Type].Draw(var + " >> " + histName0tag, "(" + cut + cutzerobtags + ")", 'goff')
        elif (Type.startswith('WJets')): # Here we go...
            ############################################
            ##### >= 1 btag
            ############################################
            #Trees[Type].Draw(var + " >> " + histName, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*(" + cut + cutbtag + ")", 'goff')
            #if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
            #    Trees[Type].Draw(var+" >> "+histNamePUup,"(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*("+cut+cutbtag+")",'goff')
            #    Trees[Type].Draw(var+" >> "+ histNamePUdown,"(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*("+cut+cutbtag+")",'goff')
            #Trees[Type].Draw(var+" >> "+histName,"(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*(" + cut + ")", 'goff')
            ############################################
            ##### Pretag, to be scaled down later
            ############################################
            # here keep weight_WxsecNoLight_comb in case we need to change the scale factors later             
            Trees[Type].Draw(var+" >> "+histName,"(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWjmu)+")*("+cut+cutwjj+")",'goff')
            Trees[Type].Draw(var+" >> "+"WbbHist","(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWbmu)+")*("+cut+cutwbb+")",'goff')
            Trees[Type].Draw(var+" >> "+"WccHist","(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWcmu)+")*("+cut+cutwcc+")",'goff') 
            Variables[Type].Add(WbbHist)
            Variables[Type].Add(WccHist)
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ): 
                # Pile Up 
                # here we do weight_Wxsec_comb because we don't need to vary the h.f. factors                                    
                #Trees[Type].Draw(var+" >> "+histNamePUup,"(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*("+cut+cutbtag+")",'goff')
                #Trees[Type].Draw(var+" >> "+histNamePUdown,"(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*("+cut+cutbtag+")",'goff')
                # 0 tag shape (one sided, so only one histogram)
                # here we do weight_Wxsec_comb because we don't need to vary the h.f. factors
                Trees[Type].Draw(var+" >> "+histName0tag,"(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_Wxsec_comb)*("+cut+cutzerobtags+")",'goff')
                # H.F. k-factor  
                # here we need weight_WxsecNoLight_comb              
                Trees[Type].Draw(var+" >> "+histNameHFup,"(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWjmuPlus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHistHFup","(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWbmuPlus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHistHFup","(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWcmuPlus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFup[Type].Add(WbbHistHFup)
                VariablesHFup[Type].Add(WccHistHFup)
                Trees[Type].Draw(var+" >> "+histNameHFdown,"(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWjmuMinus)+")*("+cut+cutwjj+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WbbHistHFdown","(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWbmuMinus)+")*("+cut+cutwbb+cutbtag+")",'goff')
                Trees[Type].Draw(var+" >> "+"WccHistHFdown","(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*("+str(SFWcmuMinus)+")*("+cut+cutwcc+cutbtag+")",'goff')
                VariablesHFdown[Type].Add(WbbHistHFdown)
                VariablesHFdown[Type].Add(WccHistHFdown)
        elif (not Type.startswith('T')):
            Trees[Type].Draw(var + " >> " + histName, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el)*(" + cut + ")", 'goff')
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
                #Trees[Type].Draw(var + " >> " + histNamePUup, "(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
                #Trees[Type].Draw(var + " >> " + histNamePUdown, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histName0tag, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutzerobtags + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFup, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
        else:
            Trees[Type].Draw(var + " >> " + histName, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
                #Trees[Type].Draw(var + " >> " + histNamePUup, "(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
                #Trees[Type].Draw(var + " >> " + histNamePUdown, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histName0tag, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutzerobtags + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFup, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histNameHFdown, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + cutbtag + ")", 'goff')


        if Type != 'Data':
            if Variables[Type].Integral() != 0:
                Variables[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ): 
                    #VariablesPUup[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                    #VariablesPUdown[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) )
                    Variables0tag[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) )  
                    VariablesHFup[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                    VariablesHFdown[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) )
    

        ######################################### 
        ### REBIN TO HAVE EVEN SIZED BINS  
        #########################################
       
        for x in range(1,bin+1):  
            VariablesSmooth[Type].SetBinContent(x,Variables[Type].GetBinContent(x) )
            VariablesSmooth[Type].SetBinError(x,Variables[Type].GetBinError(x) )
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):
                #VariablesSmoothPUup[Type].SetBinContent(x,VariablesPUup[Type].GetBinContent(x) )
                #VariablesSmoothPUup[Type].SetBinError(x,VariablesPUup[Type].GetBinError(x) )
                #VariablesSmoothPUdown[Type].SetBinContent(x,VariablesPUdown[Type].GetBinContent(x) )
                #VariablesSmoothPUdown[Type].SetBinError(x,VariablesPUdown[Type].GetBinError(x) )
                VariablesSmooth0tag[Type].SetBinContent(x,Variables0tag[Type].GetBinContent(x) )
                VariablesSmoothHFup[Type].SetBinContent(x,VariablesHFup[Type].GetBinContent(x) )
                VariablesSmoothHFdown[Type].SetBinContent(x,VariablesHFdown[Type].GetBinContent(x) )
                VariablesSmooth0tag[Type].SetBinError(x,Variables0tag[Type].GetBinError(x) )
                VariablesSmoothHFup[Type].SetBinError(x,VariablesHFup[Type].GetBinError(x) )
                VariablesSmoothHFdown[Type].SetBinError(x,VariablesHFdown[Type].GetBinError(x) )
        VariablesSmooth[Type].SetEntries(Variables[Type].GetEntries() )
        if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):
            #VariablesSmoothPUup[Type].SetEntries(VariablesPUup[Type].GetEntries() )
            #VariablesSmoothPUdown[Type].SetEntries(VariablesPUdown[Type].GetEntries() )
            VariablesSmooth0tag[Type].SetEntries(Variables0tag[Type].GetEntries() )
            VariablesSmoothHFup[Type].SetEntries(VariablesHFup[Type].GetEntries() )
            VariablesSmoothHFdown[Type].SetEntries(VariablesHFdown[Type].GetEntries() )

        if (Type == 'Data'):
            print 'EVENTS FOR  Data  = ',int(VariablesSmooth[Type].Integral())
            if VariablesSmooth[Type].GetBinContent(bin+1)!=0: print 'OVERFLOW!!!!!!'
            if VariablesSmooth[Type].GetBinContent(0)!=0: print 'UNDERFLOW!!!!!!'

        ######################################### 
        ### Set 0 B.G. Bins to something !=0 
        #########################################

        if (Type != 'Data'):
            if ( not Type.startswith('Wprime') ):
                for x in range(1,bin+1):
                    if (VariablesSmooth[Type].GetBinContent(x) < 0.000001 ): 
                        #print 'Setting ',VariablesSmooth[Type].GetBinContent(x),' to 10E-6 for bin ',x,' of ',Type
                        VariablesSmooth[Type].SetBinContent(x,0.000001)
                    if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ): 
                        #if (VariablesSmoothPUup[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothPUup[Type].SetBinContent(x,0.00001)
                        #if (VariablesSmoothPUdown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothPUdown[Type].SetBinContent(x,0.00001)
                        if (VariablesSmooth0tag[Type].GetBinContent(x) < 0.000001 ): VariablesSmooth0tag[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothHFup[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothHFup[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothHFdown[Type].GetBinContent(x) < 0.000001 ): VariablesSmoothHFdown[Type].SetBinContent(x,0.00001)

            print 'J = ',j, 'EVENTS FOR ',Type,'  = ',str(int(round((Variables[Type].Integral()))))

            if j < 11:
                background = background + Variables[Type].Integral()

        j = j + 1  

    VariablesSmooth['Data'].SetName("data_obs")
    VariablesSmooth['Data'].Write()

    VariablesSmooth['WW'].Add(VariablesSmooth['ZJets'])
    VariablesSmooth['WW'].Add(VariablesSmooth['QCD_80to170'])
    VariablesSmooth['WJets'].Add(VariablesSmooth['WW'])
    VariablesSmooth['WJets'].SetName("wjets")
    ######################################### 
    ### REBIN W+Jets BASED ON FIT FUCNTION  
    #########################################
    # ratio = 0.09654 
    VariablesSmooth['WJets'].Scale( 0.09654 )
    VariablesSmooth['WJets'].Write()

    VariablesSmooth['TTbar'].SetName("ttbar")
    VariablesSmooth['T_t'].Add(VariablesSmooth['Tbar_t'])
    VariablesSmooth['T_t'].Add(VariablesSmooth['T_tW'])
    VariablesSmooth['T_t'].Add(VariablesSmooth['Tbar_tW'])
    VariablesSmooth['TTbar'].Add( VariablesSmooth['T_t'])

    VariablesSmooth['T_s'].Add(VariablesSmooth['Tbar_s']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar'].Write()
            VariablesSmooth['T_s'].SetName("topstb")
            VariablesSmooth['T_s'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar'].Add(VariablesSmooth['T_s'])
            VariablesSmooth['TTbar'].Write()

    print 'Data = ', VariablesSmooth['Data'].Integral()
    print 'Total background = ', VariablesSmooth['TTbar'].Integral()+VariablesSmooth['WJets'].Integral()
    print 'Background / Data = ', (VariablesSmooth['TTbar'].Integral()+VariablesSmooth['WJets'].Integral())/VariablesSmooth['Data'].Integral()

    ##### JES UP ##### 
    VariablesSmooth['WW_JES_UP'].Add(VariablesSmooth['ZJets_JES_UP'])
    VariablesSmooth['WW_JES_UP'].Add(VariablesSmooth['QCD_80to170_JES_UP'])
    VariablesSmooth['WJets_JES_UP'].Add(VariablesSmooth['WW_JES_UP'])
    VariablesSmooth['WJets_JES_UP'].SetName("wjets_jesUp")
    ######################################### 
    ### REBIN W+Jets JES UP   
    #########################################
    #ratio = 0.09659
    VariablesSmooth['WJets_JES_UP'].Scale( 0.09659 )
    VariablesSmooth['WJets_JES_UP'].Write()

    VariablesSmooth['TTbar_JES_UP'].SetName("ttbar_jesUp")
    VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['Tbar_t_JES_UP'])
    VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['T_tW_JES_UP'])
    VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['Tbar_tW_JES_UP'])
    VariablesSmooth['TTbar_JES_UP'].Add( VariablesSmooth['T_t_JES_UP'])

    VariablesSmooth['T_s_JES_UP'].Add(VariablesSmooth['Tbar_s_JES_UP']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_JES_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_JES_UP'].Write()
            VariablesSmooth['T_s_JES_UP'].SetName("topstb_jesUp")
            VariablesSmooth['T_s_JES_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_JES_UP'].Add(VariablesSmooth['T_s_JES_UP'])
            VariablesSmooth['TTbar_JES_UP'].Write()

    ##### JES DOWN #####
    VariablesSmooth['WW_JES_DOWN'].Add(VariablesSmooth['ZJets_JES_DOWN'])
    VariablesSmooth['WW_JES_DOWN'].Add(VariablesSmooth['QCD_80to170_JES_DOWN'])
    VariablesSmooth['WJets_JES_DOWN'].Add(VariablesSmooth['WW_JES_DOWN'])
    VariablesSmooth['WJets_JES_DOWN'].SetName("wjets_jesDown")
    ######################################### 
    ### REBIN W+Jets JES UP   
    #########################################
    #ratio = 0.09758
    VariablesSmooth['WJets_JES_DOWN'].Scale( 0.09758 )
    VariablesSmooth['WJets_JES_DOWN'].Write()

    VariablesSmooth['TTbar_JES_DOWN'].SetName("ttbar_jesDown")
    VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['Tbar_t_JES_DOWN'])
    VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['T_tW_JES_DOWN'])
    VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['Tbar_tW_JES_DOWN'])
    VariablesSmooth['TTbar_JES_DOWN'].Add( VariablesSmooth['T_t_JES_DOWN'])

    VariablesSmooth['T_s_JES_DOWN'].Add(VariablesSmooth['Tbar_s_JES_DOWN']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_JES_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_JES_DOWN'].Write()
            VariablesSmooth['T_s_JES_DOWN'].SetName("topstb_jesDown")
            VariablesSmooth['T_s_JES_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_JES_DOWN'].Add(VariablesSmooth['T_s_JES_DOWN'])
            VariablesSmooth['TTbar_JES_DOWN'].Write()


    ##### BTAG UP #####
    #VariablesSmooth['WW_BTAG_UP'].Add(VariablesSmooth['ZJets_BTAG_UP'])
    #VariablesSmooth['WW_BTAG_UP'].Add(VariablesSmooth['QCD_80to170_BTAG_UP'])
    #VariablesSmooth['WJets_BTAG_UP'].Add(VariablesSmooth['WW_BTAG_UP'])
    VariablesSmooth['WJets_BTAG_UP'].SetName("wjets_btagUp")
    ######################################### 
    ### REBIN W+Jets BTAG BASED ON RATIO FIT 
    #########################################
    for step in range(len(xlow)):
        #if Variables['Data'].GetBinLowEdge(step) >= 500:  
        ratio = 1.0/0.9162
        #print 'Wjets = ',Variables['WJets'].GetBinContent(step)
        Variables['WJets_BTAG_UP'].SetBinContent(step, Variables['WJets'].GetBinContent(step)*ratio )
    VariablesSmooth['WJets_BTAG_UP'].Write()

    VariablesSmooth['TTbar_BTAG_UP'].SetName("ttbar_btagUp")
    VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['Tbar_t_BTAG_UP'])
    VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['T_tW_BTAG_UP'])
    VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['Tbar_tW_BTAG_UP'])
    VariablesSmooth['TTbar_BTAG_UP'].Add( VariablesSmooth['T_t_BTAG_UP'])

    VariablesSmooth['T_s_BTAG_UP'].Add(VariablesSmooth['Tbar_s_BTAG_UP']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_BTAG_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_BTAG_UP'].Write()
            VariablesSmooth['T_s_BTAG_UP'].SetName("topstb_btagUp")
            VariablesSmooth['T_s_BTAG_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_BTAG_UP'].Add(VariablesSmooth['T_s_BTAG_UP'])
            VariablesSmooth['TTbar_BTAG_UP'].Write()

    ##### BTAG DOWN #####
    #VariablesSmooth['WW_BTAG_DOWN'].Add(VariablesSmooth['ZJets_BTAG_DOWN'])
    #VariablesSmooth['WW_BTAG_DOWN'].Add(VariablesSmooth['QCD_80to170_BTAG_DOWN'])
    #VariablesSmooth['WJets_BTAG_DOWN'].Add(VariablesSmooth['WW_BTAG_DOWN'])
    VariablesSmooth['WJets_BTAG_DOWN'].SetName("wjets_btagDown")
    ######################################### 
    ### REBIN W+Jets BTAG BASED ON RATIO FIT 
    #########################################
    for step in range(len(xlow)):
        #if Variables['Data'].GetBinLowEdge(step) >= 500:  
        ratio = 1.0/1.099
        #print 'Wjets = ',Variables['WJets'].GetBinContent(step)
        Variables['WJets_BTAG_DOWN'].SetBinContent(step, Variables['WJets'].GetBinContent(step)*ratio )
    VariablesSmooth['WJets_BTAG_DOWN'].Write()

    VariablesSmooth['TTbar_BTAG_DOWN'].SetName("ttbar_btagDown")
    VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['Tbar_t_BTAG_DOWN'])
    VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['T_tW_BTAG_DOWN'])
    VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['Tbar_tW_BTAG_DOWN'])
    VariablesSmooth['TTbar_BTAG_DOWN'].Add( VariablesSmooth['T_t_BTAG_DOWN'])

    VariablesSmooth['T_s_BTAG_DOWN'].Add(VariablesSmooth['Tbar_s_BTAG_DOWN']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_BTAG_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_BTAG_DOWN'].Write()
            VariablesSmooth['T_s_BTAG_DOWN'].SetName("topstb_btagDown")
            VariablesSmooth['T_s_BTAG_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_BTAG_DOWN'].Add(VariablesSmooth['T_s_BTAG_DOWN'])
            VariablesSmooth['TTbar_BTAG_DOWN'].Write()

    ##### JER UP #####
    VariablesSmooth['WW_JER_UP'].Add(VariablesSmooth['ZJets_JER_UP'])
    VariablesSmooth['WW_JER_UP'].Add(VariablesSmooth['QCD_80to170_JER_UP'])
    VariablesSmooth['WJets_JER_UP'].Add(VariablesSmooth['WW_JER_UP'])
    VariablesSmooth['WJets_JER_UP'].SetName("wjets_jerUp")
    #########################################
    ### REBIN W+Jets JER UP
    #########################################
    #ratio = 0.09533
    VariablesSmooth['WJets_JER_UP'].Scale( 0.09533 )
    VariablesSmooth['WJets_JER_UP'].Write()

    VariablesSmooth['TTbar_JER_UP'].SetName("ttbar_jerUp")
    VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['Tbar_t_JER_UP'])
    VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['T_tW_JER_UP'])
    VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['Tbar_tW_JER_UP'])
    VariablesSmooth['TTbar_JER_UP'].Add( VariablesSmooth['T_t_JER_UP'])

    VariablesSmooth['T_s_JER_UP'].Add(VariablesSmooth['Tbar_s_JER_UP']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_JER_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_JER_UP'].Write()
            VariablesSmooth['T_s_JER_UP'].SetName("topstb_jerUp")
            VariablesSmooth['T_s_JER_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_JER_UP'].Add(VariablesSmooth['T_s_JER_UP'])
            VariablesSmooth['TTbar_JER_UP'].Write()
 
    ##### JER DOWN #####
    VariablesSmooth['WW_JER_DOWN'].Add(VariablesSmooth['ZJets_JER_DOWN'])
    VariablesSmooth['WW_JER_DOWN'].Add(VariablesSmooth['QCD_80to170_JER_DOWN'])
    VariablesSmooth['WJets_JER_DOWN'].Add(VariablesSmooth['WW_JER_DOWN'])
    VariablesSmooth['WJets_JER_DOWN'].SetName("wjets_jerDown")
    #########################################
    ### REBIN W+Jets JER DOWN   
    #########################################
    #ratio = 0.09639
    VariablesSmooth['WJets_JER_DOWN'].Scale( 0.09639 )
    VariablesSmooth['WJets_JER_DOWN'].Write()

    VariablesSmooth['TTbar_JER_DOWN'].SetName("ttbar_jerDown")
    VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['Tbar_t_JER_DOWN'])
    VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['T_tW_JER_DOWN'])
    VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['Tbar_tW_JER_DOWN'])
    VariablesSmooth['TTbar_JER_DOWN'].Add( VariablesSmooth['T_t_JER_DOWN'])

    VariablesSmooth['T_s_JER_DOWN'].Add(VariablesSmooth['Tbar_s_JER_DOWN']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_JER_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_JER_DOWN'].Write()
            VariablesSmooth['T_s_JER_DOWN'].SetName("topstb_jerDown")
            VariablesSmooth['T_s_JER_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_JER_DOWN'].Add(VariablesSmooth['T_s_JER_DOWN'])
            VariablesSmooth['TTbar_JER_DOWN'].Write()

    
    '''
    ##### PU Down ######
    VariablesSmoothPUdown['WW'].Add(VariablesSmoothPUdown['ZJets'])
    VariablesSmoothPUdown['WW'].Add(VariablesSmoothPUdown['QCD_80to170'])
    VariablesSmoothPUdown['WJets'].Add(VariablesSmoothPUdown['WW'])
    VariablesSmoothPUdown['WJets'].SetName("wjets_PileupDown")
    VariablesSmoothPUdown['WJets'].Write()

    VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['Tbar_t'])
    VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['T_tW'])
    VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['Tbar_tW'])
    VariablesSmoothPUdown['TTbar'].Add( VariablesSmoothPUdown['T_t'])
    VariablesSmoothPUdown['TTbar'].SetName("ttbar_PileupDown")

    VariablesSmoothPUdown['T_s'].Add(VariablesSmoothPUdown['Tbar_s']) 

    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmoothPUdown['TTbar'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmoothPUdown['TTbar'].Write()
            VariablesSmoothPUdown['T_s'].SetName("topstb_PileupDown")
            VariablesSmoothPUdown['T_s'].Write()
        elif (wprime == 'Right'):
            VariablesSmoothPUdown['TTbar'].Add(VariablesSmoothPUdown['T_s'])
            VariablesSmoothPUdown['TTbar'].Write()
  

    ##### PU Up#####
    VariablesSmoothPUup['WW'].Add(VariablesSmoothPUup['ZJets'])
    VariablesSmoothPUup['WW'].Add(VariablesSmoothPUup['QCD_80to170'])
    VariablesSmoothPUup['WJets'].Add(VariablesSmoothPUup['WW'])
    VariablesSmoothPUup['WJets'].SetName("wjets_PileupUp")
    VariablesSmoothPUup['WJets'].Write()

    VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['Tbar_t'])
    VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['T_tW'])
    VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['Tbar_tW'])
    VariablesSmoothPUup['TTbar'].Add( VariablesSmoothPUup['T_t'])
    VariablesSmoothPUup['TTbar'].SetName("ttbar_PileupUp")

    VariablesSmoothPUup['T_s'].Add(VariablesSmoothPUup['Tbar_s']) 

    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmoothPUup['TTbar'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmoothPUup['TTbar'].Write()
            VariablesSmoothPUup['T_s'].SetName("topstb_PileupUp")
            VariablesSmoothPUup['T_s'].Write()
        elif (wprime == 'Right'):
            VariablesSmoothPUup['TTbar'].Add(VariablesSmoothPUup['T_s'])
            VariablesSmoothPUup['TTbar'].Write()
    '''

    mass = copy.copy(binname)
    mass = mass.lstrip('Wprime_')
    mass = mass.rstrip('_'+wprime+'Wprime')

    if (wprime != 'ModRight'):
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime_JES_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime_JES_DOWN'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime_JER_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime_JER_DOWN'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime_BTAG_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + wprime + 'Wprime_BTAG_DOWN'].Write()
        #VariablesSmoothPUup['Wprime_'+mass+'_' + wprime + 'Wprime'].Write()    
        #VariablesSmoothPUdown['Wprime_'+mass+'_' + wprime + 'Wprime'].Write()
    else:
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JES_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JES_DOWN'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JER_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JER_DOWN'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_BTAG_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_BTAG_DOWN'].Write()
        #VariablesSmoothPUup['Wprime_'+mass+'_' + 'Right' + 'Wprime'].Write()    
        #VariablesSmoothPUdown['Wprime_'+mass+'_' + 'Right' + 'Wprime'].Write()

    VariablesSmooth['TTbar_MATCHING_DOWN'].Add(VariablesSmooth['T_t'])
    VariablesSmooth['TTbar_MATCHING_DOWN'].SetName("ttbar_matchingDown")
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_MATCHING_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_MATCHING_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_MATCHING_DOWN'].Add(VariablesSmooth['T_s'])
            VariablesSmooth['TTbar_MATCHING_DOWN'].Write()

    VariablesSmooth['TTbar_MATCHING_UP'].Add(VariablesSmooth['T_t'])
    VariablesSmooth['TTbar_MATCHING_UP'].SetName("ttbar_matchingUp")
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_MATCHING_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_MATCHING_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_MATCHING_UP'].Add(VariablesSmooth['T_s'])
            VariablesSmooth['TTbar_MATCHING_UP'].Write()

    VariablesSmooth['TTbar_SCALE_DOWN'].Add(VariablesSmooth['T_t'])
    VariablesSmooth['TTbar_SCALE_DOWN'].SetName("ttbar_q2scaleDown")
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_SCALE_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_SCALE_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_SCALE_DOWN'].Add(VariablesSmooth['T_s'])
            VariablesSmooth['TTbar_SCALE_DOWN'].Write()

    VariablesSmooth['TTbar_SCALE_UP'].Add(VariablesSmooth['T_t'])
    VariablesSmooth['TTbar_SCALE_UP'].SetName("ttbar_q2scaleUp")
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['TTbar_SCALE_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['TTbar_SCALE_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['TTbar_SCALE_UP'].Add(VariablesSmooth['T_s'])
            VariablesSmooth['TTbar_SCALE_UP'].Write()

    '''
    VariablesSmooth['WJets_MATCHING_DOWN'].Add(VariablesSmooth['WW'])
    VariablesSmooth['WJets_MATCHING_DOWN'].SetName("wjets__matching__minus")
    VariablesSmooth['WJets_MATCHING_DOWN'].Write()

    VariablesSmooth['WJets_MATCHING_UP'].Add(VariablesSmooth['WW'])
    VariablesSmooth['WJets_MATCHING_UP'].SetName("wjets__matching__plus")
    VariablesSmooth['WJets_MATCHING_UP'].Write()

    VariablesSmooth['WJets_SCALE_DOWN'].Add(VariablesSmooth['WW'])
    VariablesSmooth['WJets_SCALE_DOWN'].SetName("wjets__q2scale__minus")
    VariablesSmooth['WJets_SCALE_DOWN'].Write()

    VariablesSmooth['WJets_SCALE_UP'].Add(VariablesSmooth['WW'])
    VariablesSmooth['WJets_SCALE_UP'].SetName("wjets__q2scale__plus")
    VariablesSmooth['WJets_SCALE_UP'].Write()
    '''

    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['TTbar'],-1)
    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['T_t'],-1)
    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['Tbar_t'],-1)
    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['T_tW'],-1)
    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['Tbar_tW'],-1)
    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['T_s'],-1)
    VariablesSmooth0tag['Data'].Add(VariablesSmooth0tag['Tbar_s'],-1)
    VariablesSmooth0tag['Data'].Scale(VariablesSmooth['WJets'].Integral()/VariablesSmooth0tag['Data'].Integral())
    VariablesSmooth0tag['Data'].SetName("wjets_zerotagUp")
    for x in range(1,bin+1):  
        VariablesSmooth0tag['Data'].SetBinError(x, math.sqrt(VariablesSmooth0tag['Data'].GetBinContent(x)) )
    VariablesSmooth0tag['Data'].Write()
    VariablesSmooth0tag['WJetsDown'] = VariablesSmooth['WJets'].Clone()
    VariablesSmooth0tag['WJetsDown'].SetName("wjets_zerotagDown")
    VariablesSmooth0tag['WJetsDown'].Write()

    VariablesSmoothHFup['WW'].Add(VariablesSmoothHFup['ZJets'])
    VariablesSmoothHFup['WW'].Add(VariablesSmoothHFup['QCD_80to170'])
    VariablesSmoothHFup['WJets'].Add(VariablesSmoothHFup['WW'])
    VariablesSmoothHFup['WJets'].SetName("wjets_hfUp")
    VariablesSmoothHFup['WJets'].Write()
    VariablesSmoothHFdown['WW'].Add(VariablesSmoothHFdown['ZJets'])
    VariablesSmoothHFdown['WW'].Add(VariablesSmoothHFdown['QCD_80to170'])
    VariablesSmoothHFdown['WJets'].Add(VariablesSmoothHFdown['WW'])
    VariablesSmoothHFdown['WJets'].SetName("wjets_hfDown")
    VariablesSmoothHFdown['WJets'].Write()

    # Need to fix, this only works for WprimeRight because nbackgrounds is harcoded = 2
    datacard = open('datacards/datacard_'+binname+'_el.txt', 'w')       
    datacard.write( "# W'->tb datacard "+binname+' \n')
    datacard.write( 'imax 1  number of channels \n')
    datacard.write( 'jmax 2  number of backgrounds \n')
    datacard.write( 'kmax 11  number of nuisance parameters \n') 
    datacard.write( '--------------- \n')
    datacard.write( 'shapes * * '+str(f.GetName())+' $CHANNEL/$PROCESS  $CHANNEL/$PROCESS_$SYSTEMATIC \n' )
    datacard.write( '--------------- \n')
    datacard.write( 'bin '+binname+' \n')
    datacard.write( 'observation '+str(round(Variables['Data'].Integral(),3))+' \n')
    datacard.write( '--------------- \n')
    datacard.write( 'bin             '+binname+' '+binname+' '+binname+'  \n') 
    datacard.write( 'process         wp'+str(mass)+'    ttbar   wjets  \n')
    datacard.write( 'process          0        1       2     \n')  
    datacard.write( 'rate            '+str(round(VariablesSmooth[binname].Integral(),3))+'      '+str(round(VariablesSmooth['TTbar'].Integral(),3))+'    '+str(round(VariablesSmooth['WJets'].Integral(),3))+'  \n')
    datacard.write( '--------------- \n')
    datacard.write( 'lumi       lnN    1.045    1.045   1.045   \n')
    datacard.write( 'bgnorm     lnN    1.00     1.15    1.30    \n')
    datacard.write( 'trgeff     lnN    1.03     1.03    1.03    \n')
    datacard.write( 'ideff      lnN    1.03     1.03    1.03    \n')
    datacard.write( 'jes      shape    1        1       1       \n')
    datacard.write( 'jer      shape    1        1       1       \n')
    datacard.write( 'btag     shape    1        1       1       \n')
    datacard.write( 'q2scale  shape    -        1       -       \n')
    datacard.write( 'matching shape    -        1       -       \n')
    datacard.write( 'hf       shape    -        -       1       \n')
    datacard.write( 'zerotag  shape    -        -       1       \n')
    datacard.close()


  
#wprime = 'Right'
var = 'BestJetJet2W_M_bestTop_el'; high = 3500; xaxis = "W' invariant mass [GeV/c^{2}]"; yaxis = 'Events / 10 GeV'; save = 'BestJetJet2W_M_bestTop_el'
#btags = 0
#btagstr = '0btags'
btags = 3
btagstr = 'ge1b'
letter = 'O'

wprime = 'Right'
# Wprime_800_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1220, 3500]
xlow  = [ 200, 300,  400, 500, 600, 700, 800, 900,  1000, 1100, 1200,  1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 3500]
f = TFile("RootFiles_ForHiggsLimits/"+letter+"_bestTop_Wprime_"+wprime+"_Histos_electrons-"+btagstr+".root","RECREATE")
bins = len(xlow)-1 
List_DataBg_Wprime_800_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_800_RightWprime.extend(List_Wprime_800_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_800_RightWprime') 
f.cd('Wprime_800_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_800_RightWprime) 


# Wprime_900_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1270, 1420, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_900_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_900_RightWprime.extend(List_Wprime_900_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_900_RightWprime') 
f.cd('Wprime_900_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_900_RightWprime) 


# Wprime_1000_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1420, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1000_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1000_RightWprime.extend(List_Wprime_1000_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1000_RightWprime') 
f.cd('Wprime_1000_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1000_RightWprime) 


# Wprime_1100_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1420, 1520, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1100_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1100_RightWprime.extend(List_Wprime_1100_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1100_RightWprime') 
f.cd('Wprime_1100_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1100_RightWprime) 


# Wprime_1200_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1200_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1200_RightWprime.extend(List_Wprime_1200_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1200_RightWprime') 
f.cd('Wprime_1200_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1200_RightWprime) 


# Wprime_1300_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1300_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1300_RightWprime.extend(List_Wprime_1300_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1300_RightWprime') 
f.cd('Wprime_1300_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1300_RightWprime) 


# Wprime_1400_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1400_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1400_RightWprime.extend(List_Wprime_1400_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1400_RightWprime') 
f.cd('Wprime_1400_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1400_RightWprime) 


# Wprime_1500_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1500_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1500_RightWprime.extend(List_Wprime_1500_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1500_RightWprime') 
f.cd('Wprime_1500_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1500_RightWprime) 


# Wprime_1600_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1600_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1600_RightWprime.extend(List_Wprime_1600_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1600_RightWprime') 
f.cd('Wprime_1600_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1600_RightWprime) 


# Wprime_1700_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1700_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1700_RightWprime.extend(List_Wprime_1700_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1700_RightWprime') 
f.cd('Wprime_1700_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1700_RightWprime) 


# Wprime_1900_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1900_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1900_RightWprime.extend(List_Wprime_1900_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1900_RightWprime') 
f.cd('Wprime_1900_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1900_RightWprime) 


# Wprime_2100_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_2100_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_2100_RightWprime.extend(List_Wprime_2100_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_2100_RightWprime') 
f.cd('Wprime_2100_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_2100_RightWprime) 


# Wprime_2300_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_2300_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_2300_RightWprime.extend(List_Wprime_2300_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_2300_RightWprime') 
f.cd('Wprime_2300_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_2300_RightWprime) 


# Wprime_2500_RightWprime BestJetJet2W_M_bestTop_el
#xlow = [170, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1670, 1920, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_2500_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_2500_RightWprime.extend(List_Wprime_2500_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_2500_RightWprime') 
f.cd('Wprime_2500_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_2500_RightWprime) 
