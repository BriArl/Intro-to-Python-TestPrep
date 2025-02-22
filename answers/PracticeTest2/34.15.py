import pigAge

pig_age = int(input().strip())

human_equivlent_age = pigAge.pigAge_converter(pig_age)

print(f"{pig_age} is {human_equivlent_age} in human years")