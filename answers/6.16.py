''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
# Brute force search for x and y in the range -10 t 10
solution_found = False

for x in range(-10, 10): # x ranges from -10 to 10
    for y in range(-10, 11): # y ranges from  -10 to 10
        if (a * x + b * y ==c) and (d * x + e * y == f):
            print(f"x = {x} , y = {y}")
            solution_found = True
            break # Exit inner loop if a solution is found
    if solution_found:
        break # Exit outer loop if a solution is found

if not solution_found:
    print("There is no solution")