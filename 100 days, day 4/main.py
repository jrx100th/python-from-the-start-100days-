# 31 Random Module
## Mersenne twister - random number generator - very complicated
import random
"""

random.randint(a, b)
it will generate a integer only between a and b
it will also output a and b


module - split the code into modules


print(
random.randint(1,10)
)

# now we can import the module that we created into this file script

import my_module

print(my_module.my_fav_num)
# and the variable from the other module has been imported



## creating random floating point numbers
print(
random.random()
# generate a floating point number between 0 and 1
    # strictly between 0 and 1
    # range is 0.0 <= x < 1.0
)



random_number_0_to_1 = random.random()

print(
random_number_0_to_1
)


# kids stuff

#random.randint(a, b) # takes inputs

random_number = random.random()
print(
    random_number*10
    # now it generates in between 0 and 10, since the possibility goes upto 9.9 bar
)


# random floating point number generator
# a <= N <= b
#random_float = random.uniform(a, b)
# generates numbers between a and b inclusive a and b

random_float = random.uniform(1, 10) # but there are chances of getting a 10.0

print(random_float)
# it is same as the random.random() * 10


## Heads or tales program

print("Heads or tails program")
uc = str(input("Heads or tails :"))

comp = random.randint(0,1)

if comp == 1 :
    print("Computer says heads")
else:
    print("computer says tails")

if uc.lower() == "heads" and comp == 1:
    print("You win!!!")
if uc.lower() == "tails" and comp == 0:
    print("You win!!")
else:
    print("You loose")

"""

## 32 Video - List

"""
lists - order of data - data structure

fruits = [item1, item2]
uses square brackets

fruits = ["orange", "mango", "grape"]



state_of_america = ["Delaware", "Pennyslyvania", "etc"]
# they will be in the order
print(
state_of_america[0]
)
# indexing works from 0

print(
    state_of_america[-1]
    # prints the last item in the list
)

# changing the values in the list
# from pensylvania to pencilvania

print("Before changing")
print(
    state_of_america[1]
)
print("After changing")
state_of_america[1] = "Pencilvania"
print(
    state_of_america[1]
)

print(state_of_america)
# even here it is changed

### Adding the item in the list
## using append

state_of_america.append("holovikar")

print(
    state_of_america
)
# now the new item holovikar has been added at the end of the list

## other fucntions in the docs.python documentation

## adding another list to the existing list

print("\n before extending another list")
print(
    state_of_america
)

state_of_america.extend(["ust1", "ust2", "ust3"])

print("\n after extending another list")
print(
    state_of_america
)
print(
    "Extend only adds a single item..\n even that item can be a list"
)


## just lookup on the documentation when you need it
"""

##33 Practical activity
"""
names = ["arjun","vinay","ganesh","jai","siva"]

name = random.randint(0,4)

print(f"{names[name]} has to pay the bill today")

nam = random.choice(names)
# random.choice(list_name) is lot faster and does the same thing
print(f"{nam} has to pay the bill")
"""

# 34 IndexErrors and working with nested lists
"""

dumbfuc|<s get this error because they dont know how the indexing works...i mean 
just follow whole numbers , not natural


# nested lists
n1 = ["n123","n124", "n125", "n126", "n127", "n128"]
n2 = ["n923","n924", "n925", "n926", "n927", "n928"]

n21 = [n1, n2] ## lists in lists
print(
    n21
)
"""

# quiz
"""

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
## outputs : kale
"""

# Day 4 project : Rock Paper scissors
"""
print("Welcome to rock paper scissors")

ui = int(input("What do you want to choose : 0 for Rock, 1 for Paper, 2 for Scissors :\n"))
rps_list = ["Rock", "Paper", "Scissors"]
comp_choices = [0,1,2]
computer = random.choice(comp_choices)

print(f"You choose {rps_list[ui]}.")
print(f"Computer choose {rps_list[computer]}.")

if ui == computer:
    print("Tie, no won wins")
else :
    if ui == 0 and computer == 1:
        print("You loose")
    elif ui == 2 and computer == 1:
        print("You win")
    elif ui == 1 and computer == 0:
        print("You win")
    elif ui == 2 and computer == 0:
        print("You loose")
    elif ui == 1 and computer == 2:
        print("You loose")
    elif ui == 0 and computer == 2:
        print("You win")

i know these things in the course are so dramatic

"""