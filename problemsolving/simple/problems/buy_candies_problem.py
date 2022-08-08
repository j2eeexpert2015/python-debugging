candy_price = 0.10  # Candy price is 10 cents
total_budget = 1.00  # Total Budget 1 USD
count = 0  # Start with no candies
while total_budget >= candy_price:
    #candy_price += 1  # Buy another candy!
    total_budget -= candy_price
    count = count + 1
    #candy_price += 0.10  # Price goes up
print('Total number of candies bought :%d.' % count)
print('Money left after buy: $%f' % total_budget)
