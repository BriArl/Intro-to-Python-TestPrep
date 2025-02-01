# Define your function here 
def feet_to_steps(user_feet):
    # Calculate the number of steps and return as an integer
    return int(user_feet / 2.5)

if __name__ == '__main__':
    # Type your code here.
    
    # Input: Number of feet walked
    user_feet = float(input())
    
    # Call the function and output the result
    steps = feet_to_steps(user_feet)
    print(steps)