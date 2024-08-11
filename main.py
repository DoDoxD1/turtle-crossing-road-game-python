import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing the Road")
screen.tracer(0)

# set up the player turtle
player = Player()

# screen listen on keypress
screen.listen()
screen.onkey(key="w", fun=player.move)
screen.onkey(key="Up", fun=player.move)

# set up the cars
car_manager = CarManager()

# checking if game is still on
while car_manager.game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move()
    car_manager.detect_collision(player)
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.increase_speed()

screen.exitonclick()
