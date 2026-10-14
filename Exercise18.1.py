filename = "diary.txt"

thought = input("Enter your thoughts: ")

with open(filename, "a") as f:
    f.write(thought + "\n\n")

print("Diary entry saved successfully!")
