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

from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()

food = Food()

scoreboard = Scoreboard()

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

    # detect collision with food = using distance method in turtle class
    # comparing the distanc between turtles
    if snake.head.distance(food) < 15:   # 15 for valid collision
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail




# 3 classes
# snake class
# food class
# scoreboard

    



screen.exitonclick()



