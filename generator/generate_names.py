"""
D&D Name Generator — Console Utility

This script provides a command-line interface for generating random D&D names.
It checks for updates from a remote JSON source and allows the user to update
the local name database before generating names.

It is NOT required for the API to run. It can be used independently for testing,
data management, or offline name generation.

"""

import json
import random
import requests
from pathlib import Path

# -------------------- CONFIGURATION --------------------

# Path to the main database file (relative to this script)
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "names_database.json"

# -------------------- FUNCTIONS ------------------------


def load_database(file_path: Path):
    """
    Load the names database from a JSON file.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_for_updates(data: dict):
    """
    Check for a newer version of the database from the remote URL.

    If a newer version is found, prompts the user to update the local file.
    """
    local_version = data["meta"]["version"]
    update_url = data["meta"]["update_url"]

    try:
        response = requests.get(update_url, timeout=3)
        remote_data = response.json()
        remote_version = remote_data["meta"]["version"]
    except Exception:
        remote_version = None

    if remote_version and remote_version != local_version:
        print(f"New version is available: {remote_version} (Current version: {local_version})")
        answer = input("Do you wish to generate a new version (y/n)? ").lower()
        if answer in ['yes', 'y', 'да', 'д', 'а']:
            with open("../data/names_database.json", "w", encoding="utf-8") as f:
                json.dump(remote_data, f, ensure_ascii=False, indent=2)
            print("The database has been updated!")
            return remote_data

    return data


def generate_name(data: dict):
    """
    Run the interactive name generator loop.

    Allows the user to repeatedly generate names by entering a race name.
    Supports case-insensitive input and proves a list of available races.
    """

    races = data["races"]
    print("Available races:", ", ".join(races.keys()))

    while True:
        race = input("Enter the race: ").lower().capitalize()

        if race in data["races"]:
            prefixes = data["races"][race]["prefixes"]
            suffixes = data["races"][race]["suffixes"]
            name = random.choice(prefixes) + random.choice(suffixes)
            print(f"Generated Name: {name}")

            again_race = input("Generate another option (y/n)? ")
            if again_race in ['yes', 'y', 'да', 'д', 'а']:
                continue
            else:
                break
        else:
            print("Race not found. Available races:", ", ".join(races.keys()))

# -------------------- MAIN --------------------

def main():
    """
    Main entry point for the script.

    Loads the database, checks for updates and starts the interactive generator.
    """

    # Load database
    data = load_database(DB_PATH)
    print(f" Current version: {data['meta']['version']}")

    # Check for updates
    data = check_for_updates(data)

    # Start generator
    generate_name(data)

    print("\n Goodbye!")


if __name__ == "__main__":
    main()