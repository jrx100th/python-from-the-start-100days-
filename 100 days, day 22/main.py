"""
1. Create the screen
2. create and move a paddle
3. create another paddle
4. create the ball and make it move

5. detect collision with the wall and bounce
6. detect collision with paddle
7. detect when paddle misses
8. keep score
"""
RIGHT_CORS = (350,0)
LEFT_CORS = (-350,0)

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(RIGHT_CORS)
l_paddle = Paddle(LEFT_CORS)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=l_paddle.go_up, key="w")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # detect collision with right paddle and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        

    # detect if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        # sleep_time = 0.01

    # detect if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        # sleep_time = 0.01

        


screen.exitonclick()