class Employee:
    ...

first_employee = Employee()
second_employee = Employee()

first_employee.name = 'Александр'
first_employee.salary = 64500

second_employee.name = 'Максим'
second_employee.salary = 54600

print(f'total salary: {first_employee.salary + second_employee.salary}')