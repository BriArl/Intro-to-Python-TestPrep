filename = input().strip()

with open(filename, 'r') as file:
    lines = file.readlines()

season_dict = {}

i = 0
while i < len(lines):
    season = int(lines[i].strip())
    show = lines[i + 1].strip()
    if season in season_dict:
        season_dict[season].append(show)
    else:
        season_dict[season] = [show]
    i += 2

with open("output_keys.txt", 'w') as out_keys:
    for season in sorted(season_dict.keys()):
        shows = "; ".join(season_dict[season])
        out_keys.write(f"{season}: {shows}\n")

all_shows = sorted([show for shows in season_dict.values() for show in shows])

with open("output_titles.txt", 'w') as out_titles:
    for show in all_shows:
        out_titles.write(f"{show}\n")