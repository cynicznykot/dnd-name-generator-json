import json
import os
import random
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ru_json_path = BASE_DIR / "data" / "ru" / "names_database.json"
en_json_path = BASE_DIR / "data" / "en" / "names_database.json"


def load_race_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("races", {})
    except FileNotFoundError:
        print(f"❌ ОШИБКА: Не найден файл {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"❌ ОШИБКА: Файл {file_path} поврежден (невалидный JSON)")
        return {}


races_ru = load_race_data(ru_json_path)
races_en = load_race_data(en_json_path)

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
    return {"message": "DND Name Generator API is running"}


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
            content={"error": f"Language data '{lang}' not loaded."}
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