def format_student_id(num):
    num_str = str(num)
    
    part1 = num_str[:3]
    part2 = num_str[3:5]
    part3 = num_str[5:]
    
    formatted_id = f"{part1}-{part2}-{part3}"
    
    return formatted_id

num = int(input().strip())

formatted_id = format_student_id(num)

print(formatted_id)