synonyms = {}   # Define dictionary

def main():
    # Read the input word and letter
    word = input().strip()
    letter = input().strip().lower()
    
    # Define the filename based on the input word
    filename = f"{word}.txt"
    
    try:
        # Open the file and read its contents
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into words (synonyms)
                words = line.strip().split()
                
                # Store the words in the dictionary based on their first letter
                if words:
                    first_letter = words[0][0].lower()  # Get the first letter of the first word
                    if first_letter not in synonyms:
                        synonyms[first_letter] = []
                    synonyms[first_letter].extend(words)
        
        # Output the synonyms that start with the given letter
        if letter in synonyms and synonyms[letter]:
            for synonym in synonyms[letter]:
                print(synonym)
        else:
            print(f"No synonyms for {word} begin with {letter}.")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    main()