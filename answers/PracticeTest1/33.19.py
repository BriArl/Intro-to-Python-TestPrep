synonyms = {}   

def main():
    word = input().strip()
    letter = input().strip().lower()
    
    filename = f"{word}.txt"
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.strip().split()
                
                if words:
                    first_letter = words[0][0].lower()
                    if first_letter not in synonyms:
                        synonyms[first_letter] = []
                    synonyms[first_letter].extend(words)
        
        if letter in synonyms and synonyms[letter]:
            for synonym in synonyms[letter]:
                print(synonym)
        else:
            print(f"No synonyms for {word} begin with {letter}.")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    main()