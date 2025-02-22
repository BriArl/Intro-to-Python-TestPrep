file_name = input().strip()

with open(file_name, 'r') as file:
    words = file.readlines()

words = [word.strip() for word in words]

sentence = ' '.join(words)

with open(file_name, 'a') as file:
    file.write('\n' + sentence)

with open(file_name, 'r') as file:
    updated_contents = file.read()

print(updated_contents)