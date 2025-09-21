def check_year(year: int) -> bool:
    """Return True if the given year is a leap year, False otherwise."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def main() -> None:
    """Ask the user for a year and print whether it is a leap year."""
    try:
        year = int(input("Enter a year to check: "))
        result = "a leap year" if check_year(year) else "not a leap year"
        print(f"The year {year} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()