import math

def check_prime(number:int)->bool:
    """Returns True if number is prime, else returns False"""
    if number < 2:
        return False
    for i in range (2,math.isqrt(number)+1):
        if(number%i==0):
            return False
    return True


def main()->None:
    """Ask the user to input a number and calls check_prime"""
    number = int(input("Enter number: "))
    prime = "prime" if check_prime(number) else "not prime"

    print(f"The number {number} is {prime}")

if __name__=="__main__":
    main()
