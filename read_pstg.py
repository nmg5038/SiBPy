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

from module_sibconsts import Constants
from module_io import pstg_file, pstgid
from module_param import phencon
from module_pftinfo import clen, pft_dbg, pft_ref, pft_name, npft_stg, pftnum_stgindx
from module_time import Sib_time

#...file variables
finpft = None
finpftstg = None
finpoolpft = None

npstg = None
pftname = None

trash = None
iscomment1 = False
iscomment2 = False

#...allocation check variables
asum = 0.0
aok = False

#...misc variables
i = None
iref = None
ref = None
s = None

#...Open file
print('Reading Stage-Based Phenology File: ')
print('  ',pstg_file.strip())

if __name__ == '__main__':
    pass
