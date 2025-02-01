def reverse_binary_representation(x):
    if x <= 0:
        return "Input must be a pos integer"
    result = ""
    while x > 0:
        result += str(x % 2) # Append the remainder of x divded by 2 (0 or 1)
        x //= 2 # Update x to be x divded by 2 (int division)
    
    return result
    
# Example usage
if __name__ == "__main__":
    x = int(input())
    print(reverse_binary_representation(x))