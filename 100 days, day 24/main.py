
# """
# file = open("my_file.txt")    # open will let pythonaccess the specific python file
# contents = file.read()        # .read will read the content and will store it in a variable
# print(contents)               # now the contents will be printed out from the txt file

# file.close()                  # if not closed the resources will be taken untill the backend algo is closing it automatically

# # so sometimes it can be hard to remember to close
# with keyword comes into place

# """
# """
# with open("my_file.txt") as file:
#     # file.write("\nmy name is ,..my name is., tschka tschka slim shady")
#     contents = file.read()
#     print(contents)
# """
# # no this is the same thing as the commented out code and this will automatically close the file when we are done with it

# # mode = "r"  read only mode
# # mode = "w" write mode = will delete the existing stuff and write from fresh page in the file
# # mode = "a" a for append = add text to the existing text

# # Now writing into files
# """
# with open("my_file.txt", mode="a") as file:
#     file.write("\nmy name is ,..my name is., tschka tschka slim shady")
# """

# # in the write mode even when the specified file does not exist, it will just create from scratch

# """
# with open("new_file.txt", mode = "w") as file:
#     file.write("testing for new file")
# """
# # creates a new file in the same folder

# """with open("new_file.txt") as file:
#     contents = file.read()
#     print(type(contents))
# """

# # it is always string, even if it is string

# """
# import os
# print("Current working directory:", os.getcwd())
# """


# """
# import os

# cwd = r"C:\Users\jtx100th\PycharmProjects\100 Days\100 days, day 24"
# target = r"C:\Users\jx100th\OneDrive\Desktop\new_file.txt"

# relative_path = os.path.relpath(target, cwd)
# print(relative_path)
# """
import os
print("CWD:", os.getcwd())

with open(r"..\..\..\OneDrive\Desktop\new_file.txt") as file:
    contents = file.read()
    print(contents)
