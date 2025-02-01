def mad_libs():
    while True:
        # Get the input from the user
        user_input = input().strip()

        # Split the input into the word and the number
        parts = user_input.split()

        # Ensure the input has two parts
        if len(parts) != 2:
            continue

        word, number = parts[0], parts[1]

        # Check if the input word is 'quit'
        if word.lower() == "quit":
            break

        # Validate the number
        if not number.isdigit():
            continue

        # Convert the number to an integer
        number = int(number)

        # Output the sentence
        print(f"Eating {number} {word} a day keeps the doctor away.")

# Call the function
mad_libs()
