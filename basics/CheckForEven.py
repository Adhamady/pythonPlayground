def is_even(number: int) -> bool:
    return number % 2 == 0

def main()->None:
    try:
        number = int(input("Enter a number: "))
        result = "even" if is_even(number) else "odd"
        print(f"{number} is an {result} number")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
