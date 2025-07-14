"""# list_comprehension = creating a new list from previous loop

# new_list = [new_item for item in list]

numbers = [1,2,3]

new_list = [n+1 for n in numbers]

print(new_list)

name = "jrx100th"

chars = [letter for letter in name]
print(chars)

nums = [n*2 for n in range(1,5)]

print(nums)

# just regullar loops just in a single line

# conditional statements can also be added in this list comprehension


# new_list = [new_item for item in list if condition]

names = ["Alex","Aleksi","Catherine","Katherine","Elanor","Jeff"]
# less than or equal to len 4
short_names = [name for name in names if len(name)<=4] # same as <5
print(names)
long_names = [name.upper() for name in names if len(name) > 5]

print(names)



# now the names with len more than 4 will be captilized and then the rest will be as it is 
big_caps = [name.upper() if len(name)>4 else name for name in names]
print(big_caps)

# made changes in the list comprehension and it will work fine when it is inly opening the single folder where the main file is in 
# but when opening with multiple folders then it couldnt figure out the blank_state_gif




# Dictionary Comprehensions

# new_dict = {new key : new_value for item in list}

# create a new dict from values of existing dictionary values

# new_dict = {new_key : new_value for (key, value) in dict.items()}

# adding in the conditions

# new_dict = {new_key : new_value for (key, value) in dict.items() if test}

names = ["Alex","Beth","Caroline",'Eleanor',"Freddie"]

import random

students_scores = {student : random.randint(1,100) for student in names}

# now looping through a dictionary

passed_students = {
    key : value for (key, value) in students_scores.items() if value > 60
}

print(passed_students)






## Iterate over a pandas dataframe

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56,76,98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas 

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a df

# for (key,value) in student_data_frame.items():
#     print(key, value)

# pandas has an inbuilt function that allows us to iterate through the rows


# loop through the rows of the dataframe rather than each of the columns

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

for (index, tuple) in student_data_frame.itertuples:
    print(tuple)
    # works better

    
"""