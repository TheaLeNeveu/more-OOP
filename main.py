from datetime import date

class employee:
    def __init__(self, name, role, salary, DoB):
        self.name = name
        self.role = role
        self.salary = salary
        self.DoB = DoB

    def increase_salary(self):
        increase = input("Enter salary increase: ")
        self.salary += increase

    def calculate_age(self):
        today = date.today()
        return today.year - self.DoB[2] - ((today.month, today.day) < (self.DoB[1], self.DoB[0]))

class manager:
    def __init__(self, name, role, salary, DoB, bonus):
        self.name = name
        self.role = role
        self.salary = salary
        self.DoB = DoB
        self.bonus = bonus

    def increase_salary(self):
        increase = input("Enter salary increase: ")
        self.salary += increase

    def calculate_age(self):
        today = date.today()
        return today.year - self.DoB[2] - ((today.month, today.day) < (self.DoB[1], self.DoB[0]))

    def increase_bonus(self):
        increase = input("Enter bonus increase: ")
        self.bonus += increase

