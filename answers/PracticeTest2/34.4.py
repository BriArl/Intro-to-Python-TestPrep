#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height 
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h

def calculate_trapezoid_area(b1, b2, h):
    # Calculate the area using the trapezoid area formula
    area = (b1 + b2) / 2 * h
    return area
    
# Accept inputs from the user
b1 = int(input().strip())
b2 = int(input().strip())
h = int(input().strip())

# Calculate the area of the trapezoid
area_value = calculate_trapezoid_area(b1, b2, h)

# Print the result in the requierd format
print(f"Trapezoid area: {area_value} square meters")