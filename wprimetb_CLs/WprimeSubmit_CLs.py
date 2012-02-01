#!/usr/bin/python

import os
import re
import fileinput
import math

rel_base = os.environ['CMSSW_BASE']

#mass = ['0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1900','2100','2300','2500']  
mass = [1000]  

wprime = 'Right'

Algorithm = 'HybridNew'
#Algorithm = 'Asymptotic'
Option1 = ' --frequentist --testStat LHC --rAbsAcc=0.0001 --fork 4 -H Asymptotic '
#Option1 = ' --rAbsAcc=0.0001 '


direc = '/uscms_data/d2/dsperka/Wprimetb/Limits_CLsLHC_30Jan2012'

### What is the name of your FWLite Analyzer

print 'CONDOR work dir: '+direc
os.system('rm -rf '+direc)
os.system('mkdir -p '+direc)

for i in range(len(mass)):
   
    if i == 0: Type = 'Wprime_800_'+wprime+'Wprime'
    elif i == 1: Type = 'Wprime_900_'+wprime+'Wprime'
    else: Type = 'Wprime_'+str(mass[i])+'_'+wprime+'Wprime'
    
    print Type
  
    #for quant in ('exp.025','exp.16','exp.50','exp.84','exp.975','obs'): 
    #for quant in (0.025,0.16,0.50,0.84,0.975): 
    for quant in (0.16,0.50,0.84): 
    
        r = 0.01 
        while (r<2.01): 

            #if (quant == 'exp.025'): Option2 = ' --expectedFromGrid 0.025 --rRelAcc=0.03'
            #elif (quant == 'exp.16'): Option2 = ' --expectedFromGrid 0.16 --rRelAcc=0.03'
            #elif (quant == 'exp.50'): Option2 = ' --expectedFromGrid 0.50 --rRelAcc=0.03'
            #elif (quant == 'exp.84'): Option2 = ' --expectedFromGrid 0.84 --rRelAcc=0.03'
            #elif (quant == 'exp.975'): Option2 = ' --expectedFromGrid 0.975 --rRelAcc=0.03'
            #elif (quant == 'obs'): Option2 = ' --rRelAcc=0.03'

            Option3 = ' -s '+str(int((math.sin(r)*100000+mass[i])/quant))+' --singlePoint '+str(r)+' --saveToys --saveHybridResult --clsAcc 0'
            Option2 = ' --expectedFromGrid '+str(quant)+' '+Option3

            condor_templ_file = open(rel_base+"/src/WprimeCLscondor.templ")
            csh_templ_file    = open(rel_base+"/src/WprimeCLscsh.templ")

            condor_file = open(direc+"/"+Type+"_"+str(quant)+"_"+str(r)+".condor","w")
            for line in condor_templ_file:
                line=line.replace('DIRECTORY',direc)
                line=line.replace('TYPE',Type)
                line=line.replace('QUANTILE',str(quant)+"_"+str(r))
                condor_file.write(line)
            condor_file.close()

            csh_file = open(direc+"/"+Type+"_"+str(quant)+"_"+str(r)+".csh","w")
            for line in csh_templ_file:
                line=line.replace('CMSSWBASE',rel_base)
                line=line.replace('ALGORITHMNAME',Algorithm)
                line=line.replace('FIRSTOPTION',Option1)
                line=line.replace('MASS',str(mass[i]))
                line=line.replace('WPRIME','TestWprime'+wprime) #### CHANGE AFTER TESTING
                line=line.replace('SECONDOPTION',Option2)
                line=line.replace('THEDATACARD','datacard_'+Type+'_el.txt')
                csh_file.write(line)
            csh_file.close()

            os.system('chmod u+x '+direc+'/'+Type+"_"+str(quant)+"_"+str(r)+'.csh')
            os.system('condor_submit '+direc+'/'+Type+"_"+str(quant)+"_"+str(r)+'.condor')

            condor_templ_file.close()
            csh_templ_file.close()
             
            r = r + 0.01 
             


    
