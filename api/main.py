import json
import random
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

with open ("../data/ru/names_database.json", "r", encoding="utf-8") as f:
    data_ru = json.load(f)
    races_ru = data_ru["races"]

with open("../data/en/names_database.json", "r", encoding="utf-8") as f:
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
    race: str = Query(..., description="Race name (e.g., Elf, Эльф)"),
    lang: str = Query("ru", description="Language: ru or en")
):

    if lang not in LANG_DB:
        return JSONResponse(
            status_code=400,
            content={"error": f"Language '{lang}' not supported. Use 'ru' or 'en'."}
        )

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