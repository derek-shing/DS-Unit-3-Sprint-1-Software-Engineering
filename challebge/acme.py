import random

class Product:
    def __init__(self, name=None, price=10, weight=20,flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000,9999999)


    def stealability(self):
        s = self.price/self.weight
        if s<0.5:
            print('Not so stealable...')
        elif (s>=0.5) & (s<1):
            print('Kinda stealable')
        else:
            print('Very stealable!')

    def explode(self):
        f = self.flammability * self.weight
        if f<10:
            print('...fizzle.')
        elif (f>=10) & (f<50):
            print('...boom!')
        else:
            print('...BABOOM!!!')



class BoxingGlove(Product):

    def __init__(self,name=None, price=10, weight=10,flammability=0.5):
        super().__init__(name=name, price=price, weight=weight, flammability=flammability)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight<5:
            print('That tickles')
        elif (self.weight>5) & (self.weight<15):
            print('Hey that hurt!')
        else:
            print('OUCH!')


