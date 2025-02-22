def sum_outputs(input1, input2, input3, input4, input5):
    
    integer_sum = input1 + input2 + input3 + input4 + input5
    
    float_sum = float(integer_sum)
    
    string_sum = str(input1) + str(input2) + str(input3) + str(input4) + str(input5)
    
    return integer_sum, float_sum, string_sum

input1 = int(input().strip())
input2 = int(input().strip())
input3 = int(input().strip())
input4 = int(input().strip())
input5 = int(input().strip())

integer_sum_value, float_sum_value, string_sum_value = sum_outputs(input1, input2, input3, input4, input5)

print(f"Integer: {integer_sum_value}")
print(f"Float: {float_sum_value}")
print(f"String: {string_sum_value}")