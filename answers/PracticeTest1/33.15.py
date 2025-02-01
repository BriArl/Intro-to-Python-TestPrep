def get_month_as_int(monthString):
    if monthString == 'January':
        return 1
    elif monthString == 'February':
        return 2
    elif monthString == 'March':
        return 3
    elif monthString == 'April':
        return 4
    elif monthString == 'May':
        return 5
    elif monthString == 'June':
        return 6
    elif monthString == 'July':
        return 7
    elif monthString == 'August':
        return 8
    elif monthString == 'September':
        return 9
    elif monthString == 'October':
        return 10
    elif monthString == 'November':
        return 11
    elif monthString == 'December':
        return 12
    else:
        return 0

while True:
    try:
        user_string = input("Enter a date (or '-1' to stop): ")
        
        if user_string == '-1':
            break
        
        # Splitting the input string
        parts = user_string.split()
        
        # Validate if the date has exactly 3 parts and the second part ends with a comma
        if len(parts) == 3 and parts[1][-1] == ',':
            # Remove the comma from the day part
            day = parts[1][:-1]
            
            # Get the month as an integer
            month = get_month_as_int(parts[0])
            
            # Get the year
            year = parts[2]
            
            # If month is valid and day and year are digits, print in required format
            if month != 0 and day.isdigit() and year.isdigit():
                print(f"{month}/{int(day)}/{year}")
            else:
                print("Invalid date format.")
        else:
            print("Invalid date format.")
    
    except EOFError:
        # Handle the EOFError if input is suddenly cut off (optional, for robust handling)
        print("Input was cut off unexpectedly.")
        break