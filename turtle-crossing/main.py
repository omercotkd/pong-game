import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

"""screen setup"""
screen = Screen()
screen.setup(600, 600)
player = Player()
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, "w")
screen.onkeypress(player.move, "Up")

car = CarManager()
scoreboard = Scoreboard()

game_loops = 6
number_of_cars = 25

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    """checks if there r enough cars on screen and make them come in spaces """
    if game_loops == 6 and len(car.cars) <= number_of_cars:
        car.crate_car()
        game_loops = 0

    car.move_car()

    """move the player to the next level, more cars and increased speed"""
    if player.check_finish_line():
        scoreboard.level += 1
        scoreboard.update_score()
        car.update_speed()
        number_of_cars += 5

    """check for crashes, and if one happens ask the player if he want to start a new game"""
    for i in car.cars:
        if player.distance(i) < 22:
            scoreboard.game_over()
            new_game = screen.textinput("new game", "want to play again? [yes / no]")
            if new_game.lower() == "yes" or new_game.lower() == "y":
                screen.listen()
                player.goto(STARTING_POSITION)
                scoreboard.level = 1
                scoreboard.update_score()
                car.update_speed("new game")
                number_of_cars = 25
            else:
                game_is_on = False

    game_loops += 1
