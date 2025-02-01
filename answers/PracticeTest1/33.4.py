cars_gas_mileage = float(input())
cost_of_gas = float(input())

cost_20mi = 20/cars_gas_mileage*cost_of_gas
cost_75mi = 75/cars_gas_mileage*cost_of_gas
cost_500mi = 500/cars_gas_mileage*cost_of_gas

print(f'{cost_20mi:.2f} {cost_75mi:.2f} {cost_500mi:.2f}')