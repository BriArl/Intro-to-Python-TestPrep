purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

item = input().strip()
 
quantity = int(input().strip())
 
if item in purchase:
    cost_per_item = purchase[item]
     
    if quantity <10:
         total_cost = cost_per_item * quantity
    elif 10 <= quantity <=20:
        total_cost = cost_per_item * quantity * 0.95
    else:
        total_cost = cost_per_item * quantity * 0.90
        
    print(f"{item} ${total_cost:.2f}")
else:
    print(f"Item {item} not found.")