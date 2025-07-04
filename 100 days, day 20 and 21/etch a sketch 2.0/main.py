##146 Snake game planning

"""
7 parts in total = 3 parts in day1 and 4 parts in day 2

day 1
Create a snake body
Move the snake
control the snake


day 2
detect collision with food
create a scoreboard
detect collision with wall
detect collision with tail

"""






## 147. Screen Setup and Creating a snake body

from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


# moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    


# 3 classes
# snake class
# food class
# scoreboard

    



screen.exitonclick()

