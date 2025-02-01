# Step 1: Read file name from input
filename = input().strip()

# Step 2: Read file contents
with open(filename, 'r') as file:
    lines = file.readlines()

# Step 3: Process lines into a dictionary
season_dict = {}  # Dictionary to store seasons as keys, show lists as values

i = 0
while i < len(lines):
    season = int(lines[i].strip())  # Convert season count to int
    show = lines[i + 1].strip()     # Get the corresponding TV show
    if season in season_dict:
        season_dict[season].append(show)  # Append to existing list
    else:
        season_dict[season] = [show]  # Create new list
    i += 2  # Move to the next season-show pair

# Step 4: Sort by seasons (keys) and write to output_keys.txt
with open("output_keys.txt", 'w') as out_keys:
    for season in sorted(season_dict.keys()):  # Sort by season count
        shows = "; ".join(season_dict[season])  # Join multiple shows with semicolons
        out_keys.write(f"{season}: {shows}\n")

# Step 5: Sort TV shows alphabetically and write to output_titles.txt
all_shows = sorted([show for shows in season_dict.values() for show in shows])

with open("output_titles.txt", 'w') as out_titles:
    for show in all_shows:
        out_titles.write(f"{show}\n")