def steps_to_miles(steps):
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    
    miles = steps / 2000
    return miles

def main():
    try:
        steps = int(input())
        
        miles = steps_to_miles(steps)
        
        print(f'{miles:.2f}')
    
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()