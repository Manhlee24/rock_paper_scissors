import random

choices= ["rock", "paper", "scissors"]

print("Welcome to the Rock-Paper-Scissors game!")
print("You'll be playing against the computer. Let's see who wins!")

while True:
    player_choice= input("Choose(rock, paper, or scissors)? Or type 'exit' to quit game: ").lower()
    if(player_choice=="exit"):
        print("Thank for playing. See you next time!")
        break
    if player_choice not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'. ")
        continue
    if player_choice=="rock":
        computer_choice="paper"
    elif player_choice=="paper":
        computer_choice="scissors"
    elif player_choice=="scissors":
        computer_choice="rock"

    print(f"\nYour choose: {player_choice}")
    print(f"Computer's choice: {computer_choice}\n ")

    # #Determined the winner
    # if player_choice==computer_choice:
    #     print("It's a tie! You both chose the same")
    # elif (player_choice=="rock" and computer_choice=="scissors") or \
    #      (player_choice == "paper" and computer_choice == "rock") or \
    #      (player_choice == "scissors" and computer_choice == "paper"):
    #     print("You won!! Congratulation!!")
    # else:
    print("You lose!!Computer won ")




