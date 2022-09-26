import numpy as np

class Constants():
    def __init__(self):
        #User specific variables for SiB
        self.version = 4.0
        self.sib_source = 'SiB4'
        self.sib_source = 'lat/lon'

        # Land Unit Information
        self.nlu = 10       # of land units
        self.nsoil = 10    # of soil layers
        self.nsoiltop = 3  # of top soil layers
        self.nsnow = 5     #max snow layers
        self.ntot = self.nsoil + self.nsnow  # total soil column layers

        # Phenology/Pool Info
        self.dtpool = 86400 # seconds to update

        # Site Information
        self.slen = 6

        # PFT Info
        self.npft = None # number of PFTs
        self.ntype = None # number of PFT types
        self.ngroup = None # number of PFT groups
        self.npmeth = None # number of phenology methods
        self.npstgmax = None # maximum number of phenology stages

        # Pool Information
        self.npoolpft = None  # number of live carbon pools with PFT traits
        self.npoollu = None  # number of dead/soil carbon pools with LU traits
        self.ntpool = None  # total number of pools (npoolpft+npoollu)

        self.npoolcan = None  # number of live carbon pools in canopy
        self.npoolsfc = None  # number of dead carbon pools at surface
        self.npoolsoil = None  # number of dead carbon pools in soil

        # Control Switches (all boolean)
        self.cornsoy_switch = False     # flag: alternate between corn and soybeans
        self.grazing_switch = False     # flag: grazing
        self.green_switch = False       # flag: use greenness fraction
        self.equibclear_switch = False  # flag: set equilibrium calculation sums
                                        #      to zero at simulation start
        self.leapyear_switch = False    # flag: use leap years or constant 365 days per year
        self.updatelst_switch = False   # flag: use local standard time for phenology updates

        # Lat/Lon Information
        self.single_pt = False
        self.nsib = None     # number of SiB points in datasets
        self.sibcount = None # actual number of SiB points in simulation
        self.latsib = None # SiB point latitude (array of size nsib)
        self.lonsib = None # SiB point longitude (array of size nsib)
        self.sitenamesib = None # SiB point site name (array of size nsib, pry a list)

        # grid variables from namel file - subdomain limits
        self.minlon = None # minimum longitude
        self.maxlon = None # maximum longitude
        self.minlat = None # minimum latitude
        self.maxlat = None # maximum latitude

        self.subset = None # array of landpoint indices for subgrid based on nsib (size = subcount)
        self.sublatsib = None # latitude of subset
        self.sublonsib = None # longitude of subset

        self.sublarea = None   #land unit fractional areas (subcount, nlvc)
        self.subpref  = None   #PFT references per lvc unit (subcount, nlvc)
        self.subsitename = None # Site Name (subcount)
        """

    !----------------------------------
    !...Solar Zenith Angle Information
    real(r8) sin_dec  ! (-) sin solar declination
    real(r8) cos_dec  ! (-) cosine solar declination
    real(r8) tan_dec  ! (-) tangent solar declination
    real(r8) :: lonearth ! (rad) Earth lon about Sun from vernal equinox

   !---------------------------------------
   !...Spinup/Equilibrium Pool Information
   logical :: spinup     ! spinup simulation if set to .true.
   logical :: spinup_default ! uses default initial conditions if set to .true.
                              !    => all pools zero except minimal froot pool
                              !    => soil moisture starts at saturation
   logical :: spinup_output  ! output specified files if set to .true.
   integer(i4) :: spinup_numyrs  ! number of years to include in equilibrium pool calculation
   integer(i4) :: spinup_maxiter ! maximum number of spinup iterations 
   real(r4)    :: spinup_threshold  ! threshold to determine pool equilibrium (%)


   logical :: spinup_done  ! flag for determining if further spin-up is required
   integer(i4) :: spinup_lnum !  count of spinup iterations
   integer(i4) :: spinup_ynum !  count of years in spinup

   !---------------------------------------
   !...Balance Information
   logical  :: badtc_print    !print canopy temperatures?
   logical  :: badtc_stop     !stop for bad canopy temperatures?
   integer(i4) :: bnum_allow  !number of allowable balance offenses
   logical  :: canb_print     !print canopy balance values?
   logical  :: canb_stop      !stop if canopy balance fails?
   real(r4) :: canb_thresh    !canopy balance threshold
   logical  :: snocmbn_print  !print snow combine information?
   logical  :: snocmbn_stop   !stop if snow combine water balance fails?
   real(r4) :: snocmbn_thresh !snow combine balance threshold
   logical  :: energyb_print  !print energy balance values?
   logical  :: energyb_stop   !stop if energy balance fails?
   real(r4) :: energyb_thresh !energy balance threshold
   logical  :: waterb_print   !print water balance values?
   logical  :: waterb_stop    !stop if water balance fails?
   real(r4) :: waterb_thresh  !water balance threshold 

   !---------------------------------------
   !...Equilibrium Pool Options
   logical  :: eqjump_limit   !limit jump of equilibrium values?
   real(r4) :: eqjump_thresh !jump fraction of eq pool values
   logical  :: eq_printf      !print equilibrium pools to a file?
   logical  :: eq_pfmol       !print file eq pools in moles C? (vs Mg C)
   integer(i4) :: eq_prints  !number of eq pools to print to screen
   logical  :: eq_psmol       !print screen eq pools in moles C? (vs Mg C)

   !---------------------------------------
   !...Printing Information
   logical :: print_avec    !print avec/bvec values?
   logical :: print_driver  !print driver data?
   logical :: print_harvest !print harvest information?
   logical :: print_pftinfo !print PFT information?
   logical :: print_pooll   !print live pool values?
   logical :: print_soil    !print soil properties?
   logical :: print_sscol   !print soil/snow layer info?
   logical :: print_veg     !print vegetation values?
   logical :: print_stop    !stop when printed?
        """

        pass








if __name__ == '__main__':
    test_module = Constants()
