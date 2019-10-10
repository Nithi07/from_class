class Mammel:
    def walk(self):
        print('walk')


class Cat(Mammel):
    def annoying(self):
        print('annoying')


class Dog(Mammel):
    pass


mam = Mammel()
print(mam.walk())

cat1 = Cat()
print(cat1.walk()) # cat1. walk() or annoying() we got both options