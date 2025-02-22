stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

num_shares = int(input().strip())

total_cost = 0.0

for _ in range(num_shares):
    stock_selection = input().strip()
    if stock_selection in stocks:
        total_cost += stocks[stock_selection]
    else:
        print(f"Stock {stock_selection} not found.")

print(f"Total price: ${total_cost:.2f}")
        