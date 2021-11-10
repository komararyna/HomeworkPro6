class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name}, {self.age}'


class Student(Person):
    def __init__(self, name, surname, age, fac):
        super().__init__(name, surname, age)
        self.fac = fac

    def __str__(self):
        return f'{self.surname} {self.name[0]}.: {self.age}, {self.fac}'
