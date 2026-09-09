print("=========STUDENT SCORE FILTER=========")

grades = [75, 82, 68, 91, 88]

print("Original Grades:", grades)

index = int(input("Enter the index position to update (0-4): "))

new_grade = int(input("Enter the new grade: "))

grades[index] = new_grade

print("\nCorrected Grades:", grades)

print("****************************************")