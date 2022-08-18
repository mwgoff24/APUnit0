'''
############
# Lab 0.01 #
############

In this lab we will create a class that will represent colors 
and build a function to combine two colors.


1.  Create a class, Color.
2.  Instantiate at least 3 colors.
3.  Add attributes of r, g, and b to those instances.
4.  Create a function, add_color, which takes in two colors 
    and returns a color that is the sum of the two reds, greens, 
    and blues. Don't forget: the maximum value for R, G, or B is 255.
'''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# class Color
class Color():
    '''this creates different colors'''

# instantiate 3 color objects
color1 = Color()
color2 = Color()
color3 = Color()

# set color attributes

# color 1
color1.r = 100
color1.g = 95
color1.b = 201

# color 2
color2.r = 23
color2.g = 137
color2.b = 1

# color 3
color3.r = 255
color3.g = 55
color3.b = 62

# add color, 
def add_color(color_a, color_b):
    # intantiate a new color
    new_color = Color

    # assign red for new color object
    new_color.r = color_a.r + color_b.r
    if new_color.r > 255:
        new_color.r = 255

    # assign red for new color object
    new_color.r = color_a.r + color_b.r
    if new_color.r > 255:
        new_color.r = 255
    

    return new_color

color4 = add_color(color1, color2)

print(f"Color 4's red attribute is {color4.r}.")