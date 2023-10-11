import time

def cringe_rod_cutting(n, vals): # returns the max value, not how to cut the rod
    ret = 0
    for (L, V) in vals: # you suck
        if n >= L:
            ret = max(ret, V + cringe_rod_cutting(n-L, vals)) # slow
    return ret # i hate you

def rod_cutting(n, vals, memo={0: 0}): #yeah wooooo lets go memoization
    if n in memo:
        return memo[n] # very cool
    ret = 0
    for (L, V) in vals:
        if n >= L:
            ret = max(ret, V + rod_cutting(n-L, vals, memo))
    memo[n] = ret # awesome
    return ret

n = 90
vals = [(4,5), (6,8), (9,12)]

start_time = time.time()
paul = rod_cutting(n, vals)
print(paul)
total_time = time.time() - start_time
print(total_time)