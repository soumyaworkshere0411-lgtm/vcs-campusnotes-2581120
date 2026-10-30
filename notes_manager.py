
notes = []

def add_note():
    note = input("Enter your note: ").strip()
    if not note:
        print("Note cannot be empty!")
        return
    notes.append(note)
    print("Note added successfully!")

def view_notes():
    if not notes:
        print("No notes available.")
    else:
        for index, note in enumerate(notes, start=1):
            print(f"Note {index}: {note}")

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

if __name__ == "__main__":
    main()
