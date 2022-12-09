"""
    This module reads in the namelist designed for SiB4.
    It checks for input validity (boolean, string, numerical) and converts
    the input to be used in SiBPy.
"""

__author__ = "Nicholas Geyer"
__credits__ = ["Nicholas Geyer", "Ian Baker", "Scott Denning",
               "Katherine Haynes"]
__license__ = "GNU GPLv3.0"
__version__ = "0.5.0"
__maintainer__ = "Nicholas Geyer"
__email__ = "nicholas.geyer@colostate.edu"
__status__ = "Development"


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


def read_namel(namel_name):
    """
    This is the core definition to read and convert namelist components.  It is based off the
        one found in SiB4's FORTRAN-only version from CSU.  The function will return a dictionary
        able to be applied to input class variables.  Errors found in the namelist will raise a ValueError
        with a little bit information to help debug
    :param namel_name: A path to the namelist
    :return: A dictionary containing the names and values of all required namelist components (if they exist in the namelist)
    """
    import re

    # This is where the constants are stored...in these modules
    # use module_sibconst
    # use module_io
    # use module_time

    CONTROL_LIST_SIBDRV_NAMES = ['nsib', 'starttime',
                                 'startyear', 'endtime', 'endyear',
                                 'dtsib', 'restart_dtsib', 'qp_dtsib', 'pbp_dtsib',
                                 'hr_dtsib']

    IO_LIST_SIBDRV_NAMES_NAMES = ['pft_info', 'pool_info',
                                  'aero_file', 'pgdd_file', 'pstg_file',
                                  'phys_file', 'pool_file',
                                  'vs_file', 'ic_file', 'dr_path', 'tm5_path',
                                  'fr_path', 'out_path', 'out_info', 'out_rinfo']

    SPINUP_LIST_SIBDRV_NAMES = ['spinup', 'spinup_default',
                                'spinup_numyrs', 'spinup_maxiter', 'spinup_threshold',
                                'spinup_writediag', 'spinup_writetxtf']

    SUBGRID_SIBDRV_NAMES = ['minlon', 'maxlon',
                            'minlat', 'maxlat']

    PBP_LIST_SIBDRV_NAMES = ['npbp']

    BALAN_LIST_SIBDRV_NAMES = ['badtc_print', 'badtc_stop',
                               'canb_print', 'canb_stop', 'canb_thresh',
                               'carbonb_print', 'carbonb_stop', 'carbonb_thresh',
                               'fireb_print', 'fireb_stop', 'fireb_thresh',
                               'snocmbn_print', 'snocmbn_stop', 'snocmbn_thresh',
                               'bnum_allow', 'energyb_print', 'energyb_stop', 'energyb_thresh',
                               'waterb_print', 'waterb_stop', 'waterb_thresh']

    PRINT_LIST_SIBDRV_NAMES = ['print_avec', 'print_driver', 'print_fire',
                               'print_harvest', 'print_pftinfo', 'print_pooll', 'print_soil',
                               'print_sscol', 'print_veg', 'print_stop']

    SWITCH_LIST_SIBDRV_NAMES = ['cornsoy_switch', 'fire_switch',
                                'grazing_switch', 'green_switch', 'eqclear_switch',
                                'leapyr_switch', 'updatelst_switch', 'varcos_switch',
                                'soilogee_switch', 'varco2_switch']

    set_of_names = []
    for name_set in [CONTROL_LIST_SIBDRV_NAMES, IO_LIST_SIBDRV_NAMES_NAMES, SPINUP_LIST_SIBDRV_NAMES,
                     SUBGRID_SIBDRV_NAMES, PBP_LIST_SIBDRV_NAMES, BALAN_LIST_SIBDRV_NAMES, PRINT_LIST_SIBDRV_NAMES,
                     SWITCH_LIST_SIBDRV_NAMES]:
        set_of_names = set_of_names + name_set

    namelist_option_storage = {}
    # -----------------------------------------------------------------------
    # read in namel_sibdrv
    # -----------------------------------------------------------------------
    namel_name = namel_name.replace(" ", "")
    print('')
    check_for_file(namel_name)
    print('Reading in namelist file: ', namel_name)

    read_in_npbp_latlon = False
    pbp_latlon = None
    with open(namel_name, 'r') as f:
        line_break = False
        for line_with_spaces in f:
            line = line_with_spaces.strip()

            for strng in re.findall('[\-]+', line):
                if len(strng) > 10:
                    line_break = True
                    break
            if line_break:
                break
            if len(line) == 0 or line == '/':
                continue

            if read_in_npbp_latlon:
                latlon_line = line.split(',')
                lon_string = latlon_line[0].strip()
                lat_string = latlon_line[1].strip()

                err_msg = 'Check your namelist. A pbp value does not have a valid lon-lat pair'
                if (re.match(r'^-?\d+(?:\.\d+)$', lon_string) is not None and re.match(r'^-?\d+(?:\.\d+)$',
                                                                                       lat_string) is not None):
                    if not (abs(float(lon_string)) <= 180. and abs(float(lat_string)) <= 90.):
                        raise ValueError(err_msg)
                else:
                    raise ValueError(err_msg)

                lon_lat_location = [float(latlon_line[0].strip()), float(latlon_line[1].strip())]
                if pbp_latlon is None:
                    pbp_latlon = [lon_lat_location]
                else:
                    pbp_latlon.append(lon_lat_location)
                if len(pbp_latlon) == namelist_option_storage['nsib']:
                    read_in_npbp_latlon = False

                continue

            # See if something was declared
            if re.search('[\=]', line) is not None:
                # Zeroth index = namelist variable name
                # 1st index = value of the namelist variable
                split_line = line.split('=')

                variable_values = split_line[1].split(',')
                string_to_check = variable_values[0].strip()
                if string_to_check in ['.false.', 'False']:
                    namelist_option_storage[split_line[0].strip()] = False
                elif string_to_check in ['.true.', 'True']:
                    namelist_option_storage[split_line[0].strip()] = True
                elif re.search("[/]+?", string_to_check) is not None:
                    namelist_option_storage[split_line[0].strip()] = string_to_check
                elif re.search("[+-]?((\d+\.\d*)|(\.\d+)|(\d+))([eE][+-]?\d+)?", string_to_check) is not None:
                    namelist_option_storage[split_line[0].strip()] = float(string_to_check)
                else:
                    namelist_option_storage[split_line[0].strip()] = string_to_check

                # This implies we have reached the npbp lat/lon section
                if split_line[0].strip() == 'npbp':
                    read_in_npbp_latlon = True
                    if namelist_option_storage[split_line[0].strip()] <= 0:
                        pbp_latlon = [[0., 0.]]
                        if namelist_option_storage['nsib'] > 1:
                            for nouse in range(int(namelist_option_storage['nsib']) - 1):
                                pbp_latlon.append([0., 0.])
                        read_in_npbp_latlon = False

    # Still need to pull pbp and points
    print('   Starting Time (DOY/Year): ', namelist_option_storage['starttime'], namelist_option_storage['startyear'])
    print('   Ending Time (DOY/Year): ', namelist_option_storage['endtime'], namelist_option_storage['endyear'])
    print('   SiB time step (s) = ', namelist_option_storage['dtsib'])

    if namelist_option_storage['spinup'] and (not namelist_option_storage['spinup_writediag']):
        for other_option in ['restart_savef', 'hr_savegf', 'hr_saveluf', 'qp_savegf', 'qp_saveluf', 'pbp_savegf',
                             'pbp_saveluf']:
            namelist_option_storage[other_option] = False
    else:
        namelist_option_storage['restart_savef'] = namelist_option_storage['restart_dtsib'] != 0
        namelist_option_storage['hr_savegf'] = namelist_option_storage['hr_dtsib'] != 0
        namelist_option_storage['hr_saveluf'] = namelist_option_storage['hr_savegf']
        namelist_option_storage['qp_savegf'] = namelist_option_storage['qp_dtsib'] != 0
        namelist_option_storage['qp_saveluf'] = namelist_option_storage['qp_savegf']
        namelist_option_storage['pbp_savegf'] = namelist_option_storage['pbp_dtsib'] != 0
        namelist_option_storage['pbp_saveluf'] = namelist_option_storage['pbp_savegf']

    namelist_option_storage['single_pt'] = False
    if namelist_option_storage['restart_savef'] == 1.:
        namelist_option_storage['single_pt'] = True
        namelist_option_storage['printrank'] = False

    return namelist_option_storage

if __name__ == '__main__':
    read_namel('/Users/nmg5038/sib4v2_corral/info/sites/sib4_sample/namel_sibdrv')

