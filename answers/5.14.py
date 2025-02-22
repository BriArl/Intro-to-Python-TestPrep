highway_number = int(input())

if highway_number < 1 or highway_number > 999 or (highway_number > 99 and highway_number % 100 == 0):
    print(f"{highway_number} is not a valid interstate highway number.")
else:
    if highway_number <= 99:
        direction = "north/south" if highway_number % 2 != 0 else "east/west"
        print(f"I-{highway_number} is primary, going {direction}.")
    else:
        primary_highway = highway_number % 100
        direction = "north/south" if primary_highway % 2 != 0 else "east/west"
        print(f"I-{highway_number} is auxiliary, serving I-{primary_highway}, going {direction}.")