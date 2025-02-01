#hint: modulo (%) and floored division (//) may be used
#solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
#solution outputs formatted student identification number as a string (i.e.,"541-75-3010")

def format_student_id(num):
    #convert the number to a string for easy modification
    num_str = str(num)
    
    # Extract the componets
    part1 = num_str[:3] # first three digits
    part2 = num_str[3:5] # next 2 digits
    part3 = num_str[5:] # last four digits
    
    # Format the identification number
    formatted_id = f"{part1}-{part2}-{part3}"
    
    return formatted_id

# Accept input from the user
num = int(input().strip())

# Format the student identification number
formatted_id = format_student_id(num)

# Print the formatted identification number
print(formatted_id)