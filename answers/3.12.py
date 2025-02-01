# Read int user_num and div_num
user_num = int(input())
div_num = int(input())

# Perform three floor divisions
result1 = user_num // div_num
result2 = result1 // div_num
result3 = result2 // div_num

# Output the results
print(result1, result2, result3)