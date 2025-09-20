def main() -> None:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Before swapping:\nfirst num = {num1}, second num = {num2}")

    # Swap using tuple unpacking
    num1, num2 = num2, num1

    print(f"After swapping:\nfirst num = {num1}, second num = {num2}")


if __name__ == "__main__":
    main()
