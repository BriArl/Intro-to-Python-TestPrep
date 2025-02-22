user_input = input()

name_parts = user_input.split()

if len(name_parts) == 3:
    first_name = name_parts[0]
    middle_name = name_parts[1]
    last_name = name_parts[2]
    print(f"{last_name}, {first_name[0]}.{middle_name[0]}.")
elif len(name_parts) == 2:
    first_name = name_parts[0]
    last_name = name_parts[1]
    print(f"{last_name}, {first_name[0]}.")
else:
    print("Individual input format.")