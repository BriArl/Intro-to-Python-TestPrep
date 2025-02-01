frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

# Take input from user 
try:
        index = int(input().strip())
        #Acess the list element at given index
        print(frameworks[index])
except (IndexError, ValueError):
    # If an error occujrs, print "Error"
    print("Error")