def count_character_occurrences():
    user_input = input().strip()

    char = user_input[0]
    phrase = user_input[2:]

    count = phrase.count(char)

    if count == 1:
        print(f"{count} {char}")
    else:
        print(f"{count} {char}'s")

count_character_occurrences()