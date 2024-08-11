from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="Left", font=FONT)
