def kilometers_to_mile(kilometers:float)->float:
    return 0.621371 * kilometers
def main()->None:
    kilometers=float(input("Enter Kilometers: "))
    miles = kilometers_to_mile(kilometers)
    print(f"{kilometers} km is {miles} in miles ")
if __name__=="__main__":
    main()