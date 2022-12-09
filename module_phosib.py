# ----------------------------------------------------------------------
#   SiB4 Photosynthesis Variables
# ----------------------------------------------------------------------


# ...Parameters
numic = 6
minrad = 1.e-6
minassim = 1.e-7
minassimdiff = 10.e-6

toatosfc = 0.8
ctoco2 = 44. / 12.
convertppm = 1.e6
convertphoton = 0.219

# ...Parameters - Base values for Q10 relationship
vmax_q10 = 2.1  # VMax temperature sensitivity
vmax_tref = 298.  # VMax reference temperature
oms_q10 = 1.8  # Export-limited assimilation

# ...Parameters - Damping Variables
zln2 = 6.9314718e-1
ghalf = 1.0257068e1
dttin = 3.6e3
dmin = 6.0e1

# ...Parameters - Limits
co2_casd_min = 4.0  # CAS depth minimum for CO2 (m)
rst_max = 5.E6  # Max stomatal resistance (s/m)

rhfac_astart = 0.6  # Humidity stress curvature start (-)
rhfac_exp = 2.2  # Humidity stress curvature (-)
rhfac_exp_crop = 0.7  # Humidity stress crop exponent (-)
rhfac_nforest = 0.7  # Humidity stress min for needle forests (-)
rhfac_tundra = 0.6  # Humidity stress min for tundra (-)

# ===============================================================================
# ...Assimilation-Limiting Variables
assim_omc = None  # rubisco-limited assimilation (mol C/m2/s)
assim_ome = None  # light-limited assimilation (mol C/m2/s)
assim_oms = None  # sink-limited assimilation (mol C/m2/s)
assimpot_omc = None  # potential rubisco-unlimited assimilation (mol C/m2/s)
assimpot_ome = None  # potential light-unlimited assimilation (mol C/m2/s)
assimpot_oms = None  # potential sink-unlimited assimilation (mol C/m2/s)
assimfac = None  # assimilation rate stress factors (-, size = 4)
# (1) rubisco-limited stress
# (2) light-limited stress
# (3) sink-limited stress
# (4) product of factors 1-3

assimdiff = None  # diff btwn actual & potential assim (mol/m2/s)
rrkk = None  # export-limited rate portion
omss = None  # export-limited rate portion

# ...Assimilation/Ball-Berry Variables
bintc = None  # Minimal assimilation (y-intercept of Ball-Berry; mol/m2/s)
range = None  # Adjusted/First Guess choloroplast CO2 (Pa)
assimn = None  # Net leaf assimilation (mol/m2/s)
eyy = None  # Iterated difference between pco2 estimates (Pa,size = numic)
pco2y = None  # Iterated chloroplast CO2 (Pa,size = numic)
assimc = None  # Iterated rubisco-limited assimilation (mol/m2/s,size = numic)
assime = None  # Iterated light-limited assimilation (mol/m2/s,size = numic)
assims = None  # Iterated sink-limited assimilation (mol/m2/s,size = numic)
assimy = None  # Iterated assimilation (mol/m2/s,size = numic)

# ...Atmospheric Variables
co2cap = None  # air capacity for CO2 exchange (mol air/m2)
pressure = None  # surface pressure (mb)

# ...Conductance Variables
gxco2 = None  # Canopy biophysical-maximum conductance (mol/m2/s)
gah2o = None  # CAS-Mixed Layer conductance (mol/m2/s)
gbh2o = None  # Leaf-CAS conductance (mol/m2/s)
gsh2o = None  # Canopy conductance (mol/m2/s)
gsh2onew = None  # Updated canopy conductance (mol/m2/s)
drst = None  # Delta of stomatal resistance (s/m)

# ...CO2 Concentrations
co2cas = None  # CAS CO2 concentration (mol C/mol air)
co2m = None  # reference level CO2 concentration (mol C/mol air)
co2s = None  # leaf surface CO2 concentration (mol C/mol air)

pco2cas = None  # CAS CO2 concentration (Pa)
pco2s = None  # leaf surface CO2 partial pressure (Pa)
pco2i = None  # leaf internal (stomatal) CO2 partial pressure (Pa)
pco2c = None  # leaf chloroplast CO2 partial pressure (Pa)

# ...Damping Factors
pdamp = None
qdamp = None
tprcor = None  # Temperature correction (K)

# ...Leaf Parameters
qt = None  # Temperature Q10 factor (-)
vmaxts = None  # VMax temperature-scaled (mol/m2/s)
zkc = None  # Michaelis-Menten coefficient for CO2 (Pa)
zko = None  # Inhibition coefficient for O2 (Pa)
spfy = None  # CO2/O2 specificity (-)

# ...Potential Photosynthesis Variables
assimnp = None  # Top leaf assimilation (mol C/m2/s)
antemp = None  # Bottom stopped assimimlation (mol C/m2/s)
pco2ipot = None  # Potential intercellular CO2 (Pa)
omcpot = None  # Potential rubisco limitation (mol C/m2/s)
omepot = None  # Potential light limitation (mol C/m2/s)
omspot = None  # Potential sink or pep limitation (mol C/m2/s)

sqrtin = None  # Intermediate potential (mol C/m2/s)
omppot = None  # Intermediate top leaf photosynthesis (mol C/m2/s)

# ...Radiation and Canopy Scaling Factors
pfd = None  # Photon flux (mol/m2/s)
scatc = None  # scattering coefficient (-)
toa_pfd = None  # Top-of-Atmosphere (TOA) photon flux (mol/m2/s)
toa_apar = None  # Absorbed TOA PAR (mol/m2/s)

# ...Respiration Rates
resp_cas = None  # total respiration, auto + heterotrophic (mol C/m2/s)

# ...Vegetation Info
c3 = None
c4 = None
atheta = None
btheta = None
