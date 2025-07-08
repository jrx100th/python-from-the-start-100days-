import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
bots = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(bots.SLEEP_TIME)
    screen.update()
    
    bots.move_all()

    # detect turtle collision with the car
    
    for bot in bots.bot_list:
        if bot.distance(player) < 23:
            
            scoreboard.game_over()
            screen.exitonclick()

    # checking for a finishing in the current level, i mean the top edge
    if player.check_cross():
        player.goto((0, -280))
        bots.speed_up()
        scoreboard.score += 1
        scoreboard.update_score()




