import math

x = float(input())
y = float(input())
z = float(input())

value1 = x ** z
value2 = x ** (y ** z)
value3 = abs(x - y)
value4 = math.sqrt(x ** z)

print(f'{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}')