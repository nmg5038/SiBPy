
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

        #...Solar Zenith Angle Information
        self.sin_dec = None # (-) sin solar declination
        self.cos_dec = None # (-) cosine solar declination
        self.tan_dec = None # (-) tangent solar declination
        self.lonearth = None # (rad) Earth lon about Sun from vernal equinox

        #...Spinup/Equilibrium Pool Information
        self.spinup = False # spinup simulation if set to .true.
        self.spinup_default = False # uses default initial conditions if set to .true.
                                    # => all pools zero except minimal froot pool
                                    # => soil moisture starts at saturation
        self.spinup_output = False  # output specified files if set to .true.
        self.spinup_numyrs = None  # number of years to include in equilibrium pool calculation
        self.spinup_maxiter = None # maximum number of spinup iterations
        self.spinup_threshold = None # threshold to determine pool equilibrium (%)
        self.spinup_done = False  # flag for determining if further spin-up is required
        self.spinup_lnum = None # count of spinup iterations
        self.spinup_ynum = None # count of years in spinup

        # ---------------------------------------
        # ...Balance Information
        self.badtc_print = False  # print canopy temperatures?
        self.badtc_stop = False  # stop for bad canopy temperatures?
        self.bnum_allow = None  # number of allowable balance offenses
        self.canb_print = False  # print canopy balance values?
        self.canb_stop = False  # stop if canopy balance fails?
        self.canb_thresh = None  # canopy balance threshold
        self.snocmbn_print = False  # print snow combine information?
        self.snocmbn_stop = False  # stop if snow combine water balance fails?
        self.snocmbn_thresh = None  # snow combine balance threshold
        self.energyb_print = False  # print energy balance values?
        self.energyb_stop = False  # stop if energy balance fails?
        self.energyb_thresh = None  # energy balance threshold
        self.waterb_print = False  # print water balance values?
        self.waterb_stop = False  # stop if water balance fails?
        self.waterb_thresh = None  # water balance threshold

        # ---------------------------------------
        # ...Equilibrium Pool Options
        self.eqjump_limit = False  # limit jump of equilibrium values?
        self.eqjump_thresh = None  # jump fraction of eq pool values
        self.eq_printf = False  # print equilibrium pools to a file?
        self.eq_pfmol = False  # print file eq pools in moles C? (vs Mg C)
        self.eq_prints = None  # number of eq pools to print to screen
        self.eq_psmol = False  # print screen eq pools in moles C? (vs Mg C)

        # ---------------------------------------
        # ...Printing Information
        self.print_avec = False  # print avec/bvec values?
        self.print_driver = False  # print driver data?
        self.print_harvest = False  # print harvest information?
        self.print_pftinfo = False  # print PFT information?
        self.print_pooll = False  # print live pool values?
        self.print_soil = False  # print soil properties?
        self.print_sscol = False  # print soil/snow layer info?
        self.print_veg = False  # print vegetation values?
        self.print_stop = False  # stop when printed?

if __name__ == '__main__':
    test_module = Constants()
