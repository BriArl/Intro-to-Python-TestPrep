user_input = input()
numbers = list(map(int, user_input.split()))

# Filter out non-negative numbers
non_negative_numbers = [num for num in numbers if num >= 0]

# Sort the filtered numbers in ascending order
non_negative_numbers.sort()

# Print the numbers with a space after each and ensure a trailing space
print(' '.join(map(str, non_negative_numbers)), end=' ')