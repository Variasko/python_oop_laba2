class Student:

    name = None
    surname = None

    def upperFirstLetter(self, str):
        for i in range(len(str)):
            if i != 0:
                print(str[i], end='')
            else:
                print(str[i].upper(), end='')

student = Student()

student.name = 'александр'
student.surname = 'Комиссаров'

student.upperFirstLetter(student.name)