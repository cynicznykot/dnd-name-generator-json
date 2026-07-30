"""
Tests for the console name generator (generate_names.py).
"""

import json
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from generator.generate_names import (
    load_database,
    check_for_updates,
    generate_name,
    main
)


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "names_database.json"

# -------------------- FIXTURES --------------------

@pytest.fixture
def sample_db():
    return {
        "meta": {
            "version": "1.0.0",
            "update_url": "https://example.com/update.json"
        },
        "races": {
            "Эльф": {
                "prefixes": ["Эль", "Галад", "Эл"],
                "suffixes": ["анор", "ион", "риэль"]
            },
            "Дварф": {
                "prefixes": ["Тор", "Бал", "Дур"],
                "suffixes": ["ин", "ур", "ар"]
            }
        }
    }


# -------------------- TESTS --------------------

def test_load_database(tmp_path, sample_db):
    """Test that load_database correctly loads JSON data."""
    db_file = tmp_path / "test_db.json"
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(sample_db, f, ensure_ascii=False, indent=2)

    data = load_database(db_file)
    assert data["meta"]["version"] == "1.0.0"
    assert "Эльф" in data["races"]
    assert "Дварф" in data["races"]


def test_load_database_file_not_found():
    """Test that load_database raises FileNotFoundError if file is missing."""
    with pytest.raises(FileNotFoundError):
        load_database(Path("/nonexistent/file.json"))

@patch("generator.generate_names.requests.get")
def test_check_for_updates_no_update(mock_get, tmp_path, sample_db):
    """Test that check_for_updates does nothing if version is the same."""
    db_path = tmp_path / "test_db.json"
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(sample_db, f, ensure_ascii=False, indent=2)

    with patch("generator.generate_names.DB_PATH", db_path):
        mock_response = mock_get.return_value
        mock_response.json.return_value = sample_db  # same version

        data = load_database(db_path)
        updated_data = check_for_updates(data)

        assert updated_data["meta"]["version"] == "1.0.0"


def test_generate_name(capsys, sample_db):
    """Test that generate_name prints available races and generates a name."""
    inputs = iter(["Эльф", "n"])
    with patch("builtins.input", side_effect=inputs):
        generate_name(sample_db)

    captured = capsys.readouterr()
    assert "Available races:" in captured.out
    assert "Эльф" in captured.out
    assert "Generated Name:" in captured.out


def test_generate_name_race_not_found(capsys, sample_db):
    """Test that generate_name handles unknown race gracefully."""
    inputs = iter(["НеизвестнаяРаса", "Эльф", "n"])  # ← добавили ещё одно значение
    with patch("builtins.input", side_effect=inputs):
        generate_name(sample_db)

    captured = capsys.readouterr()
    assert "Race not found." in captured.out
    assert "Available races:" in captured.out


def test_generate_name_multiple_attempts(capsys, sample_db):
    """Test that user can generate multiple names before exiting."""
    inputs = iter(["Эльф", "y", "Дварф", "n"])
    with patch("builtins.input", side_effect=inputs):
        generate_name(sample_db)

    captured = capsys.readouterr()
    assert "Эльф" in captured.out
    assert "Дварф" in captured.out


def test_generate_name_case_insensitive(capsys, sample_db):
    """Test that race input is case-insensitive."""
    inputs = iter(["эльф", "n"])
    with patch("builtins.input", side_effect=inputs):
        generate_name(sample_db)

    captured = capsys.readouterr()
    assert "Generated Name:" in captured.out