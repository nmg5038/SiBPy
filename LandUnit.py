import os, sys
import numpy as np
from PFT import *
from POOLS import *

class LandUnit():
	def __init__(self,whatPFTs,areaDistributions):
		self.npft = 24
		self.ntype = 5
		self.ngroup = 6
		self.nphase = 5
		self.nLUPools = 6
		self.nPFTpools = 5
		# A bunch of sanity checks
		if whatPFTs.size != areaDistributions.size:
			print "INVALID NUMBER OF EITHER PFTs or Area Distributions: SHUTTING DOWN"
			sys.exit()
		#if whatPFTs.size > 10:
		#	print "TOO MANY PFT IN LAND UNIT: SHUTTING DOWN"
		#	sys.exit()
		if np.any((whatPFTs <= 0, whatPFTs > self.npft)):
			print "INVALID PFT DETECTED: SHUTTING DOWN"
			sys.exit()
		if np.any((areaDistributions < 0, areaDistributions > 1)):
			print "INVALID PFT AREA DETECTED: SHUTTING DOWN"
			sys.exit()
		
		# Map information
		self.pftSource= 'MODIS 1-km'
		self.cropSource= 'Foley and Ramankutty'
		self.soliSource= 'ISLSCP II (Dazlich et al.)'
		self.sorefSource= 'ISLSCP II (Dazlich et al.)'
		
		# Phenology Phases
		self.phaseName = ['Leaf-Out','Growth','Mature','Stress','Dormant']
		
		
		# Create PFTs within the Land Unit
		self.pftsInUnit = []
		
		for index,whatPFT in enumerate(whatPFTs):
			self.pftsInUnit.append(PFT(whatPFT,areaDistributions[index]))
		
		# Pool attribution
				

if __name__ == "__main__":
	frt = np.arange(1,24)
	
	LU = LandUnit(frt,np.ones(frt.size))
	
		
