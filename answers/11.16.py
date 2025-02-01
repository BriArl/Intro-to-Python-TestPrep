# Step 1: Read input from user
user_input = input()

# Step 2: Convert input string to a list of int
numbers = list(map(int, user_input.split()))

# Step 3: Calculate avg (rounded)
average = round(sum(numbers) / len(numbers))

# Step 4: Find the max value
max_value = max(numbers)

# Step 5: Print the results
print(average, max_value)