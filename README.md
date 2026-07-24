# D&D Name Generator API

Микросервис для генерации имён персонажей Dungeons & Dragons.  
Поддерживает **10 рас**. Написан на **Python + FastAPI**.

---

## 🎯 Для кого этот проект

- Для разработчиков, которые хотят встроить генерацию имён в свои приложения.
- Для Dungeon Masters, которым нужны готовые имена для NPC.
- Для твоего друга, который пишет C# приложение и хочет использовать генератор без лишней логики.

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

# В реальном приложении расу выбирает пользователь
race = "Elf"  # Замените на выбор пользователя

response = requests.get("http://localhost:8000/generate", params={"race": race})
print(response.json()["name"])
```

### C# (.NET)

```csharp
using System.Net.Http;
using System.Text.Json;

// В реальном приложении расу выбирает пользователь
string selectedRace = "Elf";  // Замените на raceComboBox.Text

string url = $"http://localhost:8000/generate?race={selectedRace}";
string response = await client.GetStringAsync(url);
var json = JsonSerializer.Deserialize<Dictionary<string, string>>(response);
Console.WriteLine(json["name"]);
```

### JavaScript (fetch)

```javascript
// В реальном приложении расу выбирает пользователь
const race = "Elf";  // Замените на document.getElementById("raceSelect").value

const response = await fetch(`http://localhost:8000/generate?race=${race}`);
const data = await response.json();
console.log(data.name);
```

## 📂 Структура проекта

dnd-name-generator/
├── api/
│   └── main.py              # FastAPI сервер
├── data/
│   └── names_database.json  # База данных
├── generator/
│   └── generate_names.py    # Скрипт для обновления JSON
├── requirements.txt
├── LICENSE
├── README.en.md
└── README.md

## 📜 Лицензия

MIT — используйте как хотите.







