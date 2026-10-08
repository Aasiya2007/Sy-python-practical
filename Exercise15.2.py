import math

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def main():
    print("Geometric Area Calculator")
    print("1. Circle")
    print("2. Rectangle")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        radius = float(input("Enter the radius: "))
        if radius < 0:
            print("Radius cannot be negative.")
        else:
            print(f"Area of the circle: {circle_area(radius):.2f}")

    elif choice == "2":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        if length < 0 or width < 0:
            print("Length and width cannot be negative.")
        else:
            print(f"Area of the rectangle: {rectangle_area(length, width):.2f}")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
