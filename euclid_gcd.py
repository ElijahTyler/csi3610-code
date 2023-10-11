def factor(n):
    if n == 0:
        return [0]
    factors = []
    for prime in range(2, int(n**0.5)):
        while n % prime == 0:
            factors.append(prime)
            n /= prime
    return factors

def gcd(a, b):
    a_factors = factor(a)
    b_factors = factor(b)
    if a_factors == [0] or b_factors == [0]:
        return a + b
    
    gcd = 1
    for f in a_factors:
        if f in b_factors:
            a_factors.remove(f)
            b_factors.remove(f)
            gcd *= f
    
    return gcd

assert factor(21582) == [2, 3, 3, 11, 109]
assert gcd(288, 120) == 24
assert gcd(20, 0) == 20