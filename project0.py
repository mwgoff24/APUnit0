# Pokemon Project
# Martin Goff

import random

# main pokemon class
class Pokemon():
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap

    def __str__(self):
        return f"{self.name}: {self.hp} HP, {self.ap} AP"



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










# create user class for player and computer
class User:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.current_pokemon = None

# switches pokemon to another
    def switch(self):
        self.new_pokemon = input("Which of your pokemon would you like to switch to? ")
        self.current_pokemon = self.new_pokemon

# attacks the computer's pokemon
    def attack(self, target, attack_name):
        pass

# heals current pokemon
    def heal(self):
        self.current_pokemon

# prints available choices for player's pokemon
    def print_choices(self, poke_list):
        print(f"{self.name}, Here are your available pokemon: \n")
        num = 1
        for item in poke_list:
            print(f"{item}, {num}")
            num += 1

# populates player's collection of pokemon to fight with
    def poke_choices(self, poke_list):
        poke_choice = int(input(f"\nSelect a pokemon {self.name}. ")) - 1
        player.pokemon.append(poke_list[poke_choice])
        user_poke_list.remove(poke_list[poke_choice])
        player.print_choices(poke_list)

# used for debugging purposes
    def print_current(self, poke_list):
        for item in poke_list:
            print(item)

# sets a pokemon chosen as first to fight with
    def set_current_pokemon(self, poke_list):
        player.print_choices(poke_list)
        current = int(input("Which of your pokemon would you like to use? ")) - 1
        self.current_pokemon = poke_list[current]
        poke_list.remove(self.current_pokemon)



class Computer(User):
# same as User's poke_choices but implemented for computer
    def computer_choices(self, poke_list):
        new_pokemon = random.randint(0, int(len(poke_list))-1)
        computer.pokemon.append(poke_list[new_pokemon])
        computer_poke_list.remove(poke_list[new_pokemon])

# same as User set_current_pokemon but implemented for computer
    def computer_current(self, poke_list):
        computer.current = random.randint(0, int(len(poke_list))-1)


w_poke1 = Water('Squirtle', 80, 20)
w_poke2 = Water('Psyduck', 70, 40)
w_poke3 = Water('Pollywag', 50, 50)
f_poke1 = Fire('Charamander', 25, 70)
f_poke2 = Fire('Ninetails', 30, 50)
f_poke3 = Fire('Ponyta', 40, 60)
g_poke1 = Grass('Bulbasoar', 60, 40)
g_poke2 = Grass('Bellsprout', 40, 60)
g_poke3 = Grass('Oddish', 50, 50)

user_poke_list = [w_poke1, w_poke2, w_poke3, f_poke1, f_poke2, f_poke3, g_poke1, g_poke2, g_poke3]
computer_poke_list = [w_poke1, w_poke2, w_poke3, f_poke1, f_poke2, f_poke3, g_poke1, g_poke2, g_poke3]









# pre game loop

# setting names
user_name = input("Welcome player! What is your name? ")
computer_name = input("What do you want the computer's name to be? ")

# instantiate User objects
player = User(user_name)
computer = Computer(computer_name)

# player chooses pokemon
player.print_choices(user_poke_list)

while len(player.pokemon) < 3:
    player.poke_choices(user_poke_list)

# computer chooses pokemon
while len(computer.pokemon) < 3:
    computer.computer_choices(computer_poke_list)

# game tells player what pokemon the computer chose
print(f"\n{computer.name} has now chosen their pokemon:")
computer.print_current(computer.pokemon)
print("\n")

# set player's current pokemon
player.set_current_pokemon(player.pokemon)

# set computer's current pokemon
computer.computer_current(computer.pokemon)

# game loop
while True:
    # defining some variables
    player1 = player
    player2 = computer
    turn = player1

    # asks player what move they want to do
    move = input(f"{turn.name}, what would you like to do? s for switch, a for attack, or h for heal. ")
    if move == 's':
        player.switch()
    elif move == 'a':
        player.attack()
    elif move == 'h':
        player.heal()
    else:
        print("That is not an available option.")
        move
    # turn moved to computer
    turn = player2