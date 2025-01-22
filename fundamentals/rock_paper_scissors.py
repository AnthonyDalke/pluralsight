import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input(f"Choose 'rock', 'paper', or 'scissors'.\n")

print(f"Computer choice: {computer_choice}")

if computer_choice == user_choice:
    print(f"TIE")
elif user_choice == "rock" and computer_choice == "scissors":
    print(f"WIN")
elif user_choice == "paper" and computer_choice == "rock":
    print(f"WIN")
elif user_choice == "scissors" and computer_choice == "paper":
    print(f"WIN")
else:
    print(f"You lose, computer wins :)")
