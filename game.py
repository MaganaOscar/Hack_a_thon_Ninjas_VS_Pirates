from classes import pirate
from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

print("Michelangelo lurks in the palms littered across the beach. He eyes Jack Sparrow, a pirate intruder to this Ninja lair. His turtle instincts prove quite useful in this engagement.\n")

action = input("Type 'A' to attack\nType 'C' to charge your attack (max 3 charges)\n")
action = action.lower()
while action != 'a':
    if action == 'c':
        michelangelo.chargeAttack()
    action = input("Type 'A' to attack\nType 'C' to charge your attack (max 3 charges)\n")
while michelangelo.health > 0 and jack_sparrow.health > 0:
    if action == 'a':
        print(f"{michelangelo.name} attacks {jack_sparrow.name}")
        print(f"{michelangelo.name}: {Ninja.grunt()}\n")
        michelangelo.attack(jack_sparrow)
        jack_sparrow.show_stats()
        print(f"{jack_sparrow.name} attacks {michelangelo.name}")
        print(f"{jack_sparrow.name}: {Pirate.grunt()}\n")
        jack_sparrow.attack(michelangelo)
        michelangelo.show_stats()

if michelangelo.health > 0:
    print(f"{michelangelo.name} wins the fight. The Ninja Lair remains safe!")
else:
    print(f"{jack_sparrow.name} wins the fight. The Ninja Lair's treasure is ripe for plundering!")
