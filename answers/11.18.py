# Input: First line is the list of integers, second line is the bounds
user_input = input()
bounds_input = input()

# Convert the first line into a list of integers
numbers = list(map(int, user_input.split()))

# Convert the second line into the lower and upper bounds
lower_bound, upper_bound = map(int, bounds_input.split())

# Filter the numbers within the range [lower_bound, upper_bound]
in_range_numbers = [num for num in numbers if lower_bound <= num <= upper_bound]

# Print the filtered numbers followed by a space (including a trailing space)
print(' '.join(map(str, in_range_numbers)), end=' ')