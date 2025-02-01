# Read the number of floating-point values
n = int(input())

# Read the floating-point values into a list
values = []
for _ in range(n):
    values.append(float(input()))
    
# Find the max value in the list
max_value = max(values)

# Normalize each value by dividing by the max value
normalized_values = [value / max_value for value in values]

# Output each normalized value with two decimal places
for normalized_value in normalized_values:
    print(f'{normalized_value:.2f}')