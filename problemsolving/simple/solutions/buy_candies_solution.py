candy_price = 0.10  # Candy price is 10 cents
total_budget = 1.00  # Total Budget 1 USD
count = 0  # Start with no candies
while total_budget >= candy_price:
    total_budget -= 0.10
    count += 1
print('Total number of candies bought :%d.' % count)
print('Money left after buy: $%f' % total_budget)
