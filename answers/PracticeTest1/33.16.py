services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = base_wash

service_choice1 = input()
service_choice2 = input()

print("ZyCar Wash")

# Output the base wash cost
print(f"Base car wash -- ${base_wash}")

# Check and add the first service choice
if service_choice1 != '-':
    print(f"{service_choice1} -- ${services[service_choice1]}")
    total += services[service_choice1]

# Check and add the second service choice
if service_choice2 != '-':
    print(f"{service_choice2} -- ${services[service_choice2]}")
    total += services[service_choice2]

# Output the total cost
print("----")
print(f"Total price: ${total}")