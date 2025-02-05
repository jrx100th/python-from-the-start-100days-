"""
Video 7
new line - backslash n
print("Hello World! \nHello World \nHeloo world")


#String concatenation
print("Hello" + " Jenith") ## Here i added a space in between
print("Hello" + " " + "Jenith")
##same output for both of the lines
# taking seperate strings of characters and merging them into one


## leaving unused spaces/tab - leads to indentation error
 print("world")


##8. Python Input function

#inside parenthesis is called prompt
#input("What is your name? :")
#input("A prompt for the user"),....saving the data from this field


print("Hello " + input("What is your name :"))
##first it will execute the input function and
# then it will print stuff along with our input

#   Concatenating a ! at the end of the statement

#print("Hello " + input("What is your name :") + "!")
# As i said the input function will be executed first, then
# the content from the print statement


#9. Python Variables
name = input("What is your name :")
print(name) ## referring to the piece of data

## now updating it
name = "Jenith"
print(name)
name = "Jrx100th"
print(name)

gave the name variable to different piece of information to hold onto

name = input("What is your name")
print(len(name))
## use the len() function i mean in lower cases only and
## never use LEN() like in the SQL code
print(len(input("What is ur name")))


username = input("What is your name")
length = len(username)

print(username)
print(length)

#10. Variable Naming
#make your code readable, should make sense
like username, or user_name but not user name,
you just can have spaces
or like SQL you cant have spaces in the variable and make ita a string
You should'nt use any keywords
Always refer to the existing/defined names

"""
##Day 1 project

print("Welcome to Band Name Generator.")
city = input("What's the name of the city you grew up in :\n")
pet_name = input("What's your pet's name? :\n")
print("Your band name could be " + city + " " + pet_name)

# used \n for getting the inputs in the new line