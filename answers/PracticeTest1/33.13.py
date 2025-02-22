def get_num_of_characters(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

def output_without_whitespace(input_string):
    return ''.join(char for char in input_string if not char.isspace())

if __name__ == '__main__':
    user_input = input("Enter a sentence or phrase:\n")
    
    print(f'\nYou entered: {user_input}')
    
    num_characters = get_num_of_characters(user_input)
    print(f'\nNumber of characters: {num_characters}')
    
    no_whitespace_string = output_without_whitespace(user_input)
    print(f'String with no whitespace: {no_whitespace_string}')