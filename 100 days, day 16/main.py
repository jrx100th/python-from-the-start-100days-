## Day 16  : Object oriented programming

#108 : Why we need OOP
"""
till now procedural programming

"""
#109 How to use OOP: Classes and Objects

"""
modelling a real world object

for waiter
has:
        is_holding_plate = True
        tables_responsible = [4,5,6]
                                    ** they are attributes - variable that is associated with a modelled object
does:
        def take_order(table, order):
        # takes orders to chef
        
        def take_payment(amount):
        # add money to restaurant
                                    ** they are methods - functions that a modelled object can do (associated)
                                    
trying to model real life objects and 
those objects have things - attributes
and 
can also do things - methods

Generating multiple objects from the same type
same type/ blue print - class

individual objects that are generated from the blue print/class are called objects
"""

# 110 Constructing objects and accessing their attributes and methods

"""
Class - Car
can have multiple objects

car = CarBlueprint()....here CarBlueprint() is the class, captilized(pascal case)

and 
car is the object
object name can be anything
CarBlueprint() activates the construction of the object 

Turtle graphics
"""

import turtle

# created another file named another_module, now i am going to import it and use its values
"""
import another_module

print(another_module.another_variable)
"""
# tapping into the class named 'turtle' inside the turtle module
# to construct this object we need to add the parenthesis at the end
# saving the turtle stuff into an object named timmy
# here the oop class is already developed and we just imported it and using it

"""
timmy = turtle.Turtle()
print(timmy)
"""
# turtle is a module and Turtle() is a class in that module


# now doing the same thing in a different approach
"""
from turtle import Turtle, Screen
#    i just imported the Turtle class from turtle module
timmy = Turtle()
""""""
print("printing an object")
print(timmy)
print("doing stuff with the object")
""""""
print(timmy)
timmy.shape("turtle") # giving timmy a new shape

timmy.color("red", "black") # changing the color of timmy

timmy.forward(100)
## object attribute
# attributes are the variables that are associated with the object

#car.speed --> car is the object and speed is the attribute
# seperated by a dot

# importing another class from the turtle module in line 75 - named Screen

# Screen is the window in which the turtle is going to show up

my_screen = Screen()
# tapping into Screens properties - attributes
print(my_screen.canvheight) # 300

## has attributes - properties
## does functions - methods

# object name and the function or the method are seperated by . dot notation car.stop()

# tapping into its functions - methods
my_screen.exitonclick() #only exist when screen detect a click
#it will stay untill we click the screen

# mmoving timmy by 10 paces
# timmy.forward(100)
# if i run the line of code here it wont meet the desired outcode
# so i ran it in line 88
"""


# Complete code from this turtle module
"""
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

# without using the window it will just act as a pop up and then be closed

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""

## 111 Pypi and python packages

"""
we created modules - single file like another module
packages are more than modules
packages are available in pypi.org - documentation for other python developers source code
"""

# installing pettytable package
#import prettytable

## 112 Modifying object attributes

from prettytable import PrettyTable

table = PrettyTable()
# print(table) # commenting this since there are no values

# method - x.add_column(column_name, list of values that go into that column in square brackets)

# # table.add_column("S class",["me", "only me","one and only me"])

table.add_column("Pokemon Name",["pikachu","squirtle", "Charmander"])
table.add_column("type",["Electric","water","fire"])
print(table)

# Manually changing table styles
# from the centered alingnment to left

# here i am changing the attribute value
table.align = "l"
print(table)