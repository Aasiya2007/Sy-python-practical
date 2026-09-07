print("-" * 45)
print("        BUS SEAT RESERVATION LAYOUT SYSTEM")
print("-" * 45)

total_rows = int(input("Enter number of rows in the bus: "))
seats_per_row = int(input("Enter number of seats per row: "))

bus_layout = []

for r in range(total_rows):
    row = []

    for c in range(seats_per_row):
        row.append("O")

    bus_layout.append(row)

print(f"\nBus layout created: {total_rows} rows x {seats_per_row} seats per row.")
print("All seats are currently Open (O).\n")


while True:

    print("-" * 45)
    print("1. Display Bus Layout")
    print("2. Reserve a Seat")
    print("3. Cancel a Reservation")
    print("4. Check a Specific Seat Status")
    print("5. Count Available / Reserved Seats")
    print("6. Exit")
    print("-" * 45)

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":

        print("\nCurrent Bus Layout:")
        print("Rows from top to bottom - Row 1 to Row", total_rows, "\n")

        for r in range(len(bus_layout)):
            print(f"Row {r + 1}: ", end="")

            for c in range(len(bus_layout[r])):
                print(bus_layout[r][c], end=" ")

            print()


    elif choice == "2":

        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:

            if bus_layout[row_num][col_num] == "X":
                print("This seat is already reserved.\n")

            else:

                bus_layout[row_num][col_num] = "X"
                print(f"Seat at Row {row_num + 1}, Seat {col_num + 1} ""reserved successfully.\n")
        else:

            print("Invalid row or seat number.\n")

    elif choice == "3":

        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:

            if bus_layout[row_num][col_num] == "O":
                print("This seat is already open (not reserved).\n")

            else:

                bus_layout[row_num][col_num] = "O"
                print(f"Reservation cancelled for Row {row_num + 1}, "f"Seat {col_num + 1}.\n")

        else:

            print("Invalid row or seat number.\n")

    elif choice == "4":
        row_num = int(input(f"Enter row number (1 to {total_rows}): ")) - 1
        col_num = int(input(f"Enter seat number (1 to {seats_per_row}): ")) - 1

        if 0 <= row_num < total_rows and 0 <= col_num < seats_per_row:
            status = bus_layout[row_num][col_num]

            if status == "O":
                print( f"Seat {row_num + 1}, Seat {col_num + 1} ""is OPEN.\n")

            else:
                print(f"Seat {row_num + 1}, Seat {col_num + 1} ""is RESERVED.\n")

        else:
            print("Invalid row or seat number.\n")


    elif choice == "5":
        open_count = 0
        reserved_count = 0

        for r in range(len(bus_layout)):

            for c in range(len(bus_layout[r])):

                if bus_layout[r][c] == "O":
                    open_count += 1

                elif bus_layout[r][c] == "X":
                    reserved_count += 1

        print("\nSeat Count:")
        print("Available (Open) Seats:", open_count)
        print("Reserved Seats:", reserved_count)
        print("Total Seats:", open_count + reserved_count)
        print()

    elif choice == "6":
        print("\nThank you for using Bus Seat Reservation System!")
        print("Program exited successfully.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.\n")