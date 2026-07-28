# D&D Name Generator API

A microservice for generating Dungeons & Dragons character names.  
Supports **10 races** in **two languages** (**Russian / English**).  
Built with **Python + FastAPI**.

---

## 📋 Table of Contents

- [🎯 For Whom This Project Is](#-for-whom-this-project-is)
- [⚙️ Technologies](#️-technologies)
- [📦 Installation and Setup](#-installation-and-setup)
- [📚 API Documentation](#-api-documentation)
- [🌐 Usage Examples](#-usage-examples)
- [🧩 Supported Races](#-supported-races)
- [📂 Project Structure](#-project-structure)
- [📜 License](#-license)
- [🤝 Contacts](#-contacts)

---

## 🎯 For Whom This Project Is

- For developers who want to integrate name generation into their applications.
- For Dungeon Masters who need ready-made names for NPCs.

---

## ⚙️ Technologies

- Python 3.10+
- FastAPI
- JSON
- Uvicorn

---

## 📦 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/cynicznykot/dnd-name-generator-json.git
cd dnd-name-generator-json
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the server
```bash
cd api
uvicorn main:app --reload
```
The server will be available at:
👉 http://127.0.0.1:8000

## 📚 API Documentation

After starting the server, documentation is available at:
👉 http://127.0.0.1:8000/docs (Swagger)

## 🌐 Usage Examples (C#, Python, JS)

# Russian
curl "http://localhost:8000/generate?race=Эльф&lang=ru"

# English
curl "http://localhost:8000/generate?race=Elf&lang=en"
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

## 🧩 Supported Races

```
🇬🇧 English        🇷🇺 Русский	      
Aasimar           Аасимар	          
Gnome             Гном	          
Goliath           Голиаф	          
Dwarf             Дварф	          
Dragonborn        Драконорожденный  
Orc               Орк	              
Halfling          Полурослик	      
Tiefling          Тифлинг	          
Human             Человек	          
Elf               Эльф	          
```

## 📂 Project Structure

```
dnd-name-generator/
├── api/
│   └── main.py                  # FastAPI server
├── data/
│   ├── ru/
│   │   └── names_database.json  # Russian names database
│   └── en/
│       └── names_database.json  # English names database
├── generator/
│   └── generate_names.py        # Script for updating JSON
├── requirements.txt
├── LICENSE
├── README.en.md
└── README.md
```

## 📜 License

MIT — use as you wish.

## 🤝 Contacts

Author: cynicznykot