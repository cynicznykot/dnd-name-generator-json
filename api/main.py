"""
D&D Name Generator API

This module provides a REST API for generating random character names
for 10 D&D races. Supports both Russian and English languages.

Endpoints:
- GET / → health check.
- GET /generate → generate a random name for a given race.

Language detection:
- If `lang` is not provided, the API tries to read the `Accept-Language` header.
- Defaults to `ru` (Russian) if detection fails.

Data source:
- JSON files with name prefixes and suffixes per race.
- Data is stored separately per language: data/ru/ and data/en/.
"""

import json
import os
import random
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pathlib import Path

# -------------------- LOAD DATA --------------------

BASE_DIR = Path(__file__).resolve().parent.parent
ru_json_path = BASE_DIR / "data" / "ru" / "names_database.json"
en_json_path = BASE_DIR / "data" / "en" / "names_database.json"

def load_data(file_path):
    """
    Load data from a JSON file.

    If the file is not found or an error occurs during reading,
    prints an error message and returns an empty dictionary.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"CRITICAL ERROR: File not found at {file_path}")
        return {"races": {}}
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to load file {file_path}: {e}")
        return {"races": {}}


data_ru = load_data(ru_json_path)
data_en = load_data(en_json_path)

races_ru = data_ru.get("races", {})
races_en = data_en.get("races", {})

LANG_DB = {
    "ru": races_ru,
    "en": races_en
}

# -------------------- FASTAPI APP --------------------

app = FastAPI(
    title="DND Name Generator API",
    description="Generate random names for D&D races",
    version="1.0.0"
)


@app.get("/")
def root():
    """
    Root endpoint.

    Returns a health check message to confirm the API is running.
    """
    return {"message": "DND Name Generator API is running", "status": "ok"}


@app.get("/generate")
def generate_name(race: str, request: Request, lang: str = None):
    """
    Generate a random name for the specified race.

    If 'lang' is not provided, the language is inferred from the
    'Accept-Language' header. Only 'ru' and 'en' are supported.
    On error, return a list of available races.
    """
    # Language detection
    if lang is None:
        accept_language = request.headers.get("accept-language", "ru")
        lang = accept_language[:2]
        if lang not in ["ru", "en"]:
            lang = "ru"

    races = LANG_DB.get(lang, {})

    if not races:
        return JSONResponse(
            status_code=500,
            content={"error": "Race data not loaded."}
        )

    # Case-insensitive race lookup
    found_race = None
    race_input_lower = race.strip().lower()

    for existing_race in races.keys():
        if existing_race.strip().lower() == race_input_lower:
            found_race = existing_race
            break

    if found_race:
        prefixes = races[found_race]["prefixes"]
        suffixes = races[found_race]["suffixes"]
        name = random.choice(prefixes) + random.choice(suffixes)
        return {
            "race": found_race,
            "name": name,
            "lang": lang
        }
    else:
        return JSONResponse(
            status_code=400,
            content={
                "error": f"Раса '{race}' не найдена.",
                "available_races": list(races.keys())
            }
        )