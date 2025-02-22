filename = input().strip()

with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    modified_name = line.strip().replace("_photo.jpg", "_info.txt")
    print(modified_name)