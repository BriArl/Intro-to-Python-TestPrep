def get_num_of_characters(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

def output_without_whitespace(input_string):
    return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    # Step 1: Prompt user for input
    user_input = input("Enter a sentence or phrase:\n")
    
    # Step 2: Output the entered string
    print(f'\nYou entered: {user_input}')
    
    # Step 3: Call get_num_of_characters() and output the number of characters
    num_characters = get_num_of_characters(user_input)
    print(f'\nNumber of characters: {num_characters}')
    
    # Step 4: Call output_without_whitespace() and output the modified string
    no_whitespace_string = output_without_whitespace(user_input)
    print(f'String with no whitespace: {no_whitespace_string}')