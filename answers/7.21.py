# Define your functions here.
def int_to_reverse_binary(integer_value):
    """Converts an integer to a reverse binary string."""
    reverse_binary = ""
    while integer_value > 0:
        reverse_binary += str(integer_value % 2) # Get remainer (0 or 1)
        integer_value //= 2 # Reduce the integer by dividing by 2
    return reverse_binary
    
def string_reverse(input_string):
    """Reverses a given string."""
    return input_string[::-1] # Use slicing to reverse the string

if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    
    # Read input
    integer_value = int(input())
    
    # Get binary string in reverse order
    reverse_binary = int_to_reverse_binary(integer_value)
    
    # Reverse the reverse binary string to get the correct order
    binary_string = string_reverse(reverse_binary)
    
    # Output the final binary string
    print(binary_string)