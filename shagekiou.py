import trace
import bisect as bi
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

    # Invariant
    def P(self, mid, trace = None):
        t = [] # list to keep time limits that balloons need to be shot

        H_temp = sorted(self
            .height)
        N = len(self.height)

        # 当たり前のチェック problem.isStartingHeightAboveMid(H, mid, trace)
        # "status": "isAboveOriginalHeight"
        # the penalty value is too low. Should simply set left = mid and continue to the next iteration
        if(bi.bisect(H_temp, mid) < N): 
            if not trace is None: trace.isAboveOriginalHeight(False)
            return False

        if not trace is None: trace.isAboveOriginalHeight(True)

        for i in range(N):
            # calculate the time limit for i-th balloon 
            # 時間がさし迫った順に割っていくべし
            # t[i] represents the time limit you have to shoot the balloon.
            t.append([i,(mid-self.height[i])/self.rising_speed[i]]) 
        
        # problem.isStartingHeightAboveMid(H, mid, trace)
        # Output visualization purpose
        t.sort(key=lambda tup:tup[1])

        # すべての風船を割れればok
        # Want to know if all balloons can be shot within penalty height.
        # "status": "isKaboomedBelowMid",
        for i in range(N):
            if not trace is None: trace.ballonFloat([h+i*s for (h, s) in zip(self.height, self.rising_speed)])
            if t[i][1] < i: #t = [0,2,2,3]
                # If not, record in trace which balloon violates the height limit
                if not trace is None: trace.isKaboomedBelowMid(t[i][0], False)
                return False
            else:
                if not trace is None: trace.isKaboomedBelowMid(t[i][0], True)
        return True



    # Calculate a starting upper bound for binary-search 
    def maxPenalty(self, trace = None):
        n = len(self.height)
        # find max penalty
        max_P = max([h + n*s for (h, s) in zip(self.height, self.rising_speed)])
        if not trace is None: trace.calculatingUpperbound(max_P)

        return max_P


################################################################################
################################ Helper Methods ################################
################################################################################

def createProblem(array):
    """
    Constructs an instance of the ShagekiouProblem object for the given array,
    using bounds derived from the array using the getDimensions function.
   
    RUNTIME: O(1)
    """

    # array = [[h1,h2...], [s1,s2...]]
    return ShagekiouProblem(array[0], array[1])
