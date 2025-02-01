def steps_to_miles(steps):
    # Check if the steps are negative and raise a ValueError if true
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    
    # Calculate miles
    miles = steps / 2000
    return miles

def main():
    try:
        # Read the number of steps from the user
        steps = int(input())
        
        # Call the steps_to_miles function and get the result
        miles = steps_to_miles(steps)
        
        # Print the result formatted to 2 decimal places
        print(f'{miles:.2f}')
    
    except ValueError as e:
        # Print the exception message
        print(e)

if __name__ == '__main__':
    main()