from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from midle_line import MiddleBoarder
import time


"""screen setup"""
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle()
right_paddle.side("r")

left_paddle = Paddle()
left_paddle.side("l")

ball = Ball()

scoreboard = ScoreBoard()

line = MiddleBoarder()


game_is_on = True
ball_speed = 0.1

"""checks key press"""
screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

while game_is_on:
    time.sleep(ball_speed)
    ball.start_moving()
    if ball.bounce(right_paddle, left_paddle):
        ball_speed *= 0.8

    point = ball.check_boundary()

    if point:
        if scoreboard.update_score(point):
            game_is_on = False
        ball_speed = 0.1
    screen.update()

screen.exitonclick()