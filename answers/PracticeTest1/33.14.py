def is_palindrome(input_str):
    cleaned_str = ''.join(input_str.split()).lower()
    return cleaned_str == cleaned_str[::-1]

if __name__ == '__main__':
    user_input = input()
    
    if is_palindrome(user_input):
        print(f'{user_input} is a palindrome')
    else:
        print(f'{user_input} is not a palindrome')