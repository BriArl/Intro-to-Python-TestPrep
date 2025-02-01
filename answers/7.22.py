# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    """Swaps the first value with the second and the third with the fourth."""
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__': 
    # Type your code here. Your code must call the function.
    
    # Read input values
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())
    
    # Call the function to swap values
    swapped_values = swap_values(val1, val2, val3, val4)
    
    # Output the swapped value
    print(*swapped_values) # Unpack the tuple to print values seperated by spaces