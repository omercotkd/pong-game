import tkinter as tk
import pandas as pd
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
WORD_FONT = ("Ariel", 60, "bold")
TITLE_FONT = ("Ariel", 40, "italic")
timer = None
flip_time = 3
card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/english words.csv")


to_learn = data.to_dict(orient="records")

# -------------------------------------------- FLIP MECHANISM ---------------------------------------------------#


def countdown():
    global timer, card
    card = choice(to_learn)
    x_button["state"] = "disabled"
    vi_button["state"] = "disabled"
    screen.after(800, func=active_buttons)
    timer = screen.after(flip_time * 1000, func=flip_card)


def active_buttons():
    x_button["state"] = "normal"
    vi_button["state"] = "normal"


def flip_card():
    screen.after_cancel(timer)
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(title_text, text=data.columns[1], fill="white")
    canvas.itemconfig(word_text, text=card[data.columns[1]], fill="white")


# ------------------------------------------ BUTTONS FUNCTION SETUP --------------------------------------------------#


def button_press():
    countdown()
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(title_text, text=data.columns[0], fill="black")
    canvas.itemconfig(word_text, text=card[data.columns[0]], fill="black")


def x_press():
    button_press()


def vi_press():
    button_press()
    to_learn.remove(card)
    x = pd.DataFrame(to_learn)
    x.to_csv("data/words_to_learn.csv", index=False)


# ----------------------------------------------- UI SETUP ---------------------------------------------------------- #
screen = tk.Tk()
screen.title("Learn French")
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# crate Photo images
x_image = tk.PhotoImage(file="images/wrong.png")
vi_image = tk.PhotoImage(file="images/right.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_front_image = tk.PhotoImage(file="images/card_front.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

x_button = tk.Button(image=x_image, highlightthickness=0, command=x_press)
x_button.grid(row=1, column=0)
vi_button = tk.Button(image=vi_image, highlightthickness=0, command=vi_press)
vi_button.grid(row=1, column=1)

button_press()


screen.mainloop()

