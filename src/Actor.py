import Gene
import params as p

class Actor:
    """ 
    """

    def __init__(self, new_id, position, wealth):
        """
        """
        """ int: For uniquely identifying cells """
        self._id = new_id
        """ int: To measure the success of a gene """
        self._wealth = wealth
        """ Position: The location of the Cell within the toroidal world. """
        self._position = position
        

