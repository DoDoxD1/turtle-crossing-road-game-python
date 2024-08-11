from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90
SHAPE = "turtle"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.setheading(HEADING)
        self.goto_start()

    def move(self):
        self.forward(10)

    def is_at_finish_line(self):
        return self.ycor() > 280

    def goto_start(self):
        self.goto(STARTING_POSITION)
