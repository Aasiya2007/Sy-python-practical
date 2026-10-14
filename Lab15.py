import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def logarithm(a):
    return math.log10(a)

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 11:
        print("Thank you!")
        break

    elif choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            if b != 0:
                print("Result:", divide(a, b))
            else:
                print("Cannot divide by zero")
        elif choice == 5:
            print("Result:", power(a, b))

    elif choice == 6:
        a = float(input("Enter number: "))
        if a >= 0:
            print("Result:", square_root(a))
        else:
            print("Invalid number")

    elif choice in [7, 8, 9]:
        angle = float(input("Enter angle in degrees: "))

        if choice == 7:
            print("Result:", sine(angle))
        elif choice == 8:
            print("Result:", cosine(angle))
        elif choice == 9:
            print("Result:", tangent(angle))

    elif choice == 10:
        a = float(input("Enter positive number: "))
        if a > 0:
            print("Result:", logarithm(a))
        else:
            print("Invalid number")
    else:
        print("Invalid choice")
