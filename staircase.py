def staircase(n, k, memo={}):
    if n == 0:
        return 1
    elif (n,k) in memo:
        return memo[(n,k)]
    
    total = 0
    for step in range(1, k+1):
        temp = staircase(n - step, k, memo)
        memo[(n-step,k)] = temp
        total += temp
    
    return total

staircase(3, 2)

# this does not work