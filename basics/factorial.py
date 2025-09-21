def calculate_factorial(number: int) -> int:
    """Calculate factorial of a non-negative integer."""
    result = 1
    for i in range(number, 0, -1):
        result *= i
    return result


def main() -> None:
    """Take user input and display its factorial."""
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Enter a valid integer")
        return

    if number < 0:
        print("Factorial is not defined for negative numbers")
        return

    result = calculate_factorial(number)
    print(f"Factorial of {number} = {result}")


if __name__ == "__main__":
    main()
