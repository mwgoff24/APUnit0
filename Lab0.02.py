'''
############
# Lab 0.02 #
############

In this lab, we will create a Pet class that will keep track of the type of animal, 
color, food, noise and name of a given animal.

Create a class called Pet that has the following attributes
Animal (e.g., dog, cat, fish)

Color (e.g., spotted, tabby, gold)

Food (e.g., kibbles, tuna, fish flakes)

Noise (e.g., meow, woof, splash)

Name (e.g., Scooby Doo, Fluffy, Bubbles)

Specifications
--------------
Make sure to use the __init__ method to create these attributes.

Create a list of pets.

Create a function that takes in a list of pets and prints out the name 
and the food attributes.

Test your function with your list of pets.
'''
# class Pet, instantiates pet objects
class Pet():
    # attributes added
    def __init__(self, animal, color, food, noise, name):
        self.animal = animal
        self.color = color
        self.food = food
        self.noise = noise
        self.name = name

# pet print, prints pet name and food attributes from a pet list
def pet_print(pet_list):
    for pet in pet_list:
        print(f"{pet.name} is a {pet.color} {pet.animal} that goes {pet.noise} and eats {pet.food}.")

# variables defined with instances from Pet class for list readability
my_pet1 = Pet('dog', 'spotted', 'kibbles', 'woof', 'Scooby Doo')
my_pet2 = Pet('cat', 'tabby', 'tuna', 'meow', 'Fluffy')
my_pet3 = Pet('fish', 'gold', 'fish flakes', 'splash', 'Bubbles')

# list containing pets and their attributes
my_pets = [my_pet1, my_pet2, my_pet3]

pet_print(my_pets)