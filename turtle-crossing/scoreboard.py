from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def update_score(self):
        self.goto(-290, 260)
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", font=FONT)

