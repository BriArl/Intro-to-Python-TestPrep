import random

def number_guess(num):
    random_num = random.randint(1,100)
    if num < random_num:
        print(f"{num} is too low. Random number was {random_num}.")
    elif num > random_num:
        print(f"{num} is too high. Random number was {random_num}.")
    else:
        print(f"{num} is correct!")
    
        
if __name__ == "__main__":
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)