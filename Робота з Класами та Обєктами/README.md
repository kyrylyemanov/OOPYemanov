![alt text](logo-lit.jpg)
Звіт до роботи
Тема:

Основи об’єктно-орієнтованого програмування (ООП) у Python

Мета роботи:

Навчитись використовувати основні принципи ООП, створювати класи, об’єкти та застосовувати їхні властивості й методи.

Виконання роботи
1. Результати виконання завдання

i. Розробили клас Student:

реалізовано змінну класу total_students;

створено ініціалізатор __init__;

додано методи: info, email, greet, default_student, motivation_quote.

ii. Програма вивела такі результати:
(приклад виводу в консолі)

Student #1: Ігор
Email: ігор@college.edu
Привітання: Вітаю, мене звати Ігор!
Цитата: Пам’ятай: знання — це сила 💡
----------------------------------------
Student #2: Anonymous
Email: anonymous@college.edu
Привітання: Вітаю, мене звати Anonymous!
Цитата: Пам’ятай: знання — це сила 💡
----------------------------------------
Student #3: Марія
Email: марія@college.edu
Привітання: Вітаю, мене звати Марія!
Цитата: Пам’ятай: знання — це сила 💡
----------------------------------------
Загальна кількість студентів: 3


iii. Код програми:

class Student:
    total_students = 0

    def __init__(self, name=None):
        self.name = name if name else self.default_student().name
        Student.total_students += 1
        self.student_id = Student.total_students

    @property
    def info(self):
        return f"Student #{self.student_id}: {self.name}"

    @property
    def email(self):
        return f"{self.name.lower()}@college.edu"

    def greet(self):
        return f"Вітаю, мене звати {self.name}!"

    @classmethod
    def default_student(cls):
        return cls("Anonymous")

    @staticmethod
    def motivation_quote():
        return "Пам’ятай: знання — це сила 💡"


students = {"Ігор", "Марія", None}
all_students = {name: Student(name) for name in students}

for s in all_students.values():
    print(s.info)
    print("Email:", s.email)
    print("Привітання:", s.greet())
    print("Цитата:", Student.motivation_quote())
    print("-" * 40)

print(f"Загальна кількість студентів: {Student.total_students}")

Висновок

У роботі створено клас Student, що демонструє основні принципи ООП: інкапсуляцію, властивості, методи класу та статичні методи.

Навчився створювати об’єкти класу, працювати з атрибутами та методами.

Мету роботи досягнуто, усі завдання виконано.

Нові знання: створення та застосування класів, властивостей @property, методів @classmethod і @staticmethod.

Складнощів не виникло. Формат роботи зручний для навчання.