#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
#second output: sum of five inputs converted to float values
#third output: sum of five inputs converted to string values (concatenate)

def sum_outputs(input1, input2, input3, input4, input5):
    
    # Calculate integer sum
    integer_sum = input1 + input2 + input3 + input4 + input5
    
    # Calculate float sum
    float_sum = float(integer_sum)
    
    # Calculate string concatenation sum
    string_sum = str(input1) + str(input2) + str(input3) + str(input4) + str(input5)
    
    return integer_sum, float_sum, string_sum

# Accept inputs from the user
input1 = int(input().strip())
input2 = int(input().strip())
input3 = int(input().strip())
input4 = int(input().strip())
input5 = int(input().strip())

# Calculate the sums
integer_sum_value, float_sum_value, string_sum_value = sum_outputs(input1, input2, input3, input4, input5)

# Print the results in the required format
print(f"Integer: {integer_sum_value}")
print(f"Float: {float_sum_value}")
print(f"String: {string_sum_value}")