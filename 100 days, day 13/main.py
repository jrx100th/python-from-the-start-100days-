"""# Day 13

# 94 Describe your problem

for i in range(1,20):
    print(i)

# it will not print 20 stops with 20 and prints 19
"""

# 95 Reproduce the bug
"""
import random
print(random.randint(1,6))
# here if we use a list then we will get the indexoutofbound error
# only when it generates 6 and it will never generate the first element
print(random.randint(0,5))
# this will print the correct list of length 6
"""

# 96 Play computer and evaluate each line
"""
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a genz")

# this one will only check for greater or less than 1980 or 1994
# but will never check if the value is 1980 or 1994
"""
# so you can use the else statement
# or you can use >= or <= or ==
# i mean in the first if else statement, false statements will be skipped

# 97 Fixing errors and checking for red underlines

"""
check for indentations
enter the variable according to its data type that we assigned-int(), float(), str() - ValueError()


age = int(input("How old are you :"))

def driving_permit(age):
    if age > 18:
        print(f"You can drive at age {age}.")
    else:
        print(f"You can't drive at {age}")

# driving_permit(age) # but it will throw an error if i enter a string



try:
    age = int(input("How old are you? :"))
except ValueError:
    print("Please enter only numbers in the input field")

# now this is called exception handling

# instead of breaking the program we need to give the user another chance at input field

"""
"""
try:
    age = int(input("How old are you? :"))
except ValueError:
    print("Please enter only numbers in the input field")
    age = int(input("How old are you? :"))
    # if you do the same error you are fkd for now

## these are called bugs
## they are not errors
"""

## 98 Squash bugs with print() statement
"""
word_per_page = 0
pages = int(input("Number of pages :"))
word_per_page = int(input("Number of words per page :"))
total_words = pages * word_per_page

#print(f"pages = {pages}")
#print(f"words_per_page = {word_per_page}")
print(f"total words = {total_words}")
"""

## 99 Debugger
import random
def add(n1, n2):
    return n1+n2
"""
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2 #here it just resets the value
        new_item += random.randint(1,3)
        new_item = add(new_item, item)
    b_list.append(new_item)
    print(b_list)

a_list = [1,2,3,5,8,13]

#new mutate function where multiple items can be found in the list

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item*2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
        b_list.append(new_item) ## added an indent compared to previous code
    print(b_list)

mutate(a_list)

"""

# from a coding exercise
# anyway this is the answer for is_leap() function

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(100)