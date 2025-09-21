def fibonacci(term: int) -> list[int]:
    """
    Generate the Fibonacci sequence up to the given term.
    
    Args:
        term (int): Number of terms in the sequence to generate (must be > 0).
    
    Returns:
        list[int]: A list containing the Fibonacci sequence up to 'term'.
    """
    if term == 0:
        return []
    elif term == 1:
        return [0]
    elif term == 2:
        return [0, 1]
    else:
        result = [0, 1]
        for i in range(2, term):
            result.append(result[i - 2] + result[i - 1])
        return result


def main() -> None:
    """
    Ask the user for a term and display the Fibonacci sequence up to that term.
    Handles invalid input gracefully using try/except.
    """
    try:
        term = int(input("Print Fibonacci till the ... term: "))
        if term <= 0:
            raise ValueError("Term must be a positive integer greater than zero.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    result = fibonacci(term)
    print(result)


if __name__ == "__main__":
    main()
