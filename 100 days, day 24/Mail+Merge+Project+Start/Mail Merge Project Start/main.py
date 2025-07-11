#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as f:
    names = [name.strip() for name in f.readlines()]

with open("./Input/Letters/starting_letter.txt") as f2:
    letter_template = f2.read()

for name in names:
    personalized_letter = letter_template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt",mode="w") as output_file:
        output_file.write(personalized_letter)

"""

# strip() will also strip the new lines


f = open("./Input/Names/invited_names.txt")
f = f.readlines()

# now f holds the names in each line and a new line


# starting letter address
letter = "./Input/Letters/starting_letter.txt"

f2 = open(letter).read()
replacable =  "[name]"    # f2[5:][:6]
# contains [name] which will be replaced


# f2 = f2.replace(replacable,"Batman")
# now f2 is successfully replaced

# output = f"./Output/ReadyToSend/{name}.txt"

for name in f:
    with open(f"./Output/ReadyToSend/{name}.txt",mode="w") as file:
        file.write(f2.replace(replacable,name))"""