## 127. Day 18. BS

"""
from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.pencolor("red") # can also use color

def turtle_square(t):
    for _ in range(4):
        t.forward(100)
        t.left(90)


def turtle_triangle(t):
    for _ in range(3):
        t.forward(100)
        t.left(120)


def turtle_circle_right(t):
    for _ in range(360):
        t.forward(1)
        t.right(1)


def turtle_circle_left(t):
    for _ in range(360):
        t.forward(1)
        t.left(1)



screen = Screen()
screen.exitonclick()


# tk is tk inter - tk interface - GUI - Graphic user interface



text interface shows you text and lets you type stuff,
gui shows images and allows to click, drag, rather than typing commands


turtle relies on tkinter, under the hood for these graphics
"""





## 130. Importing Modules, Installing Packages

#import turtle

#tim = turtle.Turtle()


# from      turtle         import     Turtle        # is also possible
# keyword   module_name   keyword     thing in module



# IMPORT everything from that module = *

#from turtle import *

# giving an alias
# import turtle as t

# now the t will represent the entire module 

# tim  = t.Turtle()



## there are some modules that you cant import and they need to be installed

# the one we can import are packaged with the python standard library
"""

# better pipi install
import heroes

print(heroes.gen())

import villains

print(villains.gen())
"""






## 131. Turtle Challenge 2.dashed line
"""
from turtle import Turtle, Screen

timmy = Turtle()

def dashed_line(t):
    for i in range(10):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

print(dashed_line(timmy))



screen = Screen()
screen.exitonclick()

"""



## 132. Turtle . different shapes

"""
from turtle import Turtle, Screen

timmy = Turtle()
timmy.hideturtle()

def triangle(t):
    for _ in range(3):
        t.forward(100)
        t.left(120)


def square(t):
    for _ in range(4):
        t.forward(100)
        t.left(90)


def pentagon(t):
    for _ in range(5):
        t.forward(100)
        t.left(72)


def hexagon(t):
    for _ in range(6):
        t.forward(100)
        t.left(60)


def heptagon(t):
    for _ in range(7):
        t.forward(100)
        t.left(360/7)


def octagon(t):
    for _ in range(8):
        t.forward(100)
        t.left(360/8)


def nonagon(t):
    for _ in range(9):
        t.forward(100)
        t.left(360/9)


def decagon(t):
    for _ in range(10):
        t.forward(100)
        t.left(360/10)


def draw_shape(num_sides):
    for i in range(3,num_sides+1):
        ang = 360/i
        for _ in range(i):
            timmy.forward(100)
            timmy.left(ang)

print(draw_shape(25))


screen = Screen()
screen.exitonclick()


"""





## 133. Turtle challenge : random walk

## turtle progresses by the same distance with different colours and directions

"""
from turtle import Turtle, Screen, colormode
import random

# colors = ["red","blue","green","violet","cyan","maroon","pink","orange","indigo"]


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

dirs = [90,180,270] # [(i for i in range(1,361))]
paces = [20]  # [i for i in range(100)]
timmy = Turtle()
colormode(255)

timmy.width(6)


def random_walk(timmy):
    for _ in range(2000):
        timmy.color(random_color())     # this wont work untill i use the colormode(255)
        timmy.left(random.choice(dirs))
        timmy.forward(random.choice(paces))
        timmy.right(random.choice(dirs))
        timmy.forward(random.choice(paces))

timmy.speed(0)
print(random_walk(timmy))



screen = Screen()
screen.exitonclick()"""





## 135. Making a spirograph
"""
from turtle import colormode, Turtle, Screen
import random

timmy = Turtle()


def make_circle(timmy):
    for _ in range(360):
        timmy.left(1)
        timmy.forward(1)

def make_spirograph(timmy):
    for _ in range(100):
        make_circle(timmy)
        timmy.left(3.6)

print(make_spirograph(timmy))
colormode(255)
timmy.speed("fastest")

##print(make_circle(timmy))

def randc():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


timmy.speed(100)
def spiro(timmy):
    for _ in range(100):
        timmy.pencolor(randc())
        print(timmy.circle(100))
        timmy.left(3.6)

print(spiro(timmy))



screen = Screen()
screen.exitonclick()

"""









## 136. Extracting RGB values from images

# spot paintings
"""
import colorgram

img = 'hirst-3.webp'
colors = (colorgram.extract(img,100))    # frequency of real colours

rgb_colors = []


for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

color list are the distinct colors
"""









## 137. Drawing the dots

color_list = [(213, 157, 89), (238, 214, 95), (34, 106, 151), (126, 168, 198), (152, 76, 54), (208, 134, 163), (211, 85, 62), (155, 61, 82), (22, 39, 54), (173, 161, 49), (200, 87, 121), (136, 183, 151), (57, 117, 91), (228, 168, 187), (240, 212, 5), (27, 47, 38), (88, 156, 99), (66, 47, 34), (38, 165, 188), (227, 175, 166), (10, 98, 75), (41, 60, 101), (94, 127, 174), (179, 190, 212), (171, 204, 178), (69, 35, 44), (112, 44, 38), (102, 42, 62), (156, 207, 217), (78, 69, 35), (5, 85, 111)]


import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()

timmy.width(20)
timmy.speed("fastest")
def sl(timmy):
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.pendown()
        print(timmy.forward(1))
        timmy.penup()
        print(timmy.forward(50))# 10 to 30

def hirst_one(timmy):
    for i in range(0,10,1):
        timmy.setpos(0,i*50)# 10 to 30
        print(sl(timmy))

timmy.hideturtle()


hirst_one(timmy)

screen = turtle.Screen()
screen.exitonclick()