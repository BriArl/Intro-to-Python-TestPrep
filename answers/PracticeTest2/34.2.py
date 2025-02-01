#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

def convert_ounces_to_tons_pounds_ounces(ounces):
    
    # Calculate tons
    tons = ounces // (2000 * 16)
    
    # Calculate remaining ounces after converting to tons
    remaining_ounces_after_tons = ounces % (2000 * 16)
    
    # Calculate pounds from the remaining ounces
    pounds = remaining_ounces_after_tons // 16
    
    # Calculate remaining ounces after converting to pounds
    remaining_ounces = remaining_ounces_after_tons % 16
    
    # Return formatted output
    return f"Tons: {tons}\nPounds: {pounds}\nOunces: {remaining_ounces}"
    
# Example usage:
if __name__ == "__main__":
    # Prompt user for input
    try:
        ounces_input = int(input(""))
        output = convert_ounces_to_tons_pounds_ounces(ounces_input)
        print(output)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")