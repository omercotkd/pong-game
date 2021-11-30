from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.right_score = 0
        self.left_score = 0
        self.write(f"{self.left_score}  {self.right_score}", align="center", font=("Courier", 40, "normal"))

    def update_score(self, point):
        if point == "r":
            self.right_score += 1
            self.clear()
            self.write(f"{self.left_score}  {self.right_score}", align="center", font=("Courier", 40, "normal"))
        elif point == "l":
            self.left_score += 1
            self.clear()
            self.write(f"{self.left_score}  {self.right_score}", align="center", font=("Courier", 40, "normal"))

        if self.right_score == 5:
            self.clear()
            self.write(f"Right side won!!", align="center", font=("Courier", 50, "normal"))
            return 1
        elif self.left_score == 5:
            self.clear()
            self.write(f"Left side won!!", align="center", font=("Courier", 50, "normal"))
            return 1