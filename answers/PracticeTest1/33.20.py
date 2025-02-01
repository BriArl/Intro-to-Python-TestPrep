import csv

from collections import Counter

# Read the input file name
input_file = input()

# Initialize a list to hold the words
words = []

# Read the file and populate the words list
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for word in row:
            words.append(word)

# Count the frequency of each word
word_count = Counter(words)

# Output the words and their frequencies
for word, count in word_count.items():
    print(f"{word} {count}")