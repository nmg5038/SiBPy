import os, sys
import numpy as np

class Pool():
	def __init__(self,whichPool):

		self.poolInformation(whichPool)
		
	def poolInformation(self,whichPool):		# MIMICS READ_POOLINFO
		poolInfo=[['leaf','leaf','live','canopy',1],
		['fine root','froot','live','soil',10],
		['coarse root','croot','live','soil',10],
		['wood','wood','live','canopy',1],
		['product','prod','live','canopy',1],
		['coarse woody debris','cwd','dead','surface',1],
		['litter metabolic','litmet','dead','surface',1],
		['litter structural','litstr','dead','surface',1],
		['soil litter','slit','dead','soil',10],
		['soil slow','slow','dead','soil',10],
		['slow armored','arm','dead','soil',10],]
		poolData = poolInfo[whichPool]
		
		self.poolLongName = poolData[0]
		self.poolShortName = poolData[1]
		self.poolType = poolData[2]
		self.poolLocation = poolData[3]
		self.poolVerticalLevel = poolData[4]
		
		self.pool_min= 0.1
		self.lai_min= 0.01
		self.laigs_min= 0.10
		self.assim_min= 0.01
		self.mntnr_min= 0.01
		self.assimfac_frac= 0.5
		self.gdd_nc_tbase= 32
		self.gdd_crop_tbase= 50
		

