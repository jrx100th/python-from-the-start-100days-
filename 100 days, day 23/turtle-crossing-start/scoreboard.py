FONT = ("Courier", 16, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-270,260)
        self.write(arg=f"Level : {self.score}",move=False,font=FONT)
    
    def update_score(self):
        self.clear()
        self.write(arg=f"Level : {self.score}",move=False,font=FONT)

    def game_over(self):
        self.clear()
        self.goto(-100,0)
        self.write(arg=f"Game Over\n Your score is {self.score}",move=False,font=("Monospace", 26, "bold"))