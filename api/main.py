import json
import os
import random
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ru_json_path = BASE_DIR / "data" / "ru" / "names_database.json"
en_json_path = BASE_DIR / "data" / "en" / "names_database.json"


def load_data(file_path):
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

app = FastAPI(
    title="DND Name Generator API",
    description="Generate random names for D&D races",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "DND Name Generator API is running", "status": "ok"}


@app.get("/generate")
def generate_name(race: str, request: Request, lang: str = None):
    if lang is None:
        accept_language = request.headers.get("accept-language", "ru")
        lang = accept_language[:2]
        if lang not in ["ru", "en"]:
            lang = "ru"

    races = LANG_DB.get(lang, {})

    if not races:
        return JSONResponse(
            status_code=500,
            content={"error": "Race data not loaded. Check server logs for missing JSON files."}
        )

    if race in races:
        prefixes = races[race]["prefixes"]
        suffixes = races[race]["suffixes"]
        name = random.choice(prefixes) + random.choice(suffixes)
        return {
            "race": race,
            "name": name,
            "lang": lang
        }
    else:
        return JSONResponse(
            status_code=400,
            content={"error": f"Race '{race}' not found in {lang}"}
        )