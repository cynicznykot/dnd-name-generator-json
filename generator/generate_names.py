import json
import random
import requests


with open("../data/names_database.json", "r", encoding="utf-8") as f:
    data = json.load(f)

local_version = data["meta"]["version"]
update_url = data["meta"]["update_url"]

try:
    response = requests.get(update_url, timeout=3)
    remote_data = response.json()
    remote_version = remote_data["meta"]["version"]
except:
    remote_version = None

if remote_version and remote_version != local_version:
    print(f"New version is available: {remote_version} (Current version: {local_version})")
    answer = input("Do you wish to generate a new version (y/n)? ").lower()
    if answer in ['yes', 'y', 'да', 'д', 'а']:
        with open("../data/names_database.json", "w", encoding="utf-8") as f:
            json.dump(remote_data, f, ensure_ascii=False, indent=2)
        print("The database has been updated!")
        data = remote_data
        local_version = remote_version



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

