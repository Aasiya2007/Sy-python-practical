# Digital Wallet Simulator

balance = 0.0
transactions = []


def add_funds():
    global balance

    amount = float(input("Enter amount to add: ₹"))

    if amount > 0:
        balance += amount
        transactions.append("Added funds: ₹" + str(amount))
        print("Funds added successfully!")
        print("Current balance: ₹", balance)
    else:
        print("Amount must be greater than 0.")


def pay_bill():
    global balance

    bill_name = input("Enter bill name: ")
    amount = float(input("Enter bill amount: ₹"))

    if amount <= 0:
        print("Amount must be greater than 0.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        transactions.append("Paid " + bill_name + ": ₹" + str(amount))
        print("Bill paid successfully!")
        print("Remaining balance: ₹", balance)


def view_balance():
    print("Current wallet balance: ₹", balance)


def transaction_history():
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\n===== TRANSACTION HISTORY =====")

        for i in range(len(transactions)):
            print(i + 1, ".", transactions[i])


def main():
    while True:
        print("\n===== DIGITAL WALLET =====")
        print("1. Add Funds")
        print("2. Pay Bill")
        print("3. View Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_funds()

        elif choice == "2":
            pay_bill()

        elif choice == "3":
            view_balance()

        elif choice == "4":
            transaction_history()

        elif choice == "5":
            print("Thank you for using the Digital Wallet!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
