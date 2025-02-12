## 22 Control Flow with if/else and conditional operators
"""
pseudo code
water_level = 50

if water_level > 80;
    print("drain water")
else:
    print("continue")

## rollercoaster example

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ?"))

if height >= 120:
    print("You are allowed")
else :
    print("Sorry you have to grow taller")

## compaarision operator like >, <, >=, <=, ==, !=
 = single equal sign you are assigning the value to a variaibel
 == means we are checking if both are same or not ..
 outputs a boolean such as True or False


height = 120

print(height == 120)
print(height != 120)
print(height < 120)
print(height > 120)
##print(height = 120) type error
"""


## 23 Introducing the modulo
"""
# Modulo operator - %
# gives back the remainder
10 / 5 = 2
and the remainder is 0 - the division is clean
so is 
10%5 = 0

10%3 = 1
10/3 = 3.3


# Even number 12 % 2 = 0

num_to_check = int(input("What is the number you want to check?"))

num = num_to_check%2

if num == 0:
    print(f"{num_to_check} is Even number")
else:
    print(f"{num_to_check} is odd number")

## Could be more effecient

"""

## 24 Nested if statements and elif statements
"""
now height + age
<=18 7
> 18 12

syntax : 
if condition:
    if another condition:
        do this
    else : 
        do this
else :
    do this


height = int(input("What is your height in cm :"))
age = int(input("What is your age in years :"))

if height >= 120:
    print("You are allowed, but check the price")
    if age > 18 :
        print("You have to pay $12")
    else:
        print("You have to pay $7 since you are under 18")
else :
    print("Go home grow taller")


#Angela version asking the age only after theh height verfiication

height = int(input("What is your height in cm :"))

if height >= 120:
    print("You are allowed but what is your age")
    age = int(input("What is you age : "))
    if age > 18:
        print("You have to pay $12")
    else :
        print("Ask your mommy to pay 7 bucks for your lame ass")
else :
    print("Go home and water yourself and grow taller. :)")



## Added a 3rd tier where the kid is between 12 and 18
# Maybe just introducing the elif


height = int(input("What is your height in cm :"))

if height >= 120:
    print("You are allowed but what is your age")
    age = int(input("What is you age : "))
    if age < 12:
        print("Ask your mommy to pay 5 bucks for your lame ass")
    elif 12 < age < 18:
        print("Pay 7 bucks")
    else :
        print("Pay 12 bucks for your lame ass")
else :
    print("Go home and water yourself and grow taller. :)")

"""

## practical
"""
weight = 96
height = 1.65

bmi = round((weight/(height**2)),2)

if bmi < 18.5:
    print("underweight")
elif 18.5 < bmi < 25:
    print("normal weight")
else:
    print("overweight")

"""

## 25 Multiple if statements in succession

"""
## Adding a picture to the roller coaster
extra 3 dollars for the photo
...

so multiple if
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C


height = int(input("Enter your heigtht in cm :"))
amount = 0
if height > 120:
    print("You are allowed, lets check your age ")
    age = int(input("Enter your age : "))
    if age < 12 :
        amount += 5
        picture = (input("Do you want to take a picture Y, N :"))
        if picture == "Y":
            amount += 3
            print(f"You have to pay ${amount}")
        else :
            print(f"You have to pay ${amount}")
    elif 12 < age < 18:
        amount += 7
        picture = (input("Do you want to take a picture Y, N :"))
        if picture == "Y":
            amount += 3
            print(f"You have to pay ${amount}")
        else :
            print(f"You have to pay ${amount}")
    else:
        amount += 12
        picture = (input("Do you want to take a picture Y, N :"))
        if picture == "Y":
            amount += 3
            print(f"You have to pay ${amount}")
        else :
            print(f"You have to pay ${amount}")
else :
    print("Go home grow tall")

"""

## 26 Pizza order practice
"""





print("Welcome to Python pizza delivaries")

size = input("What size pizza do you want? S, M or L :")
pepperoni = input("Do you want pepperoni on your pizza? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")

bill = 0

if size.lower() == "s":
    bill += 15
    if pepperoni.lower() == "y":
        bill += 2
        if extra_cheese.lower() == "y":
            bill += 1
            print(f"Your bill is ${bill}")
        else :
            print(f"Your bill is ${bill}")
    else :
        print(f"Your bill is ${bill}")
elif size.lower() == "m":
    bill += 20
    if pepperoni.lower() == "y":
        bill += 3
        if extra_cheese.lower() == "y":
            bill += 1
            print(f"Your bill is ${bill}")
        else:
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
    bill += 25
    if pepperoni.lower() == "y":
        bill += 3
        if extra_cheese.lower() == "y":
            bill += 1
            print(f"Your bill is ${bill}")
        else:
            print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")

## this will work
## so is this one


print("Welcome to Python Pizza Deliveries")

size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

if pepperoni == "y":
    bill += 2 if size == "s" else 3  # Small pizza gets $2, others get $3

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}")

"""

## 27. Logical Operators

"""
checking for multiple conditions 
using the logical opertors

like 
only if a condition is true then the statement will be executed
now logical operators do the same thing

syntax : 
if condtion1 & condition2 & condition3:
    do this
else:
    do this

A and B
C or D
not E



a = 12
print(
a > 15
)

print(
    a > 10
)

print(
    a > 10 and a < 10
)

print(
    True and True
)
# And - True when all the conditions are true &&
# Or  - Truw when one of the conditions are true ||

## edit this stuff with the elif in the rollercoaster stuff
# mid life crises - means we aged between 45 and 50
# so the age is more and 45 and less than 50
# age < 50 and age > 45



age = int(input("Enter the age :"))

if age > 45 and age < 50:
    print("so are you facing midlife crisis")
else :
    print("Stay happy, stay healthy")

here we are checking 2 conditions and have the "and" logical operator
"""

# Quiz
"""
a = 5
b = 7

if a >= b and a != b:
    print("A")
elif not a >= b and a != b:
    print("B")
else:
    print("C")
    
The computer will keep on checking untill one of the condition becomes true

"""

# Day 3 Project Treasure island

# lot of bs
# mind those double and single quotes, and use backslash to escape some stuff so that it wont be interpreted as code
# uses .lower() fucntion for more flexibility