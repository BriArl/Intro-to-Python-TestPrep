def remove_non_alpha():
    user_input = input().strip()

    filtered = ''.join(char for char in user_input if char.isalpha())

    print(filtered)

remove_non_alpha()