## Day 8 : Goal = ceaser cypher

"""
functions with inputs
arguments and parameters
"""
# 61 Functions with inputs

"""
functions syntax :
def my_function():
    #do stuff
    #instructions
    

def greet(name):
    print(f"Hello {name}")

greet("jenith")
def greet():
    print("hello")
    print("How do you do")
    print("isnt the weather nice")

greet()

## adding a variable as an input over the function

def my_function(something):
    #do this with something
    

def greet_with_name(name):
    print(f"hello {name}")
    print(f"How do you do {name}")

greet_with_name("jrx100th")

greet_with_name("jonjones")

here name is the parameter and the value we enter in the place when we call the function is called an argument

so name is the parameter and 
"jrx100th is the argument that has been passed

parameter is the name of the data that has been passed in
argument - the actual value that has been passed in
"""

# coding exercise
"""
age = int(input("Enter age :"))

def life_in_weeks(age):
    total_weeks = 90*52
    weeks_left = total_weeks - age*52
    print(f"You have {weeks_left} weeks left.")

if age > 90 or age < 0:
    print("You have entered an invalid input")
else:
    life_in_weeks(age)


## 62 Positional vs Keyword Arguments

def greet_with(name, location) :
    print(f"Hey {name} How is {location} !?")

greet_with("Anuj","Meldoco")

## now switching the order

greet_with("Meldoco","Anuj")
# positional arguments - order of the argument stays the same



# Keyword argumets - we can assign the values

#syntax :
def my_function(a=1,b=2,c=3):
    #do this with a
    #do stuff withh b
    # do bakchodi with c

# even after changing the order everything remains the same - because we assigned the values
# like this

my_function(c=3, a=1, b= 2)
# this wont change since the positions were assigned


def greet_with(name, location) :
    print(f"Hey {name} How is {location} !?")

# positional arguments
greet_with("Jrntih","Modypt")
# keyword arguments
greet_with(location = "5dpl", name = "uatop")
# makes code less error prone

"""

# coding exercises
"""
# love calculator

def love_calculator(name1, name2):
    t=name1.count("t")
    r=name1.count("r")
    u=name1.count("u")
    e1=name1.count("e")

    l=name1.count("l")
    o=name1.count("o")
    v=name1.count("v")
    e2=name1.count("e")

    true1_val = [t,r,u,e1]
    name1_true_sum = sum(true1_val)
    love1_val = [l,o,v,e2]
    name1_love_sum = sum(love1_val)

    print(f"T occurs {t} times")
    print(f"R occurs {r} times")
    print(f"U occurs {u} times")
    print(f"E occurs {e1} times")

    print("Total =", t+r+u+e1)

    print(f"L occurs {l} times")
    print(f"O occurs {o} times")
    print(f"V occurs {v} times")
    print(f"E occurs {e2} times")

    print("Total =", l+o+v+e2)



love_calculator("ejntth","real")

## i guess you got it how to
# just use the count() fucntion to make it lot easier else
# you just have to use the for loop to do the same

# implement the same for the 2nd name also

"""
"""
solution for the love calc

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")
"""
"""
## 63 Caesar cypher
direction = (str(input("Encode or Decode :"))).lower()

text = input("Type your message:")

shift = int(input("Type your shift number:"))
## number shift
# use index() function in python which is inbuilt function returning the index value of a particulr value in a alist
"""
"""
eg : 

alphabet = [
    # Uppercase letters
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

    # Lowercase letters
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    # Numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    # Special characters
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
    '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<',
    '.', '>', '/', '?', ' '
]

# now i want to find the value of
#print(keyboard_chars.index("j")) --> Outputs 35 as 35 is the index value of j in the list

# original text = hello and the shift_amount = 2
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount #7 --> 9

## Instead of the below method to overcome the index error you can also use more stuff in the original list containing values like me
        #shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position] #j

    print(f"Here is the encoded result : {cipher_text}")


encrypt(original_text= text, shift_amount=shift)


def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount

        output_text += alphabet[shifted_position]

    print(f"Here is the decoded result : {output_text}")

def caesar(original_text, shift_amount,encode_or_decode):
    output_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) - shift_amount

        output_text += alphabet[shifted_position]

    print(f"Here is the decoded result : {output_text}")

#decrypt(original_text = text, shift_amount= shift)
# Now lets check for the index out of range error

that one has a lot of drama
"""

import string

# Define the character set (letters, numbers, symbols, and space)
alphabet = list(string.ascii_letters + string.digits + string.punctuation + " ")


def caesar(text, shift, direction):
    output_text = ""

    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)

            # Determine shift direction
            if direction == "decode":
                shift *= -1

            new_index = (old_index + shift) % len(alphabet)
            output_text += alphabet[new_index]
        else:
            output_text += char  # Preserve characters not in alphabet

    print(f"Here is the {direction}d result: {output_text}")


# Get user input
direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ").strip().lower()
text = input("Enter your message: ")
shift = int(input("Enter shift number: "))

# Call the function
caesar(text, shift, direction)

## okay this short one might not work well
# but uses the pretty same concept
