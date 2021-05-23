import shagekiou
import trace

################################################################################
################################## 射撃王　algorithm ##################################
################################################################################

#*****************************射撃王御用*****************************
def algorithm1(problem, trace = None):

    # find the maximum in the dividing column
    bestLoc = problem.getMaximum(divider, trace)

    # see if the maximum value we found on the dividing line has a better
    # neighbor (which cannot be on the dividing line, because we know that
    # this location is the best on the dividing line)
    neighbor = problem.getBetterNeighbor(bestLoc, trace)

    # this is a peak, so return it
    if neighbor == bestLoc:
        if not trace is None: trace.foundPeak(bestLoc)
        return bestLoc
  
    if not trace is None: trace.setProblemDimensions(sub)
    result = algorithm1(sub, trace)
    return problem.getLocationInSelf(sub, result)
#*****************************射撃王御用*****************************

################################################################################
################################ Helper Methods ################################
################################################################################


