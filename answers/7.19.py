# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    # Calculate the cost of driving
    cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
    return cost

if __name__ == '__main__':
    # Type your code here.
    
    # Input for miles per gallon and dollars per gallon
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    
    # Calculate cost for 10, 50, and 400 miles
    cost_10_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    cost_50_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    cost_400_miles = driving_cost(miles_per_gallon, dollars_per_gallon, 400)
    
    # Output the results
    print(f'{cost_10_miles:.2f}')
    print(f'{cost_50_miles:.2f}')
    print(f'{cost_400_miles:.2f}')