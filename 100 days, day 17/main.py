# Day 17
"""
Creating a classes
and creating the objects from those classes

And then we create a quiz from Python OOP
"""

# 117 Creating a class

# PascalCase
# camelCase
# snake_Case
"""
class User: # naming should be PascalCase
    pass # since we are not putting anything in it

user_1 = User()
"""

# 118. working with attributes, class constructors and init function
"""
class User:
    pass

user_1 = User()

# adding attributes

user_1.id = "001"
user_1.username = "jrx"

print(user_1.username)

## attribute is a variable that is associated with an object

user_2 = User()

# adding attributes

user_2.id = "002"
user_2.username = "hrx"

print(user_2.username)

# now instead of doing stuff manually i need to understand the constructor

# constructor - initialize object...setting value

#using the constructor function
class Car:
    def __init__(self):
        # initialize attributes
        # used to initialize the attributes
        
"""

"""
Adding attributes during the initialization

class Car:
    def __init__(self, seats):
        self.seats = seats
        # now it will be initialized

my_car = Car(5) # an object named my_Car will be created and it will seats = 5 as its variable

# it is similar to creating the my_car object first and then assign seats in another line
my_car = Car()
my_car.seats = 5

print(my_car.seats) # outputs 5
"""

# Creating from the start using the init function
"""
class User:

    def __init__(self, user_id, username):
        #print("new user being created..")
        # so whenever a new object is being created then the above line of code will be executes
        # setting the user_id
        self.id = user_id   # we need to call this using the id, not the user_id
        # setting the username
        self.username = username

        # haha now we are talking....meta im coming for you
        self.followers = 0
        # no need to input this field during the object creation

# name of the parameter = name of the attribute is the naming convention, for least confusion

user_1 = User("001","jrx")

# adding attributes manually
# user_1.id = "001"
#user_1.username = "jrx"

print(user_1.username, user_1.id)

# creating another user and assigning attributes in single line

user_2 = User("002","hrx", user_1.followers)

print(user_2.username,user_2.id,user_2.followers)

"""

## 119 Adding methods to a class
# bringing all the code without the comments


# Now adding methods/functions assciated with the class
"""
for the Car: class
class Car:
    def enter_race_mode()
        seats = 2

calling this method
my_car.enter_race_mode()

#my_car has been created in the previous comments
"""
"""
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):  # self is the first parameter - self meaning referring to the object that called it
        user.followers +=1 # user is the one whom we follow...goins into parenthesis and then we refere and call here to increment their followers count
        self.following +=1


user_1 = User("001","jrx")
print(user_1.username, user_1.id)

user_2 = User("002","hrx")
print(user_2.username,user_2.id,user_2.followers)

#user_1 decided to follow user_2
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
"""



# 120 Quiz Project part 1 - quiz model file
# Creating the Question class

# now open the quiz game folder

# 121 Quiz Project part2: creating the list of question objects from the Data file
"""
like this
question_bank = [
    Question(q1,a1),
    Question(q2,a2),
    Question(q3,a3)
    ]
"""

# 122 QuizBrain and next_question method

# 123 Adding the check_answer() method

# 125 OpenTrivia DATABSE advertisement - Using the API
"""
API - on browser - JSON format - Javascript object notation
json - similar to a python dictionary
"""