with open("notes.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("Welcome to programming\n")
    f.write("File handling is easy\n")

print("File created successfully!")

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        count = 0

        print("\nFile Contents:")

        for line in f:
            print(line, end="")
            count += 1

        print("\nTotal number of lines:", count)

except FileNotFoundError:
    print("File not found!")
