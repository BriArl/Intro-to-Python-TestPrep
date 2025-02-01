#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is >100

import math

# Accept int input
num = int(input().strip())

# Calculate the factorial using math.factorial()
factorial_value = math.factorial(num)

# Determine if the factorial is greater than 100
is_greater_than_100 = factorial_value > 100

# Output the factorial value and the Boolean result
print(factorial_value)
print(is_greater_than_100)