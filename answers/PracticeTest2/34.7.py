predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list


# Function to check if input is greater than maximum value in the predefined list
def is_greater_than_max(input_value):

    # Find max value in the predefined list
    max_value = max(predef_list)

    # Compare input value with maximum value
    return input_value > max_value
    
# Accept input from the user
input_value = int(input().strip())

# Check if the input value is greater than the maximum value in the predefined list
result = is_greater_than_max(input_value)

# Print the result in the requiered format
print(f"Greater Than Max? {result}")