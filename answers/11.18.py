user_input = input()
bounds_input = input()

numbers = list(map(int, user_input.split()))

lower_bound, upper_bound = map(int, bounds_input.split())

in_range_numbers = [num for num in numbers if lower_bound <= num <= upper_bound]

print(' '.join(map(str, in_range_numbers)), end=' ')