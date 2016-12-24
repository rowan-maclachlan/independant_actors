"""
This module serves as a repository for
simulation parameters.  Dictionary values can 
be overwritten for any particular simulation run
to enable changing parameter values all across
the simulation.  Otherwise, changing parameter values
would require navigating to any number of other files.
"""

import random

""""""
params = dict()

""""""
params['seed'] = 1

""""""
params['width'] = 4
""""""
params['height'] = 4

""""""
params['default_wealth'] = 500
""""""
params['default_power'] = 200

""""""
params['wealth_variance'] = 50
""""""
params['power_variance'] = 50

""""""
params['actors_per_iter'] = 3
""""""
params['iterations'] = 10
""""""
params['dist_func'] = "uniform"
