def get_data_type(index):
    various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

    if index < 0 or index >= len(various_data_types):
        return f"Element {index}: dict"
        
    element = various_data_types[index]
    
    data_type = type(element).__name__
    
    return f"Element {index}: {data_type}"

if __name__ == "__main__":
    try:
        index = int(input(""))
        print(get_data_type(index))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")