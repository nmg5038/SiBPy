
#----------------------------------------------------------------------
#   SiB4 Local Variables
#----------------------------------------------------------------------
from module_sibconsts import Constants
sibconsts = Constants()
nsoil = sibconsts.nsoil
nsnow = sibconsts.nsnow

#...previous time-step values
capaccl_old = None      # previous canopy liquid water storage (kg/m2)
capaccs_old = None      # previous canopy snow water storeage (kg/m2)
capacg_old = None      # previous ground liquid water storage (kg/m2)
snow_cmass_old = None  # previous canopy snow cover (kg/m2)
snow_gmass_old = None  # previous ground snow cover (kg/m2)

nsl_old = None   # prev timestep number of snow layers (-, integer)

wwwliq_old = None  # prev timestep soil liquid (kg/m2, size = -nsnow+1:nsoil)
wwwice_old = None  # prev timestep soil ice (kg/m2, size = -nsnow+1:nsoil)
frac_iceold = None # prev timestep ice fraction of total soil liquid (size = -nsnow+1:nsoil)
td_old = None       # prev timestep soil temperature (K, size = -nsnow+1:nsoil)

#...saturation vapor pressures
etc   = None # saturation vapor pressure at Tc (hPa)
          #   ('e-star' of Tc)
getc  = None # derivative of etc with respect to temp
          #   (d(etc)/dTc (hPa K^-1)
etg   = None # 'e-star' of ground surface (hPa)
getg  = None # d(etg)/dTg (hPa K^-1)
ets   = None # 'e-star' of snow surface (hPa)
gets  = None # d(ets)/dTs (hPa K^-1)

#...canopy air space (CAS) and canopy
dtg   = None # change in ground surface temperature (K)
dts   = None # change in snow surface temperature (K)
dtc   = None # change in canopy temperature (K)
dth   = None # change in ref level temperature (K)
dqm   = None # change in ref level moisture (hPa)
dta   = None # change in CAS temperature (K)
dea   = None # change in CAS moisture (hPa)

gect  = None # dry fraction of veg / rc
geci  = None # wet fraction of veg / 2rb
gegs  = None # dry fraction of ground / rds
gegi  = None # wet fraction of ground /rd
coc   = None # gect + geci
cog1  = None # gegi + gegs*hrr
cog2  = None # gegi + gegs

# temp vars for humidity (size = 1)
ppl = None
ttl = None
# temp vars for easat (size = 1)
esst = None
dtesst = None

#...radiation
dtc4   = None # d(canopy thermal em)/dT (W/m2/K)
dtg4   = None # d(ground thermal em)/dT (W/m2/K)
dts4   = None # d(snow thermal em)/dT   (W/m2/K)
lcdtc  = None # d(canopy thermal em)/dtc (W/m2/K)
lcdtg  = None # d(canopy thermal em)/dtg (W/m2/K)
lcdts  = None # d(canopy thermal em)/dts (W/m2/K)
lgdtc  = None # d(ground thermal em)/dtc (W/m2/K)
lgdtg  = None # d(ground thermal em)/dtg (W/m2/K)
lsdts  = None # d(snow thermal em)/dts   (W/m2/K)
lsdtc  = None # d(snow thermal em)/dtc   (W/m2/K)
hcdtc  = None # d(canopy H)/dtc  (W/m2/K)
hcdta  = None # d(canopy H)/dta  (W/m2/K)
hgdta  = None # d(ground H)/dta  (W/m2/K)
hgdtg  = None # d(ground H)/dtg  (W/m2/K)
hsdta  = None # d(snow H)/dta  (W/m2/K)
hsdts  = None # d(snow H)/dtsnow  (W/m2/K)
hadta  = None # d(CAS H)/dta  (W/m2/K)
hadth  = None # d(CAS H)/dtheta  (W/m2/K)
ecdtc  = None # d(canopy LE)/dtc (W/m2/K)
ecdea  = None # d(canopy LE)/dea (W/m2/K)
egdtg  = None # d(ground LE)/dtg (W/m2/K)
egdea  = None # d(ground LE)/dea (W/m2/K)
esdts  = None # d(snow LE)/dtsnow (W/m2/K)
esdea  = None # d(snow LE)/dea (W/m2/hPa)
eadea  = None # d(CAS LE)/dea (W/m2/hPa)
eadem  = None # d(CAS LE)/dem (W/m2/hPa)
closs  = None   # canopy thermal loss     (W/m2)
gloss = None    # ground thermal loss     (W/m2)
sloss = None    # snow thermal loss       (W/m2)
fac1  = None    # effective ground cover for thermal radiation (-)

#...soil/snow variables to save
dtd = None # delta soil temperature (K, size = -nsnow+1:nsoil)
imelt = None  # flag for 1=melting 2=freezing in soil column (size = -nsnow+1:nsoil)

#...variables to save for energy balance
cas_e_storage = None  #CAS energy storage
cas_w_storage = None  #CAS water storage

radttc = None # copy of PFT net radiation (W/m2)
radttg = None # copy of ground net radiation (W/m2)
radtts = None # copy of snow net radiation (W/m2)
