purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

# Accept the item to be purchased
item = input().strip()
 
 # Accept the number of item to be purchased
quantity = int(input().strip())
 
 # Initalize the total cost
if item in purchase:
    cost_per_item = purchase[item]
     
     # Apply discount based on the num of items purchased 
    if quantity <10:
         total_cost = cost_per_item * quantity
    elif 10 <= quantity <=20:
        total_cost = cost_per_item * quantity * 0.95
    else: # quantity >= 21
        total_cost = cost_per_item * quantity * 0.90
        
    # Print the result formatted to two decimal places
    print(f"{item} ${total_cost:.2f}")
else:
    print(f"Item {item} not found.")