
#----------------------------------------------------------------------
#
#   SiB4 Parameter Module
#
#----------------------------------------------------------------------


#******************************************************************

#------------------------------------------------------------------
# Aerodynamic Parameters
#------------------------------------------------------------------

class AeroParam:
    def __init__(self):

     self.zo = None      #canopy roughness coeff
     self.zp_disp = None   #zero plane displacement
     self.RbC = None       #coefficient for canopy to CAS aerodynamic resistance
     self.RdC = None       #coefficient for ground to CAS aerodynamic resistance

    def load_param(self,zo, zp, rdc, rbc):
        self.zo = zo
        self.zp_disp = zp
        self.RbC = rbc
        self.RdC = rdc

#-------------------------------------------------
# Phenology Parameters
#-------------------------------------------------
class PhenParam:
    def __init__(self):

        #-------------------------------------------------
        # Defined and Dynamic Common Phenology Parameters
        #-------------------------------------------------

        #...growing season start factors
        self.precip_len = None   #length of precip running-mean (days)
        self.precip_bef = None   #time length before maximum precipitation (days)
        self.precip_aft = None   #time length after maximum precipitation (days)
        self.tawftop_len = None   #time length water must be available (days)
        self.tm_len = None         #time length temperature must be acceptable (days)

        self.daylen_mini = None  #minimum day length if day length is increasing (hr)
        self.daylen_offd = None  #day length growing ability for decreasing day length (hr)
             # > 0: Offset from maximum day length
             # < 0: Daylength threshold to restrict day lengths (winter wheat)
        self.tawftop_min = None  #minimum water availability (-)
        self.tm_min = None #minimum temperature (K)
        self.tm_max = None         #maximum temperature (K)

        #...growing season reset factors
        self.assim_resetl = None #running-mean length for assim mean
        self.assim_resetv = None   #assimilation factor threshold
                    #...to reset growing season variables

        #...phenology stage index parameters
        self.npstg = None #number of phenological stages

        #...phenology stage varying parameters
        #(size= npoolpft,npstgmax)
        self.allocp = None     #phenology-based allocation fractions

        self.adj_moist = None #adjust allocations due to moisture (logical)
        self.adj_temp = None    #adjust allocations due to temperature (logical)

        #(size=npstgmax)
        self.lptransfer = None #phenology-based leaf pool (LAI) transfer
        #(size=npstgmax)
        self.vmax0 = None     #phenology-based rubisco velocity of sun leaf (mol/m2/s)

        #---------------------------------
        #Dynamic Phenology Parameters
        #---------------------------------

        #...phenology factor parameters
        #.....day length potential

        self.psdayl_ref = None  #day length reference
        self.psdayl_mul = None  #daily change
        self.psdayl_min = None     #minimum value

        #.....growth potential
        #.....climatological suitability for growth
        #......using y=AB^clim_wa + C*(clim_wa-D)

        self.climp_a = None  #climatological suitability (climp) exponential adjustment
        self.climp_b = None  #climp exponential adjustment base
        self.climp_c = None  #climp multiplicative adjustment coefficient
        self.climp_d = None  #climp multiplicative adjustment offset
        self.climp_min = None #climp minimum
        self.climp_max = None   #climp maximum

        self.cwa_type = None #climatological suitability water availability type
        #   1=CUPR (convective precipitation)
        #   2=Total Precipitation
        #   3=PAWFRW (Plant Available Water Root-Weighted Fraction)
        #   4=TAWFRW (Total Available Water Root-Weighted Fraction)


        self.clai_coef = None   #climatological LAI coefficient (-)
        self.clai_offl = None   #climatological LAI lower offset (-)
        self.clai_offg = None    #climatological LAI upper offset (-)

        self.psg_min = None #growth potential minimum (-)

        #.....weather potential
        self.pswx_rml = None #weather potential running-mean length
        self.pswx_type = None #weather potential water availability type
        #    1=PAW_FTop
        #    2=PAW_FAll
        #    3=2*PAW_Fall
        #    4=PAW_FAll > 0. ==> 1.0
        #    5=TAW_FTop
        #    6=TAW_FAll
        #    7=RSTFAC2
        #    8=RSTFAC4

        #-----------------------------
        #Defined Phenology Parameters
        #-----------------------------

        #...phenology stage determination method
        #.....1=Growing Degree Days (GDD)
        #.....2=Days After Planting Date (DAPD)
        self.gdd_or_pd = None

        #...growing degree day information
        self.gdd_tbase = None # Base temperature (F)
        self.gdd_tmax = None  # Maximum temperature (F)

        #...growing season length (GSL) maximum (days)
        self.gslmax = None    #growing season length (GSL) max (days)

        #...phenology stage thresholds
        #(size = npstgmax-1)
        self.threshp = None  #thresholds for phenology stages

        #...seed information
        self.seed_carbon = None  #carbon in seed (mol C)
        self.seed_release = None #daily carbon released from seed (mol C)

        #-------------------------
        #Calculated Parameters
        #------------------------

        #.....weights for growing season start
        self.wt_assim = None  #time-step contribution for assimilation
        self.wt_precip = None  #time-step contribution for precipitation
        self.wt_tawftop = None  #time-step contribution for tawftop
        self.wt_tm = None        #time-step contribution for temperature

        #.....weights for dynamic phenology
        self.wt_pswx = None #time-step contribution for weather potential

#------------------------------------------------------------------
# Physiological Parameters
#------------------------------------------------------------------

class PhysParam:
    def __init__(self):
        #...vegetation-specific characteristics
        self.sla = None     #specific leaf area (m2 leaf area/g leaf)
        self.laimin = None   #m2/m2
        self.laisat = None   #m2/m2
        self.fparsat = None  #-
        self.pftgraze = None #switch for grazing (logical)

        self.c4flag  = None  # 0=c3,  1=c4
        self.chil = None    # leaf angle distribution factor (-)
        self.z1 = None      # canopy bottom (m)
        self.z2 = None      # canopy top (m)
        self.kroot = None   # root density extinction coefficient (-)
        self.rootd = None   # maximum rooting depth (m)

        #...temperature stress parameters
        self.slti = None    # slope of lo-temp inhibition (1/K)
        self.shti = None    # slope of hi-temp inhibition (1/K)
        self.hlti = None    # 1/2 point of lo-temp inhibition (K)
        self.hhti = None    # 1/2 point of hi-temp inhibition (K)
        self.hfti = None    # 1/2 point of frost inhibition (K)
        self.sfti = None    # slope of frost inhibition (1/K)

        #...soil moisture stress parameters
        #(size = nsoil/2)
        self.fc_min = None  # minimum field capacity (1/m3)
        #(size = nsoil/2)
        self.wp_min = None # minimum wilting point (1/m3)
        self.wssp = None    # water stress shape parameter (0.1-1.0)

        #...photosynthesis parameters
        self.effcon = None  # quantum efficiency (mol CO2/mol quanta)
        self.gmeso = None   # mesophyll conductance (mol/m^2/sec)
        self.binter = None  # conductance-photosynthesis intercept (mol m^-2 sec^-1)
        self.gradm = None   # conductance-photosynthesis slope parameter (-)
        self.atheta = None  # WC WE coupling parameter (-)
        self.btheta = None  # WC WE WS coupling parameter (-)

        #...radiation parameters
        self.tran = None # leaf transmittance (-, size = 2x2)
        #  (1,1) - shortwave, green plants
        #  (1,2) - shortwave, brown plants
        #  (2,1) - longwave, green plants
        #  (2,2) - longwave, brown plants
        self.ref = None  # leaf reflectance (-, size = 2x2)
        #  (1,1) - shortwave, green plants
        #  (1,2) - shortwave, brown plants
        #  (2,1) - longwave, green plants
        #  (2,2) - longwave, brown plants

#------------------------------------------------------------------
# Pool Parameters
#------------------------------------------------------------------
class PoolParam:
    def __init__(self):

        #----Live Pool Info----
        #...autotrophic respiration parameters
        #(size = npoolpft)
        self.gr_frac = None  #growth respiration coefficients (0-1)

        #(size = npoolpft)
        self.lresp_eff = None #respiration efficiency (0-1)

        self.cr_aml = None  #canopy assimilation respiration low multiplier (-)
        self.cr_amh = None  #canopy assimilation respiration high multiplier (-)
        self.cr_amin = None  #canopy assimilation respiration min (-)
        self.cr_amax = None      #canopy assimilation respiration max (-)

        self.cr_fmul = None  #canopy freeze respiration inhibition multiplier (-)
        self.cr_fref = None  #canopy freeze respiration inhibition ref temperature (K)
        self.cr_fmin = None      #canopy freeze respiration inhibition minimum (-)

        self.cr_hq10 = None  #Q10 base for canopy respiration hot scalar (-)
        self.cr_href = None  #reference temperature for canopy respiration hot scalar (K)
        self.cr_hmax = None      #max value for canopy respiration high temp scalar (-)

        #...leaf transfer parameters
        self.lt_fq10 = None  #leaf freeze transfer Q10 base (-)
        self.lt_fref = None  #leaf freeze transfer reference temperature (K)
        self.lt_fmax = None       #leaf freeze transfer maximum (fraction per day)

        self.lt_dcoef = None  #leaf daylength transfer coefficient (-)
        self.lt_dref = None   #leaf daylength transfer ref (diff from max daylenth)
        self.lt_dmax = None        #leaf daylength transfer maximum (fraction per day)

        self.lt_wref = None   #leaf water deficiency transfer pawfrw reference (-)
        self.lt_wbase = None  #leaf water deficiency transfer exponential base (-)
        self.lt_wcoef = None  #leaf water deficiency transfer coefficient (-)
        self.lt_wmax = None        #leaf water deficiency transfer maximum (fraction per day)

        #...root respiration and transfer parameters
        self.rrt_aml = None  #root resp/transfer assimilation respiration low multiplier (-)
        self.rrt_amh = None  #root resp/transfer assimilation respiration high multiplier (-)
        self.rrt_amin = None  #root resp/transfer assimilation respiration min (-)
        self.rrt_amax = None      #root resp/transfer assimilation respiration max (-)

        self.rrt_fmul = None  #root resp/transfer freeze inhibition multiplier (-)
        self.rrt_fref = None  #root resp/transfer freeze inhibition ref temperature (K)
        self.rrt_fmin = None      #root resp/transfer freeze inhibition minimum (-)

        self.rrt_hq10 = None  #root resp/transfer hot Q10 (-)
        self.rrt_href = None  #root resp/transfer hot reference temperature (K)
        self.rrt_hmax = None      #root resp/transfer max high temperature scalar (-)

        self.rrt_laimin = None  #root resp/transfer LAI ratio (LAI/Clim_LAI) min (-)
        self.rrt_laimax = None      #root resp/transfer LAI ratio max (-)

        #----Dead Pool Info----
        #...surface pool heterotrophic respiration and transfer parameters
        self.hrt_sfc_aml = None  #assimilation respiration low multiplier (-)
        self.hrt_sfc_amh = None  #assimilation respiration high multiplier (-)
        self.hrt_sfc_amin = None  #assimilation respiration min (-)
        self.hrt_sfc_amax = None      #assimilation respiration max (-)

        self.hrt_sfc_fmul = None   #freeze inhibition multiplier (-)
        self.hrt_sfc_fref = None   #freeze inhibition ref temperature (K)
        self.hrt_sfc_fmin = None       #freeze inhibition minimum (-)

        self.hrt_sfc_hq10 = None   #high temperature Q10 (-)
        self.hrt_sfc_href = None   #high temperature reference temperature (K)
        self.hrt_sfc_hmax = None       #high temperature maximum scalar (-)

        self.hrt_sfc_pml = None  #precip inhibition low multiplier (-)
        self.hrt_sfc_pmin = None     #precip inhibition minimum (-)

        #...soil pool heterotrophic respiration/transfer parameters
        self.hrt_soil_aml = None  #assimilation respiration low multiplier (-)
        self.hrt_soil_amh = None  #assimilation respiration high multiplier (-)
        self.hrt_soil_amin = None  #assimilation respiration min (-)
        self.hrt_soil_amax = None      #assimilation respiration max (-)

        self.hrt_soil_fmul = None   #freeze inhibition multiplier (-)
        self.hrt_soil_fref = None   #freeze inhibition ref temperature (K)
        self.hrt_soil_fmin = None       #freeze inhibition minimum (-)

        self.hrt_soil_hq10 = None   #high temperature Q10 (-)
        self.hrt_soil_href = None   #high temperature reference temperature (K)
        self.hrt_soil_hmax = None       #high temperature maximum scalar (-)

        self.hrt_soil_mmin = None       #moisture inhibition minimum (-)
        self.hrt_soil_pawmin = None     #PAW inhibition minimum (-)


        #...dead pool respiration efficiency (0-1)
        #(size = npoollu,npoollu)
        self.dresp_eff = None

        #...grazing and harvest transfer parameters (size=npoollu+2)

        self.graze_trans = None  # transfer fractions for grazing (0-1)
        self.harvest_trans = None    # transfer fractions for harvest (0-1)

        #----Live and Dead Pool Info----
        #...pool turnover times (yr)
        #(size = ntpool)
        self.turnover = None

        #...pool transfer fractions (0-1)
        #(size = ntpool,ntpool)
        self.pool_trans_frac = None   # transfer fractions between pools (-)


        #...calculated parameters...
        #(size=ntpool)
        self.k_rate = None #pool decay rate (1/s)

        #(size = npoolpft)
        self.poolpft_min = None #minimum pool values (mol C/m2)

def pp():
    print(AeroParams['LAIgrid'])
    print(AeroParams['AeroParam'].zo)
#***********************************************************************
#-----------------------------------------------------------------------

"""
# Aerodynamic Parameters
ngrid = None  #number of points in interpolation table
aerovar = None #(size = npft,ngrid,ngrid, type = AeroParam)
LAIgrid = None      #(size=ngrid)
fVCovergrid = None  #(size=ngrid)
"""
AeroParams={'ngrid':None,'aerovar':None,'LAIgrid':None,'fVCovergrid':None,'AeroParam':AeroParam()}

# Phenological Parameters (size = npft, type = PhenParam)
phencon = None

# Physiological Parameters (size = npft, type = PhysParam)
physcon = None

# Pool Parameters (size = npft, type = PoolParam)
poolcon = None


#-----------------------------------------------------------------------
