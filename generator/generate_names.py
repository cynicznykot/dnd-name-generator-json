import json
import random


with open("../data/names_database.json", "r", encoding="utf-8") as f:
    data = json.load(f)

race = input("Enter the race: ")

if race in data["races"]:
    prefixes = data["races"][race]["prefixes"]
    suffixes = data["races"][race]["suffixes"]
    name = random.choice(prefixes) + random.choice(suffixes)
    print(f"Name: {name}")
else:
    print("Race not found")

