import csv

from collections import Counter

input_file = input()

words = []

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for word in row:
            words.append(word)

word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word} {count}")