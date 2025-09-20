def is_positive(num: int) -> bool:
    return num > 0

def is_negative(num: int) -> bool:
    return num < 0

def main() -> None:
    num = int(input("Enter number: "))
    
    if is_positive(num):
        result = "positive"
    elif is_negative(num):
        result = "negative"
    else:
        result = "zero"
    print(f"{num} is {result}")

if __name__ == "__main__":
    main()
