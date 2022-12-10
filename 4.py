def function(coins, price):
    coins.reverse()
    n = 0
    count = 0
    while price > 0:
        if coins[n] <= price:
            price -= coins[n]
            count += 1
        else:
            n += 1
    return count