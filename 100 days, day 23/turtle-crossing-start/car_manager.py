COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from random import randint, choice


class CarManager:
    def __init__(self):
        self.bot_list = []
        self.multiple_bots()
        self.SLEEP_TIME = 0.1

        
    def multiple_bots(self):
        for _ in range(700):
            self.make_car()
    
    def make_car(self):
        bot = Turtle("square")
        bot.penup()
        bot.goto(randint(220,10000),randint(-240,240))
        bot.color(choice(COLORS))
        bot.shapesize(stretch_len=2,stretch_wid=1)
        bot.setheading(180)
        self.bot_list.append(bot)
    
    def move_all(self):
        for bot in self.bot_list:
            bot.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):     # using an object here as a parameter, will be called in the main.py and makes sense
        self.SLEEP_TIME *= 0.909