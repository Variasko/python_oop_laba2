class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def output(self):
        print(f"name: {employee.__name}"
              f"\nage: {employee.__age}"
              f"\nsalary: {employee.__salary}")

employee = Employee('Александр', 18, 64500)

employee.output()