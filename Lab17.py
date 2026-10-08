import random
import math


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

def roll_dice():
    dice = math.floor(random.random() * 6) + 1
    return dice


# Main program
def main():
    while True:
        print("\n===== RANDOM PASSWORD GENERATOR / DICE SIMULATOR =====")
        print("1. Random Password Generator")
        print("2. Dice Simulator")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length = int(input("Enter password length: "))

            if length > 0:
                password = generate_password(length)
                print("Generated Password:", password)
            else:
                print("Password length must be greater than 0.")

        elif choice == "2":
            while True:
                input("Press Enter to roll the dice...")

                result = roll_dice()
                print("You rolled:", result)

                again = input("Roll again? (y/n): ").lower()

                if again != "y":
                    break

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
