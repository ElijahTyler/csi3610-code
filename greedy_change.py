def greedy_change(coins, n):
    coins.sort() # O(k lg k) where k = # of coins
    coins.reverse()
    coins_used = []

    for coin in coins: # O(n)
        while n >= coin:
            coins_used.append(coin)
            n -= coin
    if n != 0:
        return False
    return coins_used # by keeping track of only # of coins, total reduced down to O(k lg k)



coins = [1, 5, 10, 25]
paul = greedy_change(coins, 47)
print(paul)