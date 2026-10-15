import random

def roll_dice():
    return random.randint(1, 6)

def main():
    n = int(input("Enter the number of dice to roll: "))

    if n > 0:
        total = 0

        for i in range(n):
            result = roll_dice()
            print("Dice", i + 1, ":", result)
            total += result

        print("Total score:", total)
    else:
        print("Number of dice must be greater than 0.")

if __name__ == "__main__":
    main()