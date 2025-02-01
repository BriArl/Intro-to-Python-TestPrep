# Step 1: Get filename from user
filename = input().strip()

# Step 2: Read file contents
with open(filename, 'r') as file:
    lines = file.readlines()

# Step 3: Process each line and replace "_photo.jpg" with "_info.txt"
for line in lines:
    modified_name = line.strip().replace("_photo.jpg", "_info.txt")
    print(modified_name)  # Output the new file name