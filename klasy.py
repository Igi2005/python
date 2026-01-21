class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, name,surname,age,wydzial,oceny):
        super().__init__(name,surname,age)
        self.wydzial = wydzial
        self.oceny = oceny



p1 = Student("Szymon","Puk",19,"Air",[5,5,5,5])


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return "X to " + str(self.x) + " y to " + str(self.y)

v1 = Vector(10,15)
v2 = Vector(5,10)
v3 = v1 + v2
print(v3)