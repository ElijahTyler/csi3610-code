def exp_rec(x, n):
    if n == 0: return 1
    if n%2 == 0:
        return exp_rec(x*x, n//2)
    else:
        return x * exp_rec(x*x, n//2)

paul = exp_rec(2, 13)
print(paul)