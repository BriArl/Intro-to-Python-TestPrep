#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

# Accept the file name as input
file_name = input().strip()

# Open the file and read its contents
with open(file_name, 'r') as file:
    # Read the three words, one per line
    words = file.readlines()

# Strip newline characters from each word
words = [word.strip() for word in words]

# Create a sentence from the three words
sentence = ' '.join(words)

# Open the file in append mode and write the new sentence
with open(file_name, 'a') as file:
    file.write('\n' + sentence)

# Open the file again to read the updated contents
with open(file_name, 'r') as file:
    # Read and print the updated contents of the file
    updated_contents = file.read()

# Print the updated file contents
print(updated_contents)