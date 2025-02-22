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
    else:
        water_state = "Boiling"
        saftey_coment = ""
        
    return water_state, saftey_comment
    
temperature = int(input().strip())

water_state, safety_comment = determine_water_state(temperature)

print(water_state)
if safety_comment:
    print(safety_comment)