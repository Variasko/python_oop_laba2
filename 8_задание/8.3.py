class Student:

    name = None
    surname = None

    def initial(self):
        print(self.name[0].upper(), end='.')
        print(self.surname[0].upper(), end='.')

student = Student()

student.name = 'александр'
student.surname = 'Комиссаров'

student.initial()