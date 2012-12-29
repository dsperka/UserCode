from ROOT import TFile

lumi_el = 12211.0 
lumi_mu = 12211.0 

lumiPlot_el= '12.2'
lumiPlot_mu= '12.2'

######################################################
RootFiles = {}
RootFiles['Data_el'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Single_El_12pt2fb.root")
RootFiles['Data_mu'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Single_Mu_12pt2fb.root")

RootFiles['WJets'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/WJets.root")
RootFiles['WW'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/WW.root")
RootFiles['TTbar_Madgraph'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/TTbar_Madgraph.root")
RootFiles['TTbar_Powheg'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/TTbar_Powheg.root")
RootFiles['ZJets_M50'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/ZJets_M50.root")
RootFiles['T_t'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/T_t.root")
RootFiles['Tbar_t'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Tbar_t.root")
RootFiles['T_tW'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/T_tW.root")
RootFiles['Tbar_tW'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Tbar_tW.root")
RootFiles['T_s'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/T_s.root")
RootFiles['Tbar_s'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Tbar_s.root")

RootFiles['WJets_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/WJets_JESUP.root")
RootFiles['WW_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/WW_JESUP.root")
RootFiles['TTbar_Madgraph_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/TTbar_Madgraph_JESUP.root")
RootFiles['TTbar_Powheg_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/TTbar_Powheg_JESUP.root")
RootFiles['ZJets_M50_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/ZJets_M50_JESUP.root")
RootFiles['T_t_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/T_t_JESUP.root")
RootFiles['Tbar_t_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Tbar_t_JESUP.root")
RootFiles['T_tW_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/T_tW_JESUP.root")
RootFiles['Tbar_tW_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Tbar_tW_JESUP.root")
RootFiles['T_s_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/T_s_JESUP.root")
RootFiles['Tbar_s_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Tbar_s_JESUP.root")
RootFiles['WJets_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/WJets_JESDOWN.root")
RootFiles['WW_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/WW_JESDOWN.root")
RootFiles['TTbar_Madgraph_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/TTbar_Madgraph_JESDOWN.root")
RootFiles['TTbar_Powheg_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/TTbar_Powheg_JESDOWN.root")
RootFiles['ZJets_M50_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/ZJets_M50_JESDOWN.root")
RootFiles['T_t_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/T_t_JESDOWN.root")
RootFiles['Tbar_t_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Tbar_t_JESDOWN.root")
RootFiles['T_tW_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/T_tW_JESDOWN.root")
RootFiles['Tbar_tW_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Tbar_tW_JESDOWN.root")
RootFiles['T_s_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/T_s_JESDOWN.root")
RootFiles['Tbar_s_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Tbar_s_JESDOWN.root")

RootFiles['WJets_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/WJets_JERUP.root")
RootFiles['WW_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/WW_JERUP.root")
RootFiles['TTbar_Madgraph_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/TTbar_Madgraph_JERUP.root")
RootFiles['TTbar_Powheg_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/TTbar_Powheg_JERUP.root")
RootFiles['ZJets_M50_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/ZJets_M50_JERUP.root")
RootFiles['T_t_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/T_t_JERUP.root")
RootFiles['Tbar_t_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Tbar_t_JERUP.root")
RootFiles['T_tW_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/T_tW_JERUP.root")
RootFiles['Tbar_tW_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Tbar_tW_JERUP.root")
RootFiles['T_s_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/T_s_JERUP.root")
RootFiles['Tbar_s_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Tbar_s_JERUP.root")
RootFiles['WJets_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/WJets_JERDOWN.root")
RootFiles['WW_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/WW_JERDOWN.root")
RootFiles['TTbar_Madgraph_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/TTbar_Madgraph_JERDOWN.root")
RootFiles['TTbar_Powheg_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/TTbar_Powheg_JERDOWN.root")
RootFiles['ZJets_M50_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/ZJets_M50_JERDOWN.root")
RootFiles['T_t_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/T_t_JERDOWN.root")
RootFiles['Tbar_t_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Tbar_t_JERDOWN.root")
RootFiles['T_tW_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/T_tW_JERDOWN.root")
RootFiles['Tbar_tW_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Tbar_tW_JERDOWN.root")
RootFiles['T_s_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/T_s_JERDOWN.root")
RootFiles['Tbar_s_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Tbar_s_JERDOWN.root")

RootFiles['WJets_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/WJets_BTAGUP.root")
RootFiles['WW_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/WW_BTAGUP.root")
RootFiles['TTbar_Madgraph_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/TTbar_Madgraph_BTAGUP.root")
RootFiles['TTbar_Powheg_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/TTbar_Powheg_BTAGUP.root")
RootFiles['ZJets_M50_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/ZJets_M50_BTAGUP.root")
RootFiles['T_t_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/T_t_BTAGUP.root")
RootFiles['Tbar_t_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Tbar_t_BTAGUP.root")
RootFiles['T_tW_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/T_tW_BTAGUP.root")
RootFiles['Tbar_tW_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Tbar_tW_BTAGUP.root")
RootFiles['T_s_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/T_s_BTAGUP.root")
RootFiles['Tbar_s_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Tbar_s_BTAGUP.root")
RootFiles['WJets_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/WJets_BTAGDOWN.root")
RootFiles['WW_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/WW_BTAGDOWN.root")
RootFiles['TTbar_Madgraph_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/TTbar_Madgraph_BTAGDOWN.root")
RootFiles['TTbar_Powheg_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/TTbar_Powheg_BTAGDOWN.root")
RootFiles['ZJets_M50_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/ZJets_M50_BTAGDOWN.root")
RootFiles['T_t_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/T_t_BTAGDOWN.root")
RootFiles['Tbar_t_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Tbar_t_BTAGDOWN.root")
RootFiles['T_tW_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/T_tW_BTAGDOWN.root")
RootFiles['Tbar_tW_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Tbar_tW_BTAGDOWN.root")
RootFiles['T_s_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/T_s_BTAGDOWN.root")
RootFiles['Tbar_s_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Tbar_s_BTAGDOWN.root")


RootFiles['Wprime800Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime800Right.root")
#RootFiles['Wprime900Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime900Right.root")
#RootFiles['Wprime1000Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1000Right.root")
RootFiles['Wprime1100Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1100Right.root")
RootFiles['Wprime1200Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1200Right.root")
RootFiles['Wprime1300Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1300Right.root")
RootFiles['Wprime1400Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1400Right.root")
RootFiles['Wprime1500Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1500Right.root")
RootFiles['Wprime1600Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1600Right.root")
RootFiles['Wprime1700Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1700Right.root")
RootFiles['Wprime1800Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1800Right.root")
RootFiles['Wprime1900Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime1900Right.root")
RootFiles['Wprime2000Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2000Right.root")
RootFiles['Wprime2100Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2100Right.root")
RootFiles['Wprime2200Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2200Right.root")
RootFiles['Wprime2300Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2300Right.root")
RootFiles['Wprime2400Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2400Right.root")
RootFiles['Wprime2500Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2500Right.root")
RootFiles['Wprime2600Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2600Right.root")
RootFiles['Wprime2700Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2700Right.root")
RootFiles['Wprime2800Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2800Right.root")
RootFiles['Wprime2900Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime2900Right.root")
RootFiles['Wprime3000Right'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/Wprime3000Right.root")

RootFiles['Wprime800Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime800Right_JESUP.root")
#RootFiles['Wprime900Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime900Right_JESUP.root")
#RootFiles['Wprime1000Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1000Right_JESUP.root")
RootFiles['Wprime1100Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1100Right_JESUP.root")
RootFiles['Wprime1200Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1200Right_JESUP.root")
RootFiles['Wprime1300Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1300Right_JESUP.root")
RootFiles['Wprime1400Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1400Right_JESUP.root")
RootFiles['Wprime1500Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1500Right_JESUP.root")
RootFiles['Wprime1600Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1600Right_JESUP.root")
RootFiles['Wprime1700Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1700Right_JESUP.root")
RootFiles['Wprime1800Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1800Right_JESUP.root")
RootFiles['Wprime1900Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime1900Right_JESUP.root")
RootFiles['Wprime2000Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2000Right_JESUP.root")
RootFiles['Wprime2100Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2100Right_JESUP.root")
RootFiles['Wprime2200Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2200Right_JESUP.root")
RootFiles['Wprime2300Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2300Right_JESUP.root")
RootFiles['Wprime2400Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2400Right_JESUP.root")
RootFiles['Wprime2500Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2500Right_JESUP.root")
RootFiles['Wprime2600Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2600Right_JESUP.root")
RootFiles['Wprime2700Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2700Right_JESUP.root")
RootFiles['Wprime2800Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2800Right_JESUP.root")
RootFiles['Wprime2900Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime2900Right_JESUP.root")
RootFiles['Wprime3000Right_JESUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESUP/Wprime3000Right_JESUP.root")

RootFiles['Wprime800Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime800Right_JESDOWN.root")
#RootFiles['Wprime900Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime900Right_JESDOWN.root")
#RootFiles['Wprime1000Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1000Right_JESDOWN.root")
RootFiles['Wprime1100Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1100Right_JESDOWN.root")
RootFiles['Wprime1200Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1200Right_JESDOWN.root")
RootFiles['Wprime1300Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1300Right_JESDOWN.root")
RootFiles['Wprime1400Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1400Right_JESDOWN.root")
RootFiles['Wprime1500Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1500Right_JESDOWN.root")
RootFiles['Wprime1600Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1600Right_JESDOWN.root")
RootFiles['Wprime1700Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1700Right_JESDOWN.root")
RootFiles['Wprime1800Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1800Right_JESDOWN.root")
RootFiles['Wprime1900Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime1900Right_JESDOWN.root")
RootFiles['Wprime2000Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2000Right_JESDOWN.root")
RootFiles['Wprime2100Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2100Right_JESDOWN.root")
RootFiles['Wprime2200Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2200Right_JESDOWN.root")
RootFiles['Wprime2300Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2300Right_JESDOWN.root")
RootFiles['Wprime2400Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2400Right_JESDOWN.root")
RootFiles['Wprime2500Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2500Right_JESDOWN.root")
RootFiles['Wprime2600Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2600Right_JESDOWN.root")
RootFiles['Wprime2700Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2700Right_JESDOWN.root")
RootFiles['Wprime2800Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2800Right_JESDOWN.root")
RootFiles['Wprime2900Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime2900Right_JESDOWN.root")
RootFiles['Wprime3000Right_JESDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JESDOWN/Wprime3000Right_JESDOWN.root")

RootFiles['Wprime800Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime800Right_JERUP.root")
#RootFiles['Wprime900Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime900Right_JERUP.root")
#RootFiles['Wprime1000Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1000Right_JERUP.root")
RootFiles['Wprime1100Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1100Right_JERUP.root")
RootFiles['Wprime1200Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1200Right_JERUP.root")
RootFiles['Wprime1300Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1300Right_JERUP.root")
RootFiles['Wprime1400Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1400Right_JERUP.root")
RootFiles['Wprime1500Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1500Right_JERUP.root")
RootFiles['Wprime1600Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1600Right_JERUP.root")
RootFiles['Wprime1700Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1700Right_JERUP.root")
RootFiles['Wprime1800Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1800Right_JERUP.root")
RootFiles['Wprime1900Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime1900Right_JERUP.root")
RootFiles['Wprime2000Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2000Right_JERUP.root")
RootFiles['Wprime2100Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2100Right_JERUP.root")
RootFiles['Wprime2200Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2200Right_JERUP.root")
RootFiles['Wprime2300Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2300Right_JERUP.root")
RootFiles['Wprime2400Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2400Right_JERUP.root")
RootFiles['Wprime2500Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2500Right_JERUP.root")
RootFiles['Wprime2600Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2600Right_JERUP.root")
RootFiles['Wprime2700Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2700Right_JERUP.root")
RootFiles['Wprime2800Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2800Right_JERUP.root")
RootFiles['Wprime2800Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2800Right_JERUP.root")
RootFiles['Wprime2900Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime2900Right_JERUP.root")
RootFiles['Wprime3000Right_JERUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERUP/Wprime3000Right_JERUP.root")

RootFiles['Wprime800Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime800Right_JERDOWN.root")
#RootFiles['Wprime900Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime900Right_JERDOWN.root")
#RootFiles['Wprime1000Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1000Right_JERDOWN.root")
RootFiles['Wprime1100Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1100Right_JERDOWN.root")
RootFiles['Wprime1200Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1200Right_JERDOWN.root")
RootFiles['Wprime1300Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1300Right_JERDOWN.root")
RootFiles['Wprime1400Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1400Right_JERDOWN.root")
RootFiles['Wprime1500Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1500Right_JERDOWN.root")
RootFiles['Wprime1600Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1600Right_JERDOWN.root")
RootFiles['Wprime1700Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1700Right_JERDOWN.root")
RootFiles['Wprime1800Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1800Right_JERDOWN.root")
RootFiles['Wprime1900Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime1900Right_JERDOWN.root")
RootFiles['Wprime2000Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2000Right_JERDOWN.root")
RootFiles['Wprime2100Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2100Right_JERDOWN.root")
RootFiles['Wprime2200Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2200Right_JERDOWN.root")
RootFiles['Wprime2300Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2300Right_JERDOWN.root")
RootFiles['Wprime2400Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2400Right_JERDOWN.root")
RootFiles['Wprime2500Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2500Right_JERDOWN.root")
RootFiles['Wprime2600Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2600Right_JERDOWN.root")
RootFiles['Wprime2700Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2700Right_JERDOWN.root")
RootFiles['Wprime2800Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2800Right_JERDOWN.root")
RootFiles['Wprime2900Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime2900Right_JERDOWN.root")
RootFiles['Wprime3000Right_JERDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/JERDOWN/Wprime3000Right_JERDOWN.root")

RootFiles['Wprime800Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime800Right_BTAGUP.root")
#RootFiles['Wprime900Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime900Right_BTAGUP.root")
#RootFiles['Wprime1000Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1000Right_BTAGUP.root")
RootFiles['Wprime1100Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1100Right_BTAGUP.root")
RootFiles['Wprime1200Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1200Right_BTAGUP.root")
RootFiles['Wprime1300Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1300Right_BTAGUP.root")
RootFiles['Wprime1400Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1400Right_BTAGUP.root")
RootFiles['Wprime1500Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1500Right_BTAGUP.root")
RootFiles['Wprime1600Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1600Right_BTAGUP.root")
RootFiles['Wprime1700Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1700Right_BTAGUP.root")
RootFiles['Wprime1800Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1800Right_BTAGUP.root")
RootFiles['Wprime1900Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime1900Right_BTAGUP.root")
RootFiles['Wprime2000Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2000Right_BTAGUP.root")
RootFiles['Wprime2100Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2100Right_BTAGUP.root")
RootFiles['Wprime2200Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2200Right_BTAGUP.root")
RootFiles['Wprime2300Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2300Right_BTAGUP.root")
RootFiles['Wprime2400Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2400Right_BTAGUP.root")
RootFiles['Wprime2500Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2500Right_BTAGUP.root")
RootFiles['Wprime2600Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2600Right_BTAGUP.root")
RootFiles['Wprime2700Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2700Right_BTAGUP.root")
RootFiles['Wprime2800Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2800Right_BTAGUP.root")
RootFiles['Wprime2900Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime2900Right_BTAGUP.root")
RootFiles['Wprime3000Right_BTAGUP'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGUP/Wprime3000Right_BTAGUP.root")

RootFiles['Wprime800Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime800Right_BTAGDOWN.root")
#RootFiles['Wprime900Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime900Right_BTAGDOWN.root")
#RootFiles['Wprime1000Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1000Right_BTAGDOWN.root")
RootFiles['Wprime1100Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1100Right_BTAGDOWN.root")
RootFiles['Wprime1200Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1200Right_BTAGDOWN.root")
RootFiles['Wprime1300Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1300Right_BTAGDOWN.root")
RootFiles['Wprime1400Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1400Right_BTAGDOWN.root")
RootFiles['Wprime1500Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1500Right_BTAGDOWN.root")
RootFiles['Wprime1600Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1600Right_BTAGDOWN.root")
RootFiles['Wprime1700Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1700Right_BTAGDOWN.root")
RootFiles['Wprime1800Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1800Right_BTAGDOWN.root")
RootFiles['Wprime1900Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime1900Right_BTAGDOWN.root")
RootFiles['Wprime2000Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2000Right_BTAGDOWN.root")
RootFiles['Wprime2100Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2100Right_BTAGDOWN.root")
RootFiles['Wprime2200Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2200Right_BTAGDOWN.root")
RootFiles['Wprime2300Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2300Right_BTAGDOWN.root")
RootFiles['Wprime2400Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2400Right_BTAGDOWN.root")
RootFiles['Wprime2500Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2500Right_BTAGDOWN.root")
RootFiles['Wprime2600Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2600Right_BTAGDOWN.root")
RootFiles['Wprime2700Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2700Right_BTAGDOWN.root")
RootFiles['Wprime2800Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2800Right_BTAGDOWN.root")
RootFiles['Wprime2900Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime2900Right_BTAGDOWN.root")
RootFiles['Wprime3000Right_BTAGDOWN'] = TFile("/uscms_data/d2/dsperka/8TeV/Samples/20Dec_All/BTAGDOWN/Wprime3000Right_BTAGDOWN.root")

######################################################


######################################################
Trees = {}
Trees['Data_el']  = RootFiles['Data_el'].Get("ljmet")
Trees['Data_mu']  = RootFiles['Data_mu'].Get("ljmet")

Trees['WJets'] = RootFiles['WJets'].Get("ljmet")
Trees['WW'] = RootFiles['WW'].Get("ljmet")
Trees['TTbar_Madgraph'] = RootFiles['TTbar_Madgraph'].Get("ljmet")
Trees['TTbar_Powheg'] = RootFiles['TTbar_Powheg'].Get("ljmet")
Trees['T_t'] = RootFiles['T_t'].Get("ljmet")
Trees['Tbar_t'] = RootFiles['Tbar_t'].Get("ljmet")
Trees['T_tW'] = RootFiles['T_tW'].Get("ljmet")
Trees['Tbar_tW'] = RootFiles['Tbar_tW'].Get("ljmet")
Trees['T_s'] = RootFiles['T_s'].Get("ljmet")
Trees['Tbar_s'] = RootFiles['Tbar_s'].Get("ljmet")
Trees['ZJets_M50'] = RootFiles['ZJets_M50'].Get("ljmet")

Trees['WJets_JESUP'] = RootFiles['WJets_JESUP'].Get("ljmet")
Trees['WW_JESUP'] = RootFiles['WW_JESUP'].Get("ljmet")
Trees['TTbar_Madgraph_JESUP'] = RootFiles['TTbar_Madgraph_JESUP'].Get("ljmet")
Trees['TTbar_Powheg_JESUP'] = RootFiles['TTbar_Powheg_JESUP'].Get("ljmet")
Trees['T_t_JESUP'] = RootFiles['T_t_JESUP'].Get("ljmet")
Trees['Tbar_t_JESUP'] = RootFiles['Tbar_t_JESUP'].Get("ljmet")
Trees['T_tW_JESUP'] = RootFiles['T_tW_JESUP'].Get("ljmet")
Trees['Tbar_tW_JESUP'] = RootFiles['Tbar_tW_JESUP'].Get("ljmet")
Trees['T_s_JESUP'] = RootFiles['T_s_JESUP'].Get("ljmet")
Trees['Tbar_s_JESUP'] = RootFiles['Tbar_s_JESUP'].Get("ljmet")
Trees['ZJets_M50_JESUP'] = RootFiles['ZJets_M50_JESUP'].Get("ljmet")

Trees['WJets_JESDOWN'] = RootFiles['WJets_JESDOWN'].Get("ljmet")
Trees['WW_JESDOWN'] = RootFiles['WW_JESDOWN'].Get("ljmet")
Trees['TTbar_Madgraph_JESDOWN'] = RootFiles['TTbar_Madgraph_JESDOWN'].Get("ljmet")
Trees['TTbar_Powheg_JESDOWN'] = RootFiles['TTbar_Powheg_JESDOWN'].Get("ljmet")
Trees['T_t_JESDOWN'] = RootFiles['T_t_JESDOWN'].Get("ljmet")
Trees['Tbar_t_JESDOWN'] = RootFiles['Tbar_t_JESDOWN'].Get("ljmet")
Trees['T_tW_JESDOWN'] = RootFiles['T_tW_JESDOWN'].Get("ljmet")
Trees['Tbar_tW_JESDOWN'] = RootFiles['Tbar_tW_JESDOWN'].Get("ljmet")
Trees['T_s_JESDOWN'] = RootFiles['T_s_JESDOWN'].Get("ljmet")
Trees['Tbar_s_JESDOWN'] = RootFiles['Tbar_s_JESDOWN'].Get("ljmet")
Trees['ZJets_M50_JESDOWN'] = RootFiles['ZJets_M50_JESDOWN'].Get("ljmet")

Trees['WJets_JERUP'] = RootFiles['WJets_JERUP'].Get("ljmet")
Trees['WW_JERUP'] = RootFiles['WW_JERUP'].Get("ljmet")
Trees['TTbar_Madgraph_JERUP'] = RootFiles['TTbar_Madgraph_JERUP'].Get("ljmet")
Trees['TTbar_Powheg_JERUP'] = RootFiles['TTbar_Powheg_JERUP'].Get("ljmet")
Trees['T_t_JERUP'] = RootFiles['T_t_JERUP'].Get("ljmet")
Trees['Tbar_t_JERUP'] = RootFiles['Tbar_t_JERUP'].Get("ljmet")
Trees['T_tW_JERUP'] = RootFiles['T_tW_JERUP'].Get("ljmet")
Trees['Tbar_tW_JERUP'] = RootFiles['Tbar_tW_JERUP'].Get("ljmet")
Trees['T_s_JERUP'] = RootFiles['T_s_JERUP'].Get("ljmet")
Trees['Tbar_s_JERUP'] = RootFiles['Tbar_s_JERUP'].Get("ljmet")
Trees['ZJets_M50_JERUP'] = RootFiles['ZJets_M50_JERUP'].Get("ljmet")

Trees['WJets_JERDOWN'] = RootFiles['WJets_JERDOWN'].Get("ljmet")
Trees['WW_JERDOWN'] = RootFiles['WW_JERDOWN'].Get("ljmet")
Trees['TTbar_Madgraph_JERDOWN'] = RootFiles['TTbar_Madgraph_JERDOWN'].Get("ljmet")
Trees['TTbar_Powheg_JERDOWN'] = RootFiles['TTbar_Powheg_JERDOWN'].Get("ljmet")
Trees['T_t_JERDOWN'] = RootFiles['T_t_JERDOWN'].Get("ljmet")
Trees['Tbar_t_JERDOWN'] = RootFiles['Tbar_t_JERDOWN'].Get("ljmet")
Trees['T_tW_JERDOWN'] = RootFiles['T_tW_JERDOWN'].Get("ljmet")
Trees['Tbar_tW_JERDOWN'] = RootFiles['Tbar_tW_JERDOWN'].Get("ljmet")
Trees['T_s_JERDOWN'] = RootFiles['T_s_JERDOWN'].Get("ljmet")
Trees['Tbar_s_JERDOWN'] = RootFiles['Tbar_s_JERDOWN'].Get("ljmet")
Trees['ZJets_M50_JERDOWN'] = RootFiles['ZJets_M50_JERDOWN'].Get("ljmet")

Trees['WJets_BTAGUP'] = RootFiles['WJets_BTAGUP'].Get("ljmet")
Trees['WW_BTAGUP'] = RootFiles['WW_BTAGUP'].Get("ljmet")
Trees['TTbar_Madgraph_BTAGUP'] = RootFiles['TTbar_Madgraph_BTAGUP'].Get("ljmet")
Trees['TTbar_Powheg_BTAGUP'] = RootFiles['TTbar_Powheg_BTAGUP'].Get("ljmet")
Trees['T_t_BTAGUP'] = RootFiles['T_t_BTAGUP'].Get("ljmet")
Trees['Tbar_t_BTAGUP'] = RootFiles['Tbar_t_BTAGUP'].Get("ljmet")
Trees['T_tW_BTAGUP'] = RootFiles['T_tW_BTAGUP'].Get("ljmet")
Trees['Tbar_tW_BTAGUP'] = RootFiles['Tbar_tW_BTAGUP'].Get("ljmet")
Trees['T_s_BTAGUP'] = RootFiles['T_s_BTAGUP'].Get("ljmet")
Trees['Tbar_s_BTAGUP'] = RootFiles['Tbar_s_BTAGUP'].Get("ljmet")
Trees['ZJets_M50_BTAGUP'] = RootFiles['ZJets_M50_BTAGUP'].Get("ljmet")

Trees['WJets_BTAGDOWN'] = RootFiles['WJets_BTAGDOWN'].Get("ljmet")
Trees['WW_BTAGDOWN'] = RootFiles['WW_BTAGDOWN'].Get("ljmet")
Trees['TTbar_Madgraph_BTAGDOWN'] = RootFiles['TTbar_Madgraph_BTAGDOWN'].Get("ljmet")
Trees['TTbar_Powheg_BTAGDOWN'] = RootFiles['TTbar_Powheg_BTAGDOWN'].Get("ljmet")
Trees['T_t_BTAGDOWN'] = RootFiles['T_t_BTAGDOWN'].Get("ljmet")
Trees['Tbar_t_BTAGDOWN'] = RootFiles['Tbar_t_BTAGDOWN'].Get("ljmet")
Trees['T_tW_BTAGDOWN'] = RootFiles['T_tW_BTAGDOWN'].Get("ljmet")
Trees['Tbar_tW_BTAGDOWN'] = RootFiles['Tbar_tW_BTAGDOWN'].Get("ljmet")
Trees['T_s_BTAGDOWN'] = RootFiles['T_s_BTAGDOWN'].Get("ljmet")
Trees['Tbar_s_BTAGDOWN'] = RootFiles['Tbar_s_BTAGDOWN'].Get("ljmet")
Trees['ZJets_M50_BTAGDOWN'] = RootFiles['ZJets_M50_BTAGDOWN'].Get("ljmet")


Trees['Wprime1100Right'] = RootFiles['Wprime1100Right'].Get("ljmet")
Trees['Wprime1200Right'] = RootFiles['Wprime1200Right'].Get("ljmet")
Trees['Wprime1300Right'] = RootFiles['Wprime1300Right'].Get("ljmet")
Trees['Wprime1400Right'] = RootFiles['Wprime1400Right'].Get("ljmet")
Trees['Wprime1500Right'] = RootFiles['Wprime1500Right'].Get("ljmet")
Trees['Wprime1600Right'] = RootFiles['Wprime1600Right'].Get("ljmet")
Trees['Wprime1700Right'] = RootFiles['Wprime1700Right'].Get("ljmet")
Trees['Wprime1800Right'] = RootFiles['Wprime1800Right'].Get("ljmet")
Trees['Wprime1900Right'] = RootFiles['Wprime1900Right'].Get("ljmet")
Trees['Wprime2000Right'] = RootFiles['Wprime2000Right'].Get("ljmet")
Trees['Wprime2100Right'] = RootFiles['Wprime2100Right'].Get("ljmet")
Trees['Wprime2200Right'] = RootFiles['Wprime2200Right'].Get("ljmet")
Trees['Wprime2300Right'] = RootFiles['Wprime2300Right'].Get("ljmet")
Trees['Wprime2400Right'] = RootFiles['Wprime2400Right'].Get("ljmet")
Trees['Wprime2500Right'] = RootFiles['Wprime2500Right'].Get("ljmet")
Trees['Wprime2600Right'] = RootFiles['Wprime2600Right'].Get("ljmet")
Trees['Wprime2700Right'] = RootFiles['Wprime2700Right'].Get("ljmet")
Trees['Wprime2800Right'] = RootFiles['Wprime2800Right'].Get("ljmet")
Trees['Wprime2900Right'] = RootFiles['Wprime2900Right'].Get("ljmet")
Trees['Wprime3000Right'] = RootFiles['Wprime3000Right'].Get("ljmet")

Trees['Wprime1100Right_JESUP'] = RootFiles['Wprime1100Right_JESUP'].Get("ljmet")
Trees['Wprime1200Right_JESUP'] = RootFiles['Wprime1200Right_JESUP'].Get("ljmet")
Trees['Wprime1300Right_JESUP'] = RootFiles['Wprime1300Right_JESUP'].Get("ljmet")
Trees['Wprime1400Right_JESUP'] = RootFiles['Wprime1400Right_JESUP'].Get("ljmet")
Trees['Wprime1500Right_JESUP'] = RootFiles['Wprime1500Right_JESUP'].Get("ljmet")
Trees['Wprime1600Right_JESUP'] = RootFiles['Wprime1600Right_JESUP'].Get("ljmet")
Trees['Wprime1700Right_JESUP'] = RootFiles['Wprime1700Right_JESUP'].Get("ljmet")
Trees['Wprime1800Right_JESUP'] = RootFiles['Wprime1800Right_JESUP'].Get("ljmet")
Trees['Wprime1900Right_JESUP'] = RootFiles['Wprime1900Right_JESUP'].Get("ljmet")
Trees['Wprime2000Right_JESUP'] = RootFiles['Wprime2000Right_JESUP'].Get("ljmet")
Trees['Wprime2100Right_JESUP'] = RootFiles['Wprime2100Right_JESUP'].Get("ljmet")
Trees['Wprime2200Right_JESUP'] = RootFiles['Wprime2200Right_JESUP'].Get("ljmet")
Trees['Wprime2300Right_JESUP'] = RootFiles['Wprime2300Right_JESUP'].Get("ljmet")
Trees['Wprime2400Right_JESUP'] = RootFiles['Wprime2400Right_JESUP'].Get("ljmet")
Trees['Wprime2500Right_JESUP'] = RootFiles['Wprime2500Right_JESUP'].Get("ljmet")
Trees['Wprime2600Right_JESUP'] = RootFiles['Wprime2600Right_JESUP'].Get("ljmet")
Trees['Wprime2700Right_JESUP'] = RootFiles['Wprime2700Right_JESUP'].Get("ljmet")
Trees['Wprime2800Right_JESUP'] = RootFiles['Wprime2800Right_JESUP'].Get("ljmet")
Trees['Wprime2900Right_JESUP'] = RootFiles['Wprime2900Right_JESUP'].Get("ljmet")
Trees['Wprime3000Right_JESUP'] = RootFiles['Wprime3000Right_JESUP'].Get("ljmet")

Trees['Wprime1100Right_JESDOWN'] = RootFiles['Wprime1100Right_JESDOWN'].Get("ljmet")
Trees['Wprime1200Right_JESDOWN'] = RootFiles['Wprime1200Right_JESDOWN'].Get("ljmet")
Trees['Wprime1300Right_JESDOWN'] = RootFiles['Wprime1300Right_JESDOWN'].Get("ljmet")
Trees['Wprime1400Right_JESDOWN'] = RootFiles['Wprime1400Right_JESDOWN'].Get("ljmet")
Trees['Wprime1500Right_JESDOWN'] = RootFiles['Wprime1500Right_JESDOWN'].Get("ljmet")
Trees['Wprime1600Right_JESDOWN'] = RootFiles['Wprime1600Right_JESDOWN'].Get("ljmet")
Trees['Wprime1700Right_JESDOWN'] = RootFiles['Wprime1700Right_JESDOWN'].Get("ljmet")
Trees['Wprime1800Right_JESDOWN'] = RootFiles['Wprime1800Right_JESDOWN'].Get("ljmet")
Trees['Wprime1900Right_JESDOWN'] = RootFiles['Wprime1900Right_JESDOWN'].Get("ljmet")
Trees['Wprime2000Right_JESDOWN'] = RootFiles['Wprime2000Right_JESDOWN'].Get("ljmet")
Trees['Wprime2100Right_JESDOWN'] = RootFiles['Wprime2100Right_JESDOWN'].Get("ljmet")
Trees['Wprime2200Right_JESDOWN'] = RootFiles['Wprime2200Right_JESDOWN'].Get("ljmet")
Trees['Wprime2300Right_JESDOWN'] = RootFiles['Wprime2300Right_JESDOWN'].Get("ljmet")
Trees['Wprime2400Right_JESDOWN'] = RootFiles['Wprime2400Right_JESDOWN'].Get("ljmet")
Trees['Wprime2500Right_JESDOWN'] = RootFiles['Wprime2500Right_JESDOWN'].Get("ljmet")
Trees['Wprime2600Right_JESDOWN'] = RootFiles['Wprime2600Right_JESDOWN'].Get("ljmet")
Trees['Wprime2700Right_JESDOWN'] = RootFiles['Wprime2700Right_JESDOWN'].Get("ljmet")
Trees['Wprime2800Right_JESDOWN'] = RootFiles['Wprime2800Right_JESDOWN'].Get("ljmet")
Trees['Wprime2900Right_JESDOWN'] = RootFiles['Wprime2900Right_JESDOWN'].Get("ljmet")
Trees['Wprime3000Right_JESDOWN'] = RootFiles['Wprime3000Right_JESDOWN'].Get("ljmet")

Trees['Wprime1100Right_JERUP'] = RootFiles['Wprime1100Right_JERUP'].Get("ljmet")
Trees['Wprime1200Right_JERUP'] = RootFiles['Wprime1200Right_JERUP'].Get("ljmet")
Trees['Wprime1300Right_JERUP'] = RootFiles['Wprime1300Right_JERUP'].Get("ljmet")
Trees['Wprime1400Right_JERUP'] = RootFiles['Wprime1400Right_JERUP'].Get("ljmet")
Trees['Wprime1500Right_JERUP'] = RootFiles['Wprime1500Right_JERUP'].Get("ljmet")
Trees['Wprime1600Right_JERUP'] = RootFiles['Wprime1600Right_JERUP'].Get("ljmet")
Trees['Wprime1700Right_JERUP'] = RootFiles['Wprime1700Right_JERUP'].Get("ljmet")
Trees['Wprime1800Right_JERUP'] = RootFiles['Wprime1800Right_JERUP'].Get("ljmet")
Trees['Wprime1900Right_JERUP'] = RootFiles['Wprime1900Right_JERUP'].Get("ljmet")
Trees['Wprime2000Right_JERUP'] = RootFiles['Wprime2000Right_JERUP'].Get("ljmet")
Trees['Wprime2100Right_JERUP'] = RootFiles['Wprime2100Right_JERUP'].Get("ljmet")
Trees['Wprime2200Right_JERUP'] = RootFiles['Wprime2200Right_JERUP'].Get("ljmet")
Trees['Wprime2300Right_JERUP'] = RootFiles['Wprime2300Right_JERUP'].Get("ljmet")
Trees['Wprime2400Right_JERUP'] = RootFiles['Wprime2400Right_JERUP'].Get("ljmet")
Trees['Wprime2500Right_JERUP'] = RootFiles['Wprime2500Right_JERUP'].Get("ljmet")
Trees['Wprime2600Right_JERUP'] = RootFiles['Wprime2600Right_JERUP'].Get("ljmet")
Trees['Wprime2700Right_JERUP'] = RootFiles['Wprime2700Right_JERUP'].Get("ljmet")
Trees['Wprime2800Right_JERUP'] = RootFiles['Wprime2800Right_JERUP'].Get("ljmet")
Trees['Wprime2900Right_JERUP'] = RootFiles['Wprime2900Right_JERUP'].Get("ljmet")
Trees['Wprime3000Right_JERUP'] = RootFiles['Wprime3000Right_JERUP'].Get("ljmet")

Trees['Wprime1100Right_JERDOWN'] = RootFiles['Wprime1100Right_JERDOWN'].Get("ljmet")
Trees['Wprime1200Right_JERDOWN'] = RootFiles['Wprime1200Right_JERDOWN'].Get("ljmet")
Trees['Wprime1300Right_JERDOWN'] = RootFiles['Wprime1300Right_JERDOWN'].Get("ljmet")
Trees['Wprime1400Right_JERDOWN'] = RootFiles['Wprime1400Right_JERDOWN'].Get("ljmet")
Trees['Wprime1500Right_JERDOWN'] = RootFiles['Wprime1500Right_JERDOWN'].Get("ljmet")
Trees['Wprime1600Right_JERDOWN'] = RootFiles['Wprime1600Right_JERDOWN'].Get("ljmet")
Trees['Wprime1700Right_JERDOWN'] = RootFiles['Wprime1700Right_JERDOWN'].Get("ljmet")
Trees['Wprime1800Right_JERDOWN'] = RootFiles['Wprime1800Right_JERDOWN'].Get("ljmet")
Trees['Wprime1900Right_JERDOWN'] = RootFiles['Wprime1900Right_JERDOWN'].Get("ljmet")
Trees['Wprime2000Right_JERDOWN'] = RootFiles['Wprime2000Right_JERDOWN'].Get("ljmet")
Trees['Wprime2100Right_JERDOWN'] = RootFiles['Wprime2100Right_JERDOWN'].Get("ljmet")
Trees['Wprime2200Right_JERDOWN'] = RootFiles['Wprime2200Right_JERDOWN'].Get("ljmet")
Trees['Wprime2300Right_JERDOWN'] = RootFiles['Wprime2300Right_JERDOWN'].Get("ljmet")
Trees['Wprime2400Right_JERDOWN'] = RootFiles['Wprime2400Right_JERDOWN'].Get("ljmet")
Trees['Wprime2500Right_JERDOWN'] = RootFiles['Wprime2500Right_JERDOWN'].Get("ljmet")
Trees['Wprime2600Right_JERDOWN'] = RootFiles['Wprime2600Right_JERDOWN'].Get("ljmet")
Trees['Wprime2700Right_JERDOWN'] = RootFiles['Wprime2700Right_JERDOWN'].Get("ljmet")
Trees['Wprime2800Right_JERDOWN'] = RootFiles['Wprime2800Right_JERDOWN'].Get("ljmet")
Trees['Wprime2900Right_JERDOWN'] = RootFiles['Wprime2900Right_JERDOWN'].Get("ljmet")
Trees['Wprime3000Right_JERDOWN'] = RootFiles['Wprime3000Right_JERDOWN'].Get("ljmet")

Trees['Wprime1100Right_BTAGUP'] = RootFiles['Wprime1100Right_BTAGUP'].Get("ljmet")
Trees['Wprime1200Right_BTAGUP'] = RootFiles['Wprime1200Right_BTAGUP'].Get("ljmet")
Trees['Wprime1300Right_BTAGUP'] = RootFiles['Wprime1300Right_BTAGUP'].Get("ljmet")
Trees['Wprime1400Right_BTAGUP'] = RootFiles['Wprime1400Right_BTAGUP'].Get("ljmet")
Trees['Wprime1500Right_BTAGUP'] = RootFiles['Wprime1500Right_BTAGUP'].Get("ljmet")
Trees['Wprime1600Right_BTAGUP'] = RootFiles['Wprime1600Right_BTAGUP'].Get("ljmet")
Trees['Wprime1700Right_BTAGUP'] = RootFiles['Wprime1700Right_BTAGUP'].Get("ljmet")
Trees['Wprime1800Right_BTAGUP'] = RootFiles['Wprime1800Right_BTAGUP'].Get("ljmet")
Trees['Wprime1900Right_BTAGUP'] = RootFiles['Wprime1900Right_BTAGUP'].Get("ljmet")
Trees['Wprime2000Right_BTAGUP'] = RootFiles['Wprime2000Right_BTAGUP'].Get("ljmet")
Trees['Wprime2100Right_BTAGUP'] = RootFiles['Wprime2100Right_BTAGUP'].Get("ljmet")
Trees['Wprime2200Right_BTAGUP'] = RootFiles['Wprime2200Right_BTAGUP'].Get("ljmet")
Trees['Wprime2300Right_BTAGUP'] = RootFiles['Wprime2300Right_BTAGUP'].Get("ljmet")
Trees['Wprime2400Right_BTAGUP'] = RootFiles['Wprime2400Right_BTAGUP'].Get("ljmet")
Trees['Wprime2500Right_BTAGUP'] = RootFiles['Wprime2500Right_BTAGUP'].Get("ljmet")
Trees['Wprime2600Right_BTAGUP'] = RootFiles['Wprime2600Right_BTAGUP'].Get("ljmet")
Trees['Wprime2700Right_BTAGUP'] = RootFiles['Wprime2700Right_BTAGUP'].Get("ljmet")
Trees['Wprime2800Right_BTAGUP'] = RootFiles['Wprime2800Right_BTAGUP'].Get("ljmet")
Trees['Wprime2900Right_BTAGUP'] = RootFiles['Wprime2900Right_BTAGUP'].Get("ljmet")
Trees['Wprime3000Right_BTAGUP'] = RootFiles['Wprime3000Right_BTAGUP'].Get("ljmet")

Trees['Wprime1100Right_BTAGDOWN'] = RootFiles['Wprime1100Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1200Right_BTAGDOWN'] = RootFiles['Wprime1200Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1300Right_BTAGDOWN'] = RootFiles['Wprime1300Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1400Right_BTAGDOWN'] = RootFiles['Wprime1400Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1500Right_BTAGDOWN'] = RootFiles['Wprime1500Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1600Right_BTAGDOWN'] = RootFiles['Wprime1600Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1700Right_BTAGDOWN'] = RootFiles['Wprime1700Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1800Right_BTAGDOWN'] = RootFiles['Wprime1800Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime1900Right_BTAGDOWN'] = RootFiles['Wprime1900Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2000Right_BTAGDOWN'] = RootFiles['Wprime2000Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2100Right_BTAGDOWN'] = RootFiles['Wprime2100Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2200Right_BTAGDOWN'] = RootFiles['Wprime2200Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2300Right_BTAGDOWN'] = RootFiles['Wprime2300Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2400Right_BTAGDOWN'] = RootFiles['Wprime2400Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2500Right_BTAGDOWN'] = RootFiles['Wprime2500Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2600Right_BTAGDOWN'] = RootFiles['Wprime2600Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2700Right_BTAGDOWN'] = RootFiles['Wprime2700Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2800Right_BTAGDOWN'] = RootFiles['Wprime2800Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime2900Right_BTAGDOWN'] = RootFiles['Wprime2900Right_BTAGDOWN'].Get("ljmet")
Trees['Wprime3000Right_BTAGDOWN'] = RootFiles['Wprime3000Right_BTAGDOWN'].Get("ljmet")


#############################################            

#############################################
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
masslist = ['wp1500','wp1700','wp1900','wp2100','wp2300']
couplist = ['R'] 
Typelist = ['data','wjets','ttbar','t','bt','tw','btw','s','bs','zjets','ww']
taglist = ['GE1BTag']
Samples = []

############# Root Files ###################
RootFilesBDT = {}
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
            for Type in Typelist:
                RootFilesBDT[mass+coup+'_'+Type+'_'+chan] = TFile(BDTDir+'BDT_GE1BTag_'+mass+coup+'_'+Type+'_'+chan+'.root')
                #print 'Loaded Root file for ',mass+coup+'_'+Type+'_'+chan,': ',BDTDir+'BDT_GE1BTag_'+mass+coup+'_'+Type+'_'+chan+'.root'
                Samples.extend([mass+coup+'_'+Type+'_'+chan])
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
            RootFilesBDT[mass+coup+'_'+mass+coup+'_'+chan] = TFile(BDTDir+'BDT_GE1BTag_'+mass+coup+'_'+mass+coup+'_'+chan+'.root')
            #print 'Loaded Root file for ',mass+coup+'_'+mass+coup+'_'+chan,': ',BDTDir+'BDT_GE1BTag_'+mass+coup+'_'+mass+coup+'_'+chan+'.root'
            Samples.extend([mass+coup+'_'+mass+coup+'_'+chan])


############## Trees #######################
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
            for Type in Typelist:
                Trees[mass+coup+'_'+Type+'_'+chan]  = RootFilesBDT[mass+coup+'_'+Type+'_'+chan].Get(Type)
                #print 'Loaded Tree for ',mass+coup+'_'+Type+'_'+chan,': ',mass+coup+'_'+Type+'_'+chan
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
            Trees[mass+coup+'_'+mass+coup+'_'+chan]  = RootFilesBDT[mass+coup+'_'+mass+coup+'_'+chan].Get(mass+coup)
            #print 'Loaded Tree for ',mass+coup+'_'+mass+coup+'_'+chan,': ',mass+coup+'_'+mass+coup+'_'+chan


#### Generated Events (same as above) ######
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
                Nevents[mass+coup+'_wjets_'+chan] = Nevents['WJets']
                Nevents[mass+coup+'_ww_'+chan] = Nevents['WW']
                Nevents[mass+coup+'_ttbar_'+chan] = Nevents['TTbar_Madgraph']
                Nevents[mass+coup+'_zjets_'+chan] = Nevents['ZJets_M50']
                Nevents[mass+coup+'_tw_'+chan] = Nevents['T_tW']
                Nevents[mass+coup+'_btw_'+chan] = Nevents['Tbar_tW']
                Nevents[mass+coup+'_t_'+chan] = Nevents['T_t']
                Nevents[mass+coup+'_bt_'+chan] = Nevents['Tbar_t']
                Nevents[mass+coup+'_s_'+chan] = Nevents['T_s']
                Nevents[mass+coup+'_bs_'+chan] = Nevents['Tbar_s']

for chan in chanlist:
    Nevents['wp800R_wp800R_'+chan] = Nevents['Wprime800Right'] 
    Nevents['wp900R_wp900R_'+chan] = Nevents['Wprime900Right'] 
    Nevents['wp1000R_wp1000R_'+chan] = Nevents['Wprime1000Right'] 
    Nevents['wp1100R_wp1100R_'+chan] = Nevents['Wprime1100Right'] 
    Nevents['wp1200R_wp1200R_'+chan] = Nevents['Wprime1200Right'] 
    Nevents['wp1300R_wp1300R_'+chan] = Nevents['Wprime1300Right'] 
    Nevents['wp1400R_wp1400R_'+chan] = Nevents['Wprime1400Right'] 
    Nevents['wp1500R_wp1500R_'+chan] = Nevents['Wprime1500Right'] 
    Nevents['wp1600R_wp1600R_'+chan] = Nevents['Wprime1600Right'] 
    Nevents['wp1700R_wp1700R_'+chan] = Nevents['Wprime1700Right'] 
    Nevents['wp1800R_wp1800R_'+chan] = Nevents['Wprime1800Right'] 
    Nevents['wp1900R_wp1900R_'+chan] = Nevents['Wprime1900Right'] 
    Nevents['wp2000R_wp2000R_'+chan] = Nevents['Wprime2000Right'] 
    Nevents['wp2100R_wp2100R_'+chan] = Nevents['Wprime2100Right'] 
    Nevents['wp2200R_wp2200R_'+chan] = Nevents['Wprime2200Right'] 
    Nevents['wp2300R_wp2300R_'+chan] = Nevents['Wprime2300Right'] 
    Nevents['wp2400R_wp2400R_'+chan] = Nevents['Wprime2400Right'] 
    Nevents['wp2500R_wp2500R_'+chan] = Nevents['Wprime2500Right'] 
    Nevents['wp2600R_wp2600R_'+chan] = Nevents['Wprime2600Right'] 
    Nevents['wp2700R_wp2700R_'+chan] = Nevents['Wprime2700Right'] 
    Nevents['wp2800R_wp2800R_'+chan] = Nevents['Wprime2800Right'] 
    Nevents['wp2900R_wp2900R_'+chan] = Nevents['Wprime2900Right'] 
    Nevents['wp3000R_wp3000R_'+chan] = Nevents['Wprime3000Right'] 

#### Cross sections (same as above) ######
for chan in chanlist:
    for mass in masslist:
        for coup in couplist:
                xsec[mass+coup+'_wjets_'+chan] = xsec['WJets']
                xsec[mass+coup+'_ww_'+chan] = xsec['WW']
                xsec[mass+coup+'_ttbar_'+chan] = xsec['TTbar_Madgraph']
                xsec[mass+coup+'_zjets_'+chan] = xsec['ZJets_M50']
                xsec[mass+coup+'_tw_'+chan] = xsec['T_tW']
                xsec[mass+coup+'_btw_'+chan] = xsec['Tbar_tW']
                xsec[mass+coup+'_t_'+chan] = xsec['T_t']
                xsec[mass+coup+'_bt_'+chan] = xsec['Tbar_t']
                xsec[mass+coup+'_s_'+chan] = xsec['T_s']
                xsec[mass+coup+'_bs_'+chan] = xsec['Tbar_s']

for chan in chanlist:
    xsec['wp800R_wp800R_'+chan] = xsec['Wprime800Right'] 
    xsec['wp900R_wp900R_'+chan] = xsec['Wprime900Right'] 
    xsec['wp1000R_wp1000R_'+chan] = xsec['Wprime1000Right'] 
    xsec['wp1100R_wp1100R_'+chan] = xsec['Wprime1100Right'] 
    xsec['wp1200R_wp1200R_'+chan] = xsec['Wprime1200Right'] 
    xsec['wp1300R_wp1300R_'+chan] = xsec['Wprime1300Right'] 
    xsec['wp1400R_wp1400R_'+chan] = xsec['Wprime1400Right'] 
    xsec['wp1500R_wp1500R_'+chan] = xsec['Wprime1500Right'] 
    xsec['wp1600R_wp1600R_'+chan] = xsec['Wprime1600Right'] 
    xsec['wp1700R_wp1700R_'+chan] = xsec['Wprime1700Right'] 
    xsec['wp1800R_wp1800R_'+chan] = xsec['Wprime1800Right'] 
    xsec['wp1900R_wp1900R_'+chan] = xsec['Wprime1900Right'] 
    xsec['wp2000R_wp2000R_'+chan] = xsec['Wprime2000Right'] 
    xsec['wp2100R_wp2100R_'+chan] = xsec['Wprime2100Right'] 
    xsec['wp2200R_wp2200R_'+chan] = xsec['Wprime2200Right'] 
    xsec['wp2300R_wp2300R_'+chan] = xsec['Wprime2300Right'] 
    xsec['wp2400R_wp2400R_'+chan] = xsec['Wprime2400Right'] 
    xsec['wp2500R_wp2500R_'+chan] = xsec['Wprime2500Right'] 
    xsec['wp2600R_wp2600R_'+chan] = xsec['Wprime2600Right'] 
    xsec['wp2700R_wp2700R_'+chan] = xsec['Wprime2700Right'] 
    xsec['wp2800R_wp2800R_'+chan] = xsec['Wprime2800Right'] 
    xsec['wp2900R_wp2900R_'+chan] = xsec['Wprime2900Right'] 
    xsec['wp3000R_wp3000R_'+chan] = xsec['Wprime3000Right'] 


###############################################################
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

Yield['wp1500R_wp1500R_el'] = 113.
Yield['wp1700R_wp1700R_el'] = 50.
Yield['wp1900R_wp1900R_el'] = 22.
Yield['wp2100R_wp2100R_el'] = 10.
Yield['wp2300R_wp2300R_el'] = 5.

Yield['wp1500R_wp1500R_mu'] = 99.
Yield['wp1700R_wp1700R_mu'] = 42.
Yield['wp1900R_wp1900R_mu'] = 19.
Yield['wp2100R_wp2100R_mu'] = 9.
Yield['wp2300R_wp2300R_mu'] = 4.
                              
