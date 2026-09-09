print("********MOVIE THEATER BOOKING SIMULATOR********")

seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

while True:
    print("\nCurrent Seating Arrangement:")
    for row in seats:
        print(" ".join(row))

    row = int(input("\nEnter row number (1-3), or 0 to exit: "))

    if row == 0:
        print("Thank you!")
        break

    col = int(input("Enter column number (1-3): "))

    if 1 <= row <= 3 and 1 <= col <= 3:
        if seats[row - 1][col - 1] == "O":
            seats[row - 1][col - 1] = "X"
            print("Seat reserved successfully.")
        else:
            print("Sorry, that seat is already reserved.")
    else:
        print("Invalid row or column.")