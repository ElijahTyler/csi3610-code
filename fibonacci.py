def fib(n):
    memo = [0,1]
    for i in range(n-1):
        memo.append(False)
    
    if memo[n] != False or n in [0, 1]: # calculation is done
        return memo[n]

    else: # calculation is not done >:(
        f1 = fib(n-1)
        memo[n-1] = f1
        f2 = fib(n-2)
        memo[n-2] = f2

        return (f1 + f2)

res = fib(12)
print(res)