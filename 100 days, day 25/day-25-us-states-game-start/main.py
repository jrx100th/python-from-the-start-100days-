# turtle only works with .gif image format

import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()


df = pd.read_csv("50_states.csv")
game_is_on = True
correct = 0
total = 50

answer_set = set()

while correct != total:
    answer_state = screen.textinput(title = f"{correct}/{total} States Correct", prompt="What's another state")
    if answer_state is None:
        break
    answer_state = answer_state.title()

    # checking for a correct answer
    if answer_state in (df["state"]).to_list() and answer_state not in answer_set:
        answer_set.add(answer_state)
        correct+=1
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        row = df[df["state"] == answer_state]
        x = int(row["x"].values[0])
        y = int(row["y"].values[0])
        state.goto(x,y)
        state.write(answer_state,align="center",font=("Courier",8,"normal"))

    if answer_state == "Exit":
        break

states_list = df.state.to_list()

new_dict = {
    "States" : []
}

for i in range(len(states_list)):
    if states_list[i] not in answer_set:
        new_dict["States"].append(states_list[i])

print(new_dict)

pd.DataFrame(new_dict).to_csv("states_to_learn.csv")

# "states_to_learn.csv"