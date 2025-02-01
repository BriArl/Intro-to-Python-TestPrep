word = input()
password = ''

# Iterate through each character through each character in the input word
for char in word:
    if char == 'i':
        password += '1'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password +='8'
    elif char == 's':
        password += '$'
    else:
        password += char # Keep the character uncharged if no replacement
        
# Append '!' to the strengthened password
password += '!'
    
print(password)