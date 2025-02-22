valid_months = {
    "January": 31, "February": 29, "March": 31,
    "April": 30, "May": 31, "June": 30,
    "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31
}

input_month = input()
input_day = int(input())

if input_month not in valid_months or input_day < 1 or input_day > valid_months[input_month]:
    print("Invalid")
else:
    if (input_month == "March" and input_day >= 20) or input_month in ["April", "May"] or (input_month == "June" and input_day <= 20):
        print("Spring")
    elif (input_month == "June" and input_day >= 21) or input_month in ["July", "August"] or (input_month == "September" and input_day <= 21):
        print("Summer")
    elif (input_month == "September" and input_day >= 22) or input_month in ["October", "November"] or (input_month == "December" and input_day <= 20):
        print("Autumn")
    elif (input_month == "December" and input_day >= 21) or input_month in ["January", "February"] or (input_month == "March" and input_day <= 19):
        print("Winter")