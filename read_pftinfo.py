"""
    This module reads in the aero file designed for SiB4.
"""

__author__ = "Nicholas Geyer"
__credits__ = ["Nicholas Geyer", "Ian Baker", "Scott Denning",
               "Katherine Haynes"]
__license__ = "GNU GPLv3.0"
__version__ = "0.0.1"
__maintainer__ = "Nicholas Geyer"
__email__ = "nicholas.geyer@colostate.edu"
__status__ = "Development"

import netCDF4 as nc
import re
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

def retrieve_only_numerics_from_string(string_to_check):

    pass
def read_pftinfo():
    options['pft_info'] = '/Users/nmg5038/sib4v2_corral/input/params/info_pft.dat' # This is only for dev
    pft_info = options['pft_info']

    check_for_file(pft_info)
    print('')
    print('Reading PFT Informational File:   ',pft_info.strip())

    viable_lines = []
    # Read the pft info dat file into memory.  We can parse this out since it is so small
    with open(pft_info, 'r') as f:
        for line_with_spaces in f:
            if re.search(r"[\*\-]{2,}?|^\s*$",line_with_spaces) is None:
                viable_lines.append(line_with_spaces.strip())

    # First five lines are inputs of number of pfts, types, functional groups, etc.
    npft = int(viable_lines[0].split(' ')[0])
    ntype = int(viable_lines[1].split(' ')[0])
    ngroup = int(viable_lines[2].split(' ')[0])
    npmeth = int(viable_lines[3].split(' ')[0])
    npstgmax = int(viable_lines[4].split(' ')[0])

    # ...Read in map information
    pft_source = viable_lines[6].split('\'')[1]
    crop_source = viable_lines[7].split('\'')[1]
    soil_source = viable_lines[8].split('\'')[1]
    soref_source = viable_lines[9].split('\'')[1]

    #...Read in type information
    type_name_long = []
    type_name = []
    for idx in range(12,17):
        nouse,tnl,tn=re.split(r"\s{2,}",viable_lines[idx])
        type_name_long.append(tnl)
        type_name.append(tn)

    # ...Read in group information
    group_name_long = []
    group_name = []
    for idx in range(19,25):
        nouse,gnl,gn=re.split(r"\s{2,}",viable_lines[idx])
        group_name_long.append(gnl)
        group_name.append(gn)

    # ...Read in phenology method information

    pmeth_name = []
    for idx in range(27,30):
        nouse,pmn=re.split(r"\s{2,}",viable_lines[idx])
        pmeth_name.append(pmn)


    """
#...Read in phenology method information

do i=1,npmeth
   read(pftid,'(i6,a20)') ref, pmeth_name(i)
enddo
    """
    #print(type(text))
    #open(unit=pftid,file=trim(pft_info),form='formatted')

if __name__ == '__main__':

    consts = Constants()
    options = read_namel('./unit_testing_input/namel_sibdrv')
    read_pftinfo()
