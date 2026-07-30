"""
Tests for the D&D Name Generator API.
"""

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


# -------------------- ROOT ENDPOINT --------------------

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "DND Name Generator API is running"


# -------------------- GENERATE ENDPOINT --------------------

def test_generate_name_ru():
    response = client.get("/generate?race=Эльф&lang=ru")
    assert response.status_code == 200
    data = response.json()
    assert "race" in data
    assert "name" in data
    assert data["lang"] == "ru"


def test_generate_name_en():
    response = client.get("/generate?race=Elf&lang=en")
    assert response.status_code == 200
    data = response.json()
    assert "race" in data
    assert "name" in data
    assert data["lang"] == "en"


def test_generate_name_auto_lang():
    response = client.get("/generate?race=Эльф")
    assert response.status_code == 200
    data = response.json()
    assert data["lang"] in ["ru", "en"]


# -------------------- ERROR HANDLING --------------------

def test_generate_race_not_found():
    response = client.get("/generate?race=НеизвестнаяРаса&lang=ru")
    assert response.status_code == 400
    assert "error" in response.json()
    assert "available_races" in response.json()


def test_generate_lang_not_supported():
    response = client.get("/generate?race=Elf&lang=fr")
    assert response.status_code == 500
    data = response.json()
    assert data["error"] == "Race data not loaded."


def test_generate_missing_race_param():
    response = client.get("/generate")
    assert response.status_code == 422  # validation error


# -------------------- DATA LOADING --------------------

def test_data_loaded():
    """Check that race data is loaded for both languages."""
    from api.main import LANG_DB
    assert "ru" in LANG_DB
    assert "en" in LANG_DB
    assert len(LANG_DB["ru"]) > 0
    assert len(LANG_DB["en"]) > 0