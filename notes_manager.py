notes = []

def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note added successfully!")

def view_notes():
    if not notes:
        print("No notes available.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def main():
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()