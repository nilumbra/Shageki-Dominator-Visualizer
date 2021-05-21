'''
    Given H = [h1, ... , hn], (original height of the balloons)
          S = [s1, ... , sn], (the rising speed(per sec) of i-th baloon)

    You can shoot only one baloon every second. 
    Suppose you shoot a baloon in i-th second
    Penalty P = max({h+i*s|for (h, s) in zip(H,S) with corresponding index. 
                          i ranges from 0 to N-1})

    SOLVE: Minimize P
'''


# H = [1, -1, 3, -4, 8]
# S = [2, 3,  1,  6, 5]
H = [1, 2, 3, 4, 5]
S = [5, 4, 3, 2, 1]

N = len(H)

fheight = [h + N*s for (h, s) in zip(H, S)]
ub = max(fheight) # Highest possible final height = max penalty



left, right = 0, ub
mheight = {}

while right - left > 1:
    mid = (left + right)/2 

#*************************************************************************************
    # condition P
    ok = True
    t = [-1] * N # list to keep time limits that balloons need to be shot
    for i in range(N):
        if(mid < H[i]):
            ok = False # the penalty value is too low. Should simply set left = mid and continue to the next iteration
        else:
            t[i] = (mid - H[i]) / S[i] # calculate the time limit for i-th balloon
            mheight[i] = t[i] 
    
    # Output visualization purpuse
    t.sort()
    mheight = {k: v for k, v in sorted(mheight.items(), key=lambda item: item[1])}

    for i in range(N):
        if t[i] < i:
            ok = False
#*************************************************************************************

    if(ok):
        right = mid
    else:
        left = mid

# print(mheight)

opt_height = []
for item in mheight.items():
    opt_height.append(H[item[0]] + item[1]*S[item[0]])

print("Theoretical final heights: " + ','.join([str(s) for s in fheight]))
print("The lowest penalty is: %d" %(right))
print("Optimzed final heights: " + ','.join([str(i) for i in opt_height]))






