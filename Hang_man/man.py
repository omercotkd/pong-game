from turtle import Turtle


class HangMan(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(10)
        self.goto(-50, -100)
        self.pendown()
        self.goto(120, -100)
        self.goto(-100, -100)
        self.goto(-50, -100)
        self.goto(-50, 250)
        self.goto(100, 250)
        self.goto(100, 200)
        self.pensize(5)
        self.speed(0)

    def update_the_hang_man(self, strikes):
        """update the hang man based on the number of strikes"""
        if strikes == 0:
            pass
        elif strikes == 1:
            self.penup()
            self.goto(100, 120)
            self.pendown()
        elif strikes == 2:
            self.circle(40)
        elif strikes == 3:
            self.goto(100, 100)
        elif strikes == 4:
            self.goto(50, 70)
            self.goto(100, 100)
        elif strikes == 5:
            self.goto(150, 70)
            self.goto(100, 100)
        elif strikes == 6:
            self.goto(100, 0)
        elif strikes == 7:
            self.goto(40, -60)
            self.goto(100, 0)
        elif strikes == 8:
            self.goto(160, -60)
            self.goto(100, 0)
