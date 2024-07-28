import tkinter as tk
from random import choice

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
        result_label.config(fg="#ffa500")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        result_label.config(fg="#008000")
        user_score += 1
    else:
        result = "You lose!"
        result_label.config(fg="#ff0000")
        computer_score += 1
    
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result)
    user_score_label.config(text=f"Your score: {user_score}")
    computer_score_label.config(text=f"Computer's score: {computer_score}")

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="Result: ", fg="#000000")
    user_score_label.config(text="Your score: 0")
    computer_score_label.config(text="Computer's score: 0")
    feedback_frame.pack_forget()
    prompt_user_choice()

def prompt_user_choice():
    prompt_label.config(text="Please choose Rock, Paper, or Scissors")

def submit_feedback():
    feedback = feedback_var.get()
    feedback_label.config(text=f"Thank you for your feedback! You rated us: {feedback}/5")

# Interface
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

instruction_label = tk.Label(frame, text="Rock-Paper-Scissors", font=('arial', 20, 'bold'), bg="#f0f0f0")
instruction_label.grid(row=0, column=0, columnspan=3, pady=10)

user_choice_label = tk.Label(frame, text="Your choice: ", font=('arial', 12), bg="#f0f0f0")
user_choice_label.grid(row=1, column=0, columnspan=3, pady=5)

computer_choice_label = tk.Label(frame, text="Computer's choice: ", font=('arial', 12), bg="#f0f0f0")
computer_choice_label.grid(row=2, column=0, columnspan=3, pady=5)

result_label = tk.Label(frame, text="Result: ", font=('arial', 12, 'bold'), bg="#f0f0f0")
result_label.grid(row=3, column=0, columnspan=3, pady=5)

user_score_label = tk.Label(frame, text="Your score: 0", font=('arial', 12), bg="#f0f0f0")
user_score_label.grid(row=4, column=0, padx=10, pady=10)

computer_score_label = tk.Label(frame, text="Computer's score: 0", font=('arial', 12), bg="#f0f0f0")
computer_score_label.grid(row=4, column=2, padx=10, pady=10)

rock_button = tk.Button(frame, text="Rock", font=('arial', 12), bg="#add8e6", command=lambda: play("Rock"))
rock_button.grid(row=5, column=0, padx=10, pady=10)

paper_button = tk.Button(frame, text="Paper", font=('arial', 12), bg="#add8e6", command=lambda: play("Paper"))
paper_button.grid(row=5, column=1, padx=10, pady=10)

scissors_button = tk.Button(frame, text="Scissors", font=('arial', 12), bg="#add8e6", command=lambda: play("Scissors"))
scissors_button.grid(row=5, column=2, padx=10, pady=10)

reset_button = tk.Button(frame, text="Play Again", font=('arial', 12), bg="#90ee90", command=reset)
reset_button.grid(row=6, column=0, columnspan=3, pady=20)

prompt_label = tk.Label(frame, text="", font=('arial', 12), bg="#f0f0f0")
prompt_label.grid(row=7, column=0, columnspan=3)

prompt_user_choice()

# Feedback section
feedback_frame = tk.Frame(root, bg="#f0f0f0")
feedback_frame.pack(pady=10)

feedback_label = tk.Label(feedback_frame, text="How would you rate this game? (1-5)", font=('arial', 12), bg="#f0f0f0")
feedback_label.grid(row=0, column=0, columnspan=5, pady=5)

feedback_var = tk.IntVar()
for i in range(1, 6):
    tk.Radiobutton(feedback_frame, text=str(i), variable=feedback_var, value=i, font=('arial', 12), bg="#f0f0f0").grid(row=1, column=i-1)

submit_feedback_button = tk.Button(feedback_frame, text="Submit", font=('arial', 12), bg="#90ee90", command=submit_feedback)
submit_feedback_button.grid(row=2, column=0, columnspan=5, pady=10)

feedback_label = tk.Label(feedback_frame, text="", font=('arial', 12), bg="#f0f0f0")
feedback_label.grid(row=3, column=0, columnspan=5)

root.mainloop()
