from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.cars = list()
        self.speed = STARTING_MOVE_DISTANCE

    def crate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.goto(x=300, y=random.randint(-250, 250))
        new_car.speed(0)
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1, 2)
        self.cars.append(new_car)

    def move_car(self):
        for i in self.cars:
            if i.xcor() > -320:
                i.goto(i.xcor() - self.speed, i.ycor())
            elif i.xcor() <= -320:
                i.color(random.choice(COLORS))
                i.goto(x=300, y=random.randint(-250, 250))

    def update_speed(self, next_level_or_reset="next level"):
        if next_level_or_reset == "next level":
            self.speed += MOVE_INCREMENT
        else:
            self.speed = STARTING_MOVE_DISTANCE












