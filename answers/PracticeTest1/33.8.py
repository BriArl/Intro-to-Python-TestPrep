def exact_change(user_total):
    dollars = user_total//100
    user_total %= 100
    quarters = user_total//25
    user_total %= 25
    dimes = user_total//10
    user_total %= 10
    nickels = user_total//5
    user_total %= 5
    pennies = user_total
    
    return(dollars, quarters, dimes, nickels, pennies)

if __name__ == '__main__':

    input_val = int(input())
    
    if input_val <= 0:
        print('No change')
        
    else:
        dollars, quarters, dimes, nickels, pennies = exact_change(input_val)
        
        if dollars > 0:
            if dollars == 1:
                print (f'{dollars} Dollar')
            else:
                print (f'{dollars} Dollars')
                
        
        if quarters  > 0:
            if quarters == 1:
                print (f'{quarters} Quarter')
            else:
                print (f'{quarters} Quarters')
                

        if dimes  > 0:
            if dimes == 1:
                print (f'{dimes} Dime')
            else:
                print (f'{dimes} Dimes')
                
        if nickels  > 0:
            if nickels == 1:
                print (f'{nickels} Nickel')
            else:
                print (f'{nickels} Nickels')
                
        if pennies  > 0:
            if pennies == 1:
                print (f'{pennies} Penny')
            else:
                print (f'{pennies} Pennies')