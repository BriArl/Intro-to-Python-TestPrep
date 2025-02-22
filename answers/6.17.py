n = int(input())

values = []
for _ in range(n):
    values.append(float(input()))
    
max_value = max(values)

normalized_values = [value / max_value for value in values]

for normalized_value in normalized_values:
    print(f'{normalized_value:.2f}')