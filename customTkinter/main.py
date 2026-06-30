import random
import customtkinter as ctk

# ---------------- Window ---------------- #
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Guess the Number")
app.geometry("500x400")
app.resizable(False, False)

# ---------------- Game Variables ---------------- #
random_number = random.randint(0, 1000)
attempts = 0

# ---------------- Functions ---------------- #
def check_guess():
    global attempts

    guess = guess_entry.get()

    # Check if input is empty
    if guess == "":
        result_label.configure(text="Please enter a number!", text_color="orange")
        return

    # Check if input is numeric
    if not guess.isdigit():
        result_label.configure(text="Please enter a valid number!", text_color="red")
        return

    guess = int(guess)
    attempts += 1

    if guess < random_number:
        result_label.configure(
            text="Higher!",
            text_color="yellow"
        )

    elif guess > random_number:
        result_label.configure(
            text="Lower!",
            text_color="yellow"
        )

    else:
        result_label.configure(
            text=f"🎉 Correct! You guessed it in {attempts} attempts.",
            text_color="green"
        )

        guess_button.configure(state="disabled")
        guess_entry.configure(state="disabled")


def restart_game():
    global random_number, attempts

    random_number = random.randint(0, 1000)
    attempts = 0

    guess_entry.configure(state="normal")
    guess_button.configure(state="normal")

    guess_entry.delete(0, "end")

    result_label.configure(
        text="New game started!",
        text_color="white"
    )

# ---------------- Widgets ---------------- #

title = ctk.CTkLabel(
    app,
    text="Guess the Number",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

instruction = ctk.CTkLabel(
    app,
    text="Guess a number between 0 and 1000",
    font=("Arial", 15)
)
instruction.pack()

guess_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Enter your guess"
)
guess_entry.pack(pady=20)

guess_button = ctk.CTkButton(
    app,
    text="Guess",
    command=check_guess
)
guess_button.pack()

result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 16)
)
result_label.pack(pady=20)

restart_button = ctk.CTkButton(
    app,
    text="Restart Game",
    command=restart_game,
    fg_color="green",
    hover_color="darkgreen"
)
restart_button.pack(pady=10)

app.mainloop()