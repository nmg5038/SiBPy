"""
    This module reads in the aero file designed for SiB4.
"""

__author__ = "Nicholas Geyer"
__credits__ = ["Nicholas Geyer", "Ian Baker", "Scott Denning",
               "Katherine Haynes"]
__license__ = "GNU GPLv3.0"
__version__ = "0.5.0"
__maintainer__ = "Nicholas Geyer"
__email__ = "nicholas.geyer@colostate.edu"
__status__ = "Development"

import netCDF4 as nc
from module_param import *
from read_namel import read_namel
from module_sibconsts import Constants


def check_for_file(complete_path_with_filename):
    """
    This is a generic program to make sure a file is found where you said it would be.
    It raises a ValueError if the file is not found
    :param complete_path_with_filename: A complete path string to the file in question
    :return: Nothing, if true
    """
    import os
    if os.path.isfile(complete_path_with_filename):
        return
    else:
        raise ValueError(complete_path_with_filename + ' does not exist')


def read_aerodynamics_tables(consts, aero_file):
    """
    This function will read in the aerodynamics file for SiBPy parameterizations
    :param consts: A class of constants from module_sibconsts
    :param aero_file: The path and filename of the aerodynamics file for SiBPy (string)
    :return: Returns 6 necessary aerodynamic files
    """

    npft = consts.npft
    aero_file = '/Users/nmg5038/sib4v2_corral/input/params/sib_aero.nc'  # Only for development

    # ...open file
    print('')
    print('Reading Aerodynamic File: ')
    print('  ', aero_file.strip())

    check_for_file(aero_file)
    ncfid = nc.Dataset(aero_file, 'r')

    # ...check npft
    temp = ncfid.dimensions['npft']

    npft = temp.size  # Just for development

    if temp.size != npft:
        raise ValueError('!!!Aerodynamic file does not match simulation!!!' +
                         '  Aero file npft: ', temp.size, ' Sim npft: ', npft)

    # ...read in values
    laigrid = ncfid.variables['laigrid'][:]
    fvcovergrid = ncfid.variables['fvcovergrid'][:]
    aero_zo = ncfid.variables['aero_zo'][:]
    aero_zp = ncfid.variables['aero_zp'][:]
    aero_rdc = ncfid.variables['aero_rbc'][:]
    aero_rbc = ncfid.variables['aero_rbc'][:]

    ncfid.close()

    return laigrid, fvcovergrid, aero_zo, aero_zp, aero_rdc, aero_rbc


def load_up_aero_params():
    from module_sibconsts import Constants
    consts = Constants()
    options = read_namel('./unit_testing_input/namel_sibdrv')
    AeroParams['LAIgrid'], AeroParams['fVCovergrid'], zo, zp, rdc, rbc = read_aerodynamics_tables(consts,
                                                                                                  options['aero_file'])
    AeroParams['AeroParam'].load_param(zo, zp, rdc, rbc)
    return


if __name__ == '__main__':

    consts = Constants()
    options = read_namel('./unit_testing_input/namel_sibdrv')
    AeroParams['LAIgrid'], AeroParams['fVCovergrid'], zo, zp, rdc, rbc = read_aerodynamics_tables(consts,
                                                                                                  options['aero_file'])
    AeroParams['AeroParam'].load_param(zo, zp, rdc, rbc)
