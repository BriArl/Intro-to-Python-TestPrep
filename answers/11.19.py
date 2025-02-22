contacts_input = input()
search_name = input()

contacts = {}

for pair in contacts_input.split():
    name, phone = pair.split(',')
    contacts[name] = phone

print(contacts[search_name])