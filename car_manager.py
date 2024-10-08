from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_Y = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
SHAPE = "square"
HEADING = 180
CAR_FREQUENCY = 6


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.cars_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        if random.randint(0, CAR_FREQUENCY) == 1:
            car = Turtle()
            car.shape(SHAPE)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.setheading(HEADING)
            car.color(random.choice(COLORS))
            car.goto(290, random.choice(RANDOM_Y))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.cars_speed)

    def detect_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT
