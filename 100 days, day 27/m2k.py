from tkinter import *

window = Tk()
window.minsize(width=150, height=100)
window.title("Mile to Km Converter")

blank_label = Label(text="      ")
blank_label.grid(row=0,column=0)


entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
entry.focus()
entry.grid(row=1, column=2)

miles = Label(text="Miles     ")
miles.grid(row=1, column=3)

izekval = Label(text="is equal to")
izekval.grid(row=2,column=1)

result = Label(text="0")
result.grid(row=2, column=2)

km = Label(text="Km")
km.grid(row=2, column=3)

def calculate():
    res = round(float(entry.get())*1.6,2)
    result.config(text=res)

button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=2)




window.mainloop()