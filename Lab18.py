filename = "students.txt"

while True:
     
    print("\n--- Student Record File System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice(1-5): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        with open(filename, "a") as f:
            f.write(roll + "," + name + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open(filename, "r") as f:
                records = f.readlines()

                if not records:
                    print("No records found.")
                else:
                    for record in records:
                        print(record.strip())

        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        found = False

        try:
            with open(filename, "r") as f:
                for record in f:
                    data = record.strip().split(",")

                    if data[0] == roll:
                        print("Student Found!")
                        print("Roll Number:", data[0])
                        print("Name:", data[1])
                        print("Marks:", data[2])
                        found = True
                        break

            if not found:
                print("Student not found.")

        except FileNotFoundError:
            print("No records found.")

    elif choice == "4":
        roll = input("Enter Roll Number to delete: ")
        found = False

        try:
            with open(filename, "r") as f:
                records = f.readlines()

            with open(filename, "w") as f:
                for record in records:
                    data = record.strip().split(",")

                    if data[0] == roll:
                        found = True
                    else:
                        f.write(record)

            if found:
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No records found.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")
