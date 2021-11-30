import turtle
import time
from snake import Snake
from food import Food
from score import ScoreBoard

"""screen setup"""
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""crate the snake form the Snake class i crated"""
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
game_is_on = True


def keys():
    """def the keys, its in a fun so the code will look batter"""
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="d", fun=snake.right)
    return keys


"""call the keys"""
keys()


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    """check if the snake eat and if so he grows"""
    if snake.snake[0].distance(food) <= 10:
        food.new_food()
        score_board.update_score()
        snake.grow()

    """check if the snake hit himself"""
    for i in range(5, len(snake.snake)):
        if snake.snake[0].xcor() == snake.snake[i].xcor() and snake.snake[0].ycor() == snake.snake[i].ycor():
            game_is_on = False
            score_board.game_over()

    """check if the snake hit the border"""
    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() < -280 or snake.snake[0].ycor() > 280:
        game_is_on = False
        score_board.game_over()


screen.exitonclick()
