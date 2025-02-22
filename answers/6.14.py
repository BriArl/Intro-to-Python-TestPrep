def reverse_binary_representation(x):
    if x <= 0:
        return "Input must be a pos integer"
    result = ""
    while x > 0:
        result += str(x % 2)
        x //= 2
    
    return result
    
if __name__ == "__main__":
    x = int(input())
    print(reverse_binary_representation(x))