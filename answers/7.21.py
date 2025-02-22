def int_to_reverse_binary(integer_value):
    """Converts an integer to a reverse binary string."""
    reverse_binary = ""
    while integer_value > 0:
        reverse_binary += str(integer_value % 2)
        integer_value //= 2
    return reverse_binary
    
def string_reverse(input_string):
    """Reverses a given string."""
    return input_string[::-1]

if __name__ == '__main__':

    integer_value = int(input())
    
    reverse_binary = int_to_reverse_binary(integer_value)
    
    binary_string = string_reverse(reverse_binary)
    
    print(binary_string)