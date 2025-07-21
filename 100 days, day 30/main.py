# FileNotFound

# try:
#     file = open("af.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["sddfef"])
# except FileNotFoundError:
#     # print("There was an error")
#     file = open("af.txt","w")
#     file.write("loreum ipsum")
# # except KeyError:
# #     print("That key does not exist.")
# # catching key error
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")

# else :  # when no error are found
#     content = file.read()
#     print(content)
# finally:
#     # raise TypeError
#     raise KeyError("Fuck You")


# these 4 will be in the flow




height = float(input("Height : "))
weight = int(input("Weight : "))

if height > 3:
    raise ValueError("Human height should not be over 3 meteres.")

bmi = weight/(height*height)
print(bmi)