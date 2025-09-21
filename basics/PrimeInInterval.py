import math

def check_prime(lower: int, higher: int) -> list[int]:
    """Return a list of prime numbers between lower and higher (inclusive)."""
    prime_numbers = []
    for number in range(lower, higher + 1):
        if number < 2:  # Skip 0 and 1
            continue
        is_prime = True
        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers


def main() -> None:
    """Ask user for range and display prime numbers within it."""
    try:
        lower = int(input("Enter lower bound: "))
    except ValueError:
        print("Please enter a proper number in lower bound")
        return
    try:
        higher = int(input("Enter upper bound: "))
    except ValueError:
        print("Please enter a proper number in higher bound")
        return

    if(lower == higher):
        print("Lower and higher can't be equal")
    elif(lower>higher):
        print("Lower can't be greater than higher")
    else:
        primes = check_prime(lower, higher)
        if primes:
            print(f"Prime numbers between {lower} and {higher}: {primes}")
        else:
            print(f"No prime numbers found between {lower} and {higher}.")



if __name__ == "__main__":
    main()
