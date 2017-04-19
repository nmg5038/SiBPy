import os, sys
import numpy as np
from PhenologyPhysiology import *

class PFT(PhenologyPhysiology):
	def __init__(self,whatPFTamI,areaProportionInLU):
		
		self.pftArea = areaProportionInLU
		self.pftConstruct(whatPFTamI)
		self.pftPhenology()
		self.pftPhysiology()
		
	def pftConstruct(self,whatPFTamI):  # MIMICS READ_PFTINFO

		# Type Information
		longTypeName = ['Bare Ground', 'Evergreen','Deciduous','Grass','Crop']
		typeName = ['bare','evg','decid','grass','crop']
		
		# Group Information
		longGroupName = ['Barren', 'Needleleaf Forest','Broadleaf Forest','Shrub','Grass','Crop']
		groupName = ['bare','ndlfor','bdlfor','shrub','grass','crop']
		
		pftNames = ['des_all','enf_tem','enf_bor','dnf_bor','ebf_tro','ebf_tem','dbf_tro', \
			'dbf_tem','dbf_bor','xxx_xxx','shb_nar','shb_arc','c3g_arc','c3g_nar', 'c4g_all', \
			'xxx_xxx','cro_tro','cro_tem','xxx_xxx','mze_tro','mze_tem','soy_tro','soy_tem','wwt_all']

		self.pftNumber = whatPFTamI
		
		self.pftName = pftNames[whatPFTamI-1]
		
		if np.any((self.pftNumber == 1, self.pftNumber == 10, self.pftNumber==16,self.pftNumber==19)): # Desert and XXX
  			self.pftType = 1
  			self.pftGroup = 1
  		elif np.any((self.pftNumber == 2,self.pftNumber == 3)):  # ENF (temparate, boreal)
  			self.pftType = 2
  			self.pftGroup = 2
		elif self.pftNumber == 4:			# DNF (boreal)
			self.pftType = 3
			self.pftGroup = 2
  		elif np.any((self.pftNumber == 5,self.pftNumber == 6)):  # EBF (temparate, boreal)
  			self.pftType = 2
  			self.pftGroup = 3
  		elif np.any((self.pftNumber == 7,self.pftNumber == 8,self.pftNumber == 9)):  # DBF (temparate, boreal)
  			self.pftType = 3
  			self.pftGroup = 3
  		elif np.any((self.pftNumber == 11,self.pftNumber == 12)):  # Shrubs (nar, arctic)
  			self.pftType = 3
  			self.pftGroup = 4
  		elif np.any((self.pftNumber == 13,self.pftNumber == 14,self.pftNumber == 15)):  # C3/C4 Grass (arc, nar, all) 
  			self.pftType = 4
  			self.pftGroup = 5
  		else:  					# Crops, maize, soy, winter wheat 
  			self.pftType = 5
  			self.pftGroup = 6
		
		# Type Information
		self.longTypeName = longTypeName[self.pftType-1]
		self.typeName = typeName[self.pftType-1]
		
		# Group Information
		self.longGroupName = longGroupName[self.pftGroup-1]
		self.groupName = groupName[self.pftGroup-1]
		

	def pftPhenology(self):
		vegetationInfo,allocationInfo,growingSeasonStartInfo,phenoStageFactInfo, \
		phenoStageThreshInfo,livePoolTurnoverInfo,livePoolGrowthRespInfo,livePoolRespTransInfo, \
		livePoolRespInfo,livePoolTransInfo,deadPoolTurnoverInfo,deadPoolTempRespInfo=self.phenoHelper()
		
		# Vegetation Info
		self.vmax0=np.array(vegetationInfo[0:5])
		self.sla,self.laimin,self.laisat,self.fparsat= [float(i) for i in vegetationInfo[5:9]]
		tempgrzswitch=int(vegetationInfo[9])
		
		self.tempgrzswitch = False
		if tempgrzswitch == 1:
			self.tempgrzswitch = True
		
		# Allocation Info 
		self.allocationInformation = np.reshape(allocationInfo, (5, 5))
		
		# Growing Season Info
		self.light_mini, self.light_mind, self.tawftop_min, self.tawftop_avelen, self.tm_min, self.tm_avelen = [float(i) for i in growingSeasonStartInfo]
		
		# Phenology Stage Factor Information
		self.assim_avelen, self.rst_avelen,self.cstress_a, self.cstress_b, self.cstress_c, self.cstress_d, self.cstress_min, self.cstress_max, self.lctb_coef, self.lctb_offl,  self.lctb_offg, self.lctb_min,  self.lctb_max = [float(i) for i in phenoStageFactInfo]
			
		# Phenology Stage Threshold Information
		self.assim_reset, self.pstg_fac = float(phenoStageThreshInfo[0]), np.array(phenoStageThreshInfo[1:])
		
		# Live Pool Turnover Times (yr-->sec)
		
		self.rt_rate = np.array(livePoolTurnoverInfo)
		activeRT_Rate = np.where(self.rt_rate > 0)
		self.rt_rate[activeRT_Rate] = 1. / (self.rt_rate[activeRT_Rate] * (365.0 * 24.0 * 3600.0))
		
		# Live Pool Growth Respiration Fractions (0-1)
		self.gr_frac = np.array(livePoolGrowthRespInfo)
		
		#
		self.art_can_reff, self.art_scale_off, self.art_scale_min, self.art_scale_max, \
			self.art_assim_mul, self.art_assim_offl, self.art_assim_offg, self.art_assim_min, \
			self.art_assim_max, self.art_soil_reff, self.art_soil_q10, self.art_soil_tref = [float(i) for i in livePoolRespTransInfo]

		self.art_can_teff = 1. - self.art_can_reff
		self.art_soil_teff = 1. - self.art_soil_reff
		
		# Live Pool Respiration Parameters
		self.ar_hot_q10, self.ar_hot_tref, self.ar_hot_max =  [float(i) for i in livePoolRespInfo]
		self.at_daylen_coef, self.at_daylen_ref, self.at_daylen_max, \
		self.at_cold_q10, self.at_cold_tref, self.at_cold_max, self.at_hot_q10, self.at_hot_tref, \
		self.at_hot_max =   [float(i) for i in livePoolTransInfo]
		
		# Dead pool resp turnover times
		self.turnover = np.array(deadPoolTurnoverInfo)
		
		# Dead pool heterotrophic respiration temperature
		self.hrt_lit_q10, self.hrt_lit_tref, self.hrt_soil_q10, self.hrt_soil_tref =   [float(i) for i in deadPoolTempRespInfo]

	def pftPhysiology(self):
		ecologicalParameters, stressParameters, photosynthesisParameters, radiativeParameters = self.physHelper()
		self.c4flag = int(ecologicalParameters[0]) 
		self.chil, self.z1,self.z2, self.kroot, self.rootd = [float(i) for i in ecologicalParameters[1:]]
		
		self.slti, self.shti, self.hlti, self.hhti, self.hfti, self.sfti, self.wssp = [float(i) for i in stressParameters]
		
		self.effcon, self.gmeso, self.binter, self.gradm, self.atheta, self.btheta = [float(i) for i in photosynthesisParameters]
		
		self.tran= np.reshape(radiativeParameters[0:4], (2, 2))
		self.ref= np.reshape(radiativeParameters[4:], (2, 2))

		
		
		
		