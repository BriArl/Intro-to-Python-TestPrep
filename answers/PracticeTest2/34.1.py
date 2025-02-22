def calculate_total_distance(travels_A, travels_B, travels_C):
    miles_per_commute = {
        'A': 15.62,
        'B': 41.85,
        'C': 32.67
    }
    
    total_miles_A = travels_A * miles_per_commute['A']
    total_miles_B = travels_B * miles_per_commute['B']
    total_miles_C = travels_C * miles_per_commute['C']
    
    total_distance = total_miles_A + total_miles_B + total_miles_C
    
    formatted_distance = "{:.2f}".format(total_distance)
    
    return f"Distance: {formatted_distance} miles"