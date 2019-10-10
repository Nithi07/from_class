"""consructors"""
class Person:
    def __init__(self, name):
        self.name = name   # already name assined so only deleted calling method

    def talk(self):
        print(f'hai {self.name}')


nithi = Person("i am nithi")
nithi.talk()

mahi = Person('i am mahi')
mahi.talk()
