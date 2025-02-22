filename = input().strip()
lower_bound = input().strip()
upper_bound = input().strip()

with open(filename, 'r') as file:
    words = file.readlines()

for word in words:
    word = word.strip()
    if lower_bound <= word <= upper_bound:
        print(word)
