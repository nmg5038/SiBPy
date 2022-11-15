
class Sib_time():
    def __init__(self):
        # specified times from namel_sibdrv
        self.starttime = None # day of year to start simulation
        self.startyear = None # year to start simulation
        self.endtime = None # day of year to end simulation
        self.endyear = None # year to end simulation

        self.dtsib = None  # # seconds in simulation time step
        self.dtisib = None  # inverse model timestep (1/s)
        self.steps_per_day = None  # number of time steps per day

        # time constants
        self.init_year = None  # initial year of simulation
        self.init_month = None  # initial month of simulation
        self.init_day = None  # initial day of month of simulation
        self.init_doy = None  # initial day of year of simulation
        self.init_second = None  # initial second of simulation

        self.start_year = None  # year of restart file
        self.start_month = None  # month of restart file
        self.start_day = None  # day of month of restart file
        self.start_doy = None  # day of year of restart file
        self.start_second = None  # second of restart file

        self.end_year = None  # last year of simulation
        self.end_doy = None  # last day of year of simulation
        self.end_second = None  # last second of simulation
        self.end_dtime = None  # last timestep of simulation,
        #    in fractional year

        self.total_years = None  # total number of years in simulation
        self.total_months = None  # total number of months in simulation
        self.total_days = None  # total number of days in simulation

        # time variables
        self.year = None  # current year in the simulation
        self.month = None  # current month in the simulation
        self.hour = None  # current hour of day in the simulation
        self.day = None  # current day of the current month
        self.doy = None  # current day of current year
        self.sec_day = None  # current second in the current day
        self.sec_month = None  # current second in the current month
        self.sec_year = None  # current second in the current year
        self.sec_tot = None  # current second in the whole simulation

        self.nyear = None  # year of next month of simulation
        self.nmonth = None  # next month of simulation
        self.nday = None  # next day of simulation

        self.curday_per_year = None  # number of days in current year
        self.curday_per_year_day_delay = None  # number of days in year,
        #    switched on January 2nd
        self.curday_per_mon = None  # number of days in current month
        self.curday_per_mon_day_ahead = None  # number of days in month,
        #   switched on last day
        #   of previous month
        self.cureqnx = None  # day of vernal equinox in current year

        # Flags
        self.new_day = False  # new day ?
        self.new_month = False  # new month ?
        self.new_month_day_delay = False  # second day of month?
        self.new_year = False  # new year ?

        # Local Time Information (subcount)
        self.dayfrac_lst = None  # fraction of day in local time (real)
        self.new_day_lst = None  # new day in local time? (boolean

        # Day Length Information
        self.daylenmax = None  # (real, subcount)

        # Weights
        self.wt_clim = None  # time-step weight for climatological running-mean
        self.wt_daily = None  # time-step weight for daily running-mean
        self.wt_seas = None  # time-step weight for seasonal running-mean
        self.wt_seas_precip = None  # time-step weight for precip seas mean

        self.wtd_clim = None  # daily weight for climatological running-mean
        self.wtd_seas = None  # daily weight for seasonal running-mean

if __name__ == '__main__':
    test_module = Sib_time()