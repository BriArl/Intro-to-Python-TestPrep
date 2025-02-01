# Step 1: Read input
filename = input().strip()
lower_bound = input().strip()
upper_bound = input().strip()

# Step 2: Open and read file contents
with open(filename, 'r') as file:
    words = file.readlines()

# Step 3: Process words (strip newlines and filter by range)
for word in words:
    word = word.strip()  # Remove any newline or extra spaces
    if lower_bound <= word <= upper_bound:
        print(word)
