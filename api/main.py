import json
import random
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

with open("../data/names_database.json", "r", encoding="utf-8") as f:
    data = json.load(f)

races = data["races"]

app = FastAPI(
    title="DND Name Generator API",
    description="Generate random names for D&D races",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "DND Name Generator API is running"}

@app.get("/generate")
def generate_name(race: str=Query(..., description="Race name(e.g., Elf, Dwarf)")):
    if race in races:
        prefixes = races[race]["prefixes"]
        suffixes = races[race]["suffixes"]
        name = random.choice(prefixes) + random.choice(suffixes)
        return {"race": race, "name": name}
    else:
        return JSONResponse(
            status_code=404,
            content={"error": f"Race '{race}' not found"}
        )

