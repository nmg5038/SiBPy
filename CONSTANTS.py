import os, sys, re
import numpy as np

class CONSTANTS(dict):
	def __init__(self):
		
		# User specific variables for SiB
		self['version'] = 4.0
		self['sib_source'] = 'SiB4'
		self['grid_source'] = 'lat/lon'
		
		# ...Land Unit Information
		self['nlu'] = 10							# number of land units
		self['nsoil'] = 10							# number of soil layers 
		self['nsnow'] = 5							# max number of snow layers
		self['ntot'] = self['nsoil']+self['nsnow']	# total number of layers in soil column

		#...Phenology Information
		self['dtphen'] = 86400   # seconds in simulation to update phenology
		
		self['clen'] = 7
		constList =['npft',
			'ntype',
			'ngroup',
			'nphase',
			'npoolpft',
			'npoollu',
			'ntpool',
			'cornsoy_switch',
			'grazing_switch',
			'poolclear_switch',
			'leapyear_switch',
			'savereq_switch',
			'timelst_switch',
			'updatelst_switch',
			'single_pt',
			'nsib',
			'subcount',
			'latsib',
			'lonsib',
			'sitenamesib',
			'minlon',
			'maxlon',
			'minlat',
			'maxlat',
			'subset',
			'sublatsib',
			'sublonsib',
			'subpref',
			'sublarea',
			'subsitename',
			'sin_dec',
			'cos_dec',
			'tan_dec',
			'lonearth',
			'spinup',
			'spinup_default',
			'spinup_output',
			'spinup_default',
			'spinup_maxiter',
			'spinup_threshold',
			'spinup_done',
			'spinup_lnum',
			'spinup_ynum']
		self.update(dict.fromkeys(set(constList)))
		



 
