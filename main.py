## 139. More turtle graphics, event listeners, state and multiple instances

# etch a sketch
# turtle racing game





## 140 Higher order functions and event listeners
## etch a sketch project

"""
Turtle event listeners
screen event listeners



from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    # tim.forward(10)

def move_backward():
    tim.backward(10)
    # tim.forward(10)

def counter_clock():
    tim.left(36)
    # tim.forward(10)

def clock():
    tim.right(36)
    # tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward) # no need of paranthesis, because the parenthesis will trigger the function then and there
                                            # but we want to wait untill the key is clicked
# this is an example of recursive functions something like that
# i mean onkey is a function
# when we use a function in another function parameters, no need of paranthesis

screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clock)
screen.onkey(key="d",fun=clock)
screen.onkey(key="c",fun=clear)


screen.exitonclick()


"""







## 142. Object State and instances

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

start_y = -150
counter = {}
turtle_list = ["a","b","c","d","e","f"]
colors = ["red","blue","green","violet","indigo","cyan"]
for i in range(len(turtle_list)):
    turtle_list[i] = Turtle(shape="turtle")
    start_y+=50
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y=start_y)
    # turtle_list[i].pendown()
    turtle_list[i].color(colors[i])
    counter[turtle_list[i]] = 0
paces = [0,5,10]
def start_race():
    while True:
        for i in range(len(turtle_list)):
            x = random.choice(paces)
            turtle_list[i].forward(x)
            counter[turtle_list[i]] += x
            if counter[turtle_list[i]] > 450:
                return set(turtle_list[i].color())
            
user_bet = screen.textinput(title="Make your bet", prompt="color you are betting on :")
print(f"Bet on a color from {["red","blue","green","violet","indigo","cyan"]} :", user_bet)


if user_bet in ["red","blue","green","violet","indigo","cyan"]:
    frdf = (start_race())
    print(frdf," won the race")
    if user_bet in frdf:
        print("you won the bet")
    else:
        print(f"you lost {frdf} turtle won the race")
    screen.exitonclick()
if user_bet not in ["red","blue","green","violet","indigo","cyan"]:
    print("that is not a valid input, rerun the program")
    screen.bye()


# screen.exitonclick()