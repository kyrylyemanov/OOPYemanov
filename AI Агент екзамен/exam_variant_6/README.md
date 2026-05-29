# AI Агент - Варіант 6: Агент Бібліотечного Каталогу

## 📌 Опис завдання

Реалізація AI агента для управління бібліотечним каталогом з використанням системи класів на основі парадигм об'єктно-орієнтованого програмування.

## 🏗️ OOP Парадигми (Реалізовано все 4)

### 1️⃣ **Абстракція** (`LibraryItem`)
```python
class LibraryItem(ABC):
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        pass
```
- Абстрактний базовий клас з абстрактним методом
- Визначає контракт для всіх видань

### 2️⃣ **Наслідування** (`Book`, `Magazine`)
```python
class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages
```
- Класи `Book` та `Magazine` успадковують від `LibraryItem`
- Розширюють функціональність базового класу

### 3️⃣ **Інкапсуляція** (`Library`)
```python
class Library:
    def __init__(self):
        self.__catalog: List[LibraryItem] = []  # Приватний атрибут
```
- Приватний список `__catalog` доступний тільки через методи класу
- Методи: `add()`, `find()`, `list_all()`, `remove()`

### 4️⃣ **Поліморфізм** (Різна реалізація `get_info()`)
```python
# Book
def get_info(self):
    return {"type": "Book", "title": ..., "author": ..., "pages": ...}

# Magazine  
def get_info(self):
    return {"type": "Magazine", "title": ..., "issue": ..., "topic": ...}
```
- Один метод `get_info()` поводиться по-різному в кожному класі
- Агент викликає цей метод поліморфно

## 📁 Структура проекту

```
exam_variant_6/
├── agent.py              # Основний файл з OOP класами та AI агентом
├── venv/                 # Віртуальне середовище Python
├── pyproject.toml        # Конфігурація проекту
├── .env                  # Змінні середовища (НЕ комітити!)
├── .env.example          # Приклад змінних середовища
├── .gitignore            # Ігноровані файли
└── README.md             # Цей файл
```

## 🔧 Встановлення та налаштування

### Вимоги
- Python 3.10+
- Windows, macOS або Linux

### Кроки встановлення

1. **Переходимо до папки проекту:**
```bash
cd exam_variant_6
```

2. **Створюємо віртуальне середовище (якщо ще немає):**
```bash
# Windows
py -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Встановлюємо залежності:**
```bash
pip install google-genai python-dotenv
```

4. **Налаштовуємо змінні середовища:**
```bash
# Копіюємо приклад
cp .env.example .env

# Відкриваємо .env та вставляємо ваш Google API ключ:
# GOOGLE_API_KEY=YOUR_KEY_HERE
```

### Отримання Google API ключа

1. Перейдіть на https://ai.google.dev/
2. Натисніть "Get API Key"
3. Створіть проект або виберіть існуючий
4. Скопіюйте ваш API ключ
5. Вставте його в файл `.env`

## ▶️ Запуск проекту

### Запуск основної демонстрації
```bash
python agent.py
```

### Вивід програми показуватиме:
1. ✅ Демонстрацію всіх 4 OOP парадигм
2. 📚 Поточний каталог з книгами та журналами
3. 🤖 Тестові запити до AI агента
4. 📊 Результати роботи AI агента

## 📊 Приклад виходу

```
============================================================
AI АГЕНТ ДЛЯ БІБЛІОТЕЧНОГО КАТАЛОГУ - ВАРІАНТ 6
============================================================

📚 Демонстрація OOP парадигм:
  1. АБСТРАКЦІЯ: LibraryItem (абстрактний клас)
  2. НАСЛІДУВАННЯ: Book та Magazine успадковують LibraryItem
  3. ІНКАПСУЛЯЦІЯ: Приватний список __catalog у Library
  4. ПОЛІМОРФІЗМ: get_info() по-різному в Book та Magazine

📖 Поточний каталог:
  • Book: Война и мир (1869)
  • Book: Преступление и наказание (1866)
  • Magazine: National Geographic (2024)

🤖 Агент готовий до роботи!

📝 Запит 1: Розкажи мені про всі книги в каталозі
🤖 Відповідь: [Відповідь від AI агента]
```

## 🛠️ Функціональність

### OOP Класи
- ✅ `LibraryItem` - абстрактний базовий клас
- ✅ `Book` - клас для книг з полями author, pages
- ✅ `Magazine` - клас для журналів з полями issue, topic
- ✅ `Library` - менеджер каталогу з приватним __catalog

### Методи Library
- `add(item)` - додати видання до каталогу
- `find(title)` - пошук видання за назвою
- `list_all()` - отримати список всіх видань
- `remove(title)` - видалити видання
- `get_catalog_info()` - отримати комплексну інформацію

### AI Інструменти (Tools)
- `search_catalog` - пошук в каталозі
- `list_catalog` - отримати список видань (з фільтрацією)
- `get_catalog_stats` - статистика каталогу

## 📝 Приклади використання

### Додавання видання
```python
library = Library("Моя бібліотека")

book = Book("Война и мир", 1869, "Лев Толстой", 1200)
library.add(book)

magazine = Magazine("Science Today", 2024, 1, "Інновації")
library.add(magazine)
```

### Пошук видання
```python
item = library.find("Война и мир")
if item:
    print(item.get_info())
```

### Отримання всіх видань
```python
for item_info in library.list_all():
    print(f"{item_info['type']}: {item_info['title']}")
```

## ⚠️ Поширені проблеми

### API ключ не дійсний
- **Проблема:** `API key not valid`
- **Рішення:** Переконайтеся, що ви вставили правильний API ключ в `.env`

### Модуль не знайдено
- **Проблема:** `ModuleNotFoundError: No module named 'google'`
- **Рішення:** Переконайтеся, що встановлені залежності: `pip install google-genai python-dotenv`

### Проблеми з кодуванням українських символів
- **Проблема:** Знаки питання в виводі
- **Рішення:** Переконайтесь, що файл збережений як UTF-8

## 📚 Структура файлу agent.py

```python
# 1. OOP Класи (Абстракція, Наслідування, Інкапсуляція, Поліморфізм)
class LibraryItem(ABC):  # Абстракція
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        pass

class Book(LibraryItem):  # Наслідування
    def get_info(self):  # Поліморфізм
        return {...}

class Magazine(LibraryItem):  # Наслідування
    def get_info(self):  # Поліморфізм
        return {...}

class Library:  # Інкапсуляція
    def __init__(self):
        self.__catalog = []

# 2. AI Інструменти (Tools)
def search_catalog_tool(query: str) -> str:
    ...

def list_catalog_tool(filter_type: str) -> str:
    ...

def get_catalog_stats_tool() -> str:
    ...

# 3. AI Агент
def create_root_agent():
    ...

def run_agent_conversation(agent_config, user_message):
    ...

# 4. Головна функція
def main():
    ...
```

## ✅ Контрольний список здачі

- ✅ Проект у папці `exam_variant_6`
- ✅ Файл `agent.py` з усіма OOP класами
- ✅ Абстрактний клас `LibraryItem`
- ✅ Класи `Book` та `Magazine` з успадкуванням
- ✅ Клас `Library` з інкапсуляцією (`__catalog`)
- ✅ Поліморфізм у методі `get_info()`
- ✅ AI инструменти (tools) для роботи з каталогом
- ✅ Файл `.env` з налаштованим API ключем
- ✅ Файл `.gitignore` для ігнорування чутливих даних
- ✅ Файл `README.md` з документацією
- ✅ Встановлені залежності (google-genai, python-dotenv)
- ✅ Проект запускається без помилок

## 📖 Додаткові ресурси

- [Google AI Python SDK](https://github.com/googleapis/google-generative-ai-python)
- [Python ABC модуль](https://docs.python.org/3/library/abc.html)
- [OOP в Python](https://docs.python.org/3/tutorial/classes.html)

## 🎓 Автор

**Єманов** - Варіант 6 - Агент Бібліотечного Каталогу

Дата створення: 28.05.2026
