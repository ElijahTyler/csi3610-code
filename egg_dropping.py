def egg(n='floors', k='eggs', memo={}):
    if k == 1:
        return n
    if (n,k) in memo:
        return memo[(n,k)]
    
    ret = n
    for x in range(1, n+1):
        drops = 1 + max(egg(x-1, k-1, memo), egg(n-x, k, memo))
        ret = min(ret, drops)
    memo[(n,k)] = ret
    return memo[(n,k)]

paul = egg(100, 2)
print(paul)