"""
    This module is a pseudo main for SiBPy.  Its primary purpose is to make sure all variables and codes
    are run together seamlessly.
"""

__author__ = "Nicholas Geyer"
__credits__ = ["Nicholas Geyer", "Ian Baker", "Scott Denning",
               "Katherine Haynes"]
__license__ = "GNU GPLv3.0"
__version__ = "0.0.1"
__maintainer__ = "Nicholas Geyer"
__email__ = "nicholas.geyer@colostate.edu"
__status__ = "Development"

from read_namel import read_namel
from module_sibconsts import Constants
from module_param import *
from read_aero import read_aerodynamics_tables

if __name__ == '__main__':

    consts = Constants()
    options = read_namel('./unit_testing_input/namel_sibdrv')
    AeroParams['LAIgrid'], AeroParams['fVCovergrid'], zo, zp, rdc, rbc = read_aerodynamics_tables(consts,
                                                                                               options['aero_file'])
    AeroParams['AeroParam'].load_param(zo, zp, rdc, rbc)

