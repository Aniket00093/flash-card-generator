# Flashcards Generator

flashcards = {}

while True:
    print("\n--- Flashcards Generator ---")
    print("1. Add Flashcard")
    print("2. View Flashcards")
    print("3. Practice")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        question = input("Enter question: ")
        answer = input("Enter answer: ")
        flashcards[question] = answer
        print("Flashcard added successfully!")

    elif choice == "2":
        if not flashcards:
            print("No flashcards available.")
        else:
            for i, (q, a) in enumerate(flashcards.items(), 1):
                print(f"\n{i}. Q: {q}")
                print(f"   A: {a}")

    elif choice == "3":
        if not flashcards:
            print("No flashcards available.")
        else:
            for question, answer in flashcards.items():
                print("\nQuestion:", question)
                input("Press Enter to see answer...")
                print("Answer:", answer)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")