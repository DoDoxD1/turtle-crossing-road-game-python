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

# set up a score board
scoreboard = Scoreboard()

# set up the player turtle
player = Player()

# screen listen on keypress
screen.listen()
screen.onkey(key="w", fun=player.move)
screen.onkey(key="Up", fun=player.move)

# set up the cars
car_manager = CarManager()

# checking if game is still on
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_car()
    car_manager.move()
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_is_on = False
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.increase_speed()
        scoreboard.update_scoreboard()

screen.exitonclick()
