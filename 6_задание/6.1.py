class Employee:

    name = None
    salary = None

    def show(self):
        return f'name: {self.name} \nsalary: {self.salary}'

employee = Employee()

employee.name = 'Александр'
employee.salary = 64500

print(employee.show())