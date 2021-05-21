import trace

################################################################################
########################### Class for 射撃王　Problem ############################
################################################################################

class ShagekiouProblem(object):
    """
    A class representing an instance of a peak-finding problem.
    """

    
    def __init__(self, height, rising_speed):
        """
        A method for initializing an instance of the ShagekiouProblem class.
        Takes two arrays H and S indicating balloons' starting height and their rising speed. Restrict to positive integers. 

        RUNTIME: O(1)
        """
        self.height = height
        self.rising_speed = rising_speed


    # Calculate a starting upper bound for binary-search 
    def maxPenalty(self, trace = None):
        n = len(self.height)
        max_P = max([h + n*s for (h, s) in zip(self.height, self.rising_speed)])

        if not trace is None: trace.maxPenalty(max_P)

    # Pivot condition check for each binary-search iteration
    def isShootable(self, trace = None):
        if not trace is None: trace.isShootable()
    
    def ____?(self, trace = None):
    
        if not trace is None: trace.____?()
        

################################################################################
################################ Helper Methods ################################
################################################################################

def createProblem(array):
    """
    Constructs an instance of the PeakProblem object for the given array,
    using bounds derived from the array using the getDimensions function.
   
    RUNTIME: O(len(array))
    """

    (rows, cols) = getDimensions(array)
    return PeakProblem(array, (0, 0, rows, cols))
