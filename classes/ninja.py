from random import seed
from random import choice
from random import randint

class Ninja:
    grunts = ["Cowabunga!", "Hyaaaghhh!", "Wraahhh!"]
    seed(1)

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        hitChance = 100 - (pirate.speed * 10 )
        chance = randint(0, 100)

        if(chance < hitChance):
            pirate.health -= self.strength
            if(self.strength > 10):
                self.strength = 10
        else:
            print(f"{self.name}'s attack missed!")
        return self
    def chargeAttack(self):
        if(self.strength < 30):
            self.strength += 10
            print(f"{self.name}'s strength is now {self.strength}!\n")
        else:
            print("Maximum charge reached!\n")
        return self
    @classmethod
    def grunt(cls):
        return choice(cls.grunts)