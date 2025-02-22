import csv

file_name = input().strip()

with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)
    
    dictionaries = []
    
    for row in csv_reader:
        row_dict = {row[i].strip(): row[i+1].strip() for i in range(0, len(row), 2)}
        dictionaries.append(row_dict)
        
    for dictionary in dictionaries:
        print(dictionary)