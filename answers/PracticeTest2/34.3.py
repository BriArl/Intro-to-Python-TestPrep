#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

def get_data_type(index):
    various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

    # Check if the index is within the range of the list
    if index < 0 or index >= len(various_data_types):
        return f"Element {index}: dict"
        
    # Get the element at the specified index
    element = various_data_types[index]
    
    # Get the data type of the element
    data_type = type(element).__name__
    
    # Return formatted output
    return f"Element {index}: {data_type}"

# Example usage:
if __name__ == "__main__":
    try:
        index = int(input(""))
        print(get_data_type(index))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")