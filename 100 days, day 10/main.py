## Day 10: Goal : calculator basic


## 73 Functions with outputs
"""
def my_function():

def my_function(parameter):

# functions with outputs

def my_function():
    result = 3*2
    return result



def format_name(f_name, l_name):
    ## make both names will become title from their current format
    # for making stuff to title case

    print(f_name.title())
    print(l_name.title())

    # now storing those values in a variable

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    #print(f"{formatted_f_name} {formatted_l_name}")
    # instead of printing we are going to return the formatted vlues

    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("jon","jones"))
# does the same thin


difference between print and return

def function1(text):
    return text + text

def function2:
    return text.title()

output = function2(function1("Hello"))
print(output)

the same cant be done

if we use the print function

return vs. print in Python
Feature	                                return         	print()
Purpose	Sends a value back from a function	            Displays output to the console
Where it's used	Inside functions	                    Anywhere in the code
Can be stored in a variable?	        ✅ Yes	        ❌ No (prints directly)
Affects program flow?	                ✅ Yes (stops function execution)	❌ No
Returns a value?	                    ✅ Yes	        ❌ No (always returns None)

"""

## 74 Multiple Return Values
# more than one return statement
# return statement is the last instruction in a function,
# you might not know it but the computer knows it
# So after the return statement the next statements are ignored by the compiler

# bringing back the format_name function
"""
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid input" ## now compiler is going to see the return and skip the below rest of the function
    # this is a early return
    ##  this return - returns none
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result \t{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("what is your last name")))

"""

# coding exercise

"""

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(1900))

explaination : 
the first brackets 
year % 4 == 0 and year % 100 != 0
sees if the year div by 4 and checks it is not a odd 100
if it...
just understand it, i cant explain this basic logic
"""

# 75 Docstrings
"""
name = """"""
it is a documentation string
""""""
a = (
    "..."
)

print(a)

documentating stuff
"""

# quiz
"""
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

# tricky one 
as the outer function is taking other values and calling the inner function
here outer function can access the inner values
but the inner values cant see the outer one because of theh global scope restrictions

by the way the answer is 15

# Another tricky one

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

# check for the empty return statement....they will return none, and break the flow of the program
"""

## The Calculator Project
# The Calculator Project
"""
def multiply(num1, num2):
    return num1 * num2


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def div(num1, num2):
    if num2 == 0:
        return "Error: Division by Zero"
    return num1 / num2


end_program = False
eq = ""

num1 = float(input("What is the first number: "))
while not end_program:
    eq += str(num1)
    eq += " "

    print(""""""
    +
    -
    *
    /
    """""")
    op = input("Pick an operation: ")
    eq += op
    eq += " "

    num2 = float(input("Pick another number: "))

    if op == "*":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif op == "+":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif op == "-":
        result = sub(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif op == "/":
        result = div(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation! Please enter +, -, *, or /.")
        continue  # Restart loop if an invalid operation is entered

    fut = input("Type 'y' to continue with the result, or 'n' to start new calculation, or 'exit' to stop: ").lower()

    if fut == "y":
        num1 = result  # Continue with the previous result
    elif fut == "n":
        num1 = float(input("Enter the first number for a new calculation: "))  # Start fresh
    elif fut == "exit":
        end_program = True
    else:
        print("Invalid input. Exiting program.")
        end_program = True
"""

# Forbidden knowledge @ course content

def add(n1, n2):
    return n1+n2

# Creating a variable to store the operation

func_holder = add

print(func_holder(2,3))

# now the func holder will act as the function that hass been assinged to it
# storing the functions in the operation

operations = {
    "op": "op_func"
    # operation functions
}
#@ 12 min 30 sec
#https://www.udemy.com/course/100-days-of-code/learn/lecture/19658806#content
# accessing the functions operations["op"](4,8)

# op and the numbers will be the user input