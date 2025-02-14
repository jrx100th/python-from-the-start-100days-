## Day 6
## functions, while loops and code blocks

## 44
"""
syntax :

def my_function():
    print("Hello")
    print("Bye")

triggering the fucntion we created - calling the function

# calling the function

my_function()

def - keyword...for specifying that it is the definition
my_function() - it is the name of the function
(): -- set of parenthesis and a colon
then the
    indented instructions that the function need to perform

# calling the function - my_function()

# Karel the robot

fucntion contain multiple instructions

## Reeborgs world arc
- not inbuilt turn around or the turn around function


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()
    move()
    turn_left()

def spe_sq():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

spe_sq()


"""

# Hurdles loop challenge

"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def movef_and_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def complete_basic_hurdle():
    movef_and_jump()
    movef_and_jump()
    movef_and_jump()
    movef_and_jump()
    movef_and_jump()
    movef_and_jump()

complete_basic_hurdle() ## uses 92 steps

most effecient way of jumping the basic level one hurdle


for step in range(6): ## uses 99 steps
    movef_and_jump()
    
this will also work instead of the complete_basic_hurdle() function
"""

# 46 indentation
"""

file structure is similar
# indentation will seperate the blocks of code from one another
"""

## 47 While Loops

# loop that continue going untill a condition is true

"""
# for loop syntax : 
for item in list_of_items:
    #Do something to each item
    
for number in range(a,b):
    print(number)

# While syntax : 

while something_is_true:
    #do something repeatedly

# Back to the hurdle 1 challenge


number_of_hurdles = 6
while number_of_hurdles > 0:
    movef_and_jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    
# performs 118 steps

# Hurdle level 2

right now the at_goal is false
so now it is false, when we go to the goal it is true

while not at_goal():
    jump()
    
while - infinite loop

while 5 > 3:
    #Do this
    #Then do this
    #Then do this
5 is always greater than 3 and the loop will continue forever

just incase if you get a infinite loop then 
print the condition

while 5 > 3:
    print(5 > 3) # Always print true
    jump()

"""

## 48 Hurdles using the While loops

"""
3 brand new conditions - front_is_clear(), wall_in_front(), at_goal()

Clearing Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()


    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
"""

## 49. Jumping over Hurdless with variable Heights
"""

Hurdle level 3
front_is_clear()
right_is_clear()
wall_on_front()
wall_on_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

#front_is_clear()
#right_is_clear()
#wall_on_front()
#wall_on_right()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

       
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        
this will clear the hurdle with variable heights

for the maze part i cant do it because it is a bit annoying 
single code is solving multiple mazes except one maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
this is the code im talking about:
otherwise it is just going squares

But this code can beat all the maze cases

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
"""