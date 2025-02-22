def feet_to_steps(user_feet):
    return int(user_feet / 2.5)

if __name__ == '__main__':
    
    user_feet = float(input())
    
    steps = feet_to_steps(user_feet)
    print(steps)