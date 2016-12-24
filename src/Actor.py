import params as p
import aux_actors as aa

class Actor:
    """ 
    """

    def __init__(self, new_id, position, wealth=None, power=None):
        """
        """

        """ int: 
            For uniquely identifying actors """
        self._id = new_id
        """ Position: 
            The location of the Cell within the toroidal world. """
        self._position = position
        """ """
        self.new_actor(wealth, power)

    def new_actor(self, wealth, power):
        """ 
        """
        if wealth is None and power is None:
            def_wealth = p.params['default_wealth']
            def_power = p.params['default_power']
            def_wealth_var = p.params['wealth_variance']
            def_power_var = p.params['power_variance']

            dist_type = p.params['dist_func']
            if dist_type is "uniform":
                self._wealth = \
                        aa.get_w_uniform_dist(def_wealth, def_wealth_var)
                self._power = \
                        aa.get_w_uniform_dist(def_power, def_power_var)
            elif dist_type is "gaussian":
                self._wealth = \
                        aa.get_w_normal_dist(def_wealth, def_wealth_var)
                self._power = \
                        aa.get_w_normal_dist(def_power, def_power_var)
            else: # get normal distribution
                print("not implemented.")
        else:
            """ int: 
                To measure the success of an actor """
            self._wealth = wealth
            """ int: 
                To measure the combat power of an actor. """
            self._power = power

