
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

#=================================================
#Time Invariant Variables
#---------------------------------------------------------------------
# Soil Properties (Soil)
#---------------------------------------------------------------------

class SoilProperties:
    def __init__(self):
        #...soil properties
        self.sandfrac = None= None # soil sand fraction
        self.clayfrac = None= None # soil clay fraction
        self.soref_vis = None= None # soil shortwave reflectance (-)
        self.soref_nir = None= None # soil longwave reflectance (-)

        self.poros = None= None # soil porosity (zero to one)
        self.satco = None= None # hydraulic conductivity at saturation (m/s)


        self.csolid = None = None # heat capacity, soil solids (J/m3/K)
        self.tkdry = None = None # thermal conductivity, dry soil (W/m/K)
        self.tkmg = None = None # thermal conductivity, soil minerals (W/m/K)
        self.tksat = None= None # thermal conductivity, saturated soil (W/m/K)

        #...soil variables for plant water stress
        self.bee = None # Clapp & Hornberger 'b' exponent (-)
        self.phsat = None # Soil tension at saturation (m)
        self.fieldcap = None # Field Capacity (1/m3)
        self.vwcmin = None # Wilting Point (1/m3)

        #...soil variables for respiration
        self.wopt = None # respiration function optimum soil moisture (-)
        self.woptzm = None # wopt to the zm exponent
        self.wsat = None # respiration function value (-)
        self.zm = None # respiration function exponent (-)

        #...soil variables for water availability
        self.fc_eff = None #Effective Field Capacity (1/m3, size = nsoil)
        self.wp_eff = None #Effective Wilting Point (1/m3, size = nsoil)

#===================================================================
#=================================================
#Time-Step Varying Variables
#-------------------------------------------------
# Canopy (Can) and Canopy Air Space (CAS) Variables
#-------------------------------------------------

class CasType:
    def __init__(self):
        # ...Canopy prognostic variables
        self.tc = None = None # canopy temperature (K)

        # ...CAS prognostic variables
        self.eacas = None # CAS water vapor pressure (hPa or mb)
        self.shcas = None # CAS water vapor mixing ratio (kg/kg)
        self.tcas = None # CAS temperature (K)
        self.tkecas = None # CAS turbulent kinetic energy (J/kg)

        # ...Canopy environmental variables
        self.hcapc = None # canopy heat capacity (J/m2/K)
        self.tcmin = None # frost

        # ...CAS environmental variables
        self.thcas = None # CAS potential temperature (K)
        self.hcapcas = None # CAS heat capacity (J/m2/K)
        self.vcapcas = None  # CAS vapor capacity (J/m2/hPa)

#-------------------------------------------------
# CO2/Photosynthesis Variables (CAN; CAS; PFT)
#-------------------------------------------------
class Co2Type:
    def __init__(self):
        # ...assimilation
        self.assim = None # gross assimilation (mol C/m2/s)
        self.assimd = None # daily (24hr running-mean) assimilation (mol C/m2/s)
        self.clim_assim = None # climatological assimilation (mol C/m2/s)

        # ...canopy scaling
        self.assimpot = None # potential top leaf photosynthesis (mol C/m2/s)
        self.apar = None # absorbed photosynthetically active radiation (mol/m2/s)
        self.aparkk = None # factor for scaling of leaf radiation (-)
        self.gamma = None # CO2 photocompensation point (Pa)
        self.par = None # photosynthetically active radiation (mol/m2/s)
        self.nspar = None # non-scattered photosynthetically active radiation (mol/m2/s)

        # ...canopy air space (CAS) fluxes
        self.casd = None # CAS depth for CO2 (m)
        self.cflux = None # CAS to ref height carbon flux (mol C/m2/s)

        # ...co2 concentrations
        self.pco2cas = None # CAS CO2 partial pressure (Pa)
        self.pco2c = None # chloroplast CO2 partial pressure (Pa)
        self.pco2i = None # leaf internal CO2 partial pressure (Pa)
        self.pco2s = None # leaf surface CO2 partial pressure (Pa)

        # ...resistances
        self.rst = None # prognostic stomatal resistance (s/m)

        # ..soil freeze functions
        self.soilfrz = None # soil freeze function (-)
        self.soilfrztg = None # soil freeze function for top soil layer (-)
        self.soilfrztd = None # soil freeze function for second soil layer (-)

        # .....total stress factors
        self.rstfac = [None, None, None, None] # canopy stress factors (-)
        #  (1) leaf surface RH stress
        #  (2) rootzone water stress
        #  (3) temperature stress
        #  (4) product of factors 1-3
        self.vmaxss = None # stressed rubisco velocity (mol/m2/s)

#-------------------------------------------------
# Carbonyl Sulfide (COS) Variables (CAN; CAS; PFT)
#-------------------------------------------------
class COSType:
    def __init__(self):
        # ...COS CAS
        self.cos_casd = None # CAS depth for COS (m)
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

#-------------------------------------------------
# Dead Pool Equilibrium Variables (Soil)
#-------------------------------------------------
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
        self.lupft_spunup = None(logical)


"""


!-------------------------------------------------
! Live Pool Equilibrium Variables (PFT)
!-------------------------------------------------
type, public :: equibl_type

    !...prognostic pool variables for equilibrium calculation
    real(r8), dimension(:), allocatable :: & !(npoolpft)
          poolpft_totgain, & !sum of pool gains (mol/m2)
          poolpft_totloss    !sum of pool losses (mol/m2)

     !...equilibrium variables for individual pools
     real(r8), dimension(:), allocatable :: & !(npoolpft)
          poolpft_init,  & !initial pools (mol C/m2)
          poolpft_end,   & !ending pools (mol C/m2)
          poolpft_min,   & !minimum pool value (mol C/m2)
          poolpft_max,   & !maximum pool value (mol C/m2)
          poolpft_gain,  & !net gain (mol C/m2)
          poolpft_loss,  & !net loss (mol C/m2)
          poolpft_ratio, & !ratio of input/output (-)
          poolpft_equib    !equilibrium pools (mol C/m2)

     logical, dimension(:), allocatable :: & !(npoolpft)
          poolpft_notdone  !flag for if live pools are spunup

     !...equilibrium variables for live pool sums
     !.....leaf + root + wood + prod
     real(r8) :: live_init     !initial live pool total (mol C/m2)
     real(r8) :: live_end      !ending live pool total (mol C/m2)
     real(r8) :: live_gain     !live pool net gain (mol C/m2)
     real(r8) :: live_loss     !live pool net loss (mol C/m2)
     real(r8) :: live_ratio    !gain/loss ratio (-)
     logical  :: live_notdone     !flag for if live pools are spunup

end type equibl_type


!---------------------------------------------------------------------
! Flux Variables (CAN; CAS; PFT)
!---------------------------------------------------------------------
type, public :: flux_type

    !...land-atmosphere exchange info
    real(r8) :: ct       !thermal transfer coefficient (-)
    real(r8) :: cu       !momentum transfer coefficient (-)
    real(r8) :: drag     !drag (kg/m2/s)
    real(r8) :: ustar    !friction velocity (m/s)
    real(r8) :: ventmf   !ventilation mass flux (kg/m2/s)

     !...latent heat flux
     real(r8) :: ec      ! canopy latent heat flux (J/m2)
     real(r8) :: eci     ! latent heat flux, canopy interception (puddles) (J/m2)
     real(r8) :: ect     ! latent heat flux, canopy transpiration (J/m2)
     real(r8) :: eg      ! ground latent heat flux (J/m2)
     real(r8) :: egi     ! latent heat flux, ground interception (puddles) (J/m2)
     real(r8) :: egs     ! latent heat flux, ground evaporation (J/m2)
     real(r8) :: egsmax  ! maximum ground evapotration per timestep (J/m2)
     real(r8) :: es      ! snow latent heat flux (J/m2)
     real(r8) :: fws     ! CAS-BL latent heat flux (W/m2)

     !...sensible heat flux
     real(r8) :: hc      ! canopy sensible heat flux (J/m2)
     real(r8) :: hg      ! ground sensible heat flux (J/m2)
     real(r8) :: hs      ! snow sensible heat flux (J/m2)
     real(r8) :: fss     ! CAS-BL sensible heat flux (W/m2)

     !...storage heat flux
     real(r8) :: storhc  ! canopy heat storage flux (W/m2)
     real(r8) :: storhg  ! ground heat storage flux (W/m2)

     !...resistances
     real(r8) :: ra      ! canopy air space - mixed layer resistance (s/m)
     real(r8) :: rb      ! canopy to canopy air space resistance (s/m)
     real(r8) :: rbc     ! canopy to canopy air space resistance
                         !    adjusted for snow (-)
     real(r8) :: rc      ! bulk leaf to canopy resistance (s/m)
     real(r8) :: rd      ! ground to canopy air space resistance (s/m)
     real(r8) :: rdc     ! ground to canopy air space resistance
                         !    adjusted for snow (-)
     real(r8) :: rds     ! ground and soil resistance (s/m)

    !...balance checks
    integer(i4) :: ebalnum  !energy balance
    integer(i4) :: wbalnum  !water balance

end type flux_type


!---------------------------------------------------------------------
! Soil Hydrology Variables (Soil)
!---------------------------------------------------------------------
type, public :: hydros_type

     !...environmental variables
     real(r8) :: rhsoil  ! soil surface relative humidity (-)
     real(r8) :: rsoil   ! soil surface resistance
                         !  (due to surface tension, s/m)

     !...evapotranspiration
     real(r8) :: ecmass   ! canopy evapotranspiration (kg/m2 or mm water)
     real(r8) :: egmass   ! ground evaporation (kg/m2 or mm water)

     !...precipitation
     real(r8) :: infil     ! water infiltrated into top soil layer (mm)
     real(r8) :: p0        ! ground surface precip (mm)
     real(r8) :: pcpg_rain ! ground surface rain precip (mm/s)
     real(r8) :: pcpg_snow ! ground surface snow precip (mm/s)

     !...runoff
     real(r8) :: roff      ! total subsurface runoff from soil layers (mm)
     real(r8) :: roffo     ! overland runoff (mm)

     !...snow
     real(r8) :: snow_gdepth  ! depth of snow on ground (m)
     real(r8) :: snow_gmass   ! mass of snow on ground (kg/m2)
     real(r8) :: snow_gvfc    ! snow ground cover fraction (0-1)
                              !   (formerly areas)

     !...soil diagnostics
     real(r8) :: www_tot     !total soil water-all layers, water+ice (kg/m2)
     real(r8) :: www_inflow  !water inflow at ground surface (kg/m2/s)
     real(r8) :: satfrac     !total fraction of water saturation in soil column (-)

     !...water interception
     real(r8) :: capacc_liq   ! prognostic canopy surface liquid (kg/m2)
     real(r8) :: capacc_snow  ! prognostic canopy surface snow (kg/m2)
                              !   (formerly snow_veg)
     real(r8) :: capacg       ! prognostic ground surface liquid (kg/m2)
     real(r8) :: satcapc      ! canopy wetness storage limit (kg/m2)
     real(r8) :: satcapg      ! ground wetness storage limit (kg/m2)

     real(r8) :: snow_cvfc  ! snow vertical cover fraction (-)
                            !   (formerly canex=1-snow_cvfc)
     real(r8) :: wetfracc  ! canopy wetness fraction (-)
     real(r8) :: wetfracg  ! ground wetness fraction (-)

end type hydros_type


!-------------------------------------------------
! Vegetation-Specific Hydrology Variables (PFT)
!-------------------------------------------------
type, public :: hydrov_type
     !...rooting zone information
     !......Plant Available Water (PAW; liquid only)
     real(r8), dimension(:), allocatable :: &  !(nsoil)
         paw_lay,    &  !PAW per soil layer (kg/m3)
         pawmax_lay, &  !PAW maximum per soil layer (kg/m3)
         pawfrac_lay    !PAW fraction per soil layer (-)
     real(r8) :: &
         pawfrw,  &     !Root-weighted PAW fraction in soil column (kg/m2)
         pawftop, &     !Mean PAW fraction in top 3 soil layers (-)
         pawfzw         !Soil-layer depth-weighted PAW fraction (kg/m2)

     !......Total Available Water (TAW; liquid + ice)
     real(r8), dimension(:), allocatable :: &
         taw_lay,     & !TAW per soil layer (kg/m3)
         tawfrac_lay    !TAW fraction per soil layer (-)

     real(r8) :: &
          tawfrw,  &  !Root-weighted TAW in soil column (kg/m2)
          tawftop, &  !Mean TAW fraction in top 3 soil layers (-)
          tawfzw      !Soil-layer depth weighted TAW fraction (kg/m2)

     !.....Climatological Water Availability
     real(r8) :: clim_pawfrw !climatological root-weighted PAW fraction (-)
     real(r8) :: clim_tawfrw !climatological root-weighted TAW fraction (-)

end type hydrov_type


!-----------------------------------------------------
! Phenology Variables (PFT)
!-----------------------------------------------------
type, public :: phen_type

     !...growing season start determinants
     real(r8) :: phenave_assim     !Running-Mean Assimilation (mol C/m2/s)
     real(r8) :: phenave_assimsm   !Seasonal Maximum Mean Assimilation (mol C/m2/s)
     real(r8) :: phenave_assimpot  !Mean Assimilation Potential (-)
     logical ::  phenflag_assimlow !Assimilation Flag For Growing Season Reset

     real(r8) :: phenave_pr       !Seasonal Mean Precipitation (mm/day)
     real(r8) :: phenave_prsm     !Seasonal Maximum Mean Precipitation (mm/day)
     real(r8) :: phenave_prsdoy   !Seasonal Day of Maximum Precip (doy)
     real(r8) :: phenave_prcdoy   !Climatological Mean Day of Max Precip (doy)
     real(r8) :: phenave_prpot    !Seasonal Precipitation Potential (-)
     logical  :: phenflag_precip  !Precipitation Flag for Growing Season Start

     real(r8) :: phenave_tawftop   !Running-Mean TAW in Top 3 Soil Layers (-)
     logical  :: phenflag_moist    !Moisture Flag for Growing Season Start

     real(r8) :: phenave_tm        !Running-Mean Temperature (K)
     logical  :: phenflag_temp     !Temperature Flag for Growing Season Start

     logical :: phenflag_daylen    !Daylength Flag for Growing Season Start
     logical :: phenflag_gsspass   !Combined Growing Season Start Flag

     !...growing season information
     integer(i4) :: nd_dormant !# of days dormant
     integer(i4) :: nd_gs      !# of days of growing season
     integer(i4), dimension(:), allocatable :: & !(npstg-1)
             nd_stg   !# of days per stage (npstg-1)

     !...phenology stage
     integer(i4) :: phen_istage !Phenology Stage (1-5)
     real(r8) :: phen_pi       !Phenology Stage Index

     !...dynamic phenology stage variables
     real(r8) :: phens_dayl     !Phenology Stage Daylength Potential

     real(r8) :: phenc_climp    !Climatological Suitability (-)
     real(r8) :: phenc_laimax   !Max Potential LAI (m2/m2)
     real(r8) :: phenc_laimin   !Min Potential LAI (m2/m2)
     real(r8) :: phens_grw      !Phenology Stage Growth Potential

     real(r8) :: phenave_env  !Environmental Conditions Potential
     real(r8) :: phenave_wa   !Water Availability Potential
     real(r8) :: phenave_wac  !Combined Environmental and Water Potential
     real(r8) :: phenave_wacsm !Seasonal Maximum Combined Potential
     real(r8) :: phens_wx      !Phenology Stage Weather Potential

     !...defined phenology stage variables
     integer(i4) :: ipd  !planting date (doy)
     integer(i4) :: dapd    !days after planting date (days)
     integer(i4) :: dapdaf  !days after planting above freezing (days)
     real(r8) :: gdd     !growing degree days (-)
     real(r8) :: seed_pool    !seed pool carbon (mol C/m2)

end type phen_type


!---------------------------------------------------------------------
! Dead Pool Variables (Soil)
!---------------------------------------------------------------------
type, public :: poold_type

     !====Dead Pool Gains (per timestep)====!

     !-------------
     !Grazing Gains (per soil layer)
     real(r8), dimension(:,:), allocatable :: &  !(npoollu)
             gain_grz_lay !gain from grazing (mol C/m2/s)

     !--------------
     !Harvest Gains (per soil layer)
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
            gain_hrvst_lay !gain from harvest (mol C/m2/s)

     !-------------------------
     !Live Pool Transfer Gains (per soil layer)
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
            gain_transl_lay  !gain from live pools (mol C/m2/s)

     !-------------------------
     !Dead Pool Transfer Gains (per soil layer)
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
            gain_transd_lay  !gain from dead pools (mol C/m2/s)


     !====Dead Pool Losses (per timestep)====!
     !---------------------------------------

     !Fire Loss
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
           loss_fire_lay   !loss from fire (mol C/m2/s)

     !Heterotrophic Respiration/Transfer Loss

     !...surface pools
     real(r8) :: mhrt_sfc_assim  !surface assimilation scalar (-)
     real(r8) :: mhrt_sfc_freeze !surface cold/freezing scalar (-)
     real(r8) :: mhrt_sfc_hot    !surface high temperature scalar (-)
     real(r8) :: mhrt_sfc_precip !surface precip scaling factor (-)
     real(r8) :: mhrt_sfc_scale  !surface respiration scaling coefficient (-)

     !...soil pools per soil layer
     real(r8), dimension(:), allocatable ::  &  !(nsoil)
            mhrt_soil_freeze_lay, & !freeze inhibition scalar (-)
            mhrt_soil_hot_lay,   & !high temperature scalar (-)
            mhrt_soil_moist_lay, & !soil moisture scalar (-)
            mhrt_soil_pawf_lay,  & !PAW fraction scalar (-)
            mhrt_soil_scale_lay    !combined soil scalar (-)

     !...soil scalars root-weighted
     real(r8) :: &
            mhrt_soil_assim,  & !assimilation scalar (-)
            mhrt_soil_freeze, & !freeze inhibition scalar (-)
            mhrt_soil_hot,    & !high temperature scalar (-)
            mhrt_soil_moist,  & !soil moisture scaling factor (-)
            mhrt_soil_pawfrw, & !soil pawfrw scalar (-)
            mhrt_soil_precip, & !soil precipitation scalar (-)
            mhrt_soil_scale     !combined soil scalar (-)

     !...respiration and transfer information per soil layer
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
           kratert_lay,    & !scaled decay rate (1/s)
           loss_resp_lay,  & !loss from respiration (mol C/m2/s)
           loss_trans_lay    !loss from decay transfers (mol C/m2/s)

     !...combined respiration rates
     real(r8) :: resp_het  !heterotrophic respiration (mol C/m2/s)
     real(r8) :: resp_soil !soil respiration (mol C/m2/s)
     real(r8), dimension(:), allocatable :: &  !(nsoil)
            resp_soil_lay
     real(r8) :: resp_soilnr  !soil respiration w/o roots (mol C/m2/s)
     real(r8), dimension(:), allocatable :: &  !(nsoil)
            resp_soilnr_lay

     !------------------------
     !Daily net pool change (per soil layer)
     real(r8), dimension(:,:), allocatable ::   &  !(npoollu,nsoil)
           poollu_dgain,  & !pool gain (mol C/m2/day)
           poollu_dloss     !pool loss (mol C/m2/day)

     !------------------------
     !Prognostic Carbon Pools
     real(r8), dimension(:), allocatable ::   &  !(npoollu)
           poollu  !vertically integrated pool size (mol C/m2)
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
           poollu_lay !prognostic dead carbon pools (mol C/m2)
     real(r8), dimension(:,:), allocatable :: &  !(npoollu,nsoil)
           poollu_flay  !fraction of carbon per soil layer (-)

     !---------------
     !Carbon Balance
     real(r8), dimension(:), allocatable :: & !(npoollu)
         poollup !previous carbon pool (mol C/m2)

end type poold_type


!-------------------------------------------------
! Live Pool Variables (PFT)
!-------------------------------------------------
type, public :: pooll_type

    !====Live Pool Gains (lpg, per timestep)====!
     !===========================================!

     !------------------
     !Assimilation Gains
     !...allocation fractions for live biomass (vary from 0 to 1)
     real(r8), dimension(:), allocatable :: &  !(npoolpft)
          alloc !allocation fractions

     !...dynamic allocation contributions (vary from -1 to 1)
     logical :: aadj_moist !allow moisture adjustments?
     logical :: aadj_temp  !allow temperature adjustments?

     real(r8), dimension(:), allocatable :: &  !(npoolpft)
          alloc_phen,  & !allocation based on phenological state
          alloc_moist, & !allocation adjustments due to moisture stress
          alloc_temp     !allocation adjustments due to temperature stress

     !...pool gains from photosynthesis divied up by allocation fraction
     real(r8), dimension(:), allocatable :: &  !(npoolpft)
          gain_assim  !gain from photosynthesis (mol C/m2/s)

     !---------------------
     !Seed (Transfer) Gains
     real(r8), dimension(:), allocatable :: &  !(npoolpft)
          gain_seed   !gain from seed (mol C/m2/s)

     !====Live Pool Losses (lpl, per timestep)====!
     !===========================================!

     !-----------------------
     !Autotrophic Respiration
     !....Growth.....
     real(r8), dimension(:), allocatable :: &  !(npoolpft)
          loss_gresp   !loss from growth resp (mol C/m2/s)

     !.....Maintenance.....
     !...canopy respiration scaling coefficients
     real(r8) :: mcr_assim     !canopy assimilation scalar
     real(r8) :: mcr_freeze    !canopy freeze inhibition
     real(r8) :: mcr_hot       !canopy high temperature exponential
     real(r8) :: mcr_scale     !combined canopy respiration scalar

     !...root respiration scaling coefficients
     real(r8), dimension(:), allocatable :: &  !(per soil layer)
           mrr_freeze_lay, & !roots freeze inhibition scalar
           mrr_hot_lay,    & !roots high temperature exponential
           mrr_scale_lay     !combined roots scalar

     real(r8) :: &        !root-weighted
           mrr_assim,  &  !assimilation
           mrr_freeze, &  !freeze inhibition
           mrr_hot,    &  !high temperature
           mrr_lai,    &  !leaf support
           mrr_scale      !combined root-weighted scalar for respiration

     !...maintenance respiration information per soil layer
     real(r8), dimension(:,:), allocatable :: &  !(npoolpft,nsoil)
          krater_lay, &  !scaled maintainance loss rate (1/s)
          loss_mresp_lay !loss from maintainence (mol C/m2/s)

     !.....Combined Respiration Rates.....
     real(r8) :: resp_auto !autotrophic respiration (mol C/m2/s)
     real(r8) :: resp_grow !growth respiration (mol C/m2/s)
     real(r8) :: resp_leaf !leaf respiration (mol C/m2/s)
     real(r8) :: resp_mntn !maintainence respiration (mol C/m2/s)
     real(r8) :: resp_nveg !non-vegetation respiration (mol C/m2/s)
     real(r8) :: resp_root !root respiration (mol C/m2/s)

     !----------------------
     !Live-To-Dead Transfer
     !.....transfers use fractions of the pool that is transferring
     !.....transfer = fraction * pool_size

     !...leaf transfer (fractions per day)
     real(r8) :: tfl_daylen   !shortening daylength
     real(r8) :: tfl_freeze   !freezing
     real(r8) :: tfl_dry      !water deficiency
     real(r8) :: tfl_pstage   !phenology stage
     real(r8) :: tfl_total    !total leaf transfer

     !.....turnover transfer
     real(r8), dimension(:), allocatable :: &  !(npoolpft)
           tf_turnover !fractions per day

     !...transfer loss information (per soil layer)
     real(r8), dimension(:,:), allocatable :: &  !(npoolpft,nsoil)
          loss_trans_lay  !loss to dead pool transfers (mol C/m2/s)

     !------------
     !Fire Loss
     real(r8) :: nd_fire   !# of days burned
     real(r8) :: resp_fire !fire respiration (mol C/m2/s)
     real(r8) :: rmmd_fire !fire emitted but not removed due to
                           !  fire dataset and SiB4 mismatch (mol C/m2/s)
     real(r8), dimension(:,:), allocatable :: &  !(npoolpft,nsoil)
              loss_fire_lay  !loss from fire (mol C/m2/s)

     !------------
     !Grazing Loss
     real(r8) :: nd_grz !# of days grazed
     real(r8) :: resp_grz !grazing respiration (mol C/m2/s)
     real(r8), dimension(:), allocatable :: &  !(npoolcan)
              loss_grz !loss from grazing (mol C/m2/s)

     !-------------
     !Harvest Loss
     real(r8), dimension(:,:), allocatable :: &  !(npoolpft,nsoil)
         loss_hrvst_lay     !loss from harvest per soil layer (mol C/m2/s)
     real(r8) :: resp_hrvst !C harvest respiration (mol C/m2/s)
     real(r8) :: rmvd_hrvst !C harvested and removed (mol C/m2)


     !-------------------------------------
     !Daily net pool change (per soil layer)
     real(r8), dimension(:,:), allocatable ::  & !(npoolpft,nsoil)
           poolpft_dgain, & !pool gain (mol C/m2/day)
           poolpft_dloss    !pool loss (mol C/m2/day)

     !------------------------
     !Prognostic Carbon Pools
     real(r8), dimension(:), allocatable ::  & !(npoolpft)
          poolpft      !vertically integrated pool size (mol C/m2)
     real(r8), dimension(:,:), allocatable :: &  !(npoolpft,nsoil)
          poolpft_lay  ! prognostic carbon pools (mol C/m2)
     real(r8), dimension(:,:), allocatable :: & !(npoolpft,nsoil)
          poolpft_flay !fraction of carbon per soil layer (-)

     !---------------
     !Carbon Balance
     real(r8), dimension(:), allocatable :: & !(npoolpft)
         poolpftp   !previous carbon pool (mol C/m2)

end type pooll_type


!---------------------------------------------------------------------
! Radiation Variables (CAN, CAS, Soil)
!---------------------------------------------------------------------
type, public :: rad_type

    !...albedos
    real(r8) :: albedo_visb   ! albedo, visible beam (-)
    real(r8) :: albedo_visd   ! albedo, visible diffuse (-)
    real(r8) :: albedo_nirb   ! albedo, nir beam (-)
    real(r8) :: albedo_nird   ! albedo, nir diffuse (-)

     !...radiation variables
    real(r8) :: radfacc(2,2)  ! canopy radiation absorption factors (-)
            !   (1,1) - visible, beam
            !   (1,2) - visible, diffuse
            !   (2,1) - nir, beam
            !   (2,2) - nir, diffuse
    real(r8) :: radfacg(2,2)  ! ground radiation absorption factors (-)
            !   (1,1) - visible, beam
            !   (1,2) - visible, diffuse
            !   (2,1) - nir, beam
            !   (2,2) - nir, diffuse

    real(r8) :: radc3c    ! absorbed radiation by canopy (W/m2)
    real(r8) :: radc3g    ! absorbed radiation by ground (W/m2)
    real(r8) :: radtc     ! canopy net radiation (W/m2)
    real(r8) :: radtg     ! ground net radiation (W/m2)
    real(r8) :: radts     ! snow net radiation (W/m2)
    real(r8) :: effgc     ! effective ground cover for thermal radiation (-)

    !...temperatures
    real(r8) :: tsfc      ! surface temperature (K)

end type rad_type


!-------------------------------------------------
! Fluorescence (SIF) Variables (CAN; CAS; PFT)
!-------------------------------------------------
type, public :: sif_type

     !...electron transports
     real(r8) :: sif_je    !electron transport
     real(r8) :: sif_jo    !max electron transport
     real(r8) :: sif_jejo  !fractional transport (je/jo)

     !...k coefficients, defined as the probability of
     !.....excitons to follow certain pathways (-)
     real(r8) :: sif_kd    !Heat dissipation
     real(r8) :: sif_kn    !Non-photochemical quenching (NPQ)
     real(r8) :: sif_kp    !Photosynthesis

     !...x factor (0 when GPP=potential, 1 when GPP=0)
     real(r8) :: sif_x

     !...yields (-)
     real(r8) :: phi_d  !Heat dissipation yield
     real(r8) :: phi_f  !SIF yield
     real(r8) :: phi_n  !NPQ yield
     real(r8) :: phi_p  !Photosynthetic yield

     !...resulting sif values
     real(r8) :: sif  !fluorescence (W m-2 sr-1 nm-1)

end type sif_type


!---------------------------------------------------------------------
! Soil/Snow Column Variables (Soil)
!---------------------------------------------------------------------
type, public :: sscol_type

     !...prognostic number of snow layers (negative)
     integer(byte) :: nsl

     !...soil diagnostics for soil column (nsoil)
     real(r8), dimension(:), allocatable :: &
         rootr,     & !effective rooting frac for soil hydrology (-)
         satfrac_lay  !fraction of water saturation (-)

     !...snow/soil diagnostic column variables
     real(r8), dimension(:), allocatable :: & !(-nsnow+1:nsoil)
         eff_poros, & ! soil/snow liquid effective porosity (-)
         layer_z,   & ! soil/snow layer interface depth (m)
         node_z,    & ! soil/snow layer node depth (m)
         shcap,     & ! soil/snow total heat capacity (J/m2/K)
         slamda,    & ! soil/snow heat flux term (W/m2/K)
         tksoil,    & ! soil/snow thermal conductivity (W/m/K)
         vol_liq,   & ! soil/snow liquid water volume (kg/m3)
         vol_ice      ! soil/snow ice volume (kg/m3)

     !...snow/soil prognostic column variables
     real(r8), dimension(:), allocatable :: & !(-nsnow+1:nsoil)
         dz, &      ! soil/snow layer thickness (m)
         td, &      ! soil/snow temperature (K)
         www_liq, & ! soil/snow liquid water (kg/m2)
         www_ice    ! soil/snow ice (kg/m2)

end type sscol_type


!-------------------------------------------------
! Vegetation Description and State Variables (PFT)
!-------------------------------------------------
type, public :: veg_type

     !...land-atmos interactions
     real(r8) :: z0       ! canopy snow-adjusted roughness length (m)
     real(r8) :: z0d      ! canopy roughness length (m)
     real(r8) :: zp_dispd ! zero-plane displacement (m)
     real(r8) :: zpd_adj  ! snow-adjusted zero-plane displacement (m)
     real(r8) :: zztemp   ! temperature height for mass flux (m)
     real(r8) :: zzwind   ! wind height for mass flux (m)

     !...resistances
     real(r8) :: cc1      ! bulk pbl resistance coefficient (sqrt(s/m))
     real(r8) :: cc2      ! ground to canopy air space resistance (-)

     !...root profile
     real(r8), dimension(:), allocatable :: &  !(nsoil)
          rootf  ! root fraction (-)

     !...vegetation state
     real(r8) :: fpar     ! absorbed fraction of PAR (-)
     real(r8) :: green    ! green fraction of LAI (-)
     real(r8) :: lai      ! leaf area index (-)
     real(r8) :: lait     ! canopy total leaf area index (w/ dead, -)
     real(r8) :: vcover   ! fraction of vegetation cover (-)

     !...vegetation properties
     real(r8) :: gmudmu   ! time-mean leaf projection (-)
     real(r8) :: park     ! solar absorption factor /
                          !      extinction coefficient for PAR (-)
     real(r8) :: vmax     ! rubisco velocity (mol/m2/s)

     !...climatological vegetation states
     real(r8) :: clim_lai  ! climatological LAI (-)

end type veg_type


!=================================================
! Driver Data Variables
!------------------------------------------------------------------
! Grid Cell Diagnostic Variables
! -----------------------------------------------------------------
type, public :: gdiag_type

     !...daytime/sunlight properties
     real(r8) :: cosz     ! cosine of solar zenith angle (-)
     real(r8) :: daylen   ! length of daylight (hrs)
     real(r8) :: daylendt ! change in length of day (hrs)

     !...misc driver forcings
     real(r8) :: tmdf   ! daily (24-hr running mean) temperature (F)
     real(r8) :: thm    ! mixed layer potential temperature (K)
     real(r8) :: bps(2) ! (ps/1000)**kapa - turns theta into temp
     real(r8) :: em     ! mixed layer water vapor pressure (hPa or mb)
     real(r8) :: ros    ! surface air density (kg/m3)
     real(r8) :: psy    ! psycrometric constant (gamma) (hPa/K)

    !...precipitation properties
    real(r8) :: seas_precippot ! seasonal precipitation potential (-)

    !...radiation properties
    real(r8) :: radvbc    ! visible beam radiation (W/m2)
    real(r8) :: radvdc    ! visible diffuse radiation (W/m2)
    real(r8) :: radnbc    ! nir beam radiation (W/m2)
    real(r8) :: radndc    ! nir diffuse radiation (W/m2)

    real(r8) :: toa_solar   ! Top-of-Atmosphere insolation (W/m2)
    real(r8) :: toa_radvbc  ! TOA visible beam radiation (W/m2)
    real(r8) :: toa_radvdc  ! TOA visible diffuse radiation (W/m2)
    real(r8) :: toa_radnbc  ! TOA near-infrared (NIR) beam radiation (W/m2)
    real(r8) :: toa_radndc  ! TOA NIR diffuse radiation (W/m2)

    real(r8) :: toa_par   ! TOA PAR (mol/m2/s)
    real(r8) :: aod       ! aerosol + cloud optical depth (-)

    !...solar-induced fluorescence (SIF) properties
    real(r8) :: sif_atten ! SIF attenuation factor (-)
    logical, dimension(2) :: sif_flag  !conditions suitable for
                                       !1=GOME2 2=OCO2?

    !...spinup variables
    logical :: gridcell_spunup

end type gdiag_type

!------------------------------------------------------------------
! Grid Cell Prognostic Variables
! -----------------------------------------------------------------
type, public :: gprog_type

    !...prognostic driver data/forcings
    real(r8) :: cupr      ! cumulus precipitation rate (mm/s)
    real(r8) :: cuprt     ! cumulus precip rate (m/s)
    real(r8) :: cupr1     ! cumulus precipitation rate (mm/s)
    real(r8) :: cupr2     ! cumulus precipitation rate (mm/s)
    real(r8) :: dlwbot    ! surface incident longwave
    real(r8) :: dlwbot1   ! surface incident longwave
    real(r8) :: dlwbot2   ! surface incident longwave
    real(r8) :: lspr      ! stratiform precipitation rate (mm/s)
    real(r8) :: lsprt     ! stratiform precip rate (m/s)
    real(r8) :: lspr1     ! stratiform precipitation rate (mm/s)
    real(r8) :: lspr2     ! stratiform precipitation rate (mm/s)
    real(r8) :: ps        ! surface pressure (hPa or mb)
    real(r8) :: ps1       ! surface pressure (hPa or mb)
    real(r8) :: ps2       ! surface pressure (hPa or mb)
    real(r8) :: sh        ! mixed layer water vapor mixing ratio (kg/kg)
    real(r8) :: sh1       ! mixed layer water vapor mixing ratio (kg/kg)
    real(r8) :: sh2       ! mixed layer water vapor mixing ratio (kg/kg)
    real(r8) :: spdm      ! wind speed (m/s)
    real(r8) :: spdm1     ! wind speed (m/s)
    real(r8) :: spdm2     ! wind speed (m/s)
    real(r8) :: sw_dwn    ! surface incident shortwave radiation (W/m2)
    real(r8) :: sw_dwn1   ! surface incident shortwave radiation (W/m2)
    real(r8) :: sw_dwn2   ! surface incident shortwave radiation (W/m2)
    real(r8) :: tm        ! mixed layer temperature (K)
    real(r8) :: tm1       ! mixed layer temperature (K)
    real(r8) :: tm2       ! mixed layer temperature (K)

    !...fire emissions
    real(r8) :: firec     ! C loss from fire (mol C/m2/s)
    real(r8) :: firec1    ! C loss from fire (mol C/m2/s)
    real(r8) :: firec2    ! C loss from fire (mol C/m2/s)
    real(r8) :: fireco2   ! CO2 respiration from fire (mol C/m2/s)
    real(r8) :: fireco21  ! CO2 respiration from fire (mol C/m2/s)
    real(r8) :: fireco22  ! CO2 respiration from fire (mol C/m2/s)

    !...carbon cycle
    real(r8) :: pco2m     ! Mixed Layer (background) CO2 partial pressure (Pa)
    real(r8) :: pcosm     ! Mixed Layer (background) COS partial pressure (Pa)

    !...daily values
    real(r8) :: tmd    ! daily (24-hr running mean) temperature (K)

    !...seasonal values
    real(r8) :: seas_precip !seasonal precipitation (mm/day)
    real(r8) :: seas_tm     !seasonal temperature (K)

    !...climatological values
    real(r8) :: clim_cupr   ! clim-mean convective precipitation (mm/day)
    real(r8) :: clim_precip ! clim-mean precipitation (mm/day)
    real(r8) :: clim_tm     ! clim-mean temperature (K)

    !...tm5 COS values
    real(r8) :: cosm_tm5      ! COS mixing ratio (molCOS/molAir)
    real(r8) :: cosm_tm51     ! COS mixing ratio (molCOS/molAir)
    real(r8) :: cosm_tm52     ! COS mixing ratio (molCOS/molAir)

end type gprog_type


!******************************************************************
!------------------------------------------------------------------
! Begin definition of spatial scaling hierarchy
!------------------------------------------------------------------

!------------
! define the land unit structure
! includes corresponding:
!    - soil column (Soil)
!    - vegetation (PFT)
!    - canopy (CAN) and canopy air space (CAS)
!------------
type, public :: lu_type

    ! vegetation information
    integer(i4) :: ipft   !pft reference number
    real(r4)    :: larea  !fraction of coverage per gridcell (0-1)

    ! time-invariant variables
    type(soil_type) :: soilt   !soil properties

    ! time-variant variables
    type(cas_type)     :: cast      !canopy air space variables (CAS)
    type(co2_type)     :: co2t      !photosynthetic/CO2 variables
    type(cos_type)     :: cost      !carbonyl sulfide variables
    type(equibd_type)  :: equibdt   !dead pool equilibrium variables (Soil)
    type(equibl_type)  :: equiblt   !live pool equilibrium variables (PFT)
    type(flux_type)    :: fluxt     !flux variables
    type(hydros_type)  :: hydrost   !soil hydrological variables (Soil)
    type(hydrov_type)  :: hydrovt   !veg hydrological variables (PFT)
    type(phen_type)    :: phent     !phenology variables (PFT)
    type(poold_type)   :: pooldt    !dead pool variables (Soil)
    type(pooll_type)   :: poollt    !live pool variables (PFT)
    type(rad_type)     :: radt      !radiation variables
    type(sif_type)     :: sift      !fluorescence variables
    type(sscol_type)   :: sscolt    !soil/snow column variables (Soil)
    type(veg_type)     :: vegt      !vegetation information (PFT)

end type lu_type

!------------
! define the gridcell structure
!------------
type, public :: gridcell_type

    ! gridcell information
    real(r8) :: lat         !latitude (degrees)
    real(r8) :: lon         !longitude (degrees)

    ! variables defined at the gridcell level
    type(gdiag_type) :: gdiagt !diagnostic variables
    type(gprog_type) :: gprogt !prognostic variables

    ! gridcell -> landunit hierarchy
    integer(i4) :: g_nlu !number of land units per gridcell
                         !...includes corresponding
                         !....soil, veg (PFT), and canopy

    type(lu_type), dimension(:), allocatable :: &
          l  !land unit data structure

end type gridcell_type

!-----------
! define the top-level structure
!-----------
type, public :: sib_t
   type(gridcell_type),  dimension(:), allocatable :: &
          g  !gridcell data structure
end type sib_t

!------------------------------------------------------------------
! End definition of spatial scaling hierarchy
!------------------------------------------------------------------
!******************************************************************

!***********************************************************************
!-----------------------------------------------------------------------
! Declare single instance of sibtype
    type(sib_t) :: sib
!-----------------------------------------------------------------------

end module module_sib

"""
