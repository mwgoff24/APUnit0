'''
###############
# Do Now 0.01 #
###############

Read through the following code:
--------------------------------
my_pet_1 = 'pet'
my_pet_1_type = 'cat'
my_pet_1_noise = 'meow'
my_pet_1_full_name = 'Snuffles McGruff'

my_pet_2 = 'pet'
my_pet_2_type = 'cat'
my_pet_2_noise = 'meow'
my_pet_2_full_name = 'Snowpounce Flury'

my_pet_3 = 'pet'
my_pet_3_type = 'cat'
my_pet_3_noise = 'meow'
my_pet_3_full_name = 'Snickers Snorkel'

my_pets = [my_pet_1, my_pet_2, my_pet_3]
for pet in my_pets:
    ## print full name of each pet

In your Notebook
----------------
Respond to the following:

    1.  Write a quick description of how you would print out each of the pet's names.

    
    2.  Write down some other data structures you could use to make this easier.
'''
my_pet_1 = 'pet'
my_pet_1_type = 'cat'
my_pet_1_noise = 'meow'
my_pet_1_full_name = 'Snuffles McGruff'

my_pet_2 = 'pet'
my_pet_2_type = 'cat'
my_pet_2_noise = 'meow'
my_pet_2_full_name = 'Snowpounce Flury'

my_pet_3 = 'pet'
my_pet_3_type = 'cat'
my_pet_3_noise = 'meow'
my_pet_3_full_name = 'Snickers Snorkel'

my_pets = [my_pet_1, my_pet_2, my_pet_3]
my_pet_names = [my_pet_1_full_name, my_pet_2_full_name, my_pet_3_full_name]
my_pet_index = 0
for pet in my_pets:
    print(my_pet_names[my_pet_index])
    my_pet_index +=1

print("\n")

class Cat(): 
    def __init__(self, name):
        self.attribute = 'pet'
        self.species = 'cat'
        self.noise = 'meow'
        self.name = name

cat1 = Cat("Katy Cat")
cat2 = Cat("Peanut Butter")
cat3 = Cat("Kally")

my_pets = [cat1, cat2, cat3]

for pet in my_pets:
    print(pet.name)