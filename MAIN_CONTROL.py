import os, sys, re
import numpy as np
from LandUnit import *
from IO import *
from GRID import *
from CONSTANTS import *
## MAIN PROGRAM ##

if __name__ == "__main__":
	cnsts = CONSTANTS()
	
	print cnsts['version']
	dict=READ_SIBVS('./sib_vs.txt')
	
	init_grid(dict)
	READ_AERO(dict,'/Users/nmg5038/SiB4/trunk/input/params/sib_aero.nc')
	
	