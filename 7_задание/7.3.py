class Employee:

    name = None
    salary = None

    def showName(self):
        return f'name: {self.name}'

    def showSalary(self):
        return f'salary: {self.salary}'

employee = Employee()

employee.name = 'Александр'
employee.salary = 64500

print(employee.showSalary())