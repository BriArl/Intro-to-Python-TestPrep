def swap_values(user_val1, user_val2, user_val3, user_val4):
    """Swaps the first value with the second and the third with the fourth."""
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__': 
    
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())
    
    swapped_values = swap_values(val1, val2, val3, val4)
    
    print(*swapped_values)