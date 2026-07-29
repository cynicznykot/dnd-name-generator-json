import json
import os
import random
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi import Request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ru_json_path = os.path.join(BASE_DIR, "data", "ru", "names_database.json")
en_json_path = os.path.join(BASE_DIR, "data", "en", "names_database.json")

with open(ru_json_path, "r", encoding="utf-8") as f:
    data_ru = json.load(f)
    races_ru = data_ru["races"]

with open(en_json_path, "r", encoding="utf-8") as f:
    data_en = json.load(f)
    races_en = data_en["races"]

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
def generate_name(
    race: str,
    request: Request,
    lang: str = None
):

    if lang is None:
        accept_language = request.headers.get("accept-language", "ru")
        lang = accept_language[:2]

        if lang not in ["ru", "en"]:
            lang = "ru"

    races = LANG_DB[lang]

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