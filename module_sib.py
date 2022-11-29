"""
!----------------------------------------------------------------------
!
!   SiB4 Variable Module
!
!   Using derived type hierarchy.
!   gridcell -> landpft
!
!   ---
!   every point to simulate consists of a
!      single gridcell type
!   ---
!   landpft types currently have corresponding
!      land, canopy air space (CAS),
!      canopy, and pft variables
!   ---
!
!   pft types can have values
!   1=> not vegetated (bare ground)
!   2=> needleleaf evergreen
!   4=> needleleaf deciduous
!   5=> broadleaf evergreen
!   8=> broadleaf deciduous
!  11=> shrub (non-tundra)
!  12=> tundra shrub
!  13=> tundra c3 grass
!  14=> c3 grass (non-tundra)
!  15=> c4 grass
!  17=> generic crop
!  20=> maize
!  22=> soybean
!  24=> winter wheat
!----------------------------------------------------------------------

"""


# =================================================
# Time Invariant Variables
# ---------------------------------------------------------------------
# Soil Properties (Soil)
# ---------------------------------------------------------------------

class SoilType:
    def __init__(self):
        # ...soil properties
        self.sandfrac = None  # soil sand fraction
        self.clayfrac = None  # soil clay fraction
        self.soref_vis = None  # soil shortwave reflectance (-)
        self.soref_nir = None  # soil longwave reflectance (-)

        self.poros = None  # soil porosity (zero to one)
        self.satco = None  # hydraulic conductivity at saturation (m/s)

        self.csolid = None  # heat capacity, soil solids (J/m3/K)
        self.tkdry = None  # thermal conductivity, dry soil (W/m/K)
        self.tkmg = None  # thermal conductivity, soil minerals (W/m/K)
        self.tksat = None  # thermal conductivity, saturated soil (W/m/K)

        # ...soil variables for plant water stress
        self.bee = None  # Clapp & Hornberger 'b' exponent (-)
        self.phsat = None  # Soil tension at saturation (m)
        self.fieldcap = None  # Field Capacity (1/m3)
        self.vwcmin = None  # Wilting Point (1/m3)

        # ...soil variables for respiration
        self.wopt = None  # respiration function optimum soil moisture (-)
        self.woptzm = None  # wopt to the zm exponent
        self.wsat = None  # respiration function value (-)
        self.zm = None  # respiration function exponent (-)

        # ...soil variables for water availability
        self.fc_eff = None  # Effective Field Capacity (1/m3, size = nsoil)
        self.wp_eff = None  # Effective Wilting Point (1/m3, size = nsoil)


# ===================================================================
# =================================================
# Time-Step Varying Variables
# -------------------------------------------------
# Canopy (Can) and Canopy Air Space (CAS) Variables
# -------------------------------------------------

class CasType:
    def __init__(self):
        # ...Canopy prognostic variables
        self.tc = None  # canopy temperature (K)

        # ...CAS prognostic variables
        self.eacas = None  # CAS water vapor pressure (hPa or mb)
        self.shcas = None  # CAS water vapor mixing ratio (kg/kg)
        self.tcas = None  # CAS temperature (K)
        self.tkecas = None  # CAS turbulent kinetic energy (J/kg)

        # ...Canopy environmental variables
        self.hcapc = None  # canopy heat capacity (J/m2/K)
        self.tcmin = None  # frost

        # ...CAS environmental variables
        self.thcas = None  # CAS potential temperature (K)
        self.hcapcas = None  # CAS heat capacity (J/m2/K)
        self.vcapcas = None  # CAS vapor capacity (J/m2/hPa)


# -------------------------------------------------
# CO2/Photosynthesis Variables (CAN; CAS; PFT)
# -------------------------------------------------
class Co2Type:
    def __init__(self):
        # ...assimilation
        self.assim = None  # gross assimilation (mol C/m2/s)
        self.assimd = None  # daily (24hr running-mean) assimilation (mol C/m2/s)
        self.clim_assim = None  # climatological assimilation (mol C/m2/s)

        # ...canopy scaling
        self.assimpot = None  # potential top leaf photosynthesis (mol C/m2/s)
        self.apar = None  # absorbed photosynthetically active radiation (mol/m2/s)
        self.aparkk = None  # factor for scaling of leaf radiation (-)
        self.gamma = None  # CO2 photocompensation point (Pa)
        self.par = None  # photosynthetically active radiation (mol/m2/s)
        self.nspar = None  # non-scattered photosynthetically active radiation (mol/m2/s)

        # ...canopy air space (CAS) fluxes
        self.casd = None  # CAS depth for CO2 (m)
        self.cflux = None  # CAS to ref height carbon flux (mol C/m2/s)

        # ...co2 concentrations
        self.pco2cas = None  # CAS CO2 partial pressure (Pa)
        self.pco2c = None  # chloroplast CO2 partial pressure (Pa)
        self.pco2i = None  # leaf internal CO2 partial pressure (Pa)
        self.pco2s = None  # leaf surface CO2 partial pressure (Pa)

        # ...resistances
        self.rst = None  # prognostic stomatal resistance (s/m)

        # ..soil freeze functions
        self.soilfrz = None  # soil freeze function (-)
        self.soilfrztg = None  # soil freeze function for top soil layer (-)
        self.soilfrztd = None  # soil freeze function for second soil layer (-)

        # .....total stress factors
        self.rstfac = [None, None, None, None]  # canopy stress factors (-)
        #  (1) leaf surface RH stress
        #  (2) rootzone water stress
        #  (3) temperature stress
        #  (4) product of factors 1-3
        self.vmaxss = None  # stressed rubisco velocity (mol/m2/s)


# -------------------------------------------------
# Carbonyl Sulfide (COS) Variables (CAN; CAS; PFT)
# -------------------------------------------------
class COSType:
    def __init__(self):
        # ...COS CAS
        self.cos_casd = None  # CAS depth for COS (m)
        self.cos_flux = None  # CAS COS flux (mol/m2/s)

        # ...COS concentrations
        self.coscas = None  # CAS COS (mol COS/mol air)
        self.coss = None  # Leaf Surface COS (mol COS/mol air)
        self.cosi = None  # Leaf Internal COS (mol COS/mol air)
        self.coscasp = None  # CAS COS partial pressure (Pa)

        # ...COS fluxes
        self.cos_assim = None  # COS assimilation (mol/m2/s)
        self.cos_lru = None  # COS leaf relative uptake (-)
        self.cos_lru2 = None  # COS leaf relative uptake, ci/ca calculation (-)
        self.cos_lru3 = None  # COS leaf relative uptake variant 3
        self.cos_lru4 = None  # COS leaf relative uptake variant 4
        self.cos_grnd = None  # COS uptake by the soil (mol/m2/s)
        self.cos_grnd_Ogee = None  # COS uptake by the soil (mol/m2/s)
        self.cos_soil = None  # COS uptake by the soil (mol/m2/s)
        self.gsh2onew = None  # canopy conductance (mol/m2/s)
        self.cosm = None  # reference level COS concentration (mol COS/mol air)

        # ...Conductance diagnostics
        self.cosgm = None  # 'apparent' mesophyll conductance (mol/m2/s)
        self.cosgt = None  # total conductance (mol/m2/s)


# -------------------------------------------------
# Dead Pool Equilibrium Variables (Soil)
# -------------------------------------------------
class EquibdType:
    def __init__(self):
        # ...prognostic land pool variables for equilibrium
        self.poollu_totgain = None  # sum of pool gains (mol/m2, size = npoollu)
        self.poollu_totloss = None  # sum of pool losses (mol/m2, size = npoollu)

        # ...equilibrium variables for individual dead pools
        self.poollu_init = None  # initial pools (mol C/m2, size = npoollu)
        self.poollu_end = None  # ending pools (mol C/m2, size = npoollu)
        self.poollu_min = None  # minimum pool value (mol C/m2, size = npoollu)
        self.poollu_max = None  # maximum pool value (mol C/m2, size = npoollu)
        self.poollu_gain = None  # net pool gain (mol C/m2, size = npoollu)
        self.poollu_loss = None  # net pool loss (mol C/m2, size = npoollu)
        self.poollu_ratio = None  # ratio of input/output (-, size = npoollu)
        self.poollu_equib = None  # equilibrium pools (mol C/m2, size = npoollu)

        self.poollu_notdone = None  # flag for if dead pools are spunup (logical, size = npoollu)

        # ...equilibrium variables for surface pools
        # .....cwd + litmet + litstr
        self.deadsfc_init = None  # initial pool total (mol C/m2)
        self.deadsfc_end = None  # ending pool total (mol C/m2)
        self.deadsfc_gain = None  # net gain (mol C/m2)
        self.deadsfc_loss = None  # net loss (mol C/m2)
        self.deadsfc_ratio = None  # gain/loss ratio (-)
        self.deadsfc_notdone = None  # flag for if pools are spunup (logical)

        # ...equilibrium variables for soil pools
        # .....slit + slow + arm
        self.deadsoil_init = None  # initial pool total (mol C/m2)
        self.deadsoil_end = None  # ending pool total (mol C/m2)
        self.deadsoil_gain = None  # net gain (mol C/m2)
        self.deadsoil_loss = None  # net loss (mol C/m2)
        self.deadsoil_ratio = None  # gain/loss ratio (-)
        self.deadsoil_notdone = None  # flag for if pools are spunup (logical)

        # ...spin-up variables
        self.lupft_spunup = None  # (logical)


# -------------------------------------------------
# Live Pool Equilibrium Variables (PFT)
# -------------------------------------------------
class EquiblType:
    def __init__(self):
        # ...prognostic pool variables for equilibrium calculation

        self.poolpfttotgain = None  # sum of pool gains (mol/m2, size = npoolpft)
        self.poolpfttotloss = None  # sum of pool losses (mol/m2, size = npoolpft)

        # ...equilibrium variables for individual pools

        self.poolpftinit = None  # initial pools (mol C/m2, size = npoolpft)
        self.poolpftend = None  # ending pools (mol C/m2, size = npoolpft)
        self.poolpftmin = None  # minimum pool value (mol C/m2, size = npoolpft)
        self.poolpftmax = None  # maximum pool value (mol C/m2, size = npoolpft)
        self.poolpftgain = None  # net gain (mol C/m2), size = npoolpft
        self.poolpftloss = None  # net loss (mol C/m2, size = npoolpft)
        self.poolpftratio = None  # ratio of input/output (-, size = npoolpft)
        self.poolpftequib = None  # equilibrium pools (mol C/m2, size = npoolpft)

        self.poolpftnotdone = None  # flag for if live pools are spunup (logical, size = npoolpft)

        # ...equilibrium variables for live pool sums
        # .....leaf + root + wood + prod
        self.live_init = None  # initial live pool total (mol C/m2)
        self.live_end = None  # ending live pool total (mol C/m2)
        self.live_gain = None  # live pool net gain (mol C/m2)
        self.live_loss = None  # live pool net loss (mol C/m2)
        self.live_ratio = None  # gain/loss ratio (-)
        self.live_notdone = None  # flag for if live pools are spunup (logical)


# ---------------------------------------------------------------------
# Flux Variables (CAN; CAS; PFT)
# ---------------------------------------------------------------------
class FluxType:
    def __init__(self):
        # ...land-atmosphere exchange info
        self.ct = None  # thermal transfer coefficient (-)
        self.cu = None  # momentum transfer coefficient (-)
        self.drag = None  # drag (kg/m2/s)
        self.ustar = None  # friction velocity (m/s)
        self.ventmf = None  # ventilation mass flux (kg/m2/s)

        # #...latent heat flux
        self.ec = None  # canopy latent heat flux (J/m2)
        self.eci = None  # latent heat flux, canopy interception (puddles) (J/m2)
        self.ect = None  # latent heat flux, canopy transpiration (J/m2)
        self.eg = None  # ground latent heat flux (J/m2)
        self.egi = None  # latent heat flux, ground interception (puddles) (J/m2)
        self.egs = None  # latent heat flux, ground evaporation (J/m2)
        self.egsmax = None  # maximum ground evapotration per timestep (J/m2)
        self.es = None  # snow latent heat flux (J/m2)
        self.fws = None  # CAS-BL latent heat flux (W/m2)

        # ...sensible heat flux
        self.hc = None  # canopy sensible heat flux (J/m2)
        self.hg = None  # ground sensible heat flux (J/m2)
        self.hs = None  # snow sensible heat flux (J/m2)
        self.fss = None  # CAS-BL sensible heat flux (W/m2)

        # ...storage heat flux
        self.storhc = None  # canopy heat storage flux (W/m2)
        self.storhg = None  # ground heat storage flux (W/m2)

        # ...resistances
        self.ra = None  # canopy air space - mixed layer resistance (s/m)
        self.rb = None  # canopy to canopy air space resistance (s/m)
        self.rbc = None  # canopy to canopy air space resistance
        #    adjusted for snow (-)
        self.rc = None  # bulk leaf to canopy resistance (s/m)
        self.rd = None  # ground to canopy air space resistance (s/m)
        self.rdc = None  # ground to canopy air space resistance
        #    adjusted for snow (-)
        self.rds = None  # ground and soil resistance (s/m)

        # ...balance checks
        self.ebalnum = None  # energy balance
        self.wbalnum = None  # water balance


# ---------------------------------------------------------------------
# Soil Hydrology Variables (Soil)
# ---------------------------------------------------------------------
class HydrosType:
    def __init__(self):
        # ...environmental variables
        self.rhsoil = None  # soil surface relative humidity (-)
        self.rsoil = None  # soil surface resistance
        #  (due to surface tension, s/m)

        # ...evapotranspiration
        self.ecmass = None  # canopy evapotranspiration (kg/m2 or mm water)
        self.egmass = None  # ground evaporation (kg/m2 or mm water)

        # ...precipitation
        self.infil = None  # water infiltrated into top soil layer (mm)
        self.p0 = None  # ground surface precip (mm)
        self.pcpg_rain = None  # ground surface rain precip (mm/s)
        self.pcpg_snow = None  # ground surface snow precip (mm/s)

        # ...runoff
        self.roff = None  # total subsurface runoff from soil layers (mm)
        self.roffo = None  # overland runoff (mm)

        # ...snow
        self.snow_gdepth = None  # depth of snow on ground (m)
        self.snow_gmass = None  # mass of snow on ground (kg/m2)
        self.snow_gvfc = None  # snow ground cover fraction (0-1)
        #   (formerly areas)

        # ...soil diagnostics
        self.www_tot = None  # total soil water-all layers, water+ice (kg/m2)
        self.www_inflow = None  # water inflow at ground surface (kg/m2/s)
        self.satfrac = None  # total fraction of water saturation in soil column (-)

        # ...water interception
        self.capacc_liq = None  # prognostic canopy surface liquid (kg/m2)
        self.capacc_snow = None  # prognostic canopy surface snow (kg/m2)
        #   (formerly snow_veg)
        self.capacg = None  # prognostic ground surface liquid (kg/m2)
        self.satcapc = None  # canopy wetness storage limit (kg/m2)
        self.satcapg = None  # ground wetness storage limit (kg/m2)

        self.snow_cvfc = None  # snow vertical cover fraction (-)
        #   (formerly canex=1-snow_cvfc)
        self.wetfracc = None  # canopy wetness fraction (-)
        self.wetfracg = None  # ground wetness fraction (-)


# -------------------------------------------------
# Vegetation-Specific Hydrology Variables (PFT)
# -------------------------------------------------
class HydrovType:
    def __init__(self):
        # ...rooting zone information
        # ......Plant Available Water (PAW; liquid only)
        self.paw_lay = None # PAW per soil layer (kg/m3, size = nsoil)
        self.pawmax_lay = None  # PAW maximum per soil layer (kg/m3, size = nsoil)
        self.pawfrac_lay = None  # PAW fraction per soil layer (-, size = nsoil)
        self.pawfrw = None  # Root-weighted PAW fraction in soil column (kg/m2)
        self.pawftop = None  # Mean PAW fraction in top 3 soil layers (-)
        self.pawfzw = None # Soil-layer depth-weighted PAW fraction (kg/m2)

        # ......Total Available Water (TAW; liquid + ice)
        self.taw_lay = None  # TAW per soil layer (kg/m3, size = nsoil?)
        self.tawfrac_lay = None  # TAW fraction per soil layer (-, size = nsoil?)
        self.tawfrw = None  # Root-weighted TAW in soil column (kg/m2)
        self.tawftop = None  # Mean TAW fraction in top 3 soil layers (-)
        self.tawfzw = None  # Soil-layer depth weighted TAW fraction (kg/m2)

        # .....Climatological Water Availability
        self.clim_pawfrw = None  # climatological root-weighted PAW fraction (-)
        self.clim_tawfrw = None  # climatological root-weighted TAW fraction (-)


# -----------------------------------------------------
# Phenology Variables (PFT)
# -----------------------------------------------------
class PhenType:
    def __init__(self):
        # ...growing season start determinants
        self.phenave_assim = None  # Running-Mean Assimilation (mol C/m2/s)
        self.phenave_assimsm = None  # Seasonal Maximum Mean Assimilation (mol C/m2/s)
        self.phenave_assimpot = None  # Mean Assimilation Potential (-)
        self.phenflag_assimlow = None  # Assimilation Flag For Growing Season Reset (logical)

        self.phenave_pr = None  # Seasonal Mean Precipitation (mm/day)
        self.phenave_prsm = None  # Seasonal Maximum Mean Precipitation (mm/day)
        self.phenave_prsdoy = None  # Seasonal Day of Maximum Precip (doy)
        self.phenave_prcdoy = None  # Climatological Mean Day of Max Precip (doy)
        self.phenave_prpot = None  # Seasonal Precipitation Potential (-)
        self.phenflag_precip = None  # Precipitation Flag for Growing Season Start (logical)

        self.phenave_tawftop = None  # Running-Mean TAW in Top 3 Soil Layers (-)
        self.phenflag_moist = None  # Moisture Flag for Growing Season Start (logical)

        self.phenave_tm = None  # Running-Mean Temperature (K)
        self.phenflag_temp = None  # Temperature Flag for Growing Season Start (logical)

        self.phenflag_daylen = None  # Daylength Flag for Growing Season Start (logical)
        self.phenflag_gsspass = None  # Combined Growing Season Start Flag (logical)

        # ...growing season information
        self.nd_dormant = None  ## of days dormant
        self.nd_gs = None  ## of days of growing season
        self.nd_stg = None  ## of days per stage (size = npstg-1)

        # ...phenology stage
        self.phen_istage = None  # Phenology Stage (1-5)
        self.phen_pi = None  # Phenology Stage Index

        # ...dynamic phenology stage variables
        self.phens_dayl = None  # Phenology Stage Daylength Potential

        self.phenc_climp = None  # Climatological Suitability (-)
        self.phenc_laimax = None  # Max Potential LAI (m2/m2)
        self.phenc_laimin = None  # Min Potential LAI (m2/m2)
        self.phens_grw = None  # Phenology Stage Growth Potential

        self.phenave_env = None  # Environmental Conditions Potential
        self.phenave_wa = None  # Water Availability Potential
        self.phenave_wac = None  # Combined Environmental and Water Potential
        self.phenave_wacsm = None  # Seasonal Maximum Combined Potential
        self.phens_wx = None  # Phenology Stage Weather Potential

        # ...defined phenology stage variables
        self.ipd = None  # planting date (doy)
        self.dapd = None  # days after planting date (days)
        self.dapdaf = None  # days after planting above freezing (days)
        self.gdd = None  # growing degree days (-)
        self.seed_pool = None  # seed pool carbon (mol C/m2)


# ---------------------------------------------------------------------
# Dead Pool Variables (Soil)
# ---------------------------------------------------------------------
class PooldType:
    def __init__(self):
        # ====Dead Pool Gains (per timestep)====#

        # -------------
        # Grazing Gains (per soil layer)
        self.gain_grz_lay = None  # gain from grazing (mol C/m2/s, size = npoollu,nsoil)

        # --------------
        # Harvest Gains (per soil layer)
        self.gain_hrvst_lay = None  # gain from harvest (mol C/m2/s, size = npoollu,nsoil)

        # -------------------------
        # Live Pool Transfer Gains (per soil layer)
        self.gain_transl_lay = None  # gain from live pools (mol C/m2/s, size = npoollu,nsoil)

        # -------------------------
        # Dead Pool Transfer Gains (per soil layer)
        self.gain_transd_lay = None  # gain from dead pools (mol C/m2/s, size = npoollu,nsoil)

        # ====Dead Pool Losses (per timestep)====#
        # ---------------------------------------

        # Fire Loss
        self.loss_fire_lay = None  # loss from fire (mol C/m2/s, size = npoollu,nsoil)

        # Heterotrophic Respiration/Transfer Loss

        # ...surface pools
        self.mhrt_sfc_assim = None  # surface assimilation scalar (-)
        self.mhrt_sfc_freeze = None  # surface cold/freezing scalar (-)
        self.mhrt_sfc_hot = None  # surface high temperature scalar (-)
        self.mhrt_sfc_precip = None  # surface precip scaling factor (-)
        self.mhrt_sfc_scale = None  # surface respiration scaling coefficient (-)

        # ...soil pools per soil layer
        self.mhrt_soil_freeze_lay = None  # freeze inhibition scalar (-, size = nsoil)
        self.mhrt_soil_hot_lay = None  # high temperature scalar (-, size = nsoil)
        self.mhrt_soil_moist_lay = None  # soil moisture scalar (-, size = nsoil)
        self.mhrt_soil_pawf_lay = None  # PAW fraction scalar (-, size = nsoil)
        self.mhrt_soil_scale_lay = None  # combined soil scalar (-, size = nsoil)

        # ...soil scalars root-weighted
        self.mhrt_soil_assim = None  # assimilation scalar (-)
        self.mhrt_soil_freeze = None  # freeze inhibition scalar (-)
        self.mhrt_soil_hot = None  # high temperature scalar (-)
        self.mhrt_soil_moist = None  # soil moisture scaling factor (-)
        self.mhrt_soil_pawfrw = None  # soil pawfrw scalar (-)
        self.mhrt_soil_precip = None  # soil precipitation scalar (-)
        self.mhrt_soil_scale = None  # combined soil scalar (-)

        # ...respiration and transfer information per soil layer
        self.kratert_lay = None  # scaled decay rate (1/s, size = npoollu,nsoil)
        self.loss_resp_lay = None  # loss from respiration (mol C/m2/s, size = npoollu,nsoil)
        self.loss_trans_lay = None  # loss from decay transfers (mol C/m2/s, size = npoollu,nsoil)

        # ...combined respiration rates
        self.resp_het = None  # heterotrophic respiration (mol C/m2/s)
        self.resp_soil = None  # soil respiration (mol C/m2/s)
        self.resp_soil_lay = None  # (size = nsoil)
        self.resp_soilnr = None  # soil respiration w/o roots (mol C/m2/s)
        self.resp_soilnr_lay = None  # (size = nsoil)

        # ------------------------
        # Daily net pool change (per soil layer)
        self.poollu_dgain = None  # pool gain (mol C/m2/day, size = npoollu,nsoil)
        self.poollu_dloss = None  # pool loss (mol C/m2/day, size = npoollu,nsoil)

        # ------------------------
        # Prognostic Carbon Pools
        self.poollu = None  # vertically integrated pool size (mol C/m2, size = npoollu)
        self.poollu_lay = None  # prognostic dead carbon pools (mol C/m2, size = npoollu,nsoil)
        self.poollu_flay = None  # fraction of carbon per soil layer (-, size = npoollu,nsoil)

        # ---------------
        # Carbon Balance
        self.poollup = None  # previous carbon pool (mol C/m2, size = npoollu)


# -------------------------------------------------
# Live Pool Variables (PFT)
# -------------------------------------------------
class PoollType:
    # ====Live Pool Gains (lpg, per timestep)====#
    def __init__(self):
        # Autotrophic Respiration
        # ....Growth.....
        self.loss_gresp = None  # loss from growth resp (mol C/m2/s, size = npoolpft)

        # .....Maintenance.....
        # ...canopy respiration scaling coefficients
        self.mcr_assim = None  # canopy assimilation scalar
        self.mcr_freeze = None  # canopy freeze inhibition
        self.mcr_hot = None  # canopy high temperature exponential
        self.mcr_scale = None  # combined canopy respiration scalar

        # ...root respiration scaling coefficients
        self.mrr_freeze_lay = None  # roots freeze inhibition scalar (size = per soil layer)
        self.mrr_hot_lay = None  # roots high temperature exponential (size = per soil layer)
        self.mrr_scale_lay = None  # combined roots scalar (size = per soil layer)

        self.mrr_assim = None  # assimilation (root-weighted)
        self.mrr_freeze = None  # freeze inhibition (root-weighted)
        self.mrr_hot = None  # high temperature (root-weighted)
        self.mrr_lai = None  # leaf support (root-weighted)
        self.mrr_scale = None  # combined root-weighted scalar for respiration (root-weighted)

        # Seed (Transfer) Gains
        self.gain_seed = None  # gain from seed (mol C/m2/s, size = npoolpft)

        # ...maintenance respiration information per soil layer
        self.krater_lay = None  # (scaled maintainance loss rate (1/s), size=npoolpft,nsoil)
        self.loss_mresp_lay = None  # (loss from maintainence (mol C/m2/s), size=npoolpft,nsoil)

        # .....Combined Respiration Rates.....
        self.resp_auto = None  # autotrophic respiration (mol C/m2/s)
        self.resp_grow = None  # growth respiration (mol C/m2/s)
        self.resp_leaf = None  # leaf respiration (mol C/m2/s)
        self.resp_mntn = None  # maintainence respiration (mol C/m2/s)
        self.resp_nveg = None  # non-vegetation respiration (mol C/m2/s)
        self.resp_root = None  # root respiration (mol C/m2/s)

        # Live-To-Dead Transfer
        # .....transfers use fractions of the pool that is transferring
        # .....transfer = fraction * pool_size

        # ...leaf transfer (fractions per day)
        self.tfl_daylen = None  # shortening daylength
        self.tfl_freeze = None  # freezing
        self.tfl_dry = None  # water deficiency
        self.tfl_pstage = None  # phenology stage
        self.tfl_total = None  # total leaf transfer

        # .....turnover transfer
        self.tf_turnover = None  # (fractions per day, size = npoolpft)

        # ...transfer loss information (per soil layer)
        self.loss_trans_lay = None  # (loss to dead pool transfers (mol C/m2/s),size= npoolpft,nsoil)

        # Fire Loss
        self.nd_fire = None  ## of days burned
        self.resp_fire = None  # fire respiration (mol C/m2/s)
        self.rmmd_fire = None  # fire emitted but not removed due to fire dataset and SiB4 mismatch (mol C/m2/s)
        self.loss_fire_lay = None  # (loss from fire (mol C/m2/s),size = npoolpft,nsoil)

        # Grazing Loss
        self.nd_grz = None  ## of days grazed
        self.resp_grz = None  # grazing respiration (mol C/m2/s)
        self.loss_grz = None  # loss from grazing (mol C/m2/s, size= npoolcan)

        # Harvest Loss
        self.loss_hrvst_lay = None  # loss from harvest per soil layer (mol C/m2/s, size=npoolpft,nsoil)
        self.resp_hrvst = None  # C harvest respiration (mol C/m2/s)
        self.rmvd_hrvst = None  # C harvested and removed (mol C/m2)

        # Daily net pool change (per soil layer)
        self.poolpft_dgain = None  # pool gain (mol C/m2/day,size=npoolpft,nsoil)
        self.poolpft_dloss = None  # pool loss (mol C/m2/day,size=npoolpft,nsoil)

        # Prognostic Carbon Pools
        self.poolpft = None  # vertically integrated pool size (mol C/m2, size = npoolpft)
        self.poolpft_lay = None  # prognostic carbon pools (mol C/m2, size = npoolpft,nsoil)
        self.poolpft_flay = None  # fraction of carbon per soil layer (-, size = npoolpft,nsoil)

        # Carbon Balance
        self.poolpftp = None  # previous carbon pool (mol C/m2, size = npoolpft)


# ---------------------------------------------------------------------
# Radiation Variables (CAN, CAS, Soil)
# ---------------------------------------------------------------------
class RadType:

    def __init__(self):
        # ...albedos
        self.albedo_visb = None  # albedo, visible beam (-)
        self.albedo_visd = None  # albedo, visible diffuse (-)
        self.albedo_nirb = None  # albedo, nir beam (-)
        self.albedo_nird = None  # albedo, nir diffuse (-)

        # ...radiation variables
        self.radfacc = None  # canopy radiation absorption factors (-, size = 2,2 )
        #   (1,1) - visible, beam
        #   (1,2) - visible, diffuse
        #   (2,1) - nir, beam
        #   (2,2) - nir, diffuse
        self.radfacg = None  # ground radiation absorption factors (-, size = 2,2)
        #   (1,1) - visible, beam
        #   (1,2) - visible, diffuse
        #   (2,1) - nir, beam
        #   (2,2) - nir, diffuse

        self.radc3c = None  # absorbed radiation by canopy (W/m2)
        self.radc3g = None  # absorbed radiation by ground (W/m2)
        self.radtc = None  # canopy net radiation (W/m2)
        self.radtg = None  # ground net radiation (W/m2)
        self.radts = None  # snow net radiation (W/m2)
        self.effgc = None  # effective ground cover for thermal radiation (-)

        # ...temperatures
        self.tsfc = None  # surface temperature (K)


# ----------------------------------------------
# Fluorescence (SIF) Variables (CAN; CAS; PFT)
# ----------------------------------------------
class SifType:

    def __init__(self):
        # ...electron transports
        self.sif_je = None  # electron transport
        self.sif_jo = None  # max electron transport
        self.sif_jejo = None  # fractional transport (je/jo)

        # ...k coefficients, defined as the probability of
        # .....excitons to follow certain pathways (-)
        self.sif_kd = None  # Heat dissipation
        self.sif_kn = None  # Non-photochemical quenching (NPQ)
        self.sif_kp = None  # Photosynthesis

        # ...x factor (0 when GPP=potential, 1 when GPP=0)
        self.sif_x = None

        # ...yields (-)
        self.phi_d = None  # Heat dissipation yield
        self.phi_f = None  # SIF yield
        self.phi_n = None  # NPQ yield
        self.phi_p = None  # Photosynthetic yield

        # ...resulting sif values
        self.sif = None  # fluorescence (W m-2 sr-1 nm-1)


# ---------------------------------------------------------------------
# Soil/Snow Column Variables (Soil)
# ---------------------------------------------------------------------
class SScolType:
    def __init__(self):
        # ...prognostic number of snow layers (negative)
        self.nsl = None

        # ...soil diagnostics for soil column (nsoil)
        self.rootr = None  # effective rooting frac for soil hydrology (-, size = nsoil)
        self.satfrac_lay = None  # fraction of water saturation (-,size = nsoil)

        # ...snow/soil diagnostic column variables
        self.eff_poros = None  # soil/snow liquid effective porosity (-, size = -nsnow+1:nsoil)
        self.layer_z = None  # soil/snow layer interface depth (m,size = -nsnow+1:nsoil)
        self.node_z = None  # soil/snow layer node depth (m,size = -nsnow+1:nsoil)
        self.shcap = None  # soil/snow total heat capacity (J/m2/K,size = -nsnow+1:nsoil)
        self.slamda = None  # soil/snow heat flux term (W/m2/K,size = -nsnow+1:nsoil)
        self.tksoil = None  # soil/snow thermal conductivity (W/m/K,size = -nsnow+1:nsoil)
        self.vol_liq = None  # soil/snow liquid water volume (kg/m3,size = -nsnow+1:nsoil)
        self.vol_ice = None  # soil/snow ice volume (kg/m3,size = -nsnow+1:nsoil)

        # ...snow/soil prognostic column variables
        self.dz = None  # soil/snow layer thickness (m,size = -nsnow+1:nsoil)
        self.td = None  # soil/snow temperature (K,size = -nsnow+1:nsoil)
        self.www_liq = None  # soil/snow liquid water (kg/m2,size = -nsnow+1:nsoil)
        self.www_ice = None  # soil/snow ice (kg/m2,size = -nsnow+1:nsoil)


# -------------------------------------------------
# Vegetation Description and State Variables (PFT)
# -------------------------------------------------
class VegType:
    def __init__(self):
        # ...land-atmos interactions
        self.z0 = None  # canopy snow-adjusted roughness length (m)
        self.z0d = None  # canopy roughness length (m)
        self.zp_dispd = None  # zero-plane displacement (m)
        self.zpd_adj = None  # snow-adjusted zero-plane displacement (m)
        self.zztemp = None  # temperature height for mass flux (m)
        self.zzwind = None  # wind height for mass flux (m)

        # ...resistances
        self.cc1 = None  # bulk pbl resistance coefficient (sqrt(s/m))
        self.cc2 = None  # ground to canopy airspace resistance (-)

        # ...root profile
        self.rootf = None  # root fraction (-,size = nsoil)

        # ...vegetation state
        self.fpar = None  # absorbed fraction of PAR (-)
        self.green = None  # green fraction of LAI (-)
        self.lai = None  # leaf area index (-)
        self.lait = None  # canopy total leaf area index (w/ dead, -)
        self.vcover = None  # fraction of vegetation cover (-)

        # ...vegetation properties
        self.gmudmu = None  # time-mean leaf projection (-)
        self.park = None  # solar absorption factor /
        #      extinction coefficient for PAR (-)
        self.vmax = None  # rubisco velocity (mol/m2/s)

        # ...climatological vegetation states
        self.clim_lai = None  # climatological LAI (-)


# =================================================
# Driver Data Variables
# ------------------------------------------------------------------
# Grid Cell Diagnostic Variables
# -----------------------------------------------------------------

class GDiagType:
    def __init__(self):
        # ...daytime/sunlight properties
        self.cosz = None  # cosine of solar zenith angle (-)
        self.daylen = None  # length of daylight (hrs)
        self.daylendt = None  # change in length of day (hrs)

        # ...misc driver forcings
        self.tmdf = None  # daily (24-hr running mean) temperature (F)
        self.thm = None  # mixed layer potential temperature (K)
        self.bps = None  # (ps/1000)**kapa - turns theta into temp (size = 2)
        self.em = None  # mixed layer water vapor pressure (hPa or mb)
        self.ros = None  # surface air density (kg/m3)
        self.psy = None  # psycrometric constant (gamma) (hPa/K)

        # ...precipitation properties
        self.seas_precippot = None  # seasonal precipitation potential (-)

        # ...radiation properties
        self.radvbc = None  # visible beam radiation (W/m2)
        self.radvdc = None  # visible diffuse radiation (W/m2)
        self.radnbc = None  # nir beam radiation (W/m2)
        self.radndc = None  # nir diffuse radiation (W/m2)

        self.toa_solar = None  # Top-of-Atmosphere insolation (W/m2)
        self.toa_radvbc = None  # TOA visible beam radiation (W/m2)
        self.toa_radvdc = None  # TOA visible diffuse radiation (W/m2)
        self.toa_radnbc = None  # TOA near-infrared (NIR) beam radiation (W/m2)
        self.toa_radndc = None  # TOA NIR diffuse radiation (W/m2)

        self.toa_par = None  # TOA PAR (mol/m2/s)
        self.aod = None  # aerosol + cloud optical depth (-)

        # ...solar-induced fluorescence (SIF) properties
        self.sif_atten = None  # SIF attenuation factor (-)
        self.sif_flag = None  # conditions suitable for
        # 1=GOME2 2=OCO2 ? (size = 2, logical)

        # ...spinup variables
        self.gridcell_spunup = None  # (logical)


# ------------------------------------------------------------------
# Grid Cell Prognostic Variables
# -----------------------------------------------------------------
class GProgType:
    def __init__(self):
        # ...prognostic driver data/forcings
        self.cupr = None  # cumulus precipitation rate (mm/s)
        self.cuprt = None  # cumulus precip rate (m/s)
        self.cupr1 = None  # cumulus precipitation rate (mm/s)
        self.cupr2 = None  # cumulus precipitation rate (mm/s)
        self.dlwbot = None  # surface incident longwave
        self.dlwbot1 = None  # surface incident longwave
        self.dlwbot2 = None  # surface incident longwave
        self.lspr = None  # stratiform precipitation rate (mm/s)
        self.lsprt = None  # stratiform precip rate (m/s)
        self.lspr1 = None  # stratiform precipitation rate (mm/s)
        self.lspr2 = None  # stratiform precipitation rate (mm/s)
        self.ps = None  # surface pressure (hPa or mb)
        self.ps1 = None  # surface pressure (hPa or mb)
        self.ps2 = None  # surface pressure (hPa or mb)
        self.sh = None  # mixed layer water vapor mixing ratio (kg/kg)
        self.sh1 = None  # mixed layer water vapor mixing ratio (kg/kg)
        self.sh2 = None  # mixed layer water vapor mixing ratio (kg/kg)
        self.spdm = None  # wind speed (m/s)
        self.spdm1 = None  # wind speed (m/s)
        self.spdm2 = None  # wind speed (m/s)
        self.sw_dwn = None  # surface incident shortwave radiation (W/m2)
        self.sw_dwn1 = None  # surface incident shortwave radiation (W/m2)
        self.sw_dwn2 = None  # surface incident shortwave radiation (W/m2)
        self.tm = None  # mixed layer temperature (K)
        self.tm1 = None  # mixed layer temperature (K)
        self.tm2 = None  # mixed layer temperature (K)

        # ...fire emissions
        self.firec = None  # C loss from fire (mol C/m2/s)
        self.firec1 = None  # C loss from fire (mol C/m2/s)
        self.firec2 = None  # C loss from fire (mol C/m2/s)
        self.fireco2 = None  # CO2 respiration from fire (mol C/m2/s)
        self.fireco21 = None  # CO2 respiration from fire (mol C/m2/s)
        self.fireco22 = None  # CO2 respiration from fire (mol C/m2/s)

        # ...carbon cycle
        self.pco2m = None  # Mixed Layer (background) CO2 partial pressure (Pa)
        self.pcosm = None  # Mixed Layer (background) COS partial pressure (Pa)

        # ...daily values
        self.tmd = None  # daily (24-hr running mean) temperature (K)

        # ...seasonal values
        self.seas_precip = None  # seasonal precipitation (mm/day)
        self.seas_tm = None  # seasonal temperature (K)

        # ...climatological values
        self.clim_cupr = None  # clim-mean convective precipitation (mm/day)
        self.clim_precip = None  # clim-mean precipitation (mm/day)
        self.clim_tm = None  # clim-mean temperature (K)

        # ...tm5 COS values
        self.cosm_tm5 = None  # COS mixing ratio (molCOS/molAir)
        self.cosm_tm51 = None  # COS mixing ratio (molCOS/molAir)
        self.cosm_tm52 = None  # COS mixing ratio (molCOS/molAir)


# ******************************************************************
# ------------------------------------------------------------------
# Begin definition of spatial scaling hierarchy
# ------------------------------------------------------------------

# ------------
# define the land unit structure
# includes corresponding:
#    - soil column (Soil)
#    - vegetation (PFT)
#    - canopy (CAN) and canopy air space (CAS)
# ------------
class LuType:
    def __init__(self):
        # vegetation information
        self.ipft = None  # pft reference number (integer)
        self.larea = None  # fraction of coverage per gridcell (0-1)

        # time-invariant variables
        self.soilt = SoilType()  # soil properties

        # time-variant variables
        self.cast = CasType()  # canopy air space variables (CAS)
        self.co2t = Co2Type()  # photosynthetic/CO2 variables
        self.cost = COSType()  # carbonyl sulfide variables
        self.equibdt = EquibdType()  # dead pool equilibrium variables (Soil)
        self.equiblt = EquiblType()  # live pool equilibrium variables (PFT)
        self.fluxt = FluxType()  # flux variables
        self.hydrost = HydrosType()  # soil hydrological variables (Soil)
        self.hydrovt = HydrovType()  # veg hydrological variables (PFT)
        self.phent = PhenType()  # phenology variables (PFT)
        self.pooldt = PooldType()  # dead pool variables (Soil)
        self.poollt = PoollType()  # live pool variables (PFT)
        self.radt = RadType()  # radiation variables
        self.sift = SifType()  # fluorescence variables
        self.sscolt = SScolType()  # soil/snow column variables (Soil)
        self.vegt = VegType()  # vegetation information (PFT)


# ------------
# define the gridcell structure
# ------------
class GridcellType:
    def __init__(self):
        # gridcell information
        self.lat = None # latitude (degrees)
        self.lon = None # longitude (degrees)

        # variables defined at the gridcell level
        self.gdiagt = GDiagType()  # diagnostic variables
        self.gprogt = GProgType()  # prognostic variables

        # gridcell -> landunit hierarchy
        self.g_nlu = None  # number of land units per gridcell
        # ...includes corresponding
        # ....soil, veg (PFT), and canopy (INTEGER)

        self.l = None  # land unit data structure (TYPE = LuType(),size= unknown)


# -----------
# define the top-level structure
# -----------
class SibT:
    def __init__(self):
        self.g = None  # !gridcell data structure (size = unknown, TYPE = GridcellType())


# ------------------------------------------------------------------
# End definition of spatial scaling hierarchy
# ------------------------------------------------------------------
def generate_sib_instance():
    # Declare single instance of sibtype
    sib = SibT()

if __name__ == '__main__':
    test_sibT = SibT()
    test_gct = GridcellType()
    test_lu = LuType()

