# -*- coding: utf-8 -*-
import shagekiou
import trace

################################################################################
################################## 射撃王　algorithm ##################################
################################################################################

#*****************************射撃王御用*****************************
def algorithm1(problem, trace = None):
    # find the upperbound and lowerbound
    ub, lb = problem.maxPenalty(trace), 0

    #setting left bound and right bound
    left, right = lb, ub
    if not trace is None:
        trace.settingLeft(left)
        trace.settingRight(right)

    while right - left > 1:
        mid = int((left + right)/2) # "status": "calculatingMid"
        if not trace is None:
            trace.calculatingMid(mid)
            trace.drawMid()

        ok = problem.P(mid, trace)

        if(ok):
            right = mid
            if not trace is None: trace.settingRight(right)
        else:
            left = mid
            if not trace is None: trace.settingLeft(left)
  

    if not trace is None: trace.answerFound()
#*****************************射撃王御用*****************************

################################################################################
################################ Helper Methods ################################
################################################################################
