import math

def solve_quadratic(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:  # Two real roots
        roots = {
            "1": (-b + math.sqrt(discriminant)) / (2 * a),
            "2": (-b - math.sqrt(discriminant)) / (2 * a)
        }
    elif discriminant == 0:  # One real root
        roots = {"1": -b / (2 * a)}
    else:  # Complex roots
        roots = {
            "real": -b / (2 * a),
            "imaginary": math.sqrt(abs(discriminant)) / (2 * a)
        }
    return roots

def main() -> None:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    roots = solve_quadratic(a, b, c)
    
    if "imaginary" in roots:
        print(f"Complex roots: {roots['real']} ± {roots['imaginary']}i")
    else:
        for key, value in roots.items():
            print(f"Root {key}: {value}")

if __name__ == "__main__":
    main()
