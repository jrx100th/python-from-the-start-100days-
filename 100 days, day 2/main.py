## 14 video

# data types
"""
string
integer
boolean
float

# indexing
print("Hello"[0]) # outputs "H"
##starts from zero

pulling out last character

print("Hello"[-1]) ## outputs o, backwards negative

# string concatenation and indexing
print(("123"+"345")[0]) #here the numbers are strings
print(123+456) # outputs a number

print(123,456,789) ## spacing
print(123456789) ## just the number
#Large number
print(123_456_789) ## again prints just the number
###print(123.456.789) ## will give an error
# float - decimal point

# boolean
print(True)
##print(false) ## will give an error
# it is case sensitive
"""

## 15 video
"""
print(len("123"))

##checking the type
print(type("Hello"))
# output : <class 'str'>

print(type("string"))
print(type(896))
print(type(5698.6))
ttt = True
print(type(ttt))
#output :
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>


##changing data types
print(type(int("123")))
## boom data type changed
# int is a built in function that changes the numbered strings into uintegers
# but it wont work on the real alphabet strings - causes invalid literal


# All the inbuilt functions
int()
bool()
str()
float() ## can do the same using multiplying the integer with 1.0 ...like those SQL days
print(2*1.0)


#Before debugging
#print("Number of letters in your name : " + (len(input("Enter your name"))))
# After debugging
print("Number of letters in your name : " + str(len(input("Enter your name"))))
## now just basic string concatenation 
# instead of concatenating the string with a number
"""

# 16 video
"""
Mathematical operations
division alsways causes floating point numbers eg 6/3
python implicit float conversion

so 
6//3
or 5//3
will give the numbers and and not the decimals


## all the types
print(123+456)
print("my age " + str(23))
print(7-3)
print(3*2)
print(5/3)
print(5//3)
print(2**3)

# Pemdas
()
**
*
/
+
-


print(3*3+3/3-3)
# output 7.0 based on pemdas and calculation goes from left to right

print(3/3*3-3+3)
## changed the positions of the symbols and
## now it will output 3.0
## you can add the parenthesis for more ease of changing the value

"""

## 17 Video - Number manipulation
"""

bmi = 84/1.65**2
print(bmi) ## original calc value
print(round(bmi,2))
#this round function will also work just like sql
## rounding to 2 decimal places

print(int(bmi))
## now this will floor the value - flooring it to the lowest whole number

print(round(bmi))
## now this will just round the whole number to the closest integer

score = 0
score += 1
# just same as
score = score + 1


score = 0
score +=1
print(score)

# f strings

print("Your score is " + str(score))
## but the above line lacks mathematical complexity
# so we use f strings

height = 1.0
is_winning = True

print(f"Your score is = {score}, your height is {height}\n,You are winning is {is_winning}")

## this sentance is a demnstration of f string

"""

# int(2.7) = 2
# 5/2 = 2.5 float value

## Day 2 Project Tip calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
count = float(input("How many people are splitting the bill? "))
total = round((bill*((tip_percent/100)+1))/count,2)

print(f"Each person shuld pay : ${total}")