from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


#---------------------------------FUNCTIONALITY--------------------------------#
main_file = pd.read_csv(r"C:\Users\jenit\PycharmProjects\100 Days\100 days, day 31\flash-card-project-start\data\french_words.csv")
main_dict = main_file.to_dict(orient="records")

flip_timer = None
current_card = {}
words_to_learn = []

def gen_rand_num():
    return random.choice(main_dict)

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = gen_rand_num() # main_dict[gen_rand_num()]
    canvas1.itemconfig(card_img, image=front_image)
    language_label.config(text="French", fg="black")
    word_label.config(text=current_card["French"], fg="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas1.itemconfig(card_img, image=back_image)
    language_label.config(text="English", fg="black")
    word_label.config(text=current_card["English"], fg="black")

def tick_button_french_func():
    next_card()
    for indict in main_dict:
        if current_card["French"] == indict["French"]:
            main_dict.remove(indict)


def wrong_button_french_func():
    next_card()
    for indict in main_dict:
        if current_card["French"] == indict["French"]:
            words_to_learn.append(indict)

# ---------------------------------GUI------------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.geometry("900x700")

canvas1 = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file=r"C:\Users\jenit\PycharmProjects\100 Days\100 days, day 31\flash-card-project-start\images\card_front.png")
back_image = PhotoImage(file=r"C:\Users\jenit\PycharmProjects\100 Days\100 days, day 31\flash-card-project-start\images\card_back.png")
card_img = canvas1.create_image(400, 263, image=front_image)
canvas1.grid(row=0, column=0, columnspan=2)

language_label = Label(window, text="French", font=LANG_FONT, bg="white", fg="black")
language_label.place(x=400, y=150, anchor="center")

word_label = Label(window, text="", font=WORD_FONT, bg="white", fg="black")
word_label.place(x=400, y=263, anchor="center")

tick_image = PhotoImage(file=r"C:\Users\jenit\PycharmProjects\100 Days\100 days, day 31\flash-card-project-start\images\right.png")
tick_button = Button(window, image=tick_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=tick_button_french_func)
tick_button.grid(row=1, column=1)

wrong_image = PhotoImage(file=r"C:\Users\jenit\PycharmProjects\100 Days\100 days, day 31\flash-card-project-start\images\wrong.png")
wrong_button = Button(window, image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong_button_french_func)
wrong_button.grid(row=1, column=0)

# Start the first card display
window.after(0, next_card)

window.mainloop()


df = pd.DataFrame(words_to_learn)

df.to_csv("words_to_learn.csv")