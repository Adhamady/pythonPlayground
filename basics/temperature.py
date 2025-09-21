def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * (9/5)) + 32

def main() -> None:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    print(f"{celsius}°C equals {fahrenheit}°F")

if __name__ == "__main__":
    main()
