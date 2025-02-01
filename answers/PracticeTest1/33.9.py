if __name__ == '__main__':
    first_int = int(input())
    second_int = int(input())
    
    if second_int < first_int:
        print("Second integer can't be less than the first.")
        
    else:
        for num in range(first_int, second_int + 1, 5):
            print(num, end=" ")
            
        print()