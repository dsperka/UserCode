#!/usr/bin/python

import os
import re
import fileinput

rel_base = os.environ['CMSSW_BASE']

mass = ['800','900','1000','1100','1200','1300','1400','1500','1600','1700','1900','2100','2300','2500']  

wprime = 'Right'

Algorithm = 'HybridNew'
Option1 = ' --frequentist --testStat LHC --rAbsAcc=0.0001 --fork 4 -H Asymptotic '

direc = '/uscms_data/d2/dsperka/Wprimetb/Limits_CLs_26Jan2012'

### What is the name of your FWLite Analyzer

print 'CONDOR work dir: '+direc
os.system('rm -rf '+direc)
os.system('mkdir -p '+direc)

for i in range(len(mass)):
   
    Type = 'Wprime_'+mass[i]+'_'+wprime+'Wprime'
    print Type
  
    for quant in ('exp.025','exp.16','exp.50','exp.84','exp.975','obs'): 

        if (quant == 'exp.025'): Option2 = ' --expectedFromGrid 0.025 --rRelAcc=0.05'
        elif (quant == 'exp.16'): Option2 = ' --expectedFromGrid 0.16 --rRelAcc=0.05'
        elif (quant == 'exp.50'): Option2 = ' --expectedFromGrid 0.50 --rRelAcc=0.05'
        elif (quant == 'exp.84'): Option2 = ' --expectedFromGrid 0.84 --rRelAcc=0.05'
        elif (quant == 'exp.975'): Option2 = ' --expectedFromGrid 0.975 --rRelAcc=0.05'
        elif (quant == 'obs'): Option2 = ' --rRelAcc=0.01'


        condor_templ_file = open(rel_base+"/src/WprimeCLscondor.templ")
        csh_templ_file    = open(rel_base+"/src/WprimeCLscsh.templ")

        condor_file = open(direc+"/"+Type+"_"+quant+".condor","w")
        for line in condor_templ_file:
            line=line.replace('DIRECTORY',direc)
            line=line.replace('TYPE',Type)
            line=line.replace('QUANTILE',quant)
            condor_file.write(line)
        condor_file.close()

        csh_file = open(direc+"/"+Type+"_"+quant+".csh","w")
        for line in csh_templ_file:
            line=line.replace('CMSSWBASE',rel_base)
            line=line.replace('ALGORITHMNAME',Algorithm)
            line=line.replace('FIRSTOPTION',Option1)
            line=line.replace('MASS',mass[i])
            line=line.replace('WPRIME','Wprime'+wprime)
            line=line.replace('SECONDOPTION',Option2)
            line=line.replace('THEDATACARD','datacard_'+Type+'_el.txt')
            csh_file.write(line)
        csh_file.close()

        os.system('chmod u+x '+direc+'/'+Type+"_"+quant+'.csh')
        os.system('condor_submit '+direc+'/'+Type+"_"+quant+'.condor')

        condor_templ_file.close()
        csh_templ_file.close()




    
