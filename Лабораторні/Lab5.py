import random

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # публічний атрибут
        self.__balance = balance  # приватний атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("Bohdan", 1000)

for _ in range(10):
    action = random.choice(["deposit", "withdraw"])
    amount = random.randint(50, 300)
    
    if action == "deposit":
        account.deposit(amount)
        print(f"Депозит: +{amount} грн")
    else:
        result = account.withdraw(amount)
        if result == "Insufficient funds":
            print(f"Зняття: -{amount} грн → Недостатньо коштів")
        else:
            print(f"Зняття: -{amount} грн")

print(f"\nКінцевий баланс: {account.get_balance()} грн")






class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return f"Тип пального для {self.brand} {self.model}: Бензин"

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # виклик конструктора базового класу
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"

car = Car("Toyota", "Camry", 5)
print(car.display_info())
print(car.fuel_type())  # виклик методу базового класу з об'єкта Car






class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    def speak(self):
        return "..."  # Риби не видають звуків!

# Використання:
animals = [Dog(), Cat(), Fish()]
for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")





from abc import ABC, abstractmethod
from random import randint, choice

class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass

class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        print(f"⚔️  Завдаємо удар мечем [{self.name}] та наносимо {current_attack} шкоди. У [{another_item.name}] залишилось здоров'я: {another_item.health}")

    @property
    def get_attack_power(self):
        return f"Атака меча [{self.name}]: {self.__attack_power + self._sharp} одиниць"

    def sharpening(self):
        self._sharp += 1
        print(f"🔧 [{self.name}] заточено! Бонус до атаки: +{self._sharp}")

class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 20)
        another_item.health -= current_attack
        print(f"🪓 Завдаємо удар сокирою [{self.name}] та наносимо {current_attack} шкоди. У [{another_item.name}] залишилось здоров'я: {another_item.health}")

    @property
    def get_attack_power(self):
        return f"Атака сокири [{self.name}]: {self.__attack_power + self._sharp} одиниць"

    def sharpening(self):
        self._sharp += 1
        print(f"🔧 [{self.name}] заточено! Бонус до атаки: +{self._sharp}")

class Bow(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name)
        self.__attack_power = attack_power
        self._range_power = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(5, 15) + self._range_power
        another_item.health -= current_attack
        print(f"🏹 Випускаємо стрілу з лука [{self.name}] та наносимо {current_attack} шкоди. У [{another_item.name}] залишилось здоров'я: {another_item.health}")

    @property
    def get_attack_power(self):
        return f"Атака лука [{self.name}]: {self.__attack_power + self._range_power} одиниць"

    def reload(self):
        self._range_power += 1
        print(f"🎯 [{self.name}] перезаряджено! Бонус дальності: +{self._range_power}")

# ── Ініціалізація ──────────────────────────────────────────
weapon_classes = [
    ("Екскалібур", Sword, 100),
    ("Кратос",     Axe,   95),
    ("Леґолас",    Bow,   85),
]

def create_weapon(name, cls, power):
    return cls(name, power)

print("⚔️  ===== ПОКРОКОВА ГРА =====")
print("Оберіть свою зброю:")
print("1 - Меч (Екскалібур)")
print("2 - Сокира (Кратос)")
print("3 - Лук (Леґолас)")

choice_input = input("Ваш вибір (1/2/3): ").strip()
weapon_map = {"1": 0, "2": 1, "3": 2}
idx = weapon_map.get(choice_input, 0)

player_data = weapon_classes[idx]
enemy_data  = weapon_classes[(idx + randint(1, 2)) % 3]  # випадковий ворог

player = create_weapon(*player_data)
enemy  = create_weapon(*enemy_data)

print(f"\n🧍 Ваша зброя : {player.name} ({type(player).__name__})")
print(f"👹 Противник  : {enemy.name} ({type(enemy).__name__})\n")

# ── Ігровий цикл ──────────────────────────────────────────
step = 1
while player.health > 0 and enemy.health > 0:
    print(f"─── Хід {step} ───────────────────────────────")
    print(f"❤️  Ваше здоров'я: {player.health}  |  👹 Ворог: {enemy.health}")
    print(player.get_attack_power)

    # Визначаємо дії залежно від типу зброї
    if isinstance(player, Bow):
        print("Дії: [1] Атакувати  [2] Перезарядити лук")
        action = input("Оберіть дію: ").strip()
        if action == "2":
            player.reload()
        else:
            player.attack(enemy)
    else:
        print("Дії: [1] Атакувати  [2] Заточити зброю")
        action = input("Оберіть дію: ").strip()
        if action == "2":
            player.sharpening()
        else:
            player.attack(enemy)

    if enemy.health <= 0:
        print(f"\n🏆 Перемога за [{player.name}]!")
        break

    # Хід ворога
    enemy.attack(player)

    if player.health <= 0:
        print(f"\n💀 Перемога за [{enemy.name}]!")
        break

    step += 1
    input("\nНатисніть Enter для наступного ходу...\n")