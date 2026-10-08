phonebook = {}

while True:
    print("\n1. Add Contact")
    print("2. Display Directory")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")

        if name in phonebook:
            print("Contact already exists!")
        else:
            number = input("Enter phone number: ")
            phonebook[name] = number
            print("Contact added successfully.")

    elif choice == "2":
        print("\nPhone Directory:")
        for name, number in phonebook.items():
            print(name, ":", number)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
