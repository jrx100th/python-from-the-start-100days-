# Day 9 : Dictionaries and nesting

## 68 Python Dictionary
"""

key and value
syntax :
{key : Value}
{"bUg": "An error in a program that prevents the program from runnning as expected."}
key, value pairs
more than one entry in the dictionary - seperate them by coma,

#incase of more than 1 pair then concentrate on the readability


programming_dictionary = {
    "Bug": "An Error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again."
}

# retrieving an pair/item from the dictionary
# list - index
# dictionary - identify by the key
"""
"""print(
programming_dictionary["Bug"] # outputs the value stored wrt the key
)

# using the key we get the value from the pair

# similar to index error we get key errors here

# use the same data type to retrieve

# Adding a pair "after" defining the dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"

# now the third value has been added
#print(programming_dictionary)

# creating an empty_list
empty_list = []

# creating an empty_dictionary
empty_dictionary = {}

# wipe an existing dictionary

#programming_dictionary = {}
"""
"""
print(
    programming_dictionary
)
# outputs an empty dictionary

# edit an item in a dictionary using the key in the dictionary
programming_dictionary["Bug"] = "A moth in your computer"

print(
programming_dictionary["Bug"]
)

# now the value that has been stored in your computer has been changed

## Looping through a dictionary using its key

for key in programming_dictionary:
    print(
        programming_dictionary[key]
    )
    
"""
"""
print(
programming_dictionary[0]
)
# This will give an error beacuse it doesnt have any index values

for key in programming_dictionary:
    print(key)
# the above loop will print the keys

"""

## Coding exercise
# filling an empty dictionary with existing keys and new values
"""
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90 and student_scores[student] < 100:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80 and student_scores[student] < 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70 and student_scores[student] < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
# Explaination : 
adding the values in the empty dictionary with student_grades[student] = based on the if else statement
"""



# 69. Nesting Lists and Dictionaries
"""
we can have a list, dictionary in the values of the dictionary
like this

{
    key : [list],
    key2 : {dict}
}

# sample dictionary
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}
# each key can only have one value

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"]
}

## printint Lille from travel_log
print(
    travel_log["France"][1]
)
# france is the key in the dictionary and then the list is the value strore in the value
# then we index the list value and then index it

nested_list = ["A","B",["C","D"]]

# printing the letter D from another list
print(
nested_list[2][1]
)
# here we indexed the first_list and then we index the value of the nested list


# Nesting a dictionary within a dictionary

travel_log = {
    "France" : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12
    }
}

#printing stuttgart from the travel log
print(
travel_log["Germany"]["cities_visited"][2]
)
# accessing the value stored in the key germany
# accessing the list stored in the key cities_visited
# indexing the value to retrieve the item in the list

"""

# Quiz question
#Which line of code will print "Steak"?
"""
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(
    order["main"][2][0] ## will output Steak
)
print(
    order["main"][2] ## will output ["Steak"] and it is not right
)
# specfics matter

"""

# 70 Secret Auction:
"""
game_end = False
holdings = {}
while not game_end :

    print("Secret Auction starts")
    name = str(input("What is your name :"))
    bid = int(input("Enter your bidding :$"))


    holdings[name] = bid

    #print(holdings)

    choice = str(input("Any other bidder? yes/no :"))

    if choice == "yes":
        print("\n"*10)
        continue
    if choice == "no":
        game_end = True

        winner = max(holdings, key=holdings.get)
        highest_bid = holdings[winner]

        print(f"The winner is {winner} with a bid of ${highest_bid}.")

"""
## last 3 lines of the code are a bit out of the current knowledge

"""

max(holdings, key = holdings.get)

holdings.get retrieves the bid amount for eachh name
and max compares the retrieved values
and assigns the max value to the winner variable


"""

test_dict = {
    "jen":987,
    "ren":968,
    "nen":932,
    "een":973,
    }

#print(max(test_dict))
## will print ren
# because it will not check the values instead it will check for the lexicographical order of the key since they are strings
"""
print(
max(test_dict, key = test_dict.get)
)"""
# will output jen, because it is comparing the values and giving the key with the highest value

# syntax :
#print(max(test_dict, key=test_dict.get))  # Output: "jen"
# use key = dictionary.get for seeing the value inside and getting key

# you must specify key= when you want to compare values instead of keys.

# coming to the .get
# it is used along with max(), min(), sorted() to compare dictionary values
