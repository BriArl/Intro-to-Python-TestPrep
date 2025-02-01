#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")


# Import the pigAge module
import pigAge

# Accept integer input representing the pig's age
pig_age = int(input().strip())

# Calculate the human equivment age using the pigAge_converter function
human_equivlent_age = pigAge.pigAge_converter(pig_age)

# Output the result in the specified format
print(f"{pig_age} is {human_equivlent_age} in human years")