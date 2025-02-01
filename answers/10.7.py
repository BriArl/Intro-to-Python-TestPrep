def count_character_occurrences():
    # Get the input from the user
    user_input = input().strip()

    # Split the input into the character and the phrase
    char = user_input[0]  # The first character
    phrase = user_input[2:]  # The rest of the string after the space

    # Count the occurrences of the character in the phrase
    count = phrase.count(char)

    # Determine the appropriate output format based on the count
    if count == 1:
        print(f"{count} {char}")
    else:
        print(f"{count} {char}'s")

# Call the function
count_character_occurrences()