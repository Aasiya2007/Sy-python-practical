library = {
    "9780135258059": {
        "title": "Python Programming",
        "author": "John Smith",
        "year": 2024,
        "available": True
    },

    "9780262033848": {
        "title": "Data Structures",
        "author": "Robert Brown",
        "year": 2023,
        "available": True
    }
}

running = True

while running:
    print("\n===== LIBRARY BOOK RECORD SYSTEM =====")
    print("1. Display all Books")
    print("2. Add new Book")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Issue/Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Display all books
    if choice == "1":
        if not library:
            print("No books available in the library.")
        else:
            print("\n===== ALL BOOKS IN LIBRARY =====")

            for isbn, book in library.items():
                print("ISBN:", isbn)
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Year:", book["year"])

                if book["available"]:
                    print("Status: Available")
                else:
                    print("Status: Issued")

                print("-----------------------------")

    # 2. Add new book
    elif choice == "2":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            print("Book with this ISBN already exists.")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            year = int(input("Enter Publication Year: "))

            library[isbn] = {
                "title": title,
                "author": author,
                "year": year,
                "available": True
            }

            print("Book added successfully.")

    # 3. Update book
    elif choice == "3":
        isbn = input("Enter ISBN to update: ")

        if isbn in library:
            library[isbn]["title"] = input("Enter new title: ")
            library[isbn]["author"] = input("Enter new author: ")
            library[isbn]["year"] = int(
                input("Enter new publication year: ")
            )

            print("Book updated successfully.")
        else:
            print("ISBN not found.")

    # 4. Delete book
    elif choice == "4":
        isbn = input("Enter ISBN to delete: ")

        if isbn in library:
            del library[isbn]
            print("Book deleted successfully.")
        else:
            print("ISBN not found.")

    # 5. Issue / Return book
    elif choice == "5":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            if library[isbn]["available"]:
                library[isbn]["available"] = False
                print("Book issued successfully.")
            else:
                library[isbn]["available"] = True
                print("Book returned successfully.")
        else:
            print("ISBN not found.")

    # 6. Exit
    elif choice == "6":
        print("Thank you for using the Library Book Record System.")
        running = False

    else:
        print("Invalid choice. Please enter 1-6.")
