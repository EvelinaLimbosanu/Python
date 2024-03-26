def max_profit(prices):
    if len(prices) == 0:
        return 0

    min_price = min(prices)
    max_price = max(prices)
    while prices.index(min_price) > prices.index(max_price):
        prices.remove(max_price)
        max_price = max(prices)

    if prices.index(min_price) == prices.index(max_price):
        return 0

    return max_price - min_price


prices = [9, 2, 3, 2]

print(max_profit(prices))
