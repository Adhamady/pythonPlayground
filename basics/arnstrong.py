def is_armstrong(number: int) -> bool:
    """
    Check if the given number is an Armstrong number.

    An Armstrong number is equal to the sum of its digits
    each raised to the power of the number of digits.

    Args:
        number (int): Positive integer to check.

    Returns:
        bool: True if the number is Armstrong, else False.
    """
    digits = [int(d) for d in str(number)]
    digits_count = len(digits)
    powered_sum = sum(d**digits_count for d in digits)
    return powered_sum == number


def main() -> None:
    """Ask user for a number and check if it's Armstrong."""
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            raise ValueError("Number must be positive.")
        result = "Armstrong" if is_armstrong(number) else "not Armstrong"
        print(f"The number {number} is {result}.")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
