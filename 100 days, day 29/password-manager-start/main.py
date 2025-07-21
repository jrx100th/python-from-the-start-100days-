from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 12)
    nr_symbols = random.randint(4, 6)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0,END)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

    # pyperclip needs to be pip installed through whatever you want first, for some reason the import doesnt work.
    # pyperclip.paste() will paste stuff from clipboard
    
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_current_data():
    current_data = f"Website : {web_entry.get()}\nUsername/Email : {usn_entry.get()}\nPassword : {pass_entry.get()}\n========================\n========================\n"
    if (len(web_entry.get()) == 0) or (len(pass_entry.get()) == 0) or (len(usn_entry.get()) == 0):
        messagebox.showinfo(title="Warning",message="Please make sure you didnt leave any fields empty")
    else:    # goes back to continue 
        # messagebox.showinfo(title="Verification", message="These will be saved\n" + current_data)
        verification = messagebox.askokcancel(title="Verification",message=f"Check these details entered \nWebsite   : {web_entry.get()}\nEmail        : {usn_entry.get()}\nPassword : {pass_entry.get()}\nSave Them?")

        if verification:  # if user press OK
            with open("data.txt", mode="a") as file:
                file.write(current_data)
            print("Data Saved")
            web_entry.delete(0,END)          # deleting from 0 to end of the password entry
            usn_entry.delete(0,END)
            pass_entry.delete(0,END)
            web_entry.focus()
            # wow now it looks like an infinite loop
            # change the data.txt to you_know_where_and_what_im_talking_about.txt
        else:             # if user press cancel and then it will automatically be closed
            pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img) # in the center of the 
canvas.grid(row=1, column=2)


website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

web_entry = Entry(width=53)
web_entry.focus()
web_entry.grid(row=2, column=2, columnspan=2,sticky="w")

user_name = Label(text="Email/Username:")
user_name.grid(row=3, column=1)

usn_entry = Entry(width=53)
usn_entry.grid(row=3, column=2, columnspan=2,sticky="w")

pwd = Label(text="Password:")
pwd.grid(row=4, column=1)

pass_entry = Entry(width=32)
pass_entry.grid(column=2,row=4, columnspan=1,sticky="w")

gpb = Button(text="Generate Password",width=16,bg="#093FB4",fg="#FFFCFB", command=generate_password)
gpb.grid(column=3, row=4,sticky="w")

adb = Button(text="Add",width=45,bg="#06923E",fg="#D3ECCD", command=save_current_data)
adb.grid(row=5,column=2, columnspan=2)









window.mainloop()