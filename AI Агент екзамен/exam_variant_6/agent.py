"""
AI Агент для управління бібліотечним каталогом
Варіант 6 - демонстрація всіх 4 парадигм ООП
"""

import os
import json
from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv
import google.genai as genai

# Завантажуємо змінні середовища
load_dotenv()

# ==================== OOP ПАРАДИГМИ ====================

# 1. АБСТРАКЦІЯ - Абстрактний клас з абстрактним методом
class LibraryItem(ABC):
    """
    Абстрактний клас для елементів бібліотеки
    Демонструє парадигму АБСТРАКЦІЇ
    """
    
    def __init__(self, title: str, year: int):
        """
        Ініціалізація базових атрибутів
        
        Args:
            title: Назва видання
            year: Рік видання
        """
        self.title = title
        self.year = year
    
    @abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """
        Абстрактний метод для отримання інформації про видання
        Кожний підклас повинен реалізувати цей метод
        
        Returns:
            Словник з інформацією про видання
        """
        pass


# 2. НАСЛІДУВАННЯ - Класи, які успадковують LibraryItem
class Book(LibraryItem):
    """
    Клас для книг
    Демонструє парадигму НАСЛІДУВАННЯ
    """
    
    def __init__(self, title: str, year: int, author: str, pages: int):
        """
        Ініціалізація книги
        
        Args:
            title: Назва книги
            year: Рік видання
            author: Автор
            pages: Кількість сторінок
        """
        super().__init__(title, year)
        self.author = author
        self.pages = pages
    
    # 4. ПОЛІМОРФІЗМ - Різна реалізація абстрактного методу
    def get_info(self) -> Dict[str, Any]:
        """
        Реалізація методу get_info для книги
        Демонструє парадигму ПОЛІМОРФІЗМУ
        """
        return {
            "type": "Book",
            "title": self.title,
            "year": self.year,
            "author": self.author,
            "pages": self.pages
        }
    
    def __repr__(self) -> str:
        return f"Book('{self.title}' by {self.author}, {self.year}, {self.pages}pp)"


class Magazine(LibraryItem):
    """
    Клас для журналів
    Демонструє парадигму НАСЛІДУВАННЯ
    """
    
    def __init__(self, title: str, year: int, issue: int, topic: str):
        """
        Ініціалізація журналу
        
        Args:
            title: Назва журналу
            year: Рік видання
            issue: Номер випуску
            topic: Тема номера
        """
        super().__init__(title, year)
        self.issue = issue
        self.topic = topic
    
    # 4. ПОЛІМОРФІЗМ - Різна реалізація абстрактного методу
    def get_info(self) -> Dict[str, Any]:
        """
        Реалізація методу get_info для журналу
        Демонструє парадигму ПОЛІМОРФІЗМУ
        """
        return {
            "type": "Magazine",
            "title": self.title,
            "year": self.year,
            "issue": self.issue,
            "topic": self.topic
        }
    
    def __repr__(self) -> str:
        return f"Magazine('{self.title}', Issue {self.issue}: {self.topic}, {self.year})"


# 3. ІНКАПСУЛЯЦІЯ - Приватні атрибути та методи
class Library:
    """
    Клас для управління бібліотечним каталогом
    Демонструє парадигму ІНКАПСУЛЯЦІЇ за допомогою приватного списку __catalog
    """
    
    def __init__(self, name: str = "Main Library"):
        """
        Ініціалізація бібліотеки
        
        Args:
            name: Назва бібліотеки
        """
        self.name = name
        # ІНКАПСУЛЯЦІЯ: приватний список __catalog доступний тільки методам класу
        self.__catalog: List[LibraryItem] = []
    
    def add(self, item: LibraryItem) -> bool:
        """
        Додавання видання до каталогу
        
        Args:
            item: Видання для додавання
            
        Returns:
            True якщо успішно додано, False якщо видання вже існує
        """
        # Перевіряємо, чи видання вже в каталозі
        if self.find(item.title):
            return False
        
        self.__catalog.append(item)
        return True
    
    def find(self, title: str) -> Optional[LibraryItem]:
        """
        Пошук видання за назвою
        
        Args:
            title: Назва видання для пошуку
            
        Returns:
            Видання якщо знайдене, None якщо не знайдене
        """
        for item in self.__catalog:
            if item.title.lower() == title.lower():
                return item
        return None
    
    def list_all(self) -> List[Dict[str, Any]]:
        """
        Отримати інформацію про всі видання в каталозі
        Демонструє ПОЛІМОРФІЗМ - кожне видання має свою реалізацію get_info()
        
        Returns:
            Список словників з інформацією про видання
        """
        return [item.get_info() for item in self.__catalog]
    
    def get_catalog_info(self) -> Dict[str, Any]:
        """
        Отримати комплексну інформацію про каталог
        
        Returns:
            Словник з інформацією про бібліотеку
        """
        return {
            "library_name": self.name,
            "total_items": len(self.__catalog),
            "items": self.list_all()
        }
    
    def remove(self, title: str) -> bool:
        """
        Видалити видання з каталогу
        
        Args:
            title: Назва видання для видалення
            
        Returns:
            True якщо успішно видалено, False якщо видання не знайдене
        """
        item = self.find(title)
        if item:
            self.__catalog.remove(item)
            return True
        return False


# ==================== AI АГЕНТ ====================

# Ініціалізуємо глобальну бібліотеку для роботи з агентом
library = Library("Бібліотека Варіанту 6")

# Попередньо завантажуємо деяке тестові дані
library.add(Book("Война и мир", 1869, "Лев Толстой", 1200))
library.add(Book("Преступление и наказание", 1866, "Федор Достоевский", 671))
library.add(Book("Мертвые души", 1842, "Николай Гоголь", 432))
library.add(Magazine("National Geographic", 2024, 1, "Природа и космос"))
library.add(Magazine("Science Today", 2024, 3, "Инновации в технологии"))


def search_catalog_tool(query: str) -> str:
    """
    Інструмент для пошуку в каталозі
    
    Args:
        query: Запит для пошуку (назва видання)
        
    Returns:
        JSON-рядок з результатами пошуку
    """
    item = library.find(query)
    
    if item:
        return json.dumps({
            "status": "found",
            "message": f"Видання '{query}' знайдене",
            "data": item.get_info()
        }, ensure_ascii=False, indent=2)
    else:
        return json.dumps({
            "status": "not_found",
            "message": f"Видання '{query}' не знайдене в каталозі",
            "suggestion": "Спробуйте пошук з іншою назвою або перегляньте весь каталог"
        }, ensure_ascii=False, indent=2)


def list_catalog_tool(filter_type: str = "all") -> str:
    """
    Інструмент для отримання списку всіх видань або фільтрованого списку
    
    Args:
        filter_type: Тип фільтра ('all', 'books', 'magazines')
        
    Returns:
        JSON-рядок з каталогом
    """
    catalog_info = library.get_catalog_info()
    
    if filter_type in ["books", "magazines"]:
        # Фільтруємо за типом
        filter_name = filter_type[:-1]  # 'books' -> 'book', 'magazines' -> 'magazine'
        catalog_info["items"] = [
            item for item in catalog_info["items"]
            if item["type"].lower() == filter_name
        ]
        catalog_info["filter"] = filter_type
    
    return json.dumps(catalog_info, ensure_ascii=False, indent=2)


def get_catalog_stats_tool() -> str:
    """
    Інструмент для отримання статистики каталогу
    
    Returns:
        JSON-рядок зі статистикою
    """
    items = library.list_all()
    books_count = sum(1 for item in items if item["type"] == "Book")
    magazines_count = sum(1 for item in items if item["type"] == "Magazine")
    
    return json.dumps({
        "library_name": library.name,
        "total_items": len(items),
        "books_count": books_count,
        "magazines_count": magazines_count,
        "stats": {
            "books_percentage": round((books_count / len(items) * 100), 1) if items else 0,
            "magazines_percentage": round((magazines_count / len(items) * 100), 1) if items else 0
        }
    }, ensure_ascii=False, indent=2)


# Визначаємо інструменти для агента
tools = [
    {
        "name": "search_catalog",
        "description": "Пошук видання в каталозі за назвою",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Назва видання для пошуку"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "list_catalog",
        "description": "Отримати список всіх видань або фільтрований список",
        "input_schema": {
            "type": "object",
            "properties": {
                "filter_type": {
                    "type": "string",
                    "enum": ["all", "books", "magazines"],
                    "description": "Тип фільтра для каталогу"
                }
            },
            "required": ["filter_type"]
        }
    },
    {
        "name": "get_catalog_stats",
        "description": "Отримати статистику про каталог (кількість книг, журналів тощо)",
        "input_schema": {
            "type": "object",
            "properties": {}
        }
    }
]


def process_tool_call(tool_name: str, tool_input: Dict[str, Any]) -> str:
    """
    Обробка виклику інструменту
    
    Args:
        tool_name: Назва інструменту
        tool_input: Вхідні параметри інструменту
        
    Returns:
        Результат виконання інструменту
    """
    if tool_name == "search_catalog":
        return search_catalog_tool(tool_input.get("query", ""))
    elif tool_name == "list_catalog":
        return list_catalog_tool(tool_input.get("filter_type", "all"))
    elif tool_name == "get_catalog_stats":
        return get_catalog_stats_tool()
    else:
        return json.dumps({
            "error": f"Невідомий інструмент: {tool_name}"
        }, ensure_ascii=False)


def create_root_agent():
    """
    Створюємо та налаштовуємо AI агента
    
    Returns:
        Налаштований агент
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY не встановлено в змінних середовища. "
            "Будь ласка, додайте його в файл .env"
        )
    
    # Налаштовуємо клієнт Google Generative AI
    client = genai.Client(api_key=api_key)
    
    # Визначаємо системний промпт для агента
    system_prompt = """Ви - помічник бібліотечного каталогу. Ваша роль допомагати користувачам:
1. Шукати книги та журнали в каталозі
2. Отримувати інформацію про видання
3. Переглядати статистику каталогу
4. Надавати рекомендації щодо видань

Користуйтесь наданими інструментами для роботи з каталогом. Надавайте чіткі та корисні відповіді.
Якщо видання не знайдене, пропонуйте альтернативні варіанти пошуку.

Мова спілкування: Українська"""
    
    return {
        "client": client,
        "system_prompt": system_prompt,
        "tools": tools
    }


def run_agent_conversation(agent_config: Dict, user_message: str) -> str:
    """
    Запустити розмову з агентом
    
    Args:
        agent_config: Конфігурація агента
        user_message: Повідомлення користувача
        
    Returns:
        Відповідь агента
    """
    client = agent_config["client"]
    system_prompt = agent_config["system_prompt"]
    
    try:
        # Створюємо повне повідомлення з системним промптом
        full_message = f"{system_prompt}\n\nЗапит користувача: {user_message}"
        
        # Надсилаємо запит до моделі без system_instruction параметра
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=full_message
        )
        
        # Обробляємо відповідь
        if response and hasattr(response, 'text'):
            return response.text
        
        # Якщо відповідь має формат з частинами (parts)
        if hasattr(response, 'candidates') and response.candidates:
            for candidate in response.candidates:
                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                    text_parts = []
                    for part in candidate.content.parts:
                        if hasattr(part, 'text'):
                            text_parts.append(part.text)
                    if text_parts:
                        return "\n".join(text_parts)
        
        return "Агент відповідь надав, але формат незрозумілий"
    
    except Exception as e:
        return f"Помилка при запиті до агента: {str(e)}"


def main():
    """
    Головна функція для демонстрації роботи агента
    """
    print("=" * 60)
    print("AI АГЕНТ ДЛЯ БІБЛІОТЕЧНОГО КАТАЛОГУ - ВАРІАНТ 6")
    print("=" * 60)
    print()
    
    print("📚 Демонстрація OOP парадигм:")
    print("  1. АБСТРАКЦІЯ: LibraryItem (абстрактний клас)")
    print("  2. НАСЛІДУВАННЯ: Book та Magazine успадковують LibraryItem")
    print("  3. ІНКАПСУЛЯЦІЯ: Приватний список __catalog у Library")
    print("  4. ПОЛІМОРФІЗМ: get_info() по-різному в Book та Magazine")
    print()
    
    print("📖 Поточний каталог:")
    print("-" * 60)
    for item in library.list_all():
        print(f"  • {item['type']}: {item['title']} ({item['year']})")
    print()
    
    try:
        # Ініціалізуємо агента
        print("🤖 Ініціалізація AI агента...")
        agent_config = create_root_agent()
        print("✓ Агент готовий до роботи!")
        print()
        
        # Тестові запити
        test_queries = [
            "Розкажи мені про всі книги в каталозі",
            "Знайди журнал про технологію",
            "Скільки видань всього в каталозі? Дай статистику"
        ]
        
        print("=" * 60)
        print("ТЕСТОВІ ЗАПИТИ:")
        print("=" * 60)
        
        for i, query in enumerate(test_queries, 1):
            print(f"\n📝 Запит {i}: {query}")
            print("-" * 60)
            response = run_agent_conversation(agent_config, query)
            print(f"🤖 Відповідь:\n{response}")
            print()
    
    except ValueError as e:
        print(f"❌ Помилка конфігурації: {e}")
        print("\n💡 Рішення:")
        print("  1. Створіть файл .env в папці проекту")
        print("  2. Скопіюйте вміст з .env.example")
        print("  3. Додайте ваш Google API ключ")
        print("  4. Збережіть та запустіть знову")
    
    except Exception as e:
        print(f"❌ Помилка під час роботи агента: {e}")
        print(f"   Деталі: {type(e).__name__}")
        
        # Демонстрація OOP функціональності
        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦІЯ OOP ФУНКЦІОНАЛЬНОСТІ (без AI):")
        print("=" * 60)
        
        book = Book("Тестова книга", 2024, "Автор", 300)
        magazine = Magazine("Тестовий журнал", 2024, 1, "Наука")
        
        print(f"\n📕 Книга: {book}")
        print(f"   Info: {book.get_info()}")
        
        print(f"\n📰 Журнал: {magazine}")
        print(f"   Info: {magazine.get_info()}")


if __name__ == "__main__":
    main()
