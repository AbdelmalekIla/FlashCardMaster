from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')
finally:
    pass


def fr_word():
    global current_card, timer
    window.after_cancel(timer)
    canvas.itemconfig(images, image=front_img)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_title, text='French', fill='black')
    timer = window.after(3000, func=second_card)


def fr_that_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    fr_word()


def second_card():
    global current_card
    canvas.itemconfig(images, image=back_img)
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_title, text='English', fill='white')


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=second_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
images = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
false = PhotoImage(file='images/wrong.png')
true = PhotoImage(file='images/right.png')
unknown_button = Button(image=false, highlightthickness=0, command=fr_word)
unknown_button.grid(column=0, row=1)
vrai_button = Button(image=true, highlightthickness=0, command=fr_that_know)
vrai_button.grid(column=1, row=1)

fr_word()

window.mainloop()
