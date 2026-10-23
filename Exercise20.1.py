flashcards = {
    "Abundant": "Existing in large quantities",
    "Brave": "Ready to face danger",
    "Curious": "Eager to know or learn",
    "Diligent": "Hardworking and careful",
    "Enormous": "Very large"
}
def run_flashcards():
    score = 0
    total = len(flashcards)
    for word, definition in flashcards.items():
        print("\nWord:", word)
        user_answer = input("Enter the definition: ").strip()
        if user_answer.lower() == definition.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("Correct definition:", definition)
    accuracy = (score / total) * 100
    print("\n--- FINAL RESULT ---")
    print("Correct answers:", score, "/", total)
    print(f"Accuracy: {accuracy:.1f}%")
run_flashcards()
