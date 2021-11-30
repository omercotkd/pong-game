import turtle

MOVE_DIS = 20


class Snake:
    def __init__(self):
        self.snake = list()
        self.create_snake()
        self.snake[0].color("blue")

    # crates the 3 starting parts of the snake body
    def create_snake(self):
        for i in range(3):
            new_snake_part = turtle.Turtle(shape='square')
            new_snake_part.penup()
            new_snake_part.color("white")
            new_snake_part.goto(x=(i * -20), y=0)
            self.snake.append(new_snake_part)

    def grow(self):
        new_snake_part = turtle.Turtle(shape='square')
        new_snake_part.penup()
        new_snake_part.color("white")
        new_snake_part.goto(self.snake[-1].position())
        self.snake.append(new_snake_part)

    def move(self):
        """move the snake 'MOVE_DIS' units"""
        for i in range((len(self.snake) - 1), 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DIS)

    def up(self):
        """turn the face of the snake to face north, will pass if the head is south"""
        if not self.snake[0].heading() == 270:
            self.snake[0].setheading(90)
        else:
            pass

    def down(self):
        """turn the face of the snake to face south, will pass if the head is north"""
        if not self.snake[0].heading() == 90:
            self.snake[0].setheading(270)
        else:
            pass

    def left(self):
        """turn the face of the snake to face west, will pass if the head is east"""
        if not self.snake[0].heading() == 0:
            self.snake[0].setheading(180)
        else:
            pass

    def right(self):
        """turn the face of the snake to face east, will pass if the head is west"""
        if not self.snake[0].heading() == 180:
            self.snake[0].setheading(0)
        else:
            pass






