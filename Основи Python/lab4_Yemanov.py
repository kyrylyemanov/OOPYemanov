
# i. Типи даних
print("=== i. Типи даних ===")
a = "змінна з текстом"
b = 1
b1 = 1.1
c = ["a", 1.25, "Слово", a]       # list
d = {"a": "Слово", "b": 1, "a1": b}  # dict
e = ("a", a)                      # tuple
f = {"ss", a, b}                  # set

print(type(a), type(b), type(c), type(d), type(e), type(f))
print()


# ii. Вбудовані константи та зарезервовані слова
print("=== ii. Вбудовані константи ===")
print("Перша константа:", True)
print("Друга константа:", None)

import keyword
print("Перевіримо чи 'for' зарезервоване слово:", keyword.iskeyword("for"))
print()


# iii. Вбудовані функції
print("=== iii. Вбудовані функції ===")
print("abs(-12.5) =", abs(-12.5))
print("len('Python') =", len("Python"))
print("round(3.14159, 2) =", round(3.14159, 2))
print()


# iv. Цикли
print("=== iv. Цикли ===")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква '{letters[i]}'")
else:
    print("Цикл завершено успішно!")
print()


# v. Розгалуження
print("=== v. Розгалуження ===")
from random import randint

A = randint(0, 10)
if A > 5:
    print(f"A={A}. Це велике число!")
elif A == 5:
    print(f"A={A}. Рівно 5!")
else:
    print(f"A={A}. Маленьке число.")
print()


# vi. Обробка помилок
print("=== vi. Обробка помилок ===")
A = 0
try:
    print("Ділення:", 10 / A)
except Exception as e:
    print("Сталася помилка:", e)
finally:
    print("Блок finally виконується завжди.")
print()


# vii. Контекст-менеджер
print("=== vii. Контекст-менеджер ===")
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python!\n")

with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("З файлу:", line.strip())
print()


# viii. Лямбда-функції
print("=== viii. Лямбда-функції ===")
def add(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print("Результат звичайної функції:", add(5, 3))
print("Результат лямбда-функції:", add_lambda(5, 3))
print()

print(" Роботу виконано успішно!")
