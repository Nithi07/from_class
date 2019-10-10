class Person:
    id = 20

    def __init__(self, name, gender, height, weight):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight




    def is_tall(self):
        if self.height > 5.7:
            return 'He/she is tall'
        else:
            return 'He/she is short'


    def print_name(self):
        print(self.name)


    def can_hear(self):
        print('i can hear')


    def can_see(self):
        print('i can see')


# overriding
class DeafPerson(Person):

    def can_hear(self):
        print('i cannot hear. sorry')


# abstraction
# inheritance
# pollymorphism

# --------------------------------
person = Person('dinesh', 'm', 5.7, 75)
print(person.name)
print(person.id)
person2 = Perso n('rajesh', 'm', 5.6, 79)
print(person2.name)
person2.id = 25
print(person2.id)


# ------------------------------------------

# Inheritance

class Student(Person):

    def __init__(self, name, gender, height, weight, in_class, section):
        super().__init__(name, gender, height, weight)
        self.in_class = in_class
        self.section = section

    def read(self):
        pass

    def write(self):
        pass


class DeafStudent(Student):
    pass


class PythonStudent(Student):

    def can_write_python_code(self):
        pass


class JavaStudent(Stundent):

    def can_write_java_code(self):
        pass


student = Student('mani', 'm', 5.5, 60, 10, 'c')
student.print_name()




