a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

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