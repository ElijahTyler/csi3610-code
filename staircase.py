# k = 2 gives the Fibonacci numbers!

memo = {}
def staircase(n, k):
    if n == 0:
        return 1
    if (n,k) not in memo:
        total = 0
        for steps in range(1, k+1):
            if n-steps >= 0:
                total += staircase(n-steps, k)
        memo[(n,k)] = total
    return memo[(n,k)]

paul = staircase(11, 2)
print(paul)