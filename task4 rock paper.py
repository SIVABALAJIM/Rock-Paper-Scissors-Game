import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")

    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("\nChoose Rock, Paper, or Scissors (or type 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        # Computer's random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Display choices
        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        # Game logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display current score
        print(f"Score: You {user_score} - {computer_score} Computer")

# Start the game
rock_paper_scissors()
