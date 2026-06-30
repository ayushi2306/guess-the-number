import tkinter as tk
import random

# ---------------- Game Variables ---------------- #
random_number = random.randint(0, 1000)
attempts = 0

# ---------------- Functions ---------------- #
def check_guess():
    global attempts

    guess = entry.get()

    if guess == "":
        result_label.config(text="Please enter a number!", fg="orange")
        return

    if not guess.isdigit():
        result_label.config(text="Please enter a valid number!", fg="red")
        return

    guess = int(guess)
    attempts += 1

    if guess < random_number:
        result_label.config(text="Higher!", fg="blue")

    elif guess > random_number:
        result_label.config(text="Lower!", fg="blue")

    else:
        result_label.config(
            text=f"🎉 Correct! You guessed it in {attempts} attempts.",
            fg="green"
        )

        guess_button.config(state="disabled")
        entry.config(state="disabled")


def restart_game():
    global random_number, attempts

    random_number = random.randint(0, 1000)
    attempts = 0

    entry.config(state="normal")
    guess_button.config(state="normal")

    entry.delete(0, tk.END)

    result_label.config(text="New Game Started!", fg="black")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Guess the Number")
root.geometry("450x300")

title = tk.Label(
    root,
    text="Guess the Number",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

instruction = tk.Label(
    root,
    text="Guess a number between 0 and 1000",
    font=("Arial", 12)
)
instruction.pack()

entry = tk.Entry(
    root,
    width=20,
    font=("Arial", 14)
)
entry.pack(pady=15)

guess_button = tk.Button(
    root,
    text="Guess",
    command=check_guess,
    width=15
)
guess_button.pack()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14)
)
result_label.pack(pady=20)

restart_button = tk.Button(
    root,
    text="Restart Game",
    command=restart_game,
    width=15
)
restart_button.pack()

root.mainloop()