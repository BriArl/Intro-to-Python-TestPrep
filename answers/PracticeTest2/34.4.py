def calculate_trapezoid_area(b1, b2, h):
    area = (b1 + b2) / 2 * h
    return area
    
b1 = int(input().strip())
b2 = int(input().strip())
h = int(input().strip())

area_value = calculate_trapezoid_area(b1, b2, h)

print(f"Trapezoid area: {area_value} square meters")