import random

def computer_turn() -> str:
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def results(computer_choice: str, user_choice: str) -> str:
    if computer_choice == user_choice:
        return "Tie"
    elif (computer_choice == "rock" and user_choice == "scissors") or\
        (computer_choice == "paper" and user_choice == "rock") or \
        (computer_choice == "scissors" and user_choice == "paper"):
        return "Computer won"
    else:
        return "User won"

def main() -> None:
    print("-------- Rock, Paper, Scissors Game --------")
    computer_choice = computer_turn()
    user_choice = input("Your turn (rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer_choice}")
    print(results(computer_choice, user_choice))

if __name__ == "__main__":
    main()
