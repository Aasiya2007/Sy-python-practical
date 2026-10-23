questions = [
    "Organizations should protect confidential information.",
    "Employees may share passwords with anyone.",
    "Compliance policies should be followed by employees.",
    "Suspected regulatory violations should be reported.",
    "Organizations should keep required compliance records."
]
answers = ["True", "False", "True", "True", "True"]
def run_screening():
    score = 0
    total = len(questions)
    user_answers = []
    print("=== COMPLIANCE SCREENING PORTAL ===")
    for i in range(total):
        print(f"\nQ{i + 1}. {questions[i]}")
        while True:
            choice = input("Enter True or False: ").strip().lower()
            if choice in ["true", "false"]:
                user_answers.append(choice.capitalize())
                break
            else:
                print("Invalid input. Enter True or False.")
        if user_answers[i].lower() == answers[i].lower():
            score += 1
    percentage = (score / total) * 100
    print("\n--- SCREENING RESULT ---")
    print("Correct answers:", score, "/", total)
    print(f"Accuracy: {percentage:.1f}%")
    if percentage >= 80:
        print("Status: PASS")
    else:
        print("Status: FAIL")
    print("\nYour responses:")
    for i in range(total):
        print(f"Q{i + 1}: Your answer: {user_answers[i]} | "
              f"Correct answer: {answers[i]}")
run_screening()
