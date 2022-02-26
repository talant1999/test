from abc import ABC, abstractmethod


class Employee(ABC):
    baseSalary = 10000

    def __init__(self, firstName, lastName, position, rate):
        self.firstName = firstName
        self.lastName = lastName
        self.position = position
        self.rate = rate

    def determine_salary(self):
        print(Employee.baseSalary * self.rate)
        return Employee.baseSalary * self.rate


class Programmer(Employee):
    rate = 4

    def __init__(self, firstName, lastName, position):
        super().__init__(firstName, lastName, position, self.rate)


class Economist(Employee):
    rate = 2

    def __init__(self, firstName, lastName, position):
        super().__init__(firstName, lastName, position, self.rate)


class Director(Employee):
    rate = 10

    def __init__(self, firstName, lastName, position):
        super().__init__(firstName, lastName, position, self.rate)


print("Базовые доходы сотрудников: Программист, Экономист и Директор")
pr = Programmer('Иван', 'Иванов', 'Программист')
pr.determine_salary()

ec = Economist('Петр', 'Петров', 'Экономист')
ec.determine_salary()

dr = Director('Василий', 'Сидоров', 'Директор')
dr.determine_salary()


