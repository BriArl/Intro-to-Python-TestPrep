# Read input for contacts and search name
contacts_input = input()
search_name = input()

# Create a dictionary for storing contacts
contacts = {}

# Split the input into pairs
for pair in contacts_input.split():
    name, phone = pair.split(',')
    contacts[name] = phone  # Store in dictionary

# Output the phone number for the searched name
print(contacts[search_name])