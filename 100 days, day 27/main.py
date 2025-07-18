from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=input.get())

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label",font=("Arial",24,"bold"))  # my_label is a dictionary **kwargs
my_label.config(text="New Text")
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

# Button 1
button = Button(text="Button 1", command=button_clicked) # command is just the name of the function
button.grid(column=2, row=2)

# Button 2
button = Button(text="Button 2", command=button_clicked) # command is just the name of the function
button.grid(column=3, row=1)



# Entry 
input = Entry(width=10)
print(input.get())
input.grid(column=4, row=3)






window.mainloop()