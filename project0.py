# Pokemon Project
# Martin Goff

import random

# create user class for player and user
class User:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.current_pokemon = None

    def switch(self):
        pass

    def attack(self, target, attack_name):
        pass

    def heal(self):
        pass

    def print_choices(self):
        pass

class Computer(User):
    pass


# main pokemon class
class Pokemon():
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap


# three child classes of pokemon
class Water(Pokemon):
    type = 'water'
    growl = 'Splish Splish'
    # contains dictionary as attacks: [HP dealt, Accuracy]
    attacks = {
        "Bubble": [40, 100],
        "Hydro Pump": [185, 30],
        "Surf": [70, 90]
              }

class Fire(Pokemon):
    type = 'fire'
    growl = 'Fire Fire'
    # contains dictionary as attacks: [HP dealt, Accuracy]
    attacks = {
        "Ember": [130, 90],
        "Fire Punch": [50, 100],
        "Flame Wheel": [55, 95]
              }


class Grass(Pokemon):
    type = 'grass'
    growl = 'Cheep Cheep'
    # contains dictionary as attacks: [HP dealt, Accuracy]
    attacks = {
        "Leaf Storm": [130, 90],
        "Mega Drain": [50, 100],
        "Razor Leaf": [55, 95]
              }

w_poke1 = Water('Squirtle', 80, 20)
w_poke2 = Water('Psyduck', 70, 40)
w_poke3 = Water('Pollywag', 50, 50)
f_poke1 = Fire('Charamander', 25, 70)
f_poke2 = Fire('Ninetails', 30, 50)
f_poke3 = Fire('Ponyta', 40, 60)
g_poke1 = Grass('Bulbasoar', 60, 40)
g_poke2 = Grass('Bellsprout', 40, 60)
g_poke3 = Grass('Oddish', 50, 50)

print(w_poke3.attacks)