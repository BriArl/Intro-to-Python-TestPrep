is_leap_year = False
   
input_year = int(input())

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True # Century must be divisible by 400
        else:
            is_leap_year = False
    else:
        is_leap_year = True # Non-century years divisible by 4 are leap years
else:
    is_leap_year = False # Not divisible by 4
    
# Output results
if is_leap_year:
    print(f"{input_year} - leap year")
else:
    print(f"{input_year} - not a leap year")