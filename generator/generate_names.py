import json
import random


with open("../data/names_database.json", "r", encoding="utf-8") as f:
    data = json.load(f)

version = data["meta"]["version"]
print(f"DND Name Generator v{version}")

races = data["races"]
print("Available races:", ", ".join(races.keys()))

while True:
    race = input("Enter the race: ").lower().capitalize()

    if race in data["races"]:
        prefixes = data["races"][race]["prefixes"]
        suffixes = data["races"][race]["suffixes"]
        name = random.choice(prefixes) + random.choice(suffixes)
        print(f"Name: {name}")

        again_race = input("Generate another option (y/n)? ")

        if again_race in ['yes', 'y', 'да', 'д', 'а']:
            continue
        else:
            break
    else:
        print("Race not found")

print("Goodbye!")

