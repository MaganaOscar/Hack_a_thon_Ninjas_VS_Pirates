from random import seed
from random import choice
from random import randint

class Pirate:
    grunts = ["Arrggghhhguhgh", "Grrrrrrrgghh", "You'll be regrettin' that!"]
    seed(1)

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        hitChance = 100 - (ninja.speed * 10 )
        chance = randint(0, 100)

        if(chance < hitChance):
            ninja.health -= self.strength
            if(self.strength > 10):
                self.strength = 10
        else:
            print(f"{self.name}'s attack missed!")
        return self
    @classmethod
    def grunt(cls):
        return choice(cls.grunts)

