# D&D Name Generator API

Микросервис для генерации имён персонажей Dungeons & Dragons.  
Поддерживает **10 рас**. 
Написан на **Python + FastAPI**.

---

## 📋 Оглавление

- [🎯 Для кого этот проект](#-для-кого-этот-проект)
- [⚙️ Технологии](#️-технологии)
- [📦 Установка и запуск](#-установка-и-запуск)
- [📚 API Документация](#-api-документация)
- [🌐 Примеры использования](#-примеры-использования)
- [🧩 Поддерживаемые расы](#-поддерживаемые-расы)
- [📂 Структура проекта](#-структура-проекта)
- [📜 Лицензия](#-лицензия)
- [🤝 Контакты](#-контакты)

## 🎯 Для кого этот проект

- Для разработчиков, которые хотят встроить генерацию имён в свои приложения.
- Для Dungeon Masters, которым нужны готовые имена для NPC.

---

## ⚙️ Технологии

- Python 3.10+
- FastAPI
- JSON
- Uvicorn

---

## 📦 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/cynicznykot/dnd-name-generator-json.git
cd dnd-name-generator-json
```

### 2. Создай виртуальное окружение
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 3. Установи зависимости 
```bash
pip install -r requirements.txt
```

### 4. Запусти сервер
```bash
cd api
uvicorn main:app --reload
```
Сервер будет доступен по адресу:
👉 http://127.0.0.1:8000

## 📚 API Документация

После запуска сервера документация доступна по адресу:
👉 http://127.0.0.1:8000/docs (Swagger)

## 🌐 Примеры использования (C#, Python, JS)

### Python

```python
import requests

race = "Эльф"   # или "Elf"
lang = "ru"     # или "en"

response = requests.get("http://localhost:8000/generate", params={
    "race": race,
    "lang": lang
})

print(response.json()["name"])
```

### C# (.NET)

```csharp
using System.Net.Http;
using System.Text.Json;

var client = new HttpClient();
string selectedRace = "Эльф";   // или "Elf"
string lang = "ru";             // или "en"

string url = $"http://localhost:8000/generate?race={selectedRace}&lang={lang}";
string response = await client.GetStringAsync(url);
var json = JsonSerializer.Deserialize<Dictionary<string, string>>(response);
Console.WriteLine(json["name"]);
```

### JavaScript (fetch)

```javascript
const race = "Эльф";   // или "Elf"
const lang = "ru";     // или "en"

const response = await fetch(`http://localhost:8000/generate?race=${race}&lang=${lang}`);
const data = await response.json();
console.log(data.name);
```

## 🧩 Поддерживаемые расы

```
🇷🇺 Русский	      🇬🇧 English
Аасимар	          Aasimar
Гном	          Gnome
Голиаф	          Goliath
Дварф	          Dwarf
Драконорожденный  Dragonborn
Орк	              Orc
Полурослик	      Halfling
Тифлинг	          Tiefling
Человек	          Human
Эльф	          Elf
```

## 📂 Структура проекта

```
dnd-name-generator/
├── api/
│   └── main.py                  # FastAPI сервер
├── data/
│   ├── ru/
│   │   └── names_database.json  # Русская база данных
│   └── en/
│       └── names_database.json  # Английская база данных
├── generator/
│   └── generate_names.py        # Скрипт для обновления JSON
├── requirements.txt
├── LICENSE
├── README.en.md
└── README.md
```

## 📜 Лицензия

MIT — используйте как хотите.

## 🤝 Контакты

Автор: cynicznykot







