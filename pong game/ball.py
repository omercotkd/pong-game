from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def start_moving(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, right_paddle, left_paddle):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_move *= -1

        if self.xcor() >= 341 and self.distance(right_paddle) <= 50 or self.xcor() <= -341 and self.distance(left_paddle) <= 50:
            self.x_move *= -1
            return 1

    def check_boundary(self):
        if self.xcor() > 380:
            self.goto(0, 0)
            self.x_move *= -1
            return "l"

        elif self.xcor() < -380:
            self.goto(0, 0)
            self.x_move *= -1
            return "r"
