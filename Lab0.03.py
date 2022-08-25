'''
##############
## Lab 0.03 ##
##############

Instructions:
-------------
1.  Finish writing the __add__ method for the time class from the Do Now.

2.  Write a definition for a class named Kangaroo with the following methods:

    An __init__ method that initializes an attribute named pouch_contents to an empty list.

    A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.

    A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.


Tips to give students:
----------------------
- This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python

- TypeError: Can't convert 'list' object to str implicitly

- Use the str() function to convert the list object to a string.

- Test your code by creating two Kangaroo objects

    assign them to variables named kanga and roo

    add roo to the contents of kanga's pouch
'''
# Kangaroo class
class Kangaroo:
    # __init__, initializes an attribute pouch_contents to empty list
    def __init__(self, name):
        self.name = name
        self.pouch_contents = []

    # put in pouch, adds an argument, object, to pouch_contents
    def put_in_pouch(self, object):
        self.pouch_contents.append(object)

    # __str__, overrides str function with f-string
    def __str__(self):
        return f"{self.name} is a kangaroo with {self.pouch_contents} in its pouch"

# define kangaroos
kanga_1 = Kangaroo("Kanga")
kanga_2 = Kangaroo("Roo")

# put objects in kangaroo pouches
kanga_1.put_in_pouch(kanga_2)
kanga_2.put_in_pouch("apple")

print(kanga_1.pouch_contents)

'''
Extra Credit
------------
Return to your Pet class from Lab 0.02. Research the isinstance function to write a method, 
is_friend that will take in another pet and return True if the two pets are friends, and 
false if they are not.

Rules:
------
- If they are both dogs they are friends.

- If the instance is a dog and the other pet is a cat, they are friends.

- If the instance is a cat and the other is a dog they are not friends.

- If they are both cats they are not friends.
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

    def is_friend(self, pet2):
        self.pet2 = pet2
        if isinstance(pet2, str):
            return True

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

# pet_print(my_pets)

print(my_pet3.is_friend(my_pet2.animal))