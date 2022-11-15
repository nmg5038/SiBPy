
#----------------------------------------------------------------------
#
#   SiB4 Vegetation Structure Module
#
#----------------------------------------------------------------------


class Sib_vs_vars():

    def __init__(self):
        # ------------------------------------------------------------------
        # SiB4 Vegetation Information
        # ------------------------------------------------------------------
        self.gnlu = None  # Number of land units (lu)
        # per grid cell

        # Land Units consist of consistent
        #  soil column (Soil), vegetation (PFT),
        #  canopy (Can), and canopy air space (CAS)

        self.larea = None  # Fractional coverage of each land unit (nlu)

        self.pftref = None  # PFT reference for each lvc unit (nlvc, integer)

        self.sandfrac = None  # (nlu, real)
        self.clayfrac = None  # (nlu, real)
        self.soref_vis = None  # (nlu, real)
        self.soref_nir = None  # (nlu, real)

if __name__ == '__main__':
    test_module = Sib_vs_vars()