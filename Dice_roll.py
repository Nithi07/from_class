import random

class Dice:

    def __init__(self, number):                    OR           def roll(self):
        self.number = number                                        a = random.randint(1,6)
                                                                    b = random.randint(1,6)
    def roll(self):                                                 return a, b
        print(f'({random.choice(self.number)},{random.choice(self.number)})')


chance = Dice(range(1, 50))                                     chance = Dice()
chance.roll()                                                   print(chance.roll())

