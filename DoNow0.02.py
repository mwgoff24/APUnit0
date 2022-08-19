'''
###############
# Do Now 0.02 #
###############

In your Console
---------------
Type the following:

class Pet:
  def __init__(self, name):
    self.name = name

my_pet = Pet('Peter')
print(my_pet.name)

In your Notebook
----------------
Respond to the following:

1.  What is the purpose of the __init__ method?
Assigns unique attributes to an instance upon its creation

2.  What if you wanted to initialize all pet objects with a name and a color?
def __init__(self, name, color)

3.  How would you modify the code to create a pet object with a name of "Peter" and a color of "brown"?
Add color to the list of arguments, self.color = color, add 'brown' to arguments in class Pet()
'''
class Pet():
  def __init__(self, name, color):
    self.name = name
    self.color = color

my_pet = Pet('Peter', 'brown')
print(f"{my_pet.name}, {my_pet.color}")