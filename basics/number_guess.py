import random

def generate_random(max_range: int) -> int:
    """Generate a random number between 0 and max_range (inclusive)."""
    return random.randint(0, max_range)

def check_guess(random_number: int, user_guess: int) -> bool:
    """Check if the user's guess matches the generated number."""
    return user_guess == random_number

def give_hint(random_number: int, user_guess: int) -> str:
    """
    Provide a hint based on the user's guess.
    
    Returns:
        str: "Too low!" or "Too high!"
    """
    if user_guess < random_number:
        return "⬆Too low! Try a bigger number."
    else:
        return "⬇Too high! Try a smaller number."

def main() -> None:
    """
    Run the number guessing game.
    Handles invalid input gracefully using try/except.
    Provides hints and counts attempts.
    """
    print("---------- Welcome to the number guessing game ----------")
    
    # Loop until valid upper bound is entered
    while True:
        try:
            max_range = int(input("Enter the upper bound of the game: "))
            if max_range <= 0:
                raise ValueError("Upper bound must be a positive integer greater than zero.")
            break
        except ValueError:
            print("Invalid input! Please enter a whole number greater than zero.")
    
    random_number = generate_random(max_range)
    attempts = 0
    
    # Guessing loop
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < 0:
                raise ValueError("Guess must be zero or a positive integer.")
            attempts += 1
        except ValueError:
            print("Invalid input! Please enter a whole number (0 or greater).")
            continue
        
        if check_guess(random_number, user_guess):
            print(f"Correct! The number was {random_number}. You guessed it in {attempts} tries.")
            break
        else:
            print(give_hint(random_number, user_guess))

if __name__ == "__main__":
    main()
