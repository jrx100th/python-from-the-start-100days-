# # opening the csv file
# with open("./weather_data.csv") as file:
#     contents = file.readlines()
# # need to strip the new lines
# c = []
# for content in contents:
#     c.append(content.strip())
    
# print(c)
"""
# inuilt library
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # data is a object and can be looped through
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))

print(temp)


import pandas as pd

data = pd.read_csv("weather_data.csv")

# print(data["temp"],"\n",type(data))

# 2 core classes

# data frame = similar to excel or table
# series = single column/list

# these are the two datatypes of pandas


# creating a dict out of the dataframe

data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()

# print("\nAvg : ",round(sum(temp_list)/len(temp_list),2))

# pandas math operation on the series
print(data["temp"].mean())

#getting max value of temp using data series methods
print(data["temp"].max())


# get data in columns
print(data["day"])        # should be the same as the csv file first row representative for the column = header
print(data.condition)     # just works as the same one above


# Get data in row
# checking for row where day is monday
print(data[data.day == "Monday"])


# getting the row where the temperature is at maximum
print(data[data.temp == data["temp"].max()])
# filled it through the condition

monday = data[data.day == "Monday"]
mon_temp = monday.temp
mon_temp_farenheit = (mon_temp*9/5)+32

print(mon_temp_farenheit)
# now it will just give a single value




# Create a data from scratch

data_dict = {
    "students" : ["A1","A2","A3"],
    "scores" : [76,56,66]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
# will create a csv file with that name in the relative path

"""

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
cinnammon_squirrels = data[data["Primary Fur Color"] == "Cinnammon"]


## seems like the process is complete manual unlike my postgresqql experience
# starting with dictionary

data_dict = {
    "Fur Color" : ["Grey","Black","Cinnamon"],
    "Count" : [len(grey_squirrels),len(black_squirrels),len(cinnammon_squirrels)]
}

result = pd.DataFrame(data_dict)

result.to_csv("squirrel_count.csv")