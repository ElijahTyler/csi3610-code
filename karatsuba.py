# assume base 10
# (x1 + x0)(y1 + y0) = x1y1 + (x1y0 + x0y1) + x0y0
# a = b + (middle digit) + c
# a - b - c = middle digit

def k_decomp(n):
    digits = 0
    paul = n

    while paul > 0:
        paul //= 10
        digits += 1
    digits //= 2 # digits is the midpoint of the number

    n1 = n // (10**digits)
    n0 = n % (10**digits)

    return n1, n0


def k_comp(n2, n1, n0):
    return (n2 * 100) + (n1 * 10) + n0


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    
    x1, x0 = k_decomp(x)
    y1, y0 = k_decomp(y)

    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0

    ret = k_comp(z2, z1, z0)
    return ret



paul = karatsuba(11, 27)
print(paul)