from turtle import Turtle
import random

random_cord = list(range(-280, 280, 20))


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.new_food()

    def new_food(self):
        self.goto(x=random.choice(random_cord), y=random.choice(random_cord))