def remove_non_alpha():
    # Get the input from the user
    user_input = input().strip()

    # Filter out non-alphabetic characters
    filtered = ''.join(char for char in user_input if char.isalpha())

    # Output the result
    print(filtered)

# Call the function
remove_non_alpha()