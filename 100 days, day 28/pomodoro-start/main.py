from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DARK_GREEN = "#06923E"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)

    # timer to 00:00
    canvas.itemconfig(timer_text, text="00:00")

    #title_label "Timer"
    timer.config(text="Timer")
    timer.config(fg=GREEN)

    # reset the checkmarks
    checkmarks.config(text="")

    # set reps to 0
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # if its the 1st/3rd/5th/7th rep:
    # count_down(work_sec)
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps%2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60

    # formatting for under 10 mins
    if count_min < 10:
        count_min = "0"+str(count_min)

    # formatting for under 10 secs
    if count_sec < 10:
        count_sec = "0"+str(count_sec)       # f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            checkmarks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# putting an image into window
window.config(padx=100,pady=50, bg=YELLOW)      # sets bg to yellow



timer = Label(text="Timer",bg=YELLOW, font=(FONT_NAME,40,"bold"),fg=GREEN)
timer.grid(row=1, column=2)


# creating a canvas(widget)
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0) # setting height, width and background color to yellow
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100,112, image=tomato_img)    # to be in center it should be having the coordinated for half of the height and the width 
timer_text = canvas.create_text(102,122, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=2, column=2)



start = Button(text="Start", command=start_timer)
start.grid(row=3,column=1)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=3, column=3)

checkmarks = Label(text="", fg=DARK_GREEN,bg=YELLOW)
checkmarks.grid(row=5, column=2)






window.mainloop()