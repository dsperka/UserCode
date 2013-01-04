from ROOT import TFile

lumi_el = 12211.0 
lumi_mu = 12211.0 

lumiPlot_el= '12.2'
lumiPlot_mu= '12.2'

######################################################

Nevents = {}
Nevents['WJets'] = 76041475.0 #v1+v2
Nevents['WW'] = 10000431.0
Nevents['TTbar_Madgraph'] = 6923750.0 
Nevents['TTbar_Powheg'] = 21591169.0 
Nevents['TTbar_Total'] = (21591169.0+6923750.0) 
Nevents['ZJets_M50'] = 30459503.0
Nevents['T_tW'] = 497658.0
Nevents['Tbar_tW'] = 493460.0
Nevents['T_t'] = 3758227.0
Nevents['Tbar_t'] = 1935072.0
Nevents['T_s'] = 259961.0
Nevents['Tbar_s'] = 139974.0

Nevents['Wprime800Right'] = 920654.0
Nevents['Wprime900Right'] = 1.0
Nevents['Wprime1000Right'] = 1.0
Nevents['Wprime1100Right'] = 831508.0
Nevents['Wprime1200Right'] = 965528.0
Nevents['Wprime1300Right'] = 881046.0
Nevents['Wprime1400Right'] = 920262.0
Nevents['Wprime1500Right'] = 907297.0
Nevents['Wprime1600Right'] = 892146.0
Nevents['Wprime1700Right'] = 924438.0
Nevents['Wprime1800Right'] = 841448.0
Nevents['Wprime1900Right'] = 835381.0
Nevents['Wprime2000Right'] = 841836.0
Nevents['Wprime2100Right'] = 926108.0
Nevents['Wprime2200Right'] = 932785.0
Nevents['Wprime2300Right'] = 784768.0
Nevents['Wprime2400Right'] = 894786.0
Nevents['Wprime2500Right'] = 878643.0
Nevents['Wprime2600Right'] = 944599.0
Nevents['Wprime2700Right'] = 915158.0
Nevents['Wprime2800Right'] = 835281.0
Nevents['Wprime2900Right'] = 910111.0
Nevents['Wprime3000Right'] = 932601.0

for sys in ['JESUP','JESDOWN','JERUP','JERDOWN','BTAGUP','BTAGDOWN']:
    
    Nevents['WJets_'+sys] = Nevents['WJets']
    Nevents['WW_'+sys] = Nevents['WW']
    Nevents['TTbar_Madgraph_'+sys] = Nevents['TTbar_Madgraph']
    Nevents['TTbar_Powheg_'+sys] = Nevents['TTbar_Powheg']
    Nevents['ZJets_M50_'+sys] = Nevents['ZJets_M50']
    Nevents['T_tW_'+sys] = Nevents['T_tW']
    Nevents['Tbar_tW_'+sys] = Nevents['Tbar_tW']
    Nevents['T_t_'+sys] = Nevents['T_t']
    Nevents['Tbar_t_'+sys] = Nevents['Tbar_t']  
    Nevents['T_s_'+sys] = Nevents['T_s']
    Nevents['Tbar_s_'+sys] = Nevents['Tbar_s']    

    Nevents['Wprime800Right_'+sys] = Nevents['Wprime800Right']
    Nevents['Wprime900Right_'+sys] = Nevents['Wprime900Right']
    Nevents['Wprime1000Right_'+sys] = Nevents['Wprime1000Right']
    Nevents['Wprime1100Right_'+sys] = Nevents['Wprime1100Right']
    Nevents['Wprime1200Right_'+sys] = Nevents['Wprime1200Right']
    Nevents['Wprime1300Right_'+sys] = Nevents['Wprime1300Right']
    Nevents['Wprime1400Right_'+sys] = Nevents['Wprime1400Right']
    Nevents['Wprime1500Right_'+sys] = Nevents['Wprime1500Right']
    Nevents['Wprime1600Right_'+sys] = Nevents['Wprime1600Right']
    Nevents['Wprime1700Right_'+sys] = Nevents['Wprime1700Right']
    Nevents['Wprime1800Right_'+sys] = Nevents['Wprime1800Right']
    Nevents['Wprime1900Right_'+sys] = Nevents['Wprime1900Right']
    Nevents['Wprime2000Right_'+sys] = Nevents['Wprime2000Right']
    Nevents['Wprime2100Right_'+sys] = Nevents['Wprime2100Right']
    Nevents['Wprime2200Right_'+sys] = Nevents['Wprime2200Right']
    Nevents['Wprime2300Right_'+sys] = Nevents['Wprime2300Right']
    Nevents['Wprime2400Right_'+sys] = Nevents['Wprime2400Right']
    Nevents['Wprime2500Right_'+sys] = Nevents['Wprime2500Right']
    Nevents['Wprime2600Right_'+sys] = Nevents['Wprime2600Right']
    Nevents['Wprime2700Right_'+sys] = Nevents['Wprime2700Right']
    Nevents['Wprime2800Right_'+sys] = Nevents['Wprime2800Right']
    Nevents['Wprime2900Right_'+sys] = Nevents['Wprime2900Right']
    Nevents['Wprime3000Right_'+sys] = Nevents['Wprime3000Right']

#############################################

#############################################
xsec = {}
xsec['WJets'] = 36257.2 # fixme, adding zjets number
xsec['WW'] = 54.838 # CTEQ
#xsec['TTbar_Madgraph'] = 225.197 # MCFM NLO
#xsec['TTbar_Powheg'] = 225.197 # MCFM NLO
xsec['TTbar_Madgraph'] = 234 # approx NNLO
xsec['TTbar_Powheg'] = 234 # approx NNLO
xsec['TTbar_Total'] = 234 # approx NNLO
xsec['ZJets_M50'] = 3503.71
xsec['T_tW'] = 11.1
xsec['Tbar_tW'] = 11.1
xsec['T_t'] = 56.4
xsec['Tbar_t'] = 30.7
xsec['T_s'] = 3.79
xsec['Tbar_s'] = 1.76

xsec['Wprime800Right'] = 1.5352
xsec['Wprime900Right'] = 0.9214
xsec['Wprime1000Right'] = 0.5704
xsec['Wprime1100Right'] = 0.3623
xsec['Wprime1200Right'] = 0.2348
xsec['Wprime1300Right'] = 0.1548
xsec['Wprime1400Right'] = 0.1036
xsec['Wprime1500Right'] = 0.0701
xsec['Wprime1600Right'] = 0.048
xsec['Wprime1700Right'] = 0.0331
xsec['Wprime1800Right'] = 0.0231
xsec['Wprime1900Right'] = 0.0162
xsec['Wprime2000Right'] = 0.0114
xsec['Wprime2100Right'] = 0.008
xsec['Wprime2200Right'] = 0.006
xsec['Wprime2300Right'] = 0.004
xsec['Wprime2400Right'] = 0.003
xsec['Wprime2500Right'] = 0.002
xsec['Wprime2600Right'] = 0.0017
xsec['Wprime2700Right'] = 0.0012
xsec['Wprime2800Right'] = 0.00094
xsec['Wprime2900Right'] = 0.00072
xsec['Wprime3000Right'] = 0.00056

for sys in ['JESUP','JESDOWN','JERUP','JERDOWN','BTAGUP','BTAGDOWN']:
    
    xsec['WJets_'+sys] = xsec['WJets']
    xsec['WW_'+sys] = xsec['WW']
    xsec['TTbar_Madgraph_'+sys] = xsec['TTbar_Madgraph']
    xsec['TTbar_Powheg_'+sys] = xsec['TTbar_Powheg']
    xsec['ZJets_M50_'+sys] = xsec['ZJets_M50']
    xsec['T_tW_'+sys] = xsec['T_tW']
    xsec['Tbar_tW_'+sys] = xsec['Tbar_tW']
    xsec['T_t_'+sys] = xsec['T_t']
    xsec['Tbar_t_'+sys] = xsec['Tbar_t']  
    xsec['T_s_'+sys] = xsec['T_s']
    xsec['Tbar_s_'+sys] = xsec['Tbar_s']    

    xsec['Wprime800Right_'+sys] = xsec['Wprime800Right']
    xsec['Wprime900Right_'+sys] = xsec['Wprime900Right']
    xsec['Wprime1000Right_'+sys] = xsec['Wprime1000Right']
    xsec['Wprime1100Right_'+sys] = xsec['Wprime1100Right']
    xsec['Wprime1200Right_'+sys] = xsec['Wprime1200Right']
    xsec['Wprime1300Right_'+sys] = xsec['Wprime1300Right']
    xsec['Wprime1400Right_'+sys] = xsec['Wprime1400Right']
    xsec['Wprime1500Right_'+sys] = xsec['Wprime1500Right']
    xsec['Wprime1600Right_'+sys] = xsec['Wprime1600Right']
    xsec['Wprime1700Right_'+sys] = xsec['Wprime1700Right']
    xsec['Wprime1800Right_'+sys] = xsec['Wprime1800Right']
    xsec['Wprime1900Right_'+sys] = xsec['Wprime1900Right']
    xsec['Wprime2000Right_'+sys] = xsec['Wprime2000Right']
    xsec['Wprime2100Right_'+sys] = xsec['Wprime2100Right']
    xsec['Wprime2200Right_'+sys] = xsec['Wprime2200Right']
    xsec['Wprime2300Right_'+sys] = xsec['Wprime2300Right']
    xsec['Wprime2400Right_'+sys] = xsec['Wprime2400Right']
    xsec['Wprime2500Right_'+sys] = xsec['Wprime2500Right']
    xsec['Wprime2600Right_'+sys] = xsec['Wprime2600Right']
    xsec['Wprime2700Right_'+sys] = xsec['Wprime2700Right']
    xsec['Wprime2800Right_'+sys] = xsec['Wprime2800Right']
    xsec['Wprime2900Right_'+sys] = xsec['Wprime2900Right']
    xsec['Wprime3000Right_'+sys] = xsec['Wprime3000Right']


#############################################

#############################################
xsec_norm = {}
xsec_norm['WJets'] = xsec['WJets']
xsec_norm['WW'] = xsec['WW']
xsec_norm['TTbar_Madgraph'] = xsec['TTbar_Madgraph']
xsec_norm['TTbar_Powheg'] = xsec['TTbar_Powheg']
xsec_norm['T_t'] = xsec['T_t'] 
xsec_norm['Tbar_t'] = xsec['Tbar_t'] 
xsec_norm['T_tW'] = xsec['T_tW'] 
xsec_norm['Tbar_tW'] = xsec['Tbar_tW'] 
xsec_norm['T_s'] = xsec['T_s'] 
xsec_norm['Tbar_s'] = xsec['Tbar_s'] 
xsec_norm['ZJets_M50'] = xsec['ZJets_M50']

xsec_norm['Wprime800Right'] = 1.0
xsec_norm['Wprime900Right'] = 1.0
xsec_norm['Wprime1000Right'] = 1.0
xsec_norm['Wprime1100Right'] = 1.0 
xsec_norm['Wprime1200Right'] = 1.0 
xsec_norm['Wprime1300Right'] = 1.0 
xsec_norm['Wprime1400Right'] = 1.0 
xsec_norm['Wprime1500Right'] = 1.0 
xsec_norm['Wprime1600Right'] = 1.0 
xsec_norm['Wprime1700Right'] = 1.0 
xsec_norm['Wprime1800Right'] = 1.0 
xsec_norm['Wprime1900Right'] = 1.0 
xsec_norm['Wprime2000Right'] = 1.0 
xsec_norm['Wprime2100Right'] = 1.0 
xsec_norm['Wprime2200Right'] = 1.0 
xsec_norm['Wprime2300Right'] = 1.0
xsec_norm['Wprime2400Right'] = 1.0
xsec_norm['Wprime2500Right'] = 1.0
xsec_norm['Wprime2600Right'] = 1.0 
xsec_norm['Wprime2700Right'] = 1.0 
xsec_norm['Wprime2800Right'] = 1.0 
xsec_norm['Wprime2900Right'] = 1.0 
xsec_norm['Wprime3000Right'] = 1.0 

for sys in ['JESUP','JESDOWN','JERUP','JERDOWN','BTAGUP','BTAGDOWN']:
    
    xsec_norm['WJets_'+sys] = xsec_norm['WJets']
    xsec_norm['WW_'+sys] = xsec_norm['WW']
    xsec_norm['TTbar_Madgraph_'+sys] = xsec_norm['TTbar_Madgraph']
    xsec_norm['TTbar_Powheg_'+sys] = xsec_norm['TTbar_Powheg']
    xsec_norm['ZJets_M50_'+sys] = xsec_norm['ZJets_M50']
    xsec_norm['T_tW_'+sys] = xsec_norm['T_tW']
    xsec_norm['Tbar_tW_'+sys] = xsec_norm['Tbar_tW']
    xsec_norm['T_t_'+sys] = xsec_norm['T_t']
    xsec_norm['Tbar_t_'+sys] = xsec_norm['Tbar_t']  
    xsec_norm['T_s_'+sys] = xsec_norm['T_s']
    xsec_norm['Tbar_s_'+sys] = xsec_norm['Tbar_s']    

    xsec_norm['Wprime800Right_'+sys] = xsec_norm['Wprime800Right']
    xsec_norm['Wprime900Right_'+sys] = xsec_norm['Wprime900Right']
    xsec_norm['Wprime1000Right_'+sys] = xsec_norm['Wprime1000Right']
    xsec_norm['Wprime1100Right_'+sys] = xsec_norm['Wprime1100Right']
    xsec_norm['Wprime1200Right_'+sys] = xsec_norm['Wprime1200Right']
    xsec_norm['Wprime1300Right_'+sys] = xsec_norm['Wprime1300Right']
    xsec_norm['Wprime1400Right_'+sys] = xsec_norm['Wprime1400Right']
    xsec_norm['Wprime1500Right_'+sys] = xsec_norm['Wprime1500Right']
    xsec_norm['Wprime1600Right_'+sys] = xsec_norm['Wprime1600Right']
    xsec_norm['Wprime1700Right_'+sys] = xsec_norm['Wprime1700Right']
    xsec_norm['Wprime1800Right_'+sys] = xsec_norm['Wprime1800Right']
    xsec_norm['Wprime1900Right_'+sys] = xsec_norm['Wprime1900Right']
    xsec_norm['Wprime2000Right_'+sys] = xsec_norm['Wprime2000Right']
    xsec_norm['Wprime2100Right_'+sys] = xsec_norm['Wprime2100Right']
    xsec_norm['Wprime2200Right_'+sys] = xsec_norm['Wprime2200Right']
    xsec_norm['Wprime2300Right_'+sys] = xsec_norm['Wprime2300Right']
    xsec_norm['Wprime2400Right_'+sys] = xsec_norm['Wprime2400Right']
    xsec_norm['Wprime2500Right_'+sys] = xsec_norm['Wprime2500Right']
    xsec_norm['Wprime2600Right_'+sys] = xsec_norm['Wprime2600Right']
    xsec_norm['Wprime2700Right_'+sys] = xsec_norm['Wprime2700Right']
    xsec_norm['Wprime2800Right_'+sys] = xsec_norm['Wprime2800Right']
    xsec_norm['Wprime2900Right_'+sys] = xsec_norm['Wprime2900Right']
    xsec_norm['Wprime3000Right_'+sys] = xsec_norm['Wprime3000Right']


#############################################
############### FOR BDT #####################
#############################################


BDTDir = 'BDTDone/'
chanlist = ['el','mu']
masslist = ['wp1100','wp1300','wp1500','wp1700','wp1900','wp2100','wp2300','wp2500','wp2700','wp2900']
couplist = ['R']  
Typelist = ['data','wjets','ttbar','t','bt','tw','btw','s','bs','zjets','ww']
Syslist = ['','_JESUP','_JESDOWN','_JERUP','_JERDOWN','_BTAGUP','_BTAGDOWN']
taglist = ['GE1BTag']
Samples = []

#### Generated Events (same as above) ######
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
            for Sys in Syslist:
                Nevents[mass+coup+'_wjets'+Sys+'_'+chan] = Nevents['WJets']
                Nevents[mass+coup+'_ww'+Sys+'_'+chan] = Nevents['WW']
                Nevents[mass+coup+'_ttbar'+Sys+'_'+chan] = Nevents['TTbar_Madgraph']
                Nevents[mass+coup+'_zjets'+Sys+'_'+chan] = Nevents['ZJets_M50']
                Nevents[mass+coup+'_tw'+Sys+'_'+chan] = Nevents['T_tW']
                Nevents[mass+coup+'_btw'+Sys+'_'+chan] = Nevents['Tbar_tW']
                Nevents[mass+coup+'_t'+Sys+'_'+chan] = Nevents['T_t']
                Nevents[mass+coup+'_bt'+Sys+'_'+chan] = Nevents['Tbar_t']
                Nevents[mass+coup+'_s'+Sys+'_'+chan] = Nevents['T_s']
                Nevents[mass+coup+'_bs'+Sys+'_'+chan] = Nevents['Tbar_s']

for chan in chanlist:
    for Sys in Syslist:
         Nevents['wp800R_wp800R'+Sys+'_'+chan] = Nevents['Wprime800Right'] 
         Nevents['wp900R_wp900R'+Sys+'_'+chan] = Nevents['Wprime900Right'] 
         Nevents['wp1000R_wp1000R'+Sys+'_'+chan] = Nevents['Wprime1000Right'] 
         Nevents['wp1100R_wp1100R'+Sys+'_'+chan] = Nevents['Wprime1100Right'] 
         Nevents['wp1200R_wp1200R'+Sys+'_'+chan] = Nevents['Wprime1200Right'] 
         Nevents['wp1300R_wp1300R'+Sys+'_'+chan] = Nevents['Wprime1300Right'] 
         Nevents['wp1400R_wp1400R'+Sys+'_'+chan] = Nevents['Wprime1400Right'] 
         Nevents['wp1500R_wp1500R'+Sys+'_'+chan] = Nevents['Wprime1500Right'] 
         Nevents['wp1600R_wp1600R'+Sys+'_'+chan] = Nevents['Wprime1600Right'] 
         Nevents['wp1700R_wp1700R'+Sys+'_'+chan] = Nevents['Wprime1700Right'] 
         Nevents['wp1800R_wp1800R'+Sys+'_'+chan] = Nevents['Wprime1800Right'] 
         Nevents['wp1900R_wp1900R'+Sys+'_'+chan] = Nevents['Wprime1900Right'] 
         Nevents['wp2000R_wp2000R'+Sys+'_'+chan] = Nevents['Wprime2000Right'] 
         Nevents['wp2100R_wp2100R'+Sys+'_'+chan] = Nevents['Wprime2100Right'] 
         Nevents['wp2200R_wp2200R'+Sys+'_'+chan] = Nevents['Wprime2200Right'] 
         Nevents['wp2300R_wp2300R'+Sys+'_'+chan] = Nevents['Wprime2300Right'] 
         Nevents['wp2400R_wp2400R'+Sys+'_'+chan] = Nevents['Wprime2400Right'] 
         Nevents['wp2500R_wp2500R'+Sys+'_'+chan] = Nevents['Wprime2500Right']  
         Nevents['wp2600R_wp2600R'+Sys+'_'+chan] = Nevents['Wprime2600Right'] 
         Nevents['wp2700R_wp2700R'+Sys+'_'+chan] = Nevents['Wprime2700Right'] 
         Nevents['wp2800R_wp2800R'+Sys+'_'+chan] = Nevents['Wprime2800Right'] 
         Nevents['wp2900R_wp2900R'+Sys+'_'+chan] = Nevents['Wprime2900Right'] 
         Nevents['wp3000R_wp3000R'+Sys+'_'+chan] = Nevents['Wprime3000Right'] 

#### Cross sections (same as above) ######
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
            for Sys in Syslist:
                xsec[mass+coup+'_wjets'+Sys+'_'+chan] = xsec['WJets']
                xsec[mass+coup+'_ww'+Sys+'_'+chan] = xsec['WW']
                xsec[mass+coup+'_ttbar'+Sys+'_'+chan] = xsec['TTbar_Madgraph']
                xsec[mass+coup+'_zjets'+Sys+'_'+chan] = xsec['ZJets_M50']
                xsec[mass+coup+'_tw'+Sys+'_'+chan] = xsec['T_tW']
                xsec[mass+coup+'_btw'+Sys+'_'+chan] = xsec['Tbar_tW']
                xsec[mass+coup+'_t'+Sys+'_'+chan] = xsec['T_t']
                xsec[mass+coup+'_bt'+Sys+'_'+chan] = xsec['Tbar_t']
                xsec[mass+coup+'_s'+Sys+'_'+chan] = xsec['T_s']
                xsec[mass+coup+'_bs'+Sys+'_'+chan] = xsec['Tbar_s']

                xsec_norm[mass+coup+'_wjets'+Sys+'_'+chan] = xsec['WJets']
                xsec_norm[mass+coup+'_ww'+Sys+'_'+chan] = xsec['WW']
                xsec_norm[mass+coup+'_ttbar'+Sys+'_'+chan] = xsec['TTbar_Madgraph']
                xsec_norm[mass+coup+'_zjets'+Sys+'_'+chan] = xsec['ZJets_M50']
                xsec_norm[mass+coup+'_tw'+Sys+'_'+chan] = xsec['T_tW']
                xsec_norm[mass+coup+'_btw'+Sys+'_'+chan] = xsec['Tbar_tW']
                xsec_norm[mass+coup+'_t'+Sys+'_'+chan] = xsec['T_t']
                xsec_norm[mass+coup+'_bt'+Sys+'_'+chan] = xsec['Tbar_t']
                xsec_norm[mass+coup+'_s'+Sys+'_'+chan] = xsec['T_s']
                xsec_norm[mass+coup+'_bs'+Sys+'_'+chan] = xsec['Tbar_s']

                                                                                                                                                                
for chan in chanlist:
    for Sys in Syslist:
        xsec['wp800R_wp800R'+Sys+'_'+chan] = xsec['Wprime800Right'] 
        xsec['wp900R_wp900R'+Sys+'_'+chan] = xsec['Wprime900Right'] 
        xsec['wp1000R_wp1000R'+Sys+'_'+chan] = xsec['Wprime1000Right'] 
        xsec['wp1100R_wp1100R'+Sys+'_'+chan] = xsec['Wprime1100Right'] 
        xsec['wp1200R_wp1200R'+Sys+'_'+chan] = xsec['Wprime1200Right'] 
        xsec['wp1300R_wp1300R'+Sys+'_'+chan] = xsec['Wprime1300Right'] 
        xsec['wp1400R_wp1400R'+Sys+'_'+chan] = xsec['Wprime1400Right'] 
        xsec['wp1500R_wp1500R'+Sys+'_'+chan] = xsec['Wprime1500Right'] 
        xsec['wp1600R_wp1600R'+Sys+'_'+chan] = xsec['Wprime1600Right'] 
        xsec['wp1700R_wp1700R'+Sys+'_'+chan] = xsec['Wprime1700Right'] 
        xsec['wp1800R_wp1800R'+Sys+'_'+chan] = xsec['Wprime1800Right'] 
        xsec['wp1900R_wp1900R'+Sys+'_'+chan] = xsec['Wprime1900Right'] 
        xsec['wp2000R_wp2000R'+Sys+'_'+chan] = xsec['Wprime2000Right'] 
        xsec['wp2100R_wp2100R'+Sys+'_'+chan] = xsec['Wprime2100Right'] 
        xsec['wp2200R_wp2200R'+Sys+'_'+chan] = xsec['Wprime2200Right'] 
        xsec['wp2300R_wp2300R'+Sys+'_'+chan] = xsec['Wprime2300Right'] 
        xsec['wp2400R_wp2400R'+Sys+'_'+chan] = xsec['Wprime2400Right'] 
        xsec['wp2500R_wp2500R'+Sys+'_'+chan] = xsec['Wprime2500Right'] 
        xsec['wp2600R_wp2600R'+Sys+'_'+chan] = xsec['Wprime2600Right'] 
        xsec['wp2700R_wp2700R'+Sys+'_'+chan] = xsec['Wprime2700Right'] 
        xsec['wp2800R_wp2800R'+Sys+'_'+chan] = xsec['Wprime2800Right'] 
        xsec['wp2900R_wp2900R'+Sys+'_'+chan] = xsec['Wprime2900Right'] 
        xsec['wp3000R_wp3000R'+Sys+'_'+chan] = xsec['Wprime3000Right'] 

        xsec_norm['wp800R_wp800R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp900R_wp900R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1000R_wp1000R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1100R_wp1100R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1200R_wp1200R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1300R_wp1300R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1400R_wp1400R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1500R_wp1500R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1600R_wp1600R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1700R_wp1700R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1800R_wp1800R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp1900R_wp1900R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2000R_wp2000R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2100R_wp2100R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2200R_wp2200R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2300R_wp2300R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2400R_wp2400R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2500R_wp2500R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2600R_wp2600R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2700R_wp2700R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2800R_wp2800R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp2900R_wp2900R'+Sys+'_'+chan] = 1.0
        xsec_norm['wp3000R_wp3000R'+Sys+'_'+chan] = 1.0
    

##############################################################
# These are the expected yields after all BDT training cuts
###############################################################
Yield = {}
for mass in masslist:
    for coup in couplist:
        Yield[mass+coup+'_ttbar_el'] = 41389.
        Yield[mass+coup+'_wjets_el'] = 17288.
        Yield[mass+coup+'_t_el'] = 1715.
        Yield[mass+coup+'_bt_el'] = 848.
        Yield[mass+coup+'_tw_el'] = 1202.
        Yield[mass+coup+'_btw_el'] = 1224.
        Yield[mass+coup+'_s_el'] = 204.
        Yield[mass+coup+'_bs_el'] = 72.
        Yield[mass+coup+'_zjets_el'] = 1345.
        Yield[mass+coup+'_ww_el'] = 173.

        Yield[mass+coup+'_ttbar_mu'] = 45491.
        Yield[mass+coup+'_wjets_mu'] = 19062.
        Yield[mass+coup+'_t_mu'] = 2052.
        Yield[mass+coup+'_bt_mu'] = 1048.
        Yield[mass+coup+'_tw_mu'] = 1319.
        Yield[mass+coup+'_btw_mu'] = 1357.
        Yield[mass+coup+'_s_mu'] = 230.
        Yield[mass+coup+'_bs_mu'] = 108.
        Yield[mass+coup+'_zjets_mu'] = 1547.
        Yield[mass+coup+'_ww_mu'] = 192.

Yield['wp1100R_wp1100R_el'] = 113.
Yield['wp1300R_wp1300R_el'] = 113.
Yield['wp1500R_wp1500R_el'] = 113.
Yield['wp1700R_wp1700R_el'] = 50.
Yield['wp1900R_wp1900R_el'] = 22.
Yield['wp2100R_wp2100R_el'] = 10.
Yield['wp2300R_wp2300R_el'] = 5.
Yield['wp2500R_wp2500R_el'] = 5.

Yield['wp1100R_wp1100R_mu'] = 99.
Yield['wp1300R_wp1300R_mu'] = 99.
Yield['wp1500R_wp1500R_mu'] = 99.
Yield['wp1700R_wp1700R_mu'] = 42.
Yield['wp1900R_wp1900R_mu'] = 19.
Yield['wp2100R_wp2100R_mu'] = 9.
Yield['wp2300R_wp2300R_mu'] = 4.
Yield['wp2500R_wp2500R_mu'] = 4.

