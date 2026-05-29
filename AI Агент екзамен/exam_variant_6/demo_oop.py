"""
Демонстрація OOP парадигм - Варіант 6
Цей скрипт демонструє всі 4 парадигми ООП без потреби Google API
"""

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any


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
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Отримати статистику каталогу
        
        Returns:
            Словник зі статистикою
        """
        items = self.list_all()
        books_count = sum(1 for item in items if item["type"] == "Book")
        magazines_count = sum(1 for item in items if item["type"] == "Magazine")
        
        return {
            "library_name": self.name,
            "total_items": len(items),
            "books": {
                "count": books_count,
                "percentage": round((books_count / len(items) * 100), 1) if items else 0
            },
            "magazines": {
                "count": magazines_count,
                "percentage": round((magazines_count / len(items) * 100), 1) if items else 0
            }
        }


# ==================== ДЕМОНСТРАЦІЯ ====================

def main():
    """Демонстрація всіх OOP парадигм"""
    
    print("=" * 70)
    print("ДЕМОНСТРАЦІЯ OOP ПАРАДИГМ - ВАРІАНТ 6")
    print("Агент Бібліотечного Каталогу")
    print("=" * 70)
    print()
    
    # ===== ДЕМОНСТРАЦІЯ АБСТРАКЦІЇ =====
    print("1️⃣  АБСТРАКЦІЯ - LibraryItem")
    print("-" * 70)
    print("Абстрактний клас LibraryItem з абстрактним методом get_info()")
    print("Неможливо створити екземпляр LibraryItem безпосередньо")
    print("Кожний підклас ПОВИНЕН реалізувати метод get_info()")
    print()
    
    # ===== ДЕМОНСТРАЦІЯ НАСЛІДУВАННЯ =====
    print("2️⃣  НАСЛІДУВАННЯ - Book та Magazine")
    print("-" * 70)
    
    # Створюємо книги
    book1 = Book("Война и мир", 1869, "Лев Толстой", 1200)
    book2 = Book("Преступление и наказание", 1866, "Федор Достоевский", 671)
    book3 = Book("Мертвые души", 1842, "Николай Гоголь", 432)
    
    print(f"Створена книга 1: {book1}")
    print(f"Створена книга 2: {book2}")
    print(f"Створена книга 3: {book3}")
    print()
    
    # Створюємо журнали
    mag1 = Magazine("National Geographic", 2024, 1, "Природа и космос")
    mag2 = Magazine("Science Today", 2024, 3, "Инновации в технологии")
    
    print(f"Створений журнал 1: {mag1}")
    print(f"Створений журнал 2: {mag2}")
    print()
    
    # ===== ДЕМОНСТРАЦІЯ ІНКАПСУЛЯЦІЇ =====
    print("3️⃣  ІНКАПСУЛЯЦІЯ - Приватний список __catalog")
    print("-" * 70)
    
    library = Library("Бібліотека Варіанту 6")
    
    print(f"Створена бібліотека: '{library.name}'")
    print("Додавання видань до каталогу...")
    print()
    
    # Додаємо видання
    library.add(book1)
    library.add(book2)
    library.add(book3)
    library.add(mag1)
    library.add(mag2)
    
    print("✅ Видання успішно додані")
    print()
    print("📝 Приватний атрибут __catalog:")
    print("   - Недоступний для прямого звернення: library.__catalog ❌")
    print("   - Доступний через методи класу: library.list_all() ✅")
    print()
    
    # ===== ДЕМОНСТРАЦІЯ ПОЛІМОРФІЗМУ =====
    print("4️⃣  ПОЛІМОРФІЗМ - Метод get_info()")
    print("-" * 70)
    print("Один метод get_info() поводиться по-різному в різних класах:\n")
    
    print("📕 Book.get_info():")
    print(f"   {book1.get_info()}\n")
    
    print("📰 Magazine.get_info():")
    print(f"   {mag1.get_info()}\n")
    
    print("Коли ми викликаємо get_info() на всіх елементах,")
    print("кожен елемент знає як себе представити:\n")
    
    for item_info in library.list_all():
        print(f"  • {item_info['type']:10} | {item_info['title']:30} | {item_info['year']}")
    print()
    
    # ===== ФУНКЦІОНАЛЬНІСТЬ =====
    print("=" * 70)
    print("ФУНКЦІОНАЛЬНІСТЬ БІБЛІОТЕКИ")
    print("=" * 70)
    print()
    
    # Пошук
    print("🔍 Пошук видання:")
    search_result = library.find("Война и мир")
    if search_result:
        print(f"   Знайдено: {search_result.get_info()}")
    print()
    
    # Статистика
    print("📊 Статистика каталогу:")
    stats = library.get_statistics()
    print(f"   Назва: {stats['library_name']}")
    print(f"   Всього видань: {stats['total_items']}")
    print(f"   Книг: {stats['books']['count']} ({stats['books']['percentage']}%)")
    print(f"   Журналів: {stats['magazines']['count']} ({stats['magazines']['percentage']}%)")
    print()
    
    # Видалення
    print("🗑️  Видалення видання:")
    print(f"   Видалення 'Война и мир'... ", end="")
    if library.remove("Война и мир"):
        print("✅ Успішно")
    print(f"   Сумарно видань: {len(library.list_all())}")
    print()
    
    # Остаточний каталог
    print("=" * 70)
    print("ОСТАТОЧНИЙ КАТАЛОГ")
    print("=" * 70)
    catalog_info = library.get_catalog_info()
    print(f"\n📚 {catalog_info['library_name']}")
    print(f"   Видань: {catalog_info['total_items']}\n")
    
    for idx, item in enumerate(catalog_info['items'], 1):
        if item['type'] == 'Book':
            print(f"   {idx}. 📕 {item['title']}")
            print(f"      Автор: {item['author']}, Сторінок: {item['pages']}, Рік: {item['year']}")
        else:
            print(f"   {idx}. 📰 {item['title']}")
            print(f"      Випуск: {item['issue']}, Тема: {item['topic']}, Рік: {item['year']}")
    
    print()
    print("=" * 70)
    print("✅ ДЕМОНСТРАЦІЯ ЗАВЕРШЕНА")
    print("=" * 70)
    print()
    print("📋 Підсумок OOP парадигм:")
    print("   ✅ Абстракція - Абстрактний клас LibraryItem")
    print("   ✅ Наслідування - Класи Book та Magazine успадковують LibraryItem")
    print("   ✅ Інкапсуляція - Приватний список __catalog у Library")
    print("   ✅ Поліморфізм - Метод get_info() у Book та Magazine")
    print()


if __name__ == "__main__":
    main()
