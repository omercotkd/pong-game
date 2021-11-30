from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5)
        self.color("white")
        self.setheading(90)

    def side(self, right_or_left):
        if right_or_left.lower() == "right" or right_or_left.lower() == "r":
            self.goto(370, 0)
        elif right_or_left.lower() == "left" or right_or_left.lower() == "l":
            self.goto(-370, 0)

    def move_up(self):
        if self.ycor() < 225:
            self.forward(30)

    def move_down(self):
        if self.ycor() > -225:
            self.backward(30)