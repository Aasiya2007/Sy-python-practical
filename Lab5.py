print(" ========= Monthly Expenses Tracker* =========")
n = int(input("Enter the number of expenses:"))

expenses = []
total = 0 

for i in range(n):
    amount = float (input(f"Enter Expenses {i + 1}:"))
    expenses.append(amount)
    total += amount

while True:
    print("\n------- Expenses Tracker Menu -----")
    print("1. show All Expenses")
    print("2. show Total Expenses")
    print("3. Add New Expenses")
    print("4. Exit")

    choice = int(input(" Enter your choice:"))

    if choice == 1:
        print("\n Expenses List : ")
        for i in range(len(expenses)):
            print(f" Expenses {i+1}: {expenses[i]}")

    elif choice == 2:
        print(" Total Monthly Expenses =",total)

    elif choice == 3:
        new_expenses = float(input("Enter new expenses:"))
        expenses.append( new_expenses )
        total += new_expenses
        print("Expenses Added Successfully.")

    elif choice ==4:
        print(" Thank You for using monthly Expenses Tracker!")

        break

