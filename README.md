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
- [🌐 Инструкция по использованию D&D Name Generator API](#-инструкция-по-использованию-d&d-name-generator-api)
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
git clone https://github.com/cynicznykot/dnd-name-generator-api.git
cd dnd-name-generator-api
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

## 🌐 Примеры использования (C#, Python, JS) локально

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

## 📘 Инструкция по использованию D&D Name Generator API

### Базовая ссылка API:
```bash
https://dnd-name-generator-api.vercel.app
```

### Эндпоинт:
```bash
GET /generate
```

### Параметры:
```bash
Параметр	Тип	      Обязательный	   Описание
race	    string	  ✅ Да	           Название расы (например, Эльф, Elf, Дварф)
lang	    string	  ❌ Нет	           Язык ответа: ru (русский, по умолчанию) или en (английский)
```

### Пример запроса:
```bash
https://dnd-name-generator-api.vercel.app/generate?race=Эльф&lang=ru
```

### Пример ответа (JSON):
```json

{
  "race": "Эльф",
  "name": "Эльриэль",
  "lang": "ru"
}
```

### Ошибка (если раса не найдена):
```json
{
  "error": "Race 'НеизвестнаяРаса' not found.",
  "available_races": ["Эльф", "Дварф", ...]
}
```

### 🌐 Примеры на разных языках

### 1. C# (.NET)
```csharp
using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Collections.Generic;

public class DndNameClient : IDisposable
{
    private readonly HttpClient _httpClient;
    private readonly string _baseUrl;

    public DndNameClient(string baseUrl = "https://dnd-name-generator-api.vercel.app")
    {
        _httpClient = new HttpClient();
        _baseUrl = baseUrl.TrimEnd('/');
    }

    public async Task<string> GenerateNameAsync(string race, string lang = "ru")
    {
        if (string.IsNullOrWhiteSpace(race))
            throw new ArgumentException("Раса не может быть пустой.", nameof(race));

        string url = $"{_baseUrl}/generate?race={Uri.EscapeDataString(race)}&lang={lang}";
        string jsonResponse = await _httpClient.GetStringAsync(url);
        var result = JsonSerializer.Deserialize<Dictionary<string, string>>(jsonResponse);
        return result?["name"] ?? "Ошибка: имя не получено";
    }

    public void Dispose() => _httpClient?.Dispose();
}

// Пример использования
var client = new DndNameClient();
string name = await client.GenerateNameAsync("Эльф", "ru");
Console.WriteLine(name);
```

### 2. Python
```python
import requests

def generate_name(race, lang="ru"):
    base_url = "https://dnd-name-generator-api.vercel.app"
    params = {"race": race, "lang": lang}
    response = requests.get(f"{base_url}/generate", params=params)
    response.raise_for_status()
    data = response.json()
    return data["name"]

# Пример использования
name = generate_name("Эльф", "ru")
print(name)
```

### 3. JavaScript (Node.js / Fetch)
```javascript
// Node.js (axios)
const axios = require('axios');

async function generateName(race, lang = 'ru') {
    const baseUrl = 'https://dnd-name-generator-api.vercel.app';
    const response = await axios.get(`${baseUrl}/generate`, {
        params: { race, lang }
    });
    return response.data.name;
}

// Пример использования
generateName('Эльф', 'ru').then(console.log);
```

```javascript
// Браузер (fetch)
async function generateName(race, lang = 'ru') {
    const baseUrl = 'https://dnd-name-generator-api.vercel.app';
    const response = await fetch(`${baseUrl}/generate?race=${encodeURIComponent(race)}&lang=${lang}`);
    const data = await response.json();
    return data.name;
}

// Пример использования
generateName('Эльф', 'ru').then(console.log);
```

### 4. cURL (командная строка)
```java
curl "https://dnd-name-generator-api.vercel.app/generate?race=Эльф&lang=ru"

5. Java (Unirest / HttpClient)
java

import kong.unirest.Unirest;
import kong.unirest.HttpResponse;
import kong.unirest.JsonNode;

public class DndNameClient {
    private static final String BASE_URL = "https://dnd-name-generator-api.vercel.app";

    public static String generateName(String race, String lang) {
        HttpResponse<JsonNode> response = Unirest.get(BASE_URL + "/generate")
                .queryString("race", race)
                .queryString("lang", lang)
                .asJson();
        return response.getBody().getObject().getString("name");
    }

    public static void main(String[] args) {
        String name = generateName("Эльф", "ru");
        System.out.println(name);
    }
}
```

### 6. Ruby
```ruby

require 'net/http'
require 'json'

def generate_name(race, lang = 'ru')
    url = URI("https://dnd-name-generator-api.vercel.app/generate")
    params = {race: race, lang: lang}
    url.query = URI.encode_www_form(params)

    response = Net::HTTP.get_response(url)
    data = JSON.parse(response.body)
    data["name"]
end

# Пример использования
puts generate_name("Эльф", "ru")
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







