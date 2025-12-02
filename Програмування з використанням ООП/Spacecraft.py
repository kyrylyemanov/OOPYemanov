# === Базовий клас - Космічний корабель ===
class Spacecraft:
    total_missions = 0  # змінна класу для підрахунку всіх місій

    def __init__(self, name, launch_year):
        self.name = name
        self.launch_year = launch_year
        self.__status = "Очікує запуску"  # приватний атрибут

    def launch(self):
        self.__status = "Запущено"
        Spacecraft.total_missions += 1
        return f"{self.name} запущено у {self.launch_year} році!"

    def get_status(self):
        return f"{self.name} статус: {self.__status}"

    def get_info(self):
        return f"Корабель: {self.name}, Рік: {self.launch_year}, Статус: {self.__status}"

    @staticmethod
    def get_total_missions():
        return f"Загальна кількість місій: {Spacecraft.total_missions}"

# === Похідний клас - Спільна космічна станція ===
class SpaceStation(Spacecraft):
    def __init__(self, name, launch_year, crew_capacity):
        super().__init__(name, launch_year)
        self.crew_capacity = crew_capacity
        self.crew_members = []  # список для збереження астронавтів

    def add_crew_member(self, astronaut):
        if len(self.crew_members) < self.crew_capacity:
            self.crew_members.append(astronaut)
            return f"{astronaut.name} доданий до борту {self.name}."
        else:
            return "Кількість членів екіпажу досягнута."

    def remove_crew_member(self, astronaut):
        if astronaut in self.crew_members:
            self.crew_members.remove(astronaut)
            return f"{astronaut.name} видалений з борту {self.name}."
        else:
            return f"{astronaut.name} не знайдено у екіпажі."

    def get_crew_list(self):
        return [member.name for member in self.crew_members]

# === Похідний клас - Ракета ===
class Rocket(Spacecraft):
    def __init__(self, name, launch_year, engine_type):
        super().__init__(name, launch_year)
        self.engine_type = engine_type

    def get_info(self):
        return f"{self.name} (Ракета), Тип двигуна: {self.engine_type}, Рік запуску: {self.launch_year}"

# === Клас - Астронавт ===
class Astronaut:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def get_info(self):
        return f"Астронавт: {self.name}, Спеціалізація: {self.specialization}"

    def perform_task(self):
        return f"{self.name} виконує задачу як {self.specialization}."

# === Демонстрація роботи ===
def show_mission_details(objects):
    print("\n=== Деталі космічних об'єктів ===")
    for obj in objects:
        print(obj.get_info())

# === Створюємо об'єкти (комірки) ===
# 1. Створимо ракету
rocket1 = Rocket("Atlas V", 2018, "Рідкий кисень/керосин")
# 2. Створимо космічну станцію
station1 = SpaceStation("Міжнародна космічна станція", 1998, 6)
# 3. Створимо астронавтів
astro1 = Astronaut("Іван", "Інженер")
astro2 = Astronaut("Марія", "Медик")
astro3 = Astronaut("Джон", "Дослідник")

# 4. Створимо ще одну ракету
rocket2 = Rocket("Falcon Heavy", 2018, "Рідкий кисень/керосин")

# 5. Додаємо астронавтів до станції
print(station1.add_crew_member(astro1))
print(station1.add_crew_member(astro2))
print(station1.add_crew_member(astro3))

# 6. Виводимо інформацію про об'єкти
show_mission_details([rocket1, station1, rocket2])

# 7. Запускаємо ракети
print(rocket1.launch())
print(rocket2.launch())

# 8. Перевіряємо статус
print(rocket1.get_status())
print(station1.get_status())

# 9. Виводимо загальну кількість місій
print(Spacecraft.get_total_missions())

# 10. Виводимо список екіпажу
print(f"Екіпаж станції {station1.name}: {station1.get_crew_list()}")