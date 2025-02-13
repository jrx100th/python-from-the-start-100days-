## Day 5
"""
today goal is to make a program that will generate string passwords
"""

## 38 For loop with python lists
"""
# syntax : 
for item in list_of_items:
    # Do something to each item



fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    
# now all the intems in the list will be printed in the name of fruit

fruits = ["Apples", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    # indentations are important
print(fruits)
# it is printed only once after the for loop because it is not in the
# for loop

"""

## 39 Highest Score
"""
student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

#sum is an inbuilt function - sum takes a list of numbers and then sums it
total_exam_score = sum(student_scores)

print(total_exam_score)

#summing the same thing using the for loop

#creating the variable that holds the sum outside the loop
sum = 0

for score in student_scores:
    sum += score
    print(sum)
print(sum)



print(
    max(student_scores)
)
# it will output the maximum value in the list...
# now doing the same thing using for loops

maxn = 0
for sco in student_scores:
    if sco > maxn :
        maxn = sco
print(maxn)

## same as the max() function to a list

## remember the variable holding the value should be created outside the loop

"""

# 40 for loops and the range function

"""

syntax : 
for item in list_of_items:
    #do something to each item...stuff like that



# using a loop that is independent of the list

# carl gauss - german mathboy

sum = 0

for i in range(0,101,1):
    sum += i
    print(sum)
    
syntax : 
for i in range(start, stop, step):
    do stuff
    
# range function - used with for loop


for num in range(1,11):
    print(num)

# it prints from range(a,b, step) - starts from a and ends at b-1



# adding 1 to 100 using code
sum = 0
for i in range(1,101,1):
    sum += i
    print(sum)

"""

## coding challenge - fizz buzz
# mutiple conditions on the top of the order
"""
for i in range(1,101,1):
    if i%3 ==0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

"""

# 41 Day 5 Project : Password Generator

import random

print("Welcome to PyPassword Generator!")

lc = int(input("How many letters you want in your password? :"))

sc = int(input("How many symbols? :"))

nc = int(input("How many numbers? :"))

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numer = [0,1,2,3,4,5,6,7,8,9]
symbols = [
    "+", "-", "*", "/", "//", "%", "**",  # Arithmetic operators
    "=", "+=", "-=", "*=", "/=", "//=", "%=", "**=",  # Assignment operators
    "==", "!=", ">", "<", ">=", "<=",  # Comparison operators
    "and", "or", "not",  # Logical operators
    "&", "|", "^", "~", "<<", ">>",  # Bitwise operators
    "(", ")", "[", "]", "{", "}",  # Brackets
    ",", ":", ".", ";", "@", "=", "->",  # Miscellaneous
    "'", '"', "\\", "#",  # String and comment symbols
    "_", "?",  # Underscore, optional (not used in syntax)
]

# random.shuffle() for shuffling the password after formation
# random.choice() for picking the random item from the list

pwd = []
# always create the variable holding the values outside the loops

## adding the letters to the password
for i in range(1,lc+1,1):
    pwd.append(random.choice(alpha))

#print(len(pwd))
# adding symbols to the password
for i in range(1,sc+1,1):
    pwd.append(random.choice(symbols))

## adding numbers
for i in range(1,nc+1,1):
    pwd.append(random.choice(numer))

## shuffling the password
random.shuffle(pwd)
# random.shuffle() will shuffle ...dont assign this value
# like pwd = random.shuffle(pwd)... == outputs none

print(pwd)
"""
pwd = ''.join(map(str,pwd))


# usuallu ''.join(pwd) will just join as desired when we have all the values as strings
# since all the values are not in strings
# we are going to map the items in strings and then join
# ''.join(map(str, list))

## damn we can also use a for loop and add all the things to a emty string

fpwd = ""

for char in pwd:
    fpwd += i
    print(fpwd)
"""
## even for this every item in the list needs to be string for the string concatenation

