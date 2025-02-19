# Day 12 : Number Guessing Project

#87 Namespaces: Local vs Global Scopes

# Local scope

"""

global scope is available anywhere within our file

and even from inside the function we can access the variable or stuff

but the variables outside a function cant acces the values that were created inside the function

namespace - defining stuff in the scope
it is mapping from names to objects.

"""

## 88 Does python have a block scope

"""
if 5>3:
    a_variable = 10

print(a_variable)

still the a_varaible is accessible to the outside

but if i put the 5>3 case statement in a new function....it wont be accessible to the outside
def func1():
    if 5>3:
        a_variable = 10

print(a_variable)# wont work outside the function
    
"""
# if i create a variable within a functioin then it is available only in the function
"""
game_level = 10
enemies = ["Skelton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = "Toy bots"
    if game_level < 5:
        new_enemy = enemies[0]
    """"""else:
        new_enemy = "Metal Heads"
        """"""

    print(new_enemy)

create_enemy() ## will work

#print(new_enemy) # will create an error stating NameError: name 'new_enemy' is not defined

# if the game_level is more than 5 then the if statement is never true and new_enemy wont be formed and the
# it sats UnboundLocalError: cannot access local variable 'new_enemy' where it is not associated with a value
# so for that add a else statment Or initialse the varibale outside the case statements

"""

# Coding exercise prime number checker
"""
def is_prime(num):
    if num < 2:
        return False
    # Checking if the number is less than 2
    for i in range(2,int(num**0.5+1)):
        if num % i == 0 :
            return False
    # Checking if the number is divisible by the numbers upto its square root

    # since a function stops after its first encounter with the return statement
    # if any of the above statements is true a return statement is triggered
    # if they arent triggered then it is prime and this one will trigger
    return True

print(is_prime(97))
"""

##89 How to modify a global variable
"""
enemies = 1

def em():
    print(enemies)

(em())"""
# this will use the enemies from the global scope

# global and local variables should'nt be the same name
"""
enemies = 1

def increase_enemies():
    enemies = 2 # we just created a new variable inside the function
    print(enemies)
# here the enemies variable from inside the function will be called 
increase_enemies()"""

# calling the global variable from inside the function
"""
enemies = 1

def increase_enemies():
    global enemies
    enemies +=1
    print(enemies)

increase_enemies() # now the global enemies variable will be used and moified
"""
# it is not advised to modify the global variable within the function
"""
#modifying the global variable outside the function
# instead of printing it at the end of the function we can return it and increment or alter the value
enemies = 1
def increase_enemies():
    return enemies + 1

print(increase_enemies())

# then it is increased by 1 and the value is not changed in variable
# only changed in the function output
"""

# 90 Python Constraints and global scope

# global contraints - the values that you are never going to change - constant
# Naming conventions - ALL UPPERCASE and seperated by UNDERSCORE
# Naming conventions are not mandatory but recommended

# so that next time when you use that and see the uppercase you will be reminded not to change the value


"""
## Number Guessing project
import random

print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
comp_num = (random.randint(1,100))
diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts_left = 0

if diff_level.lower() == "hard":
    attempts_left = 5
elif diff_level.lower() == "easy":
    attempts_left = 10
else:
    print("\n\nInvalid input in the difficulty field!")
    exit()

while attempts_left > 0:
    print(f"\n\tYou have {attempts_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > comp_num:
        print("\t\nYour guessed value is higher")
    elif guess < comp_num:
        print("\t\nYour guessed value is lower")
    else:
        print(f"\n\t\n\tYou win the number is {comp_num}")
        exit()
    attempts_left -= 1

# here still it will crash when the user enters a text or sc in the guess field
"""