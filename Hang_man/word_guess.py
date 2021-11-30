from random import choice
from turtle import Turtle

with open("words.txt", "r") as f:
    x = f.read()
    x = x.replace("\n", " ")
    words = list(x.split(" "))


class WordGuss(Turtle):
    def __init__(self):
        super().__init__()
        self.word = choice(words).lower()
        self.word_len = len(self.word)
        self.temp_guess = ["_" for _ in range(self.word_len)]
        self.wrong_guess = list()
        self.strikes = 0
        self.speed(0)
        self.penup()
        self.goto(-120, -220)
        self.hideturtle()
        self.write(f"{' '.join(self.temp_guess)}", font=("ariel", 40, "normal"))

    def check_guess(self, guess):
        if self.strikes < 8:
            if guess in self.word:
                for i in range(self.word_len):
                    if self.word[i] == guess:
                        self.temp_guess[i] = guess
                self.clear()
                self.write(f"{' '.join(self.temp_guess)}", font=("ariel", 40, "normal"))
                self.goto(-480, -350)
                self.write(f"wrong guess:\n{', '.join(self.wrong_guess)}", font=("ariel", 22, "normal"))
                self.goto(-120, -220)
            else:
                self.wrong_guess.append(guess)
                self.clear()
                self.write(f"{' '.join(self.temp_guess)}", font=("ariel", 40, "normal"))
                self.goto(-480, -350)
                self.write(f"wrong guess:\n{', '.join(self.wrong_guess)}", font=("ariel", 22, "normal"))
                self.goto(-120, -220)
                return True

    def lost_message(self):
        self.clear()
        self.write(f"{' '.join(self.temp_guess)}", font=("ariel", 40, "normal"))
        self.goto(-480, -350)
        self.write(f"wrong guess:\n{', '.join(self.wrong_guess)}", font=("ariel", 22, "normal"))
        self.goto(-100, -280)
        self.write(f"you lost, the word was {self.word}", align="center", font=("ariel", 30, "normal"))

    def win_message(self):
        self.clear()
        self.write(f"{' '.join(self.temp_guess)}", font=("ariel", 40, "normal"))
        self.goto(-480, -350)
        self.write(f"wrong guess:\n{', '.join(self.wrong_guess)}", font=("ariel", 22, "normal"))
        self.goto(-100, -280)
        self.write(f"you won!!", align="center", font=("ariel", 40, "normal"))

    def key_press_a(self):
        if self.check_guess("a"):
            self.strikes += 1

    def key_press_b(self):
        if self.check_guess("b"):
            self.strikes += 1

    def key_press_c(self):
        if self.check_guess("c"):
            self.strikes += 1

    def key_press_d(self):
        if self.check_guess("d"):
            self.strikes += 1

    def key_press_e(self):
        if self.check_guess("e"):
            self.strikes += 1

    def key_press_f(self):
        if self.check_guess("f"):
            self.strikes += 1

    def key_press_g(self):
        if self.check_guess("g"):
            self.strikes += 1

    def key_press_h(self):
        if self.check_guess("h"):
            self.strikes += 1

    def key_press_i(self):
        if self.check_guess("i"):
            self.strikes += 1

    def key_press_j(self):
        if self.check_guess("j"):
            self.strikes += 1

    def key_press_k(self):
        if self.check_guess("k"):
            self.strikes += 1

    def key_press_l(self):
        if self.check_guess("l"):
            self.strikes += 1

    def key_press_m(self):
        if self.check_guess("m"):
            self.strikes += 1

    def key_press_n(self):
        if self.check_guess("n"):
            self.strikes += 1

    def key_press_o(self):
        if self.check_guess("o"):
            self.strikes += 1

    def key_press_p(self):
        if self.check_guess("p"):
            self.strikes += 1

    def key_press_q(self):
        if self.check_guess("q"):
            self.strikes += 1

    def key_press_r(self):
        if self.check_guess("r"):
            self.strikes += 1

    def key_press_s(self):
        if self.check_guess("s"):
            self.strikes += 1

    def key_press_t(self):
        if self.check_guess("t"):
            self.strikes += 1

    def key_press_u(self):
        if self.check_guess("u"):
            self.strikes += 1

    def key_press_v(self):
        if self.check_guess("v"):
            self.strikes += 1

    def key_press_w(self):
        if self.check_guess("w"):
            self.strikes += 1

    def key_press_x(self):
        if self.check_guess("x"):
            self.strikes += 1

    def key_press_y(self):
        if self.check_guess("y"):
            self.strikes += 1

    def key_press_z(self):
        if self.check_guess("z"):
            self.strikes += 1


