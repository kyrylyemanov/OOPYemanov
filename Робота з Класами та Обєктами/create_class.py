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

