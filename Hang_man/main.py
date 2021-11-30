from turtle import Screen
from man import HangMan
from word_guess import WordGuss
from time import sleep

screen = Screen()
screen.title("Hang man game")
screen.setup(1000, 800)

hang_man = HangMan()
word_to_guess = WordGuss()
game_is_on = True
screen.tracer()
screen.listen()


def keys():
    screen.onkey(word_to_guess.key_press_a, "a")
    screen.onkey(word_to_guess.key_press_b, "b")
    screen.onkey(word_to_guess.key_press_c, "c")
    screen.onkey(word_to_guess.key_press_d, "d")
    screen.onkey(word_to_guess.key_press_e, "e")
    screen.onkey(word_to_guess.key_press_f, "f")
    screen.onkey(word_to_guess.key_press_g, "g")
    screen.onkey(word_to_guess.key_press_h, "h")
    screen.onkey(word_to_guess.key_press_i, "i")
    screen.onkey(word_to_guess.key_press_j, "j")
    screen.onkey(word_to_guess.key_press_k, "k")
    screen.onkey(word_to_guess.key_press_l, "l")
    screen.onkey(word_to_guess.key_press_m, "m")
    screen.onkey(word_to_guess.key_press_n, "n")
    screen.onkey(word_to_guess.key_press_o, "o")
    screen.onkey(word_to_guess.key_press_p, "p")
    screen.onkey(word_to_guess.key_press_q, "q")
    screen.onkey(word_to_guess.key_press_r, "r")
    screen.onkey(word_to_guess.key_press_s, "s")
    screen.onkey(word_to_guess.key_press_t, "t")
    screen.onkey(word_to_guess.key_press_u, "u")
    screen.onkey(word_to_guess.key_press_v, "v")
    screen.onkey(word_to_guess.key_press_w, "w")
    screen.onkey(word_to_guess.key_press_x, "x")
    screen.onkey(word_to_guess.key_press_y, "y")
    screen.onkey(word_to_guess.key_press_z, "z")
    return keys


keys()
while game_is_on:
    sleep(0.01)
    screen.update()
    hang_man.update_the_hang_man(word_to_guess.strikes)
    if word_to_guess.strikes >= 8:
        word_to_guess.lost_message()
        hang_man.update_the_hang_man(word_to_guess.strikes)
        game_is_on = False

    if word_to_guess.word == "".join(word_to_guess.temp_guess):
        word_to_guess.win_message()
        game_is_on = False


screen.exitonclick()
