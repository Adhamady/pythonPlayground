def main()->None:
    # Take user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Perform arithmetic operations
    results = {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "product": num1 * num2,
        "quotient": num1 / num2 if num2 != 0 else "undefined (division by zero)"
    }

    # Print results
    print(f"The sum of {num1} and {num2} is {results['sum']}")
    print(f"The difference between {num1} and {num2} is {results['difference']}")
    print(f"The product of {num1} and {num2} is {results['product']}")
    print(f"{num1} divided by {num2} is {results['quotient']}")


if __name__ == "__main__":
    main()
