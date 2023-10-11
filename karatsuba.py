def k_len(n, base):
    ret = 0
    while n > 0:
        n //= base
        ret += 1
    return ret

def k_split(num, base, index):
    return (num // (base ** index)), num % (base ** index)

def karatsuba(x, y, base):
    if x < 10 or y < 10:
        return x * y # normal multiplication
    
    m = max(k_len(x, base), k_len(y, base))
    m2 = m // 2

    high1, low1 = k_split(x, base, m2)
    high2, low2 = k_split(y, base, m2)

    z0 = karatsuba(low1, low2, base)
    z1 = karatsuba(low1 + high1, low2 + high2, base)
    z2 = karatsuba(high1, high2, base)

    ret = (z2 * base**(2*m2)) + ((z1 - z2 - z0) * base**m2) + z0
    return ret

paul = karatsuba(11, 27, 10)
print(paul)