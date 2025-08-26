import random
import tkinter as tk
from contextlib import nullcontext

choices= ["rock", "paper", "scissors"]

# Create the main window

window= tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("350x250")
window.configure(bg="#e6e6e6")

#Function to handle button clicks
def play_game(player_choice):
    #Determine the winner
    # if player_choice==computer_choice:
    #     result= "It's a tie!"
    # elif (player_choice=="rock" and computer_choice=="scissors") or \
    #      (player_choice=="paper" and computer_choice=="rock") or \
    #      (player_choice=="scissors" and computer_choice=="paper"):
    #     result="You win!"
    # else:
    #     result="You lose!"
    if player_choice == "rock":
        computer_choice = "paper"
    elif player_choice == "paper":
        computer_choice = "scissors"
    else :
        computer_choice = "rock"
    result="You lose!!"
    result_label.config(text=result)
    # update the computer's choice label
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
#Create the GUI WIDGETS
#Label to display the result
result_label= tk.Label(window, text="Make your choice!", font=("Helvetica", 14), bg="#e6e6e6")
result_label.pack(pady=10)

#Label to display the computer's choice
computer_choice_label= tk.Label(window, text="", font=("Helvetica", 12), bg="#e6e6e6")
computer_choice_label.pack()

#Frame to hold the buttons
button_frame = tk.Frame(window, bg="#e6e6e6")
button_frame.pack(pady=20)

#Rock button
rock_button= tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"), font=("Helvetica", 12), bg="#f08080", fg="white", width=8)
rock_button.pack(side="left", padx=5)

# Paper button
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"), font=("Helvetica", 12), bg="#80b3ff", fg="white", width=8)
paper_button.pack(side="left", padx=5)

# Scissors button
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"), font=("Helvetica", 12), bg="#90ee90", fg="white", width=8)
scissors_button.pack(side="left", padx=5)

# Start the main event loop
window.mainloop()

