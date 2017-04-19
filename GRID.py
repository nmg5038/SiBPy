import os, sys, re
import numpy as np
from LandUnit import *

def init_grid(dict):
	# CURRENTLY MIMICS SINGLE POINT RUN ONLY SIB4 INIT_GRID.f90
	print 'Setting Grid'
	# Single Point Simulations
	if dict['nsib'] != 1:
		print 'Expecting nsib value of 1.  Stopping.'
		sys.exit()
	print '     SiB points simulated =', dict['nsib']
	
	subset = np.array([1])
	sublatsib = np.array([dict['Latitude']])
	sublonsib = np.array([dict['Longitude']])
	subsitename = np.array(dict['Site Name'])
	
	latpbp = sublatsib
	lonpbp = sublonsib
	sibptpbp = np.array([1])
	
	npbp = 1
	sitenamepbp = subsitename
	grefpbp = subset
	
	prefpbp = np.array([[dict['PFT reference per landunit']]])
	lareapbp=np.array([[dict['Areal coverage of landunit']]])

	print '     Site Name: ',subsitename[0]
	print '     Site Lon/Lat: ',sublonsib[0] ,sublatsib[0]