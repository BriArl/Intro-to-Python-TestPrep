quarters = int(input())
dimes = int(input())
nickels = int(input())
pennies = int(input())

dollars = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

print(f'Amount: ${dollars:.2f}')