from turtle import Turtle


class MiddleBoarder(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, -280)
        self.pendown()
        self.pensize(3)
        self.setheading(90)
        for i in range(29):
            if i % 2 == 0:
                self.pendown()
                self.forward(20)
            else:
                self.penup()
                self.forward(20)
