balance = 0
transactions = []


def deposit():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: ₹{amount:.2f}")
        print("Amount deposited successfully.")
    else:
        print("Invalid deposit amount.")


def withdrawal():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        transactions.append(f"Withdrawn: ₹{amount:.2f}")
        print("Amount withdrawn successfully.")


def check_balance():
    print(f"Current balance: ₹{balance:.2f}")


def show_transactions():
    print("\n===== TRANSACTION HISTORY =====")

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)


# Banking Menu
while True:
    print("\n===== BANKING MENU =====")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit()

    elif choice == "2":
        withdrawal()

    elif choice == "3":
        check_balance()

    elif choice == "4":
        show_transactions()

    elif choice == "5":
        print("Thank you for using the Banking System.")
        break

    else:
        print("Invalid choice. Please try again.")
