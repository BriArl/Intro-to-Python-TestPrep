def convert_ounces_to_tons_pounds_ounces(ounces):
    
    tons = ounces // (2000 * 16)
    
    remaining_ounces_after_tons = ounces % (2000 * 16)
    
    pounds = remaining_ounces_after_tons // 16
    
    remaining_ounces = remaining_ounces_after_tons % 16
    
    return f"Tons: {tons}\nPounds: {pounds}\nOunces: {remaining_ounces}"
    
if __name__ == "__main__":
    try:
        ounces_input = int(input(""))
        output = convert_ounces_to_tons_pounds_ounces(ounces_input)
        print(output)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")