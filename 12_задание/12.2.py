class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def outputName(self):
        print(self.name)

employee = Employee('Александр', 18, 64500)

