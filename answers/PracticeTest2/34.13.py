#import csv module and call open(), reader()
#solution accepts input identifying name of CSV file (i.e., "input1.csv")
#solution outputs each row of CSV file contents as a dictionary of elements

import csv

# Read the name of the CSV file
file_name = input().strip()

# Open and read the CSV file
with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Initialize a list to store the dictionaries
    dictionaries = []
    
    # Read each row in the CSV file and convert it to a dictionary
    for row in csv_reader:
        row_dict = {row[i].strip(): row[i+1].strip() for i in range(0, len(row), 2)}
        dictionaries.append(row_dict)
        
    # Print the dictionaries
    for dictionary in dictionaries:
        print(dictionary)