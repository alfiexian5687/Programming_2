
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return "{:15}{:10} {:2}".format(self.first_name, self.last_name, self.age)


people = [Person("James", "Smith", 21), Person("Catherine", "Aniston", 32)]
for i in people:
    print(i)