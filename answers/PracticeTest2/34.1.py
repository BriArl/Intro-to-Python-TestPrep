#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

def calculate_total_distance(travels_A, travels_B, travels_C):
    # Define miles per commute for each employee
    miles_per_commute = {
        'A': 15.62,
        'B': 41.85,
        'C': 32.67
    }
    
    # Calculate total distance for each employee
    total_miles_A = travels_A * miles_per_commute['A']
    total_miles_B = travels_B * miles_per_commute['B']
    total_miles_C = travels_C * miles_per_commute['C']
    
    # Calculate overall total distance
    total_distance = total_miles_A + total_miles_B + total_miles_C
    
    # Format the output to two decimal places
    formatted_distance = "{:.2f}".format(total_distance)
    
    # Return the formatted output
    return f"Distance: {formatted_distance} miles"