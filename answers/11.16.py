user_input = input()

numbers = list(map(int, user_input.split()))

average = round(sum(numbers) / len(numbers))

max_value = max(numbers)

print(average, max_value)