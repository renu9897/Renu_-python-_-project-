# renu_notes.py
print("Welcome to Renu's Notes App")
notes = []
while True:
    choice = input("1.Add 2.View 3.Exit: ")
    if choice == "1":
        note = input("Enter note: ")
        notes.append(note)
        print("Note added!")
    elif choice == "2":
        print("Your notes:", notes)
    elif choice == "3":
        break
    else:
        print("Wrong choice")