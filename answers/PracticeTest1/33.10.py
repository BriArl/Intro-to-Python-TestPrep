def reverse_text():
    while True:
        user_input = input()
        if user_input.lower() in ['done', 'd']:
            break
        else:
            reversed_input = user_input[::-1]
            print(reversed_input)

reverse_text()