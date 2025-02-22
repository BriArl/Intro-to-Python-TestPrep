def mad_libs():
    while True:
        user_input = input().strip()

        parts = user_input.split()

        if len(parts) != 2:
            continue

        word, number = parts[0], parts[1]

        if word.lower() == "quit":
            break

        if not number.isdigit():
            continue

        number = int(number)

        print(f"Eating {number} {word} a day keeps the doctor away.")

mad_libs()
