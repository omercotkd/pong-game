from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score} ", False, align="center", font=("arial", 18, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", False, align="center", font=("arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER! ", False, align="center", font=("arial", 24, "normal"))
