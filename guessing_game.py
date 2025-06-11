
import tkinter as tk
import random

# Random number to guess
number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            result.set("Too low! Try again.")
        elif guess > number:
            result.set("Too high! Try again.")
        else:
            result.set("🎉 Correct! You guessed it!")
    except ValueError:
        result.set("Please enter a valid number.")

def restart_game():
    global number
    number = random.randint(1, 100)
    result.set("Game restarted! Guess a number from 1 to 100.")
    entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Number Guessing Game")

result = tk.StringVar()
result.set("Guess a number from 1 to 100.")

tk.Label(root, text="Enter your guess:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check_guess).pack(pady=5)
tk.Label(root, textvariable=result).pack(pady=5)
tk.Button(root, text="Restart", command=restart_game).pack()

root.mainloop()
