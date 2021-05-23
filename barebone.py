# -*- coding: utf-8 -*-
'''
    Given H = [h1, ... , hn], (original height of the balloons)
          S = [s1, ... , sn], (the rising speed(per sec) of i-th baloon)

    You can shoot only one baloon every second. 
    Suppose you shoot a baloon in i-th second
    Penalty P = max({h+i*s|for (h, s) in zip(H,S) with corresponding index. 
                          i ranges from 0 to N-1})

    SOLVE: Minimize P
'''
import bisect as bi

# いわゆる判定条件
def P(height, rspeed, mid, mheight):
    t = [-1] * N # list to keep time limits that balloons need to be shot

    H_temp = sorted(height)

    # 当たり前のチェック problem.isStartingHeightAboveMid(H, mid, trace)
    # "status": "isAboveOriginalHeight"
    # the penalty value is too low. Should simply set left = mid and continue to the next iteration
    if(bi.bisect(H_temp, mid) < N): return mheight, False
    for i in range(N):
        # calculate the time limit for i-th balloon 
        # 時間がさし迫った順に割っていくべし
        # t[i] represents the time limit you have to shoot the balloon.
        t[i] = int((mid - height[i]) / rspeed[i])
        mheight[i] = t[i] 
    
    # problem.isStartingHeightAboveMid(H, mid, trace)
    # Output visualization purpose
    t.sort()
    mheight = {k: v for k, v in sorted(mheight.items(), key=lambda item: item[1])}

    # すべての風船を割れればok
    # Want to know if all balloons can be shot within penalty height.
    # "status": "isKaboomedBelowMid",
    for i in range(N):
        if t[i] < i: #t = [0,2,2,3]
            # If not, record in trace which balloon violates the height limit
            return mheight, False

    return mheight, True

# H = [1, -1, 3, -4, 8]
# S = [2, 3,  1,  6, 5]
H = [1, 2, 3, 4, 5]
S = [5, 4, 3, 2, 1]

N = len(H)

fheight = [h + N*s for (h, s) in zip(H, S)]

# Highest possible final height = max penalty
ub = max(fheight) # status: "calculatingUpperbound"
lb = min(feight) 

left, right = lb, ub # status: "settingRight" 
mheight = {}  

while right - left > 1:
    mid = (left + right)/2 # "status": "calculatingMid"
    mheight, ok = P(H, S, mid, mheight)

    # "status": "updateBound"
    if(ok):
        right = mid
    else:
        left = mid

# End of binary search. => "status": "answerFound"

# Calculating final height for each balloon in the original input order 
opt_height = []
for item in mheight.items():
    opt_height.append(H[item[0]] + item[0]*S[item[0]])

print("Theoretical final heights: " + ','.join([str(s) for s in fheight]))
print("The lowest possible penalty is: %d" %(right))
print("Optimzed final heights: " + ','.join([str(i) for i in opt_height]))
print(mheight)






