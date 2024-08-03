import random

choices = ["rock", "paper", "scissors"]

while (True):
    player = input("Choose rock, paper, or scissors (or 'quit' to end): ").lower()
    
    if (player == 'quit'):
        break
    
    if (player not in choices):
        print("Invalid choice. Please try again.")
        continue
    
    computer = random.choice(choices)
    
    print(f"You chose {player}, computer chose {computer}.")
    
    if (player == computer):
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

print("Thanks for playing!")