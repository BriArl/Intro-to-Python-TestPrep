import math

num = int(input().strip())

factorial_value = math.factorial(num)

is_greater_than_100 = factorial_value > 100

print(factorial_value)
print(is_greater_than_100)