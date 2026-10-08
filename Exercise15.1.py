# Temperature Conversion Library

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


# Main Program Loop
while True:
    print("\n===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"Temperature in Fahrenheit: {result:.2f} °F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"Temperature in Celsius: {result:.2f} °C")

    elif choice == "3":
        print("Thank you for using the Temperature Converter.")
        break

    else:
        print("Invalid choice. Please try again.")
