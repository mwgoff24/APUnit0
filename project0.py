# Pokemon Project
# Martin Goff

import random

# main pokemon class
class Pokemon():
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.MAX_HEALTH = hp

    def __str__(self):
        return f"{self.name}: {self.hp} HP, {self.ap} AP"

    def attack(self, attack, attack_stats, other):
    # sets variables as a random attack power and random number to determine success
        attack_power = random.randint(int(attack_stats[0]) - 20, int(attack_stats[0]))
        # checks if attack can do 1.5 times more damage
        if isinstance(self, Water) and isinstance(other.current_pokemon, Fire):
            attack_power *= 1.5
        elif isinstance(self, Fire) and isinstance(other.current_pokemon, Grass):
            attack_power *= 1.5
        elif isinstance(self, Grass) and isinstance(other.current_pokemon, Water):
            attack_power *= 1.5
        attack_success = random.randint(0, 100)
        print(f"{self.name} used {attack}!")
    # if number chosen is greater than accuracy of attack, enemy dodges attack 
        if attack_success > int(attack_stats[1]):
            print(f"{other.current_pokemon.name} dodged the attack!")
    # else is when number chosen is within range 0 to accuracy of attack, enemy loses chosen amt hp
        else:
            other.current_pokemon.hp -= attack_power
            print(f"{other.current_pokemon.name} just lost {attack_power} hp!")
            if other.current_pokemon.hp <= 0:
                other.poke_death(other)


# three child classes of pokemon
class Water(Pokemon):
    type = 'water'
    growl = 'Splish Splish'
    # contains dictionary as attacks: [HP dealt, Accuracy]
    attacks = {
        "bubble": [40, 100],
        "hydro pump": [185, 30],
        "surf": [70, 90]
              }

class Fire(Pokemon):
    type = 'fire'
    growl = 'Fire Fire'
    # contains dictionary as attacks: [HP dealt, Accuracy]
    attacks = {
        "ember": [130, 90],
        "fire punch": [50, 100],
        "flame wheel": [55, 95]
              }


class Grass(Pokemon):
    type = 'grass'
    growl = 'Cheep Cheep'
    # contains dictionary as attacks: [HP dealt, Accuracy]
    attacks = {
        "leaf storm": [130, 90],
        "mega drain": [50, 100],
        "razor leaf": [55, 95]
              }


# create user class for player and computer
class User:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.current_pokemon = None

# switches current pokemon
    def switch(self, poke_list):
    # used if user tries to switch and there are no pokemon remaining
        if len(poke_list) == 0:
            print("You just wasted a turn! Type in 0 to proceed.")
    # used when user's current pokemon dies
        elif self.current_pokemon.hp == 0:
            self.pokemon.append(self.current_pokemon)
            self.pokemon.remove(self.current_pokemon)
    # used whether called upon by player or when pokemon dies, prints out choices to switch to
        print("\n")
        self.print_choices(self.pokemon)
        # asks user what to switch to
        print("\n")
        new_pokemon = int(input("Which of your pokemon would you like to switch to? "))-1
        # adds current pokemon back to personal list, makes the chosen pokemon the new one, removes new current from list
        self.pokemon.append(self.current_pokemon)
        self.current_pokemon = self.pokemon[new_pokemon]
        self.pokemon.remove(self.current_pokemon)
        print("\n")
        print(f"{self.name} switched to {self.current_pokemon.name}!")

# attacks the computer's pokemon
    def player_attack(self, other):
        # displays the available attacks
        print(f"\nThese are your attacks.\n{self.current_pokemon.attacks}\nThe left number is HP dealt, the right is the accuracy. \n")
        attack = input(f"Which attack would you like to use, {self.name}? Type the full name of the attack. ")
        print("\n")
        # instantiates the attack from the dictionary and prints its stats
        chosen_attack = self.current_pokemon.attacks.get(attack)
        self.current_pokemon.attack(attack, chosen_attack, other)

# runs if attack put computer's pokemon below or at 0 hp
    def poke_death(self, other):
        if other.current_pokemon.hp <= 0:
            other.current_pokemon.hp = 0
    # checks if computer's health is at 0, then checks if computer has available pokemon to switch to
            print(f"{other.name} just lost {other.current_pokemon.name}!")
            if len(other.pokemon) > 0:
                if turn == player1:
                    other.computer_switch(other.pokemon)
                    other.check_list(other.pokemon)
                else:
                    self.switch(self.pokemon)
                    self.check_list(self.pokemon)
            else:
                other.current_pokemon = None
                
# checks pokemon list to see if any pokemon have 0 hp
    def check_list(self, poke_list):
        for item in poke_list:
            if item.hp == 0:
                poke_list.remove(item)

# heals current pokemon
    def heal(self):
        if self.current_pokemon.hp == self.current_pokemon.MAX_HEALTH:
            print("\n")
            print(f"{self.name} just wasted a turn trying to heal their pokemon with full hp!")
        else:
            hp_back = 20
            self.current_pokemon.hp += hp_back
            if self.current_pokemon.hp > self.current_pokemon.MAX_HEALTH:
                self.current_pokemon.hp = self.current_pokemon.MAX_HEALTH
                print("\n")
                print(f"{self.name} has healed {self.current_pokemon.name} back to max!")
            else:
                print("\n")
                print(f"{self.name} has healed {self.current_pokemon.name}!")

# prints available choices for player's pokemon
    def print_choices(self, poke_list):
        print(f"{self.name}, Here are your available pokemon:")
        num = 1
        for item in poke_list:
            print(f"{item}, {num}")
            num += 1

# populates player's collection of pokemon to fight with
    def poke_choices(self, poke_list):
        player.print_choices(poke_list)
        poke_choice = int(input(f"\nSelect a pokemon {self.name}. "))-1
        self.pokemon.append(poke_list[poke_choice])
        main_poke_list.remove(poke_list[poke_choice])

# sets a pokemon chosen as first to fight with
    def set_current_pokemon(self, poke_list):
        player.print_choices(poke_list)
        current = int(input("Which of your pokemon would you like to use? "))-1
        self.current_pokemon = poke_list[current]
        self.pokemon.remove(self.current_pokemon)
        print("\n")
        print(f"{self.name} is using {self.current_pokemon.name} as their current!")

# checks health of each pokemon and ends game if a player lost all their pokemon
    def check_health(self, other):
        global gameplay
        if len(self.pokemon) == 0 and self.current_pokemon == None:
            print("\n")
            print(f"{other.name} has won this battle. Thank you for playing {self.name} and {other.name}.")
            gameplay = False
        elif len(other.pokemon) == 0 and other.current_pokemon == None:
            print("\n")
            print(f"{self.name} has won this battle. Thank you for playing {self.name} and {other.name}.")
            gameplay = False
        else:
            print(f"{self.name}'s pokemon has {self.current_pokemon.hp} hp. {other.name}'s pokemon has {other.current_pokemon.hp} hp.\n")


# subclass of User
class Computer(User):
# all methods are User methods just implemented for computer
# same as User's poke_choices
    def computer_choices(self, poke_list):
        new_pokemon = random.randint(0, int(len(poke_list))-1)
        computer.pokemon.append(poke_list[new_pokemon])
        main_poke_list.remove(poke_list[new_pokemon])

# same as User set_current_pokemon
    def computer_current(self, poke_list):
        current_poke = random.randint(0, int(len(poke_list))-1)
        self.current_pokemon = poke_list[current_poke]
        self.pokemon.remove(self.current_pokemon)
        print(f"{self.name} is using {self.current_pokemon.name} as their current!")

# same as User switch
    def computer_switch(self, poke_list):
        # used when computer tries to switch but only has one remaining pokemon
        if len(poke_list) == 0:
            print(f"{self.name} tried to switch but they have no available pokemon! {self.name} just lost their turn!\n")
        # used after poke_death to eliminate the current pokemon when there are no remaining pokemon
        elif len(poke_list) == 0 and self.current_pokemon.hp == 0:
            self.current_pokemon = None
        # used after poke_death to eliminate the current pokemon and switch to a new one
        elif self.current_pokemon.hp == 0:
            self.current_pokemon = None
            new_pokemon = random.randint(0, int(len(poke_list))-1)
            self.current_pokemon = self.pokemon[new_pokemon]
            self.pokemon.remove(self.pokemon[new_pokemon])
            print("\n")
            print(f"{self.name} switched to {self.current_pokemon.name}!")
        # used if computer calls method in battle
        else:
            new_pokemon = random.randint(0, int(len(poke_list))-1)
            self.pokemon.append(self.current_pokemon)
            self.current_pokemon = self.pokemon[new_pokemon]
            self.pokemon.remove(self.pokemon[new_pokemon])
            print(f"{self.name} switched to {self.current_pokemon.name}!")
        
# same as User attack
    def computer_attack(self, other):
        attack_names = []
        attack_values = []
        for item in list(self.current_pokemon.attacks.keys()):
            attack_names.append(item)
        for item in list(self.current_pokemon.attacks.values()):
            attack_values.append(item)
        chosen_attack_val = random.randint(0, len(attack_names)-1)
        chosen_attack = attack_values[chosen_attack_val]
        self.current_pokemon.attack(attack_names[chosen_attack_val], chosen_attack, other)
            


w_poke1 = Water('Squirtle', 80, 20)
w_poke2 = Water('Psyduck', 70, 40)
w_poke3 = Water('Pollywag', 50, 50)
f_poke1 = Fire('Charamander', 25, 70)
f_poke2 = Fire('Ninetails', 30, 50)
f_poke3 = Fire('Ponyta', 40, 60)
g_poke1 = Grass('Bulbasoar', 60, 40)
g_poke2 = Grass('Bellsprout', 40, 60)
g_poke3 = Grass('Oddish', 50, 50)

main_poke_list = [w_poke1, w_poke2, w_poke3, f_poke1, f_poke2, f_poke3, g_poke1, g_poke2, g_poke3]

# pre game loop

# setting names
user_name = input("Welcome player! What is your name? ")
computer_name = input("What do you want the computer's name to be? ")

# instantiate User objects
player = User(user_name)
computer = Computer(computer_name)

# player chooses pokemon
while len(player.pokemon) < 3:
    player.poke_choices(main_poke_list)
print("\n")
print(f"{player.name}'s pokemon are {player.pokemon[0].name}, {player.pokemon[1].name}, and {player.pokemon[2].name}!")

# computer chooses pokemon
while len(computer.pokemon) < 3:
    computer.computer_choices(main_poke_list)
print(f"{computer.name}'s pokemon are {computer.pokemon[0].name}, {computer.pokemon[1].name}, and {computer.pokemon[2].name}!")

# set player's current pokemon
print("\n")
player.set_current_pokemon(player.pokemon)

# set computer's current pokemon
computer.computer_current(computer.pokemon)
print("\n")

# defining some variables
player1 = player
player2 = computer
gameplay = True

# game loop
while gameplay:
    turn = player1
    # checks both pokemon lists
    player.check_health(computer)
    if gameplay == False:
        break
    # asks player what move they want to do
    move = input(f"Go, {turn.name}! Type either s for switch, a for attack, or h for heal. ")
    if move == 's':
        player.switch(player.pokemon)
    elif move == 'a':
        player.player_attack(computer)
    elif move == 'h':
        player.heal()
    else:
        print("You have to hit s, a, or h to play the game! You just lost your turn!")
        turn = player1
        move
    player.check_health(computer)
    if gameplay == False:
        break
    turn = player2
    print(f"Go, {turn.name}!")
    advance = input("Press ENTER.")
    print("\n")
    c_move = random.randint(1, 6)
    if c_move == 1:
        computer.computer_switch(computer.pokemon)
    elif c_move == 2:
        computer.heal()
    else:
        computer.computer_attack(player)