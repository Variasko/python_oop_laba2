class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def outputName(self):
        print(self.name)

    def outputSalary(self):
        print(self.salary)

    def add_10_persent_to_salary(self):
        print(f'old salary: {self.salary}'
              f'\nnew salary: {self.salary * 1.1}')



employee = Employee('Александр', 18, 64500)

employee.add_10_persent_to_salary()