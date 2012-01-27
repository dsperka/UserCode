import ROOT, sys, os, re, string
from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH1D, TH2F,TF1, TPad, TPaveLabel, TPaveText, TLegend, TLatex, THStack
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double, gPad

from array import array
import copy

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


    cutwbb = ' &&  n_Bjets_el > 0' # Wb(b)
    cutwcc = ' && n_Bjets_el==0 && n_Cjets_el>0' # Wc(c)
    cutwjj = ' && n_Bjets_el==0 && n_Cjets_el==0' # W+light

    SFWjmu = 0.91
    SFWcmu = 1.07
    SFWbmu = 1.07
  
    print wprime
    print cut
 
    List = List_to_use
    
    Variables = {}
    VariablesPUup = {}
    VariablesPUdown = {}

    VariablesSmooth = {}
    VariablesSmoothPUup = {}
    VariablesSmoothPUdown = {}

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
        
        histName = prefix + suffix+'pre'
        histNamePUup = prefix + suffix+'pre' + '_PileupUp'
        histNamePUdown = prefix + suffix+'pre' + '_PileupDown'

        histNameSmooth = prefix + suffix
        histNameSmoothPUup = prefix + suffix + '_PileupUp'
        histNameSmoothPUdown = prefix + suffix + '_PileupDown'

        #print histName
        #print Type, '  ',histName
               
        SF = 0.985
        #if Type == 'WJets': SF *= 0.930
        #if Type == 'TTbar': SF *= (165/157.5)
        #Variables[Type] = TH1D(histName, histName, bin, low, high)
        Variables[Type] = TH1D(histName, histName, bin, array('d',xlow)) 
        Variables[Type].Sumw2()
        VariablesSmooth[Type] = TH1D(histNameSmooth, histNameSmooth, bin, 0, bin) 
        VariablesSmooth[Type].Sumw2()
        
        if ( Type.startswith('WJets') ):
            WccHist = TH1D('WccHist', 'WccHist', bin,array('d',xlow))
            WbbHist = TH1D('WbbHist', 'WbbHist', bin,array('d',xlow))
            WccHist.Sumw2()
            WbbHist.Sumw2()
 
        if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
            VariablesPUup[Type] = TH1D(histNamePUup, histNamePUup, bin, array('d',xlow))
            VariablesPUdown[Type] = TH1D(histNamePUdown, histNamePUdown, bin, array('d',xlow))
            VariablesPUup[Type].Sumw2()
            VariablesPUdown[Type].Sumw2()
            VariablesSmoothPUup[Type] = TH1D(histNameSmoothPUup, histNameSmoothPUup, bin, 0, bin)
            VariablesSmoothPUdown[Type] = TH1D(histNameSmoothPUdown, histNameSmoothPUdown, bin, 0, bin)
            VariablesSmoothPUup[Type].Sumw2()
            VariablesSmoothPUdown[Type].Sumw2()
            
            if ( Type.startswith('WJets') ):
                WccHistPUup = TH1D('WccHistPUup', 'WccHistPUup', bin,array('d',xlow))
                WbbHistPUup = TH1D('WbbHistPUup', 'WbbHistPUup', bin,array('d',xlow))
                WccHistPUdown = TH1D('WccHistPUdown', 'WccHistPUdown', bin,array('d',xlow))
                WbbHistPUdown = TH1D('WbbHistPUdown', 'WbbHistPUdown', bin,array('d',xlow))
                WccHistPUup.Sumw2()
                WbbHistPUup.Sumw2()
                WccHistPUdown.Sumw2()
                WbbHistPUdown.Sumw2()
               
        #print Type
        if (Type == 'Data'):
            Trees[Type].Draw(var + " >> " + histName, "(" + cut + ")", 'goff')
        elif (Type.startswith('WJets')):
            Trees[Type].Draw(var + " >> " + histName, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWjmu) + ")*(" + cut + cutwjj + ")", 'goff')
            Trees[Type].Draw(var + " >> " + "WbbHist", "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWbmu) + ")*(" + cut + cutwbb + ")", 'goff')
            Trees[Type].Draw(var + " >> " + "WccHist", "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWcmu) + ")*(" + cut + cutwcc + ")", 'goff')
            Variables[Type].Add(WbbHist)
            Variables[Type].Add(WccHist)
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
                Trees[Type].Draw(var + " >> " + histNamePUup, "(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWjmu) + ")*(" + cut + cutwjj + ")", 'goff')
                Trees[Type].Draw(var + " >> " + "WbbHistPUup", "(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWbmu) + ")*(" + cut + cutwbb + ")", 'goff')
                Trees[Type].Draw(var + " >> " + "WccHistPUup", "(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWcmu) + ")*(" + cut + cutwcc + ")", 'goff')
                VariablesPUup[Type].Add(WbbHistPUup)
                VariablesPUup[Type].Add(WccHistPUup)
                Trees[Type].Draw(var + " >> " + histNamePUdown, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWjmu) + ")*(" + cut + cutwjj + ")", 'goff')
                Trees[Type].Draw(var + " >> " + "WbbHistPUdown", "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWbmu) + ")*(" + cut + cutwbb + ")", 'goff')
                Trees[Type].Draw(var + " >> " + "WccHistPUdown", "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el*weight_WxsecNoLight_comb)*(" + str(SFWcmu) + ")*(" + cut + cutwcc + ")", 'goff')
                VariablesPUdown[Type].Add(WbbHistPUdown)
                VariablesPUdown[Type].Add(WccHistPUdown)     
        else:
            Trees[Type].Draw(var + " >> " + histName, "(weight_PU_3D_73mb_el*weight_eleTrigTotal_el)*(" + cut + ")", 'goff')
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):                      
                Trees[Type].Draw(var + " >> " + histNamePUup, "(weight_PU_3D_shiftUp_73mb_el*weight_eleTrigTotal_el)*(" + cut + ")", 'goff')
                Trees[Type].Draw(var + " >> " + histNamePUdown, "(weight_PU_3D_shiftDown_73mb_el*weight_eleTrigTotal_el)*(" + cut + ")", 'goff')

        if Type != 'Data':
            if Variables[Type].Integral() != 0:
                Variables[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ): 
                    VariablesPUup[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) ) 
                    VariablesPUdown[Type].Scale ( (SF*lumi*xsec_norm[Type]/Nevents[Type]) )

        for x in range(1,bin+1):  
            VariablesSmooth[Type].SetBinContent(x,Variables[Type].GetBinContent(x) )
            VariablesSmooth[Type].SetBinError(x,Variables[Type].GetBinError(x) )
            if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):
                VariablesSmoothPUup[Type].SetBinContent(x,VariablesPUup[Type].GetBinContent(x) )
                VariablesSmoothPUup[Type].SetBinError(x,VariablesPUup[Type].GetBinError(x) )
                VariablesSmoothPUdown[Type].SetBinContent(x,VariablesPUdown[Type].GetBinContent(x) )
                VariablesSmoothPUdown[Type].SetBinError(x,VariablesPUdown[Type].GetBinError(x) )
        VariablesSmooth[Type].SetEntries(Variables[Type].GetEntries() )
        if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ):
            VariablesSmoothPUup[Type].SetEntries(VariablesPUup[Type].GetEntries() )
            VariablesSmoothPUdown[Type].SetEntries(VariablesPUdown[Type].GetEntries() )

        if (Type == 'Data'):
            print 'EVENTS FOR  Data  = ',int(VariablesSmooth[Type].Integral())
            if VariablesSmooth[Type].GetBinContent(bin+1)!=0: print 'OVERFLOW!!!!!!'
            if VariablesSmooth[Type].GetBinContent(0)!=0: print 'UNDERFLOW!!!!!!'

        if (Type != 'Data'):
            if ( not Type.startswith('Wprime') ):
                for x in range(1,bin+1):
                    if (VariablesSmooth[Type].GetBinContent(x) < 0.00001 ): 
                        print 'Setting ',VariablesSmooth[Type].GetBinContent(x),' to 10E-5 for bin ',x,' of ',Type
                        VariablesSmooth[Type].SetBinContent(x,0.00001)
                    if ( (not Type.endswith('UP')) and (not Type.endswith('DOWN')) ): 
                        if (VariablesSmoothPUup[Type].GetBinContent(x) < 0.00001 ): VariablesSmoothPUup[Type].SetBinContent(x,0.00001)
                        if (VariablesSmoothPUdown[Type].GetBinContent(x) < 0.00001 ): VariablesSmoothPUdown[Type].SetBinContent(x,0.00001)

            print 'J = ',j, 'EVENTS FOR ',Type,'  = ',str(int(round((Variables[Type].Integral()))))
            #, ' eff = ',(Variables[Type].Integral()/Nevents[Type]) 
            #print 'xsec = ',xsec_norm[Type]
            #print '---'

            if j < 11:
                background = background + Variables[Type].Integral()

        j = j + 1
        
    
    print 'Total background = ', background
    print 'Background / Data = ', float(background/VariablesSmooth['Data'].Integral())

        
    VariablesSmooth['Data'].SetName("data_obs")
    VariablesSmooth['Data'].Write()

    VariablesSmooth['WJets'].SetName("wjets")
    VariablesSmooth['WJets'].Write()
    VariablesSmooth['TTbar'].SetName("ttbar")
    VariablesSmooth['TTbar'].Write()
    
    VariablesSmooth['WW'].Add(VariablesSmooth['ZJets'])
    VariablesSmooth['WW'].Add(VariablesSmooth['QCD_80to170'])
    VariablesSmooth['WW'].SetName("other")
    VariablesSmooth['WW'].Write()

    VariablesSmooth['T_t'].Add(VariablesSmooth['Tbar_t'])
    VariablesSmooth['T_t'].Add(VariablesSmooth['T_tW'])
    VariablesSmooth['T_t'].Add(VariablesSmooth['Tbar_tW'])

    VariablesSmooth['T_s'].Add(VariablesSmooth['Tbar_s']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t'].SetName("topsntb")
        VariablesSmooth['T_t'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t'].SetName("topsntb")
            VariablesSmooth['T_t'].Write()
            VariablesSmooth['T_s'].SetName("topstb")
            VariablesSmooth['T_s'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t'].Add(VariablesSmooth['T_s'])
            VariablesSmooth['T_t'].SetName("tops")
            VariablesSmooth['T_t'].Write()

    ##### JES UP ##### 
    VariablesSmooth['WJets_JES_UP'].SetName("wjets_jesUp")
    VariablesSmooth['WJets_JES_UP'].Write()
    VariablesSmooth['TTbar_JES_UP'].SetName("ttbar_jesUp")
    VariablesSmooth['TTbar_JES_UP'].Write()
    
    VariablesSmooth['WW_JES_UP'].Add(VariablesSmooth['ZJets_JES_UP'])
    VariablesSmooth['WW_JES_UP'].Add(VariablesSmooth['QCD_80to170_JES_UP'])
    VariablesSmooth['WW_JES_UP'].SetName("other_jesUp")
    VariablesSmooth['WW_JES_UP'].Write()

    VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['Tbar_t_JES_UP'])
    VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['T_tW_JES_UP'])
    VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['Tbar_tW_JES_UP'])
    
    VariablesSmooth['T_s_JES_UP'].Add(VariablesSmooth['Tbar_s_JES_UP']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t_JES_UP'].SetName("topsntb_jesUp")
        VariablesSmooth['T_t_JES_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t_JES_UP'].SetName("topsntb_jesUp")
            VariablesSmooth['T_t_JES_UP'].Write()
            VariablesSmooth['T_s_JES_UP'].SetName("topstb_jesUp")
            VariablesSmooth['T_s_JES_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t_JES_UP'].Add(VariablesSmooth['T_s_JES_UP'])
            VariablesSmooth['T_t_JES_UP'].SetName("tops_jesUp")
            VariablesSmooth['T_t_JES_UP'].Write()

    ##### JES DOWN #####
    VariablesSmooth['WJets_JES_DOWN'].SetName("wjets_jesDown")
    VariablesSmooth['WJets_JES_DOWN'].Write()
    VariablesSmooth['TTbar_JES_DOWN'].SetName("ttbar_jesDown")
    VariablesSmooth['TTbar_JES_DOWN'].Write()
    
    VariablesSmooth['WW_JES_DOWN'].Add(VariablesSmooth['ZJets_JES_DOWN'])
    VariablesSmooth['WW_JES_DOWN'].Add(VariablesSmooth['QCD_80to170_JES_DOWN'])
    VariablesSmooth['WW_JES_DOWN'].SetName("other_jesDown")
    VariablesSmooth['WW_JES_DOWN'].Write()

    VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['Tbar_t_JES_DOWN'])
    VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['T_tW_JES_DOWN'])
    VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['Tbar_tW_JES_DOWN'])
    
    VariablesSmooth['T_s_JES_DOWN'].Add(VariablesSmooth['Tbar_s_JES_DOWN']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t_JES_DOWN'].SetName("topsntb_jesDown")
        VariablesSmooth['T_t_JES_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t_JES_DOWN'].SetName("topsntb_jesDown")
            VariablesSmooth['T_t_JES_DOWN'].Write()
            VariablesSmooth['T_s_JES_DOWN'].SetName("topstb_jesDown")
            VariablesSmooth['T_s_JES_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t_JES_DOWN'].Add(VariablesSmooth['T_s_JES_DOWN'])
            VariablesSmooth['T_t_JES_DOWN'].SetName("tops_jesDown")
            VariablesSmooth['T_t_JES_DOWN'].Write()

    ##### BTAG UP #####
    VariablesSmooth['WJets_BTAG_UP'].SetName("wjets_btagUp")
    VariablesSmooth['WJets_BTAG_UP'].Write()
    VariablesSmooth['TTbar_BTAG_UP'].SetName("ttbar_btagUp")
    VariablesSmooth['TTbar_BTAG_UP'].Write()
    
    VariablesSmooth['WW_BTAG_UP'].Add(VariablesSmooth['ZJets_BTAG_UP'])
    VariablesSmooth['WW_BTAG_UP'].Add(VariablesSmooth['QCD_80to170_BTAG_UP'])
    VariablesSmooth['WW_BTAG_UP'].SetName("other_btagUp")
    VariablesSmooth['WW_BTAG_UP'].Write()

    VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['Tbar_t_BTAG_UP'])
    VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['T_tW_BTAG_UP'])
    VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['Tbar_tW_BTAG_UP'])
    
    VariablesSmooth['T_s_BTAG_UP'].Add(VariablesSmooth['Tbar_s_BTAG_UP']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t_BTAG_UP'].SetName("topsntb_btagUp")
        VariablesSmooth['T_t_BTAG_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t_BTAG_UP'].SetName("topsntb_btagUp")
            VariablesSmooth['T_t_BTAG_UP'].Write()
            VariablesSmooth['T_s_BTAG_UP'].SetName("topstb_btagUp")
            VariablesSmooth['T_s_BTAG_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t_BTAG_UP'].Add(VariablesSmooth['T_s_BTAG_UP'])
            VariablesSmooth['T_t_BTAG_UP'].SetName("tops_btagUp")
            VariablesSmooth['T_t_BTAG_UP'].Write()

    ##### BTAG DOWN #####
    VariablesSmooth['WJets_BTAG_DOWN'].SetName("wjets_btagDown")
    VariablesSmooth['WJets_BTAG_DOWN'].Write()
    VariablesSmooth['TTbar_BTAG_DOWN'].SetName("ttbar_btagDown")
    VariablesSmooth['TTbar_BTAG_DOWN'].Write()
    
    VariablesSmooth['WW_BTAG_DOWN'].Add(VariablesSmooth['ZJets_BTAG_DOWN'])
    VariablesSmooth['WW_BTAG_DOWN'].Add(VariablesSmooth['QCD_80to170_BTAG_DOWN'])
    VariablesSmooth['WW_BTAG_DOWN'].SetName("other_btagDown")
    VariablesSmooth['WW_BTAG_DOWN'].Write()

    VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['Tbar_t_BTAG_DOWN'])
    VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['T_tW_BTAG_DOWN'])
    VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['Tbar_tW_BTAG_DOWN'])

    VariablesSmooth['T_s_BTAG_DOWN'].Add(VariablesSmooth['Tbar_s_BTAG_DOWN']) 
       
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t_BTAG_DOWN'].SetName("topsntb_btagDown")
        VariablesSmooth['T_t_BTAG_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t_BTAG_DOWN'].SetName("topsntb_btagDown")
            VariablesSmooth['T_t_BTAG_DOWN'].Write()
            VariablesSmooth['T_s_BTAG_DOWN'].SetName("topstb_btagDown")
            VariablesSmooth['T_s_BTAG_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t_BTAG_DOWN'].Add(VariablesSmooth['T_s_BTAG_DOWN'])
            VariablesSmooth['T_t_BTAG_DOWN'].SetName("tops_btagDown")
            VariablesSmooth['T_t_BTAG_DOWN'].Write()

    ##### JER UP #####
    VariablesSmooth['WJets_JER_UP'].SetName("wjets_jerUp")
    VariablesSmooth['WJets_JER_UP'].Write()
    VariablesSmooth['TTbar_JER_UP'].SetName("ttbar_jerUp")
    VariablesSmooth['TTbar_JER_UP'].Write()
    
    VariablesSmooth['WW_JER_UP'].Add(VariablesSmooth['ZJets_JER_UP'])
    VariablesSmooth['WW_JER_UP'].Add(VariablesSmooth['QCD_80to170_JER_UP'])
    VariablesSmooth['WW_JER_UP'].SetName("other_jerUp")
    VariablesSmooth['WW_JER_UP'].Write()

    VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['Tbar_t_JER_UP'])
    VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['T_tW_JER_UP'])
    VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['Tbar_tW_JER_UP'])
    
    VariablesSmooth['T_s_JER_UP'].Add(VariablesSmooth['Tbar_s_JER_UP']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t_JER_UP'].SetName("topsntb_jerUp")
        VariablesSmooth['T_t_JER_UP'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t_JER_UP'].SetName("topsntb_jerUp")
            VariablesSmooth['T_t_JER_UP'].Write()
            VariablesSmooth['T_s_JER_UP'].SetName("topstb_jerUp")
            VariablesSmooth['T_s_JER_UP'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t_JER_UP'].Add(VariablesSmooth['T_s_JER_UP'])
            VariablesSmooth['T_t_JER_UP'].SetName("tops_jerUp")
            VariablesSmooth['T_t_JER_UP'].Write()

    ##### JER DOWN #####
    VariablesSmooth['WJets_JER_DOWN'].SetName("wjets_jerDown")
    VariablesSmooth['WJets_JER_DOWN'].Write()
    VariablesSmooth['TTbar_JER_DOWN'].SetName("ttbar_jerDown")
    VariablesSmooth['TTbar_JER_DOWN'].Write()
    
    VariablesSmooth['WW_JER_DOWN'].Add(VariablesSmooth['ZJets_JER_DOWN'])
    VariablesSmooth['WW_JER_DOWN'].Add(VariablesSmooth['QCD_80to170_JER_DOWN'])
    VariablesSmooth['WW_JER_DOWN'].SetName("other_jerDown")
    VariablesSmooth['WW_JER_DOWN'].Write()

    VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['Tbar_t_JER_DOWN'])
    VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['T_tW_JER_DOWN'])
    VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['Tbar_tW_JER_DOWN'])
    
    VariablesSmooth['T_s_JER_DOWN'].Add(VariablesSmooth['Tbar_s_JER_DOWN']) 
   
    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmooth['T_t_JER_DOWN'].SetName("topsntb_jerDown")
        VariablesSmooth['T_t_JER_DOWN'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmooth['T_t_JER_DOWN'].SetName("topsntb_jerDown")
            VariablesSmooth['T_t_JER_DOWN'].Write()
            VariablesSmooth['T_s_JER_DOWN'].SetName("topstb_jerDown")
            VariablesSmooth['T_s_JER_DOWN'].Write()
        elif (wprime == 'Right'):
            VariablesSmooth['T_t_JER_DOWN'].Add(VariablesSmooth['T_s_JER_DOWN'])
            VariablesSmooth['T_t_JER_DOWN'].SetName("tops_jerDown")
            VariablesSmooth['T_t_JER_DOWN'].Write()
    
    ##### PU Down ######
    VariablesSmoothPUdown['WJets'].SetName("wjets_PileupDown")
    VariablesSmoothPUdown['WJets'].Write()
    VariablesSmoothPUdown['TTbar'].SetName("ttbar_PileupDown")
    VariablesSmoothPUdown['TTbar'].Write()
    
    VariablesSmoothPUdown['WW'].Add(VariablesSmoothPUdown['ZJets'])
    VariablesSmoothPUdown['WW'].Add(VariablesSmoothPUdown['QCD_80to170'])
    VariablesSmoothPUdown['WW'].SetName("other_PileupDown")
    VariablesSmoothPUdown['WW'].Write()

    VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['Tbar_t'])
    VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['T_tW'])
    VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['Tbar_tW'])

    VariablesSmoothPUdown['T_s'].Add(VariablesSmoothPUdown['Tbar_s']) 

    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmoothPUdown['T_t'].SetName("topsntb_PileupDown")
        VariablesSmoothPUdown['T_t'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmoothPUdown['T_t'].SetName("topsntb_PileupDown")
            VariablesSmoothPUdown['T_t'].Write()
            VariablesSmoothPUdown['T_s'].SetName("topstb_PileupDown")
            VariablesSmoothPUdown['T_s'].Write()
        elif (wprime == 'Right'):
            VariablesSmoothPUdown['T_t'].Add(VariablesSmoothPUdown['T_s'])
            VariablesSmoothPUdown['T_t'].SetName("tops_PileupDown")
            VariablesSmoothPUdown['T_t'].Write()
  

    ##### PU Up#####
    VariablesSmoothPUup['WJets'].SetName("wjets_PileupUp")
    VariablesSmoothPUup['WJets'].Write()
    VariablesSmoothPUup['TTbar'].SetName("ttbar_PileupUp")
    VariablesSmoothPUup['TTbar'].Write()
    
    VariablesSmoothPUup['WW'].Add(VariablesSmoothPUup['ZJets'])
    VariablesSmoothPUup['WW'].Add(VariablesSmoothPUup['QCD_80to170'])
    VariablesSmoothPUup['WW'].SetName("other_PileupUp")
    VariablesSmoothPUup['WW'].Write()

    VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['Tbar_t'])
    VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['T_tW'])
    VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['Tbar_tW'])
    
    VariablesSmoothPUup['T_s'].Add(VariablesSmoothPUup['Tbar_s']) 

    if (wprime == 'Left' or wprime == 'MixRL'): 
        VariablesSmoothPUup['T_t'].SetName("topsntb_PileupUp")
        VariablesSmoothPUup['T_t'].Write()
    else:
        if ( wprime == 'ModRight' ):
            VariablesSmoothPUup['T_t'].SetName("topsntb_PileupUp")
            VariablesSmoothPUup['T_t'].Write()
            VariablesSmoothPUup['T_s'].SetName("topstb_PileupUp")
            VariablesSmoothPUup['T_s'].Write()
        elif (wprime == 'Right'):
            VariablesSmoothPUup['T_t'].Add(VariablesSmoothPUup['T_s'])
            VariablesSmoothPUup['T_t'].SetName("tops_PileupUp")
            VariablesSmoothPUup['T_t'].Write()
   
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
        VariablesSmoothPUup['Wprime_'+mass+'_' + wprime + 'Wprime'].Write()    
        VariablesSmoothPUdown['Wprime_'+mass+'_' + wprime + 'Wprime'].Write()
    else:
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JES_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JES_DOWN'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JER_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_JER_DOWN'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_BTAG_UP'].Write()
        VariablesSmooth['Wprime_'+mass+'_' + 'Right' + 'Wprime_BTAG_DOWN'].Write()
        VariablesSmoothPUup['Wprime_'+mass+'_' + 'Right' + 'Wprime'].Write()    
        VariablesSmoothPUdown['Wprime_'+mass+'_' + 'Right' + 'Wprime'].Write()

    VariablesSmooth['TTbar_MATCHING_DOWN'].SetName("ttbar_matchingDown")
    VariablesSmooth['TTbar_MATCHING_DOWN'].Write()
    VariablesSmooth['TTbar_MATCHING_UP'].SetName("ttbar_matchingUp")
    VariablesSmooth['TTbar_MATCHING_UP'].Write()
    VariablesSmooth['TTbar_SCALE_DOWN'].SetName("ttbar_q2scaleDown")
    VariablesSmooth['TTbar_SCALE_DOWN'].Write()
    VariablesSmooth['TTbar_SCALE_UP'].SetName("ttbar_q2scaleUp")
    VariablesSmooth['TTbar_SCALE_UP'].Write()
    VariablesSmooth['WJets_MATCHING_DOWN'].SetName("wjets_matchingDown")
    VariablesSmooth['WJets_MATCHING_DOWN'].Write()
    VariablesSmooth['WJets_MATCHING_UP'].SetName("wjets_matchingUp")
    VariablesSmooth['WJets_MATCHING_UP'].Write()
    VariablesSmooth['WJets_SCALE_DOWN'].SetName("wjets_q2scaleDown")
    VariablesSmooth['WJets_SCALE_DOWN'].Write()
    VariablesSmooth['WJets_SCALE_UP'].SetName("wjets_q2scaleUp")
    VariablesSmooth['WJets_SCALE_UP'].Write()

    datacard = open('datacard_'+binname+'_el.txt', 'w')       
    datacard.write( "# W'->tb datacard "+binname+' \n')
    datacard.write( 'imax 1  number of channels \n')
    datacard.write( 'jmax 4  number of backgrounds \n')
    datacard.write( 'kmax 10  number of nuisance parameters \n') 
    datacard.write( '--------------- \n')
    datacard.write( 'shapes * * '+str(f.GetName())+' $CHANNEL/$PROCESS  $CHANNEL/$PROCESS_$SYSTEMATIC \n' )
    datacard.write( '--------------- \n')
    datacard.write( 'bin '+binname+' \n')
    datacard.write( 'observation '+str(round(Variables['Data'].Integral(),3))+' \n')
    datacard.write( '--------------- \n')
    datacard.write( 'bin             '+binname+' '+binname+' '+binname+' ' +binname+' '+binname+' \n') 
    datacard.write( 'process         wp'+str(mass)+'    ttbar   wjets   tops    other \n')
    datacard.write( 'process          0        1       2       3       4    \n')  
    datacard.write( 'rate            '+str(round(VariablesSmooth[binname].Integral(),3))+'      '+str(round(VariablesSmooth['TTbar'].Integral(),3))+'    '+str(round(VariablesSmooth['WJets'].Integral(),3))+'    '+str(round(VariablesSmooth['T_t'].Integral(),3))+'     '+str(round(VariablesSmooth['WW'].Integral(),3))+' \n')
    datacard.write( '--------------- \n')
    datacard.write( 'lumi       lnN    1.045    1.045   1.045   1.045   1.045 \n')
    datacard.write( 'bgnorm     lnN    1.00     1.15    1.15    1.30    1.30 \n')
    datacard.write( 'trgeff     lnN    1.03     1.03    1.03    1.03    1.03 \n')
    datacard.write( 'ideff      lnN    1.03     1.03    1.03    1.03    1.03 \n')
    datacard.write( 'jes      shape    1        1       1       1       1   \n')
    datacard.write( 'jer      shape    1        1       1       1       1   \n')
    datacard.write( 'btag     shape    1        1       1       1       1   \n')
    datacard.write( 'Pileup   shape    1        1       1       1       1   \n')
    datacard.write( 'q2scale  shape    -        -       -       -       -   \n')
    datacard.write( 'matching shape    -        -       -       -       -   \n')
    datacard.close()

#wprime = 'Right'
var = 'BestJetJet2W_M_bestTop_el'; high = 3500; xaxis = "W' invariant mass [GeV/c^{2}]"; yaxis = 'Events / 10 GeV'; save = 'BestJetJet2W_M_bestTop_el'
btags = 3
letter = 'O'

wprime = 'Right'
f = TFile("RootFiles_ForHiggsLimits/"+letter+"_bestTop_Wprime_Right_Histos_electrons.root","RECREATE")
# Wprime_800_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 450, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 975, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_800_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_800_RightWprime.extend(List_Wprime_800_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_800_RightWprime') 
f.cd('Wprime_800_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_800_RightWprime) 


# Wprime_900_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 500, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1075, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_900_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_900_RightWprime.extend(List_Wprime_900_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_900_RightWprime') 
f.cd('Wprime_900_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_900_RightWprime) 


# Wprime_1000_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 550, 600, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1075, 1175, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1000_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1000_RightWprime.extend(List_Wprime_1000_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1000_RightWprime') 
f.cd('Wprime_1000_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1000_RightWprime) 


# Wprime_1100_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 575, 625, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1075, 1125, 1175, 1275, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1100_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1100_RightWprime.extend(List_Wprime_1100_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1100_RightWprime') 
f.cd('Wprime_1100_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1100_RightWprime) 


# Wprime_1200_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 550, 625, 675, 725, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1075, 1125, 1175, 1275, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1200_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1200_RightWprime.extend(List_Wprime_1200_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1200_RightWprime') 
f.cd('Wprime_1200_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1200_RightWprime) 


# Wprime_1300_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 600, 675, 725, 775, 825, 875, 900, 925, 950, 975, 1000, 1025, 1075, 1125, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1300_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1300_RightWprime.extend(List_Wprime_1300_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1300_RightWprime') 
f.cd('Wprime_1300_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1300_RightWprime) 


# Wprime_1400_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 550, 650, 725, 775, 825, 875, 925, 950, 975, 1000, 1025, 1075, 1125, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1400_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1400_RightWprime.extend(List_Wprime_1400_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1400_RightWprime') 
f.cd('Wprime_1400_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1400_RightWprime) 


# Wprime_1500_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 650, 725, 800, 850, 900, 950, 1000, 1025, 1075, 1125, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1500_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1500_RightWprime.extend(List_Wprime_1500_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1500_RightWprime') 
f.cd('Wprime_1500_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1500_RightWprime) 


# Wprime_1600_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 600, 700, 775, 850, 925, 975, 1025, 1075, 1125, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1600_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1600_RightWprime.extend(List_Wprime_1600_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1600_RightWprime') 
f.cd('Wprime_1600_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1600_RightWprime) 


# Wprime_1700_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 725, 875, 1000, 1075, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1700_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1700_RightWprime.extend(List_Wprime_1700_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1700_RightWprime') 
f.cd('Wprime_1700_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1700_RightWprime) 


# Wprime_1900_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 550, 700, 825, 950, 1075, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_1900_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_1900_RightWprime.extend(List_Wprime_1900_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_1900_RightWprime') 
f.cd('Wprime_1900_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_1900_RightWprime) 


# Wprime_2100_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 625, 750, 900, 1025, 1175, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_2100_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_2100_RightWprime.extend(List_Wprime_2100_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_2100_RightWprime') 
f.cd('Wprime_2100_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_2100_RightWprime) 


# Wprime_2300_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 550, 650, 750, 850, 975, 1125, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_2300_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_2300_RightWprime.extend(List_Wprime_2300_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_2300_RightWprime') 
f.cd('Wprime_2300_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_2300_RightWprime) 


# Wprime_2500_RightWprime BestJetJet2W_M_bestTop_el
xlow = [170, 475, 550, 625, 700, 775, 875, 1000, 1125, 1275, 1425, 3500]
bins = len(xlow)-1 
List_DataBg_Wprime_2500_RightWprime = copy.copy(List_DataBg) 
List_DataBg_Wprime_2500_RightWprime.extend(List_Wprime_2500_RightWprime) 
f.cd('..') 
f.mkdir('Wprime_2500_RightWprime') 
f.cd('Wprime_2500_RightWprime') 
plot_DataVsMc(letter,var, bins, xlow, high, yaxis, xaxis , save, wprime, btags, List_DataBg_Wprime_2500_RightWprime) 
