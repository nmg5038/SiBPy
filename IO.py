import os, sys, re
import numpy as np
import netCDF4 as net

def READ_AERO(dict,textFile):
	print 
	print 'Reading Aerodynamic File: '
	print '  ',textFile.strip()
	
	if os.path.exists(textFile.strip()):
		ncfid = net.Dataset(textFile.strip(),'r')
		temp = ncfid.dimensions['npft'].size
		
		if temp != dict['npft']:
			print
			print '!!!Aerodynamic file does not match simulation!!!'
			print'  Aero file npft: ',temp,' Sim npft: ',dict['npft']
			print
			sys.exit()
		    
		laigrid = ncfid.variables['laigrid'][:].copy()
		fvcovergrid = ncfid.variables['fvcovergrid'][:].copy()
		aero_zo = ncfid.variables['aero_zo'][:].copy()
		aero_zp = ncfid.variables['aero_zp'][:].copy()
		aero_rbc = ncfid.variables['aero_rbc'][:].copy()
		aero_rdc = ncfid.variables['aero_rdc'][:].copy()
		ncfid.close()
		aerodict ={'zo':aero_zo,'zp_disp':aero_zp,'rbc':aero_rbc,'rdc':aero_rdc}

	return aerodict

def READ_SIBVS(textFile):	# Mimics READ_SIBVS (SINGLE POINT RUNS)
	stuffToLookFor =['nsib',
	'npft',
	'nlu',
	 'Latitude',
	 'Longitude',
	 'SiB Point',
	 'Site Name',
	 'Number of landunits per gridcell',
	 'Areal coverage of landunit',
	'Sand fraction of landunit',
	'Clay fraction of landunit',
	 'soref_vis of landunit',
	 'soref_nir of landunit',
	 'Number of PFTs in landunit',
	 'Areal coverage of PFTs in landunit',
	 'PFT reference per landunit']
	dict = {}
	with open(textFile,'rb') as f:
		for line in f:
			condensedLine = re.split('\n| \s{2,}',line.strip())  # Split by newline and anything more than 2 spaces
			
			bool = (not set(stuffToLookFor).isdisjoint(condensedLine)) # Check to see if any general items have overlapping
			
			if bool:
				value = condensedLine[0]							# Value of item is first in file
				if all(z in dict for z in [condensedLine[1]]):		# Check to see if key is already in dictionary
					pulledDict = dict[condensedLine[1]]				# If so, we will append the list
				else:
					pulledDict = []									# Else, we will make a new one
					
				try:												# If value is numerical we need to find out if it is
					a=float(value)									# a float or integer
					b=int(a)
					
					if a==b:										# If an integer, save integer value
						valueUsed = b
					else: 
						valueUsed = a								# Else, use the float
					
					pulledDict.append(valueUsed)					# Append list
					
					dict[condensedLine[1]] = pulledDict				# Store list in dictionary
					
				except ValueError:
					wordsWithHyphens = re.findall(r'\w+(?:-\w+)+',value)  # In case of a word, find site name
					
					if len(wordsWithHyphens) == 0:						# Spurrious issue (no hyphen in site name)?
						continue
						
					pulledDict.append(wordsWithHyphens)				# Store list in dictionary
					
					dict[condensedLine[1]] = pulledDict				# Store list in dictionary
											
		for i in dict:						# Special check: If item in dictionary has 1 value, just remove it from list form
			if len(dict[i]) == 1:
				dict[i] = dict[i][0]
		return dict