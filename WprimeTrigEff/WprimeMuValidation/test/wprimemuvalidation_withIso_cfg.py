import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi")
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi")
process.load("TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorOpposite_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'GR10_P_V11::All'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.options = cms.untracked.PSet(
    fileMode  =  cms.untracked.string('NOMERGE') 
)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

myfilelist = cms.untracked.vstring()
myfilelist.extend( [

'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_10_1_P4Q.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_11_1_ps9.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_12_2_dNn.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_13_1_lrP.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_14_2_e72.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_15_1_cFw.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_16_2_Idv.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_17_1_G8Z.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_18_2_u0l.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_19_1_VRM.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_1_1_Z4y.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_20_2_vkn.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_21_1_1cM.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_22_1_p6B.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_23_2_7pi.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_24_2_XRF.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_25_1_9dJ.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_26_1_DXm.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_27_1_lpm.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_28_2_BxB.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_29_1_4UV.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_2_2_CCZ.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_30_1_KDp.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_31_1_ywT.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_33_2_gQj.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_36_3_v0m.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_37_1_Kc7.root',
#'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_38_1_vAw.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_39_1_YyA.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_3_2_gdd.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_40_2_WGX.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_41_1_K5m.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_42_1_1OZ.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_43_2_6dK.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_44_1_VXI.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_45_2_OVK.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_46_2_q7H.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_47_2_GbY.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_48_1_C5p.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_4_1_xBb.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_50_2_sNc.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_51_3_MIT.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_51_4_JG7.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_52_2_UfX.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_53_2_qQV.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_54_2_7Ht.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_55_2_9Cm.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_56_2_x9n.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_57_1_9zG.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_58_2_JDJ.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_59_1_h4Y.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_5_1_gXZ.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_60_1_tSu.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_61_2_8WD.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_62_1_8kL.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_6_2_lum.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_7_1_pRb.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_8_2_Oti.root',
'rfio:/castor/cern.ch/user/d/dsperka/wprime_munu/MultiJet/WprimeTrigEffMuSkim_9_1_9n8.root'

] )


process.source = cms.Source("PoolSource",
    # replace 'myfile.root',',' with the source file you want to use
    fileNames = myfilelist
)

process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange(
#   	'147196:1-147196:90',
#	'147214:1-147214:79',
#	'147216:1-147216:63',
#	'147217:1-147217:193',
#	'147218:1-147218:45',
#	'147219:1-147219:293',
#	'147219:309-147219:320',
#	'147222:1-147222:444',
#	'147284:32-147284:306',
#	'147390:1-147390:478',
#	'147390:480-147390:839',
#	'147450:80-147450:166',
#	'147451:1-147451:116',
#	'147451:118-147451:129',
#	'147452:1-147452:44',
#	'147453:1-147453:146',
#	'147454:1-147454:97',
#	'147754:1-147754:167',
#	'147754:170-147754:377',
#	'147755:81-147755:231',
#	'147757:1-147757:363',
#	'147926:77-147926:548',
#	'147927:1-147927:152',
#	'147929:1-147929:266',
#	'147929:272-147929:618',
#	'147929:620-147929:643',
#	'148002:92-148002:203',
#	'148029:50-148029:483',
#	'148029:485-148029:569',
#	'148029:571-148029:571',
#	'148031:1-148031:341',
#	'148031:472-148031:757',
#	'148031:759-148031:855',
#	'148032:1-148032:199',
#	'148058:1-148058:97',
    # Mu 11 Got Prescaled 
	'148822:1-148822:446',
	'148829:1-148829:73',
	'148829:75-148829:240',
	'148829:244-148829:303',
	'148860:1-148860:39',
	'148862:1-148862:18',
	'148862:20-148862:108',
	'148862:110-148862:149',
	'148862:151-148862:165',
	'148862:224-148862:258',
	'148862:262-148862:297',
	'148862:299-148862:366',
	'148862:368-148862:504',
	'148862:512-148862:679',
	'148864:1-148864:31',
	'148864:33-148864:141',
	'148864:224-148864:236',
	'148864:238-148864:476',
	'148864:478-148864:680',
	'148952:70-148952:257',
	'148953:1-148953:100',
	'149003:84-149003:238',
	'149011:1-149011:341',
	'149011:343-149011:706',
	'149058:1-149058:65',
	'149063:1-149063:102',
	'149181:229-149181:1840',
	'149181:1844-149181:1920',
	'149182:1-149182:16',
	'149182:18-149182:62',
	'149182:84-149182:169',
	'149182:171-149182:444',
	'149291:79-149291:79',
	'149291:82-149291:786',
	'149291:788-149291:788',
	'149291:790-149291:790',
	'149291:794-149291:794',
	'149294:1-149294:171'
    )

process.TFileService = cms.Service("TFileService", 
      #fileName = cms.string("histos.root',"),
      fileName = cms.string("WprimeTrigEff_MultiJet_148822-149294-v2.root"),
      closeFileFast = cms.untracked.bool(True)
  )


process.demo = cms.EDAnalyzer('WprimeMuValidation_v2',
    HLTriggerResults = cms.InputTag("TriggerResults","","HLT"),
    useTrack = cms.string("global"),  # 'none' to use Candidate P4; or 'tracker', 'muon', 'global'
    useState = cms.string("atVertex"), # 'innermost' and 'outermost' require the TrackExtra
    useSimpleGeometry = cms.bool(True), # just use a cylinder plus two disks.
    fallbackToME1 = cms.bool(False),    # If propagation to ME2 fails, propagate to ME1
    tevMuonLabel = cms.string("tevMuons"),
    triggerConditions = cms.vstring('HLT_Mu9',
                                    'HLT_Mu9_v*',
                                    'HLT_Mu11',
                                    'HLT_Mu11_v*',
                                    'HLT_Mu13',
                                    'HLT_Mu13_v*',
                                    'HLT_Mu15',
                                    'HLT_Mu15_v*',
                                    'HLT_Mu17',
                                    'HLT_Mu17_v*',
                                    'HLT_Mu19',
                                    'HLT_Mu19_v*',
                                    'HLT_Mu21',
                                    'HLT_Mu21_v*'
                                    )
)


process.p = cms.Path(process.demo)

