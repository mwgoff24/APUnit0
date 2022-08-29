'''
############
# Lab 0.04 #
############

Overview
--------
Given the following Sample Code, practice using inheritance 
to create specific child classes for different types of Pokemon.

Create the three child classes below:
1. Water Type
When attacking a fire type, the attack is more effective

When attacking a grass type the effect is less effective

When growl is called print out Splish Splash

2. Fire Type
When attacking a water type, the attack is less effective

When attacking a grass type the effect is more effective

When growl is called print out "Fire Fire"

3. Grass Type
When attacking a water type, the attack is more effective

When attacking a fire type the effect is less effective

When growl is called print out "Cheep Cheep"

##############################################################
# Note: In order to check what type an object is you can use #
# isinstance which takes in an object, a class and returns a #
# Boolean if the object is the type of the inputted class.   #
##############################################################

Example Code
------------
my_pet = Pet()
isinstance(my_pet, Pet) # returns true
isinstance(my_pet, Dog) # returns false
'''
# main pokemon class
class Pokemon():
    def __init__(self, name):
        self.name = name


class Water(Pokemon):
    type = 'water'
    growl = 'Splish Splish'


class Fire(Pokemon):
    type = 'fire'
    growl = 'Fire Fire'


class Grass(Pokemon):
    type = 'grass'
    growl = 'Cheep Cheep'


def attack(self, other):
    # water to fire
    if isinstance(self, Water) and isinstance(other, Fire):
        print(f"{self.name}'s attack is more effective against {other.name}.")

    # fire to grass
    elif isinstance(self, Fire) and isinstance(other, Grass):
        print(f"{self.name}'s attack is more effective against {other.name}.")

    # grass to water
    elif isinstance(self, Grass) and isinstance(other, Water):
        print(f"{self.name}'s attack is more effective against {other.name}.")

    # water to grass
    elif isinstance(self, Water) and (other, Grass):
        print(f"{self.name}'s attack is less effective against {other.name}.")

    # fire to water
    elif isinstance(self, Fire) and (other, Water):
        print(f"{self.name}'s attack is less effective against {other.name}.")

    # grass to fire
    elif isinstance(self, Grass) and (other, Fire):
        print(f"{self.name}'s attack is less effective against {other.name}.")



my_pokemon1 = Water('Squirtle')
my_pokemon2 = Fire('Charizard')
my_pokemon3 = Grass('Weedy')

attack(my_pokemon1, my_pokemon2)

attack(my_pokemon1, my_pokemon3)

attack(my_pokemon2, my_pokemon1)

attack(my_pokemon2, my_pokemon3)

attack(my_pokemon3, my_pokemon2)

attack(my_pokemon3, my_pokemon1)