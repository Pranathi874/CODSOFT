import tkinter as tk
from tkinter import messagebox
import random


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}")
    
 
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    score_label.config(text=f"Your Score: {user_score} | Computer's Score: {computer_score}")


def play_again():
    play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if play_again:
        reset_game()

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text=f"Your Score: {user_score} | Computer's Score: {computer_score}")
    result_label.config(text="Choose rock, paper, or scissors!")


root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x600")


instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 16), bg="lightblue")
instructions_label.pack(pady=20)


score_label = tk.Label(root, text="Your Score: 0 | Computer's Score: 0", font=("Arial", 14), bg="lightblue")
score_label.pack(pady=20)


result_label = tk.Label(root, text="Choose rock, paper, or scissors!", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)


rock_button = tk.Button(root, text="Rock", width=20, height=2, font=("Arial", 14), command=lambda: play_game("rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", width=20, height=2, font=("Arial", 14), command=lambda: play_game("paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", width=20, height=2, font=("Arial", 14), command=lambda: play_game("scissors"))
scissors_button.pack(pady=10)


reset_button = tk.Button(root, text="Reset Game", width=20, height=2, font=("Arial", 14), command=reset_game)
reset_button.pack(pady=20)


play_again_button = tk.Button(root, text="Play Again", width=20, height=2, font=("Arial", 14), command=play_again)
play_again_button.pack(pady=20)


user_score = 0
computer_score = 0


root.mainloop()
