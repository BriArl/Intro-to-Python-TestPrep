predef_list = [4, -27, 15, 33, -10]

def is_greater_than_max(input_value):

    max_value = max(predef_list)

    return input_value > max_value
    
input_value = int(input().strip())

result = is_greater_than_max(input_value)

print(f"Greater Than Max? {result}")