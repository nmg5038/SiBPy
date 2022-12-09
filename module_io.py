
#use module_sibconst only: slen

iofnlen = 256
missing = -9999.

nchunks = None      # number of processors (integer)
rank = None         # process number (integer)

# file path names read in from namel file
pft_info = None # path to pft information (string, len = iofnlen)
pool_info = None # path to pool information (string, len = iofnlen)
aero_file = None # path to morphological/aerovar parameters (string, len = iofnlen)
pgdd_file = None # path to phenology gdd parameters (string, len = iofnlen)
pstg_file = None # path to phenology stage parameters (string, len = iofnlen)
phys_file = None # path to plant physiological parameters (string, len = iofnlen)
pool_file = None # path to pool parameters (string, len = iofnlen)
vs_file = None # path to PFT/soil file (string, len = iofnlen)
ic_file = None # path to initial conditions file (string, len = iofnlen)
driver_path = None # path to driver data (string, len = iofnlen)
tm5_path = None # path to tm5 data (string, len = iofnlen)
fire_path = None # path to fire data (string, len = iofnlen)
out_path = None # path for output files (string, len = iofnlen)
out_info = None # path to diagnostic preferences (sib_outopts) (string, len = iofnlen)
out_rinfo  = None  # path to restart preferences (sib_routopts) (string, len = iofnlen)

# constant file id numbers
pftid  = 23 #file id for pft information
piid   = 24 #file id for pool information
pgddid = 25 #file id for stage-phenology parameters
pstgid = 26 #file id for gdd-phenology parameters
physid = 28 #file id for physiological parameters
poolid = 32 #file id for pool parameters

#####DRIVER DATA#########
# parameters
nodata = -9999.

ztemp = 100.     # temperature measurement height (m)
zwind = 100.     # wind measurement height (m)

# driver file variable names
nsibname = 'nsib' # number of landpoints
psname = 'ps' # pressure
tmname = 'tm' # temperature
shname = 'sh' # sensible heat
spdmname = 'spdm' # wind speed
lsprname = 'lspr_scaled' # large-scale precip
cuprname = 'cupr_scaled' # convective precip
swdname = 'swd' # downwelling shortwave radiation
lwdname = 'lwd' # downwelling longwave radiation
lsprnameopt = 'lspr' # optional/secondary large-scale precip
cuprnameopt = 'cupr' # optional/secondary convective precip

# file access information
driverid = None # netcdf id for driver data (integer)
driver_filename = None #(string)

# flags
driver_readf = None   # read driver data ? (logical)
driver_switchf = None # switch driver data file ? (logical)
driver_updatef = None # update driver data ? (logical)

# time information
driver_step    = None # # seconds in driver data timestep
driver_perday  = None # # driver data timesteps per day
driver_permon  = None # # driver data timesteps per month

driver_recnum  = None # driver data current record number
driver_year    = None # year of driver data to read
driver_month   = None # month of driver data to read
driver_day     = None # day of month of driver data to read
driver_hour    = None # hour of driver data to read
driver_seccur  = None # current total second of driver data
driver_secnext = None # next total second of driver data

##### COS data #########
# tm5 file variable names
nsibname_tm5 = 'nsib' # number of landpoints
psname_tm5 = 'pressure' # pressure
cosmname_tm5 = 'mixing_ratio'    # COS mixing ratio

# flags
tm5_readf = None   # read driver data ? (logical)
tm5_switchf = None # switch driver data file ? (logical)
tm5_updatef = None # update driver data ? (logical)

# time information
tm5_step    = None # # seconds in tm5 data timestep
tm5_perday  = None # # tm5 data timesteps per day
tm5_permon  = None # # tm5 data timesteps per month

tm5_recnum  = None # tm5 data current record number
tm5_year    = None # year of tm5 data to read
tm5_month   = None # month of tm5 data to read
tm5_day     = None # day of month of tm5 data to read
tm5_hour    = None # hour of tm5 data to read
tm5_seccur  = None # current total second of tm5 data
tm5_secnext = None # next total second of tm5 data
tm5id = None # netcdf id for tm5 data
tm5_filename = None #(string, len = iofnlen)

#####FIRE DATA#########
# switch to stop if fire fires are not present
firefile_stop = False

# fire file variable names
fnsibname = 'nsib' # number of landpoints
ftimename = 'time' # time dimension
firecname = 'emis_C' # fire C emissions
fireco2name = 'emis_CO2'    # fire CO2 emissions

# fire file access information
fireid = None
fire_filename = None #(string, len = iofnlen)

# flags
fire_readf = None  # read fire data ? (logical)
fire_switchf = None # switch fire data file ? (logical)
fire_updatef = None # update fire data? (logical)

# time information
fire_step    = None # # seconds in fire data timestep
fire_perday  = None # # fire data timesteps per day
fire_permon  = None # # fire data timesteps per month

fire_recnum  = None # fire data current record number
fire_year    = None # year of fire data to read
fire_month   = None # month of fire data to read
fire_day     = None # day of fire data to read
fire_hour    = None # hour of fire data to read
fire_seccur = None # current total second of firedata
fire_secnext = None # next total second of fire data

#####RESTART DATA#####
# flags
restart_savef = None   # write restart files at all ? (logical)

# time information
restart_dtsib = None #restart output interval
                      # > 0 units of seconds, < 0 units of months
restart_ntpersave  = None # total # of timesteps per restart output
restart_countt  = None   # simulated # of timesteps between restart output

# file information (string)
restart_filename = None #(string, len=iofnlen)

# variable information
#....number of variables
sibr_nvar = None

#...variable names

sibr_vname = None #(string array, size=unknown)

#...variable references
sibr_vref = None #(integer array, size=unknown)

#...variable default values
sibr_vd = None #(float array, size=unknown)

#...output flags (for restart and requib)
sibr_doref = None #(logical array, size=unknown)

#####REQUIB DATA#####
requib_writef = None  # calculate and write equilibrium pools ? (logical)

# file information
requib_filename = None #(string, len=iofnlen)

#...output flags
sibreq_doref = None #(logical array, size=unknown)



#######################OUTPUT DATA#################################
##  HR=Global Time-Series Output (typically hourly)              ##
##  PBP=Selected Point Time-Series Output                        ##
##       - Typically hourly for global runs with selected sites  ##
##       - Typically daily for site/single point runs            ##
##  QP=Global Time-Series Output (typically monthly)             ##
###################################################################

# parameters
dtoutwrite = 86400

# filename information
printrank = True
hr_prefix = 'hsib_'
pbp_prefix = 'psib_'
qp_prefix = 'qsib_'


hr_suffixg  = '.g.hr2.nc'
hr_suffixlu = '.lu.hr3.nc'
pbp_suffixg  = '.g.pbp1.nc'
pbp_suffixlu = '.lu.pbp2.nc'
qp_suffixg  = '.g.qp2.nc'
qp_suffixlu = '.lu.qp3.nc'

# file names
hr_filenameg = None  # filename for hr gridcell files (len=iofnlen)
hr_filenamelu = None  # filename for hr land unit files (len=iofnlen)
pbp_filenameg = None  # filename for pbp gridcell files (len=iofnlen)
pbp_filenamelu = None  # filename for pbp land unit files (len=iofnlen)
qp_filenameg = None  # filename for qp gridcell files (len=iofnlen)
qp_filenamelu = None  # filename for qp land unit files (len=iofnlen)

# flags (all logical)
hr_savegf = None   # flag to save hr g info
hr_saveluf = None   # flag to save hr lu info
pbp_savegf = None   # flag to save pbp g info
pbp_saveluf = None   # flag to save pbp lu info
qp_savegf = None   # flag to save qp g info
qp_saveluf = None     # flag to save qp lu info


hr_openf = None  # open hourly files?
hr_writef = None  # write to hourly files?
pbp_openf = None  # open pbp files?
pbp_writef = None  # write to pbp files?
qp_openf = None  # open qp files?
qp_writef = None  # write to qp files?

# time information

# > 0 units of seconds; < 0 units of months
# output intervals (from namel file, integer)
hr_dtsib = None  # hr output interval
pbp_dtsib = None # pbp output interval
qp_dtsib = None  # qp output interval

# number of timesteps per file (integers)
hr_nsaveperfile = None
qp_nsaveperfile = None
pbp_nsaveperfile = None

# number of saved steps per output (integer)
hr_nsaveperout = None
qp_nsaveperout = None
pbp_nsaveperout = None

# number of timesteps per save (integer)
hr_ntpersave = None
qp_ntpersave = None
pbp_ntpersave = None
# weight of timestep output to saved output (float)
hr_wtpersave  = None
qp_wtpersave = None
pbp_wtpersave = None

# (units of days)
hr_start = None  # day of hr starting period
pbp_start = None  # day of pbp starting period
qp_start = None   # day of qp starting period

# (units of day fractions)
hr_step = None    # day fraction of hourly timestep
pbp_step = None    # day fraction of pbp timestep
qp_step = None         # day fraction of qp timestep

# variable information (integer)
hr_nvarg = None  # number of saved hrsib fields on Grid Cell
hr_nvarlu = None  # number of saved hrsib fields on Land Units
pbp_nvarg = None  # number of saved pbp fields on Grid Cell
pbp_nvarlu = None  # number of saved pbp fields on Land Units
qp_nvarg = None  # number of saved qpsib fields on Grid Cell
qp_nvarlu  = None      # number of saved qpsib fields on Land Units

#(hr/pbp/qp nvar, integer)
hr_vrefg = None  # reference # for saved grid cell hr variables
hr_vreflu = None  # reference # for hrsib fields on Land Units to be saved
pbp_vrefg = None  # reference # for pbpsib fields on Grid Cell to be saved
pbp_vreflu = None  # reference # for pbpsib fields on Land Units to be saved
qp_vrefg = None  # reference # for qpsib fields on Grid Cell to be saved
qp_vreflu   = None   # reference # for qpsib fields on Land Units to be saved

#(hr/pbp/qp nvar, len = 100 char, size = ?)
hr_listoutg = None  # descriptions of hr variables on Grid Cell
hr_listoutlu = None  # descriptions of hr variables on Land Unitse
pbp_listoutg = None  # descriptions of pbp variables on Grid Cell
pbp_listoutlu = None  # descriptions of pbp variables on Land Units
qp_listoutg = None  # descriptions of qp variables on Grid Cell
qp_listoutlu  = None     # descriptions of qp variables on Land Units

#(hr/pbp/qp nvar, len= 21 char, size = ?)
hr_nameoutg = None  # field names of hr variables on Grid Cell
hr_nameoutlu = None  # field names of hr variables on Land Units
pbp_nameoutg = None  # field names of pbp variables on Grid Cell
pbp_nameoutlu = None  # field names of pbp variables on Land Units
qp_nameoutg = None  # field names of qp variables on Grid Cell
qp_nameoutlu  = None      # field names of qp variables on Land Units

# output information
# file ids (integer)
hr_idg  = None
hr_idlu = None
pbp_idg = None
pbp_idlu = None
qp_idg = None
qp_idlu = None

# time ids (integer)
hr_idtimeg = None
hr_idtimelu = None
pbp_idtimeg = None
pbp_idtimelu = None
qp_idtimeg = None
qp_idtimelu = None

#(nvars, size = nvars?, integers)
hr_idvarlu = None
hr_idvarg = None  #variable ids for hr variables
pbp_idvarlu = None
pbp_idvarg = None  #variable ids for pbp variables
qp_idvarlu = None
qp_idvarg = None   #variable ids for qp variables

# counter information (integer)
hr_countt = None  # count of timestep being saved per output interval
hr_countsave = None  # count of saved value per output interval
hr_countwrite = None  # count of timestep being written out
pbp_countt = None
pbp_countsave = None
pbp_countwrite = None
qp_countt = None
qp_countsave = None
qp_countwrite = None

#(size = subcount,nvar,ntperout)
hr_g = None  # time series diagnostics all points (typically hourly)
qp_g = None  # time series diagnostics all points (typically monthly)
pbp_g = None  #time series diagnostics at selected points

#(size=subcount,nlu,nvar,ntperout)
hr_lu = None  # time-series diagnostics all points (typically hourly)
qp_lu = None # time-series diagnostics all points (typically monthly)
pbp_lu  = None     # time-series diagnostics at selected points


#####PBP-Specific Information
npbp = None  # number of gridpoints where pbp fields are saved (integer)

#(size=subcount, integer)
pbp_outref = None

#(size=npbp, integer)
pbp_sibpt = None   # original sibpt references
pbp_gref = None    # references for PBP output

#(size=npbp,npbp)
pbp_lonlat = None   #lon and lat of pbp points from namelist

#(size =npbp)
pbp_lon = None  #  Longitudes for PBP output
pbp_lat = None     #  Latitudes for PBP output

#(integer, size = npbp,nlu)
pbp_pref = None # land unit PFT refs for PBP output
#(size=npbp,nlu)
pbp_larea = None  # land unit areas for PBP output

#(string, len = slen, size=npbp)
pbp_sitename  = None

#####Satellite Information - Fluorescence
#Output times for GOME-2 and OCO-2
sif_gome2_tstart = 0.375
sif_gome2_tstop = 0.4585
sif_oco2_tstart = 0.5104
sif_oco2_tstop = 0.5521

# Count of output times for satellite SIF comparisons
# 1=GOME-2  2=OCO-2
#(integer, size=subcount,ntperout,2)
hr_sif_satcount = None
pbp_sif_satcount = None
qp_sif_satcount = None
