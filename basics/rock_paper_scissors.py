import random

def computer_turn(options: tuple[str, ...]) -> str:
    """Randomly pick rock, paper, or scissors for the computer."""
    return random.choice(options)

def results(computer_choice: str, user_choice: str) -> str:
    """Determine the winner of Rock, Paper, Scissors."""
    if computer_choice == user_choice:
        return "Tie"
    elif (
        (computer_choice == "rock" and user_choice == "scissors")
        or (computer_choice == "paper" and user_choice == "rock")
        or (computer_choice == "scissors" and user_choice == "paper")
    ):
        return "Computer won"
    else:
        return "User won"

def main() -> None:
    print("-------- Rock, Paper, Scissors Game --------")
    
    options: tuple[str, ...] = ("rock", "paper", "scissors")  # constant + encapsulated

    # validate user input
    while True:
        try:
            user_choice = input("Your turn: Rock, Paper or Scissors? : ").lower()
            if user_choice not in options:
                raise ValueError("Invalid choice. Please pick rock, paper, or scissors.")
            break
        except ValueError as e :
            print(e)

    computer_choice = computer_turn(options)
    print(f"Computer chose: {computer_choice}")
    print(results(computer_choice, user_choice))

if __name__ == "__main__":
    main()
