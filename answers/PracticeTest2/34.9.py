#solution accepts integer input representing a water temperature
#temperature >= 212, water state is "Boiling"
#temperature between 115-211, exclusive of the stop, water state is "Hot"
#temperature between 80-115, water state is "Warm"
#temperature between 33-80, water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution outputs the water state and potential safety comment based on temperature

def determine_water_state(temperature):
    if temperature < 33:
        water_state = "Frozen"
        saftey_comment = "Watch out for ice!"
    elif 33 <= temperature < 80:
        water_state = "Cold"
        saftey_comment = ""
    elif 80 <= temperature < 115:
        water_state = "Warm"
        saftey_comment = ""
    elif 115 <= temperature < 212:
        water_state = "Hot"
        saftey_comment = ""
    elif temperature == 212:
        water_state = "Boiling"
        saftey_comment = "Caution: Hot!"
    else: # temperature > 212
        water_state = "Boiling"
        saftey_coment = ""
        
    return water_state, saftey_comment
    
# Take in user input from the user
temperature = int(input().strip())

# Determine the water state and saftey comment
water_state, safety_comment = determine_water_state(temperature)

# Print the results
print(water_state)
if safety_comment:
    print(safety_comment)