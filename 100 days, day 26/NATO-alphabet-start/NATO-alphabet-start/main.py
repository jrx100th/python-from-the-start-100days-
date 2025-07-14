student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
csv = pandas.read_csv(r"C:\Users\jenit\PycharmProjects\100 Days\100 days, day 26\NATO-alphabet-start\NATO-alphabet-start\nato.csv")

#TODO 1. Create a dictionary in this format:
mapper_dict = {row.letter: row.code for (index, row) in csv.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# literally creating a list

prompt = str(input("Enter a word :"))
print(prompt)
response = ["____" if letter == " " else mapper_dict[letter] for letter in prompt.upper()]

"""for letter in prompt.upper():
    if letter == " ": response.append(" ")
    else :response.append(mapper_dict[letter])
"""
print(response)