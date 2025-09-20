def calculate_area(base:float,height:float)-> float:
    return 0.5 * base* height
def main()->None:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: ")) 
    area=calculate_area(base,height)
    print(f"Area of triangle = {area}")

if __name__=="__main__":
    main()

