print("-" * 50)
print("    PHONEBOOK / WORD FREQUENCY COUNTER APP")
print("-" * 50)

phonebook = {}
word_freq = {}

while True:
    print("\n----- MAIN MENU -----")
    print("1. Add Contact (Phonebook)")
    print("2. Search Contact (Phonebook)")
    print("3. Display All Contacts (Phonebook)")
    print("4. Delete Contact (Phonebook)")
    print("5. Analyze Word Frequency (Enter a paragraph)")
    print("6. Display Word Frequency")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    # ---------------- ADD CONTACT ----------------
    if choice == "1":
        name = input("Enter name: ").strip()
        contact = input("Enter contact number: ").strip()

        phonebook[name] = contact

        print(f"Contact '{name}' added successfully.\n")

    # ---------------- SEARCH CONTACT ----------------
    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in phonebook:
            print(f"Name: {name}")
            print(f"Contact Number: {phonebook[name]}\n")
        else:
            print(f"'{name}' not found in phonebook.\n")

    # ---------------- DISPLAY ALL CONTACTS ----------------
    elif choice == "3":
        if len(phonebook) == 0:
            print("No contacts available.\n")
        else:
            print("\n{:20} {:15}".format("Name", "Contact Number"))
            print("-" * 35)

            for name in phonebook:
                print("{:20} {:15}".format(name, phonebook[name]))

            print()

    # ---------------- DELETE CONTACT ----------------
    elif choice == "4":
        name = input("Enter name to delete: ").strip()

        if name in phonebook:
            del phonebook[name]
            print(f"Contact '{name}' deleted successfully.\n")
        else:
            print(f"'{name}' not found in phonebook.\n")

    # ---------------- WORD FREQUENCY ANALYSIS ----------------
    elif choice == "5":
        paragraph = input("Enter a paragraph to analyze: ").strip()

        paragraph = paragraph.lower()       

        # remove common punctuation marks using replace()
        for symbol in ".,!?;:\"()":
            paragraph = paragraph.replace(symbol, "")

        words = paragraph.split()           # split into list of words

        word_freq = {}                      # reset frequency dictionary

        for word in words:                  # traverse the word list
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1
            else:
                word_freq[word] = 1         # first occurrence

        print("Word frequency analysis complete. Use option 6 to view results.\n")

    # ---------------- DISPLAY WORD FREQUENCY ----------------
    elif choice == "6":
        if len(word_freq) == 0:
            print("No word frequency data yet. Use option 5 first.\n")
        else:
            print("\n{:20} {:10}".format("Word", "Count"))
            print("-" * 30)

            for word in word_freq:
                print("{:20} {:10}".format(word, word_freq[word]))

            most_common_word = max(word_freq, key=word_freq.get)
            print(f"\nMost frequent word: '{most_common_word}'")
            print(f"({word_freq[most_common_word]} times)\n")

    # ---------------- EXIT ----------------
    elif choice == "7":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.\n")
