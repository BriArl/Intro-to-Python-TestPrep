current_price = int(input())
last_months_price = int(input())

price_change = current_price - last_months_price

monthly_mortgage = (current_price * 0.051) / 12

print(f'This house is ${current_price}. The change is ${price_change} since last month.')
print(f'The estimated monthly mortgage is ${monthly_mortgage:.2f}.')