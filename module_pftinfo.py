# ----------------------------------------------------------------------
#
#   SiB4 PFT Informational Module
#
# ----------------------------------------------------------------------

# ...Parameters
alen = 8  # Abreviated type/group name lengths
clen = 3  # PFT name length
llen = 40  # Long name lengths
plen = 20  # Phenology method/stage name lengths

# ...Map information (strings)
pft_source = None  # PFT Reference (size = llen)
crop_source = None  # Crop Reference (size = llen)
soil_source = None  # Soil Type Reference (size = llen)
soref_source = None  # Soil Reflectance Reference (size = llen)

# ...Type Information (bare, evg, decid, grass, crop)
type_name_long = None  # Full type name (size = ?, len = llen)
type_name = None  # Abbreviated type name (size = ?, len = alen)

# ......type references (integer)
type_bare = None  # Type number for bare ground
type_evg = None  # Type number for evergreen
type_decid = None  # Type number for deciduous
type_grass = None  # Type number for grass
type_crop = None  # Type number for crops

# ...Group Information (bare, ndlfor, bdlfor, shrub, grass, crop)
group_name_long = None  # Full type name (size = ?, len = llen)
group_name = None  # Abbreviated type name (size = ?, len = alen)

# ......group references
group_bare = None  # Group number for bare ground
group_ndlfor = None  # Group number for needle forests
group_bdlfor = None  # Group number for broadleaf forests
group_shrub = None  # Group number for shrub
group_grass = None  # Group number for grass
group_crop = None  # Group number for crop

# ...Phenology Method (non-veg, stage-based, gdd-based)
pmeth_name = None  # Method name (size = ?, len = plen)

# .....method references
pmeth_nvg = None  # Method # for non-vegetation
pmeth_stg = None  # Method # for stage-based phenology
pmeth_gdd = None  # Method # for gdd-based phenology

# ...PFT Information
pft_name = None  # PFT names (size = ?, len = clen)
pft_name_long = None  # (size = ?, len = llen)
pft_ref = None  # PFT reference numbers (integer, size = ?)
pft_num = None  # PFT sequential numbers (no skips) (integer, size = ?)
pft_type = None  # PFT types (1-5) (integer, size = ?)
pft_group = None  # PFT group (integer, size = ?)
pft_pmeth = None  # PFT phenology method (integer, size = ?)

# ......PFT type counts (integers)
type_nbare = None  # Number of bare ground PFTs
type_nevg = None  # Number of evergreen PFTs
type_ndecid = None  # Number of deciduous PFTs
type_ngrass = None  # Number of grass PFTs
type_ncrop = None  # Number of crop PFTs

# ......PFT group counts (integers)
group_nbare = None  # Number of bare PFTs
group_nndlfor = None  # Number of needle forest PFTs
group_nbdlfor = None  # Number of broadleaf forest PFTs
group_nshb = None  # Number of shrub PFTs
group_ngrass = None  # Number of grass PFTs
group_ncrop = None  # Number of crop PFTs

# .....PFT phenology method counts and indices
npft_nvg = None  # Number of non-veg PFTs
npft_stg = None  # Number of stage-based PFTs
npft_gdd = None  # Number of gdd-based PFTs

nvgindx_pftref = None  # nvg index number for PFT references (integer, size = max PFT ref)
gddindx_pftref = None  # gdd index number for PFT references (integer, size = max PFT ref)
stgindx_pftref = None  # stg index number for PFT references (integer, size = max PFT ref)

pftnum_nvgindx = None  # PFT numbers for non-veg PFTs (integer, size = npft_nvg)
pftnum_gddindx = None  # PFT numbers for gdd-based PFTs (integer, size = npft_gdd)
pftnum_stgindx = None  # PFT numbers for stage-based PFTs (integer, size = npft_stg)

# .....PFT Numbers
pft_dbg = None  # PFT number for desert and bare ground
pft_enf = None  # PFT number for temperate evergreen needleleaf forest
pft_dnf = None  # PFT number for boreal deciduous needleleaf forest
pft_ebf = None  # PFT number for tropical evergreen broadleaf forest
pft_dbf = None  # PFT number for tropical deciduous broadleaf forest

pft_shb = None  # PFT number for shrubs (non-tundra)
pft_sha = None  # PFT number for tundra shrubs
pft_c3a = None  # PFT number for tundra grasslands
pft_c3g = None  # PFT number for C3 grasslands (non-tundra)
pft_c4g = None  # PFT number for C4 grasslands

pft_c3c = None  # PFT number for C3 crops (generic)
pft_c4c = None  # PFT number for C4 crops (generic)
pft_mze = None  # PFT number for maize
pft_soy = None  # PFT number for soybeans
pft_wwt = None  # PFT number for winter wheat
