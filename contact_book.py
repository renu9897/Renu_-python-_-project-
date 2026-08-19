# contact_book.py
contacts = {}

while True:
    print("\n1.Add Contact 2.View Contacts 3.Search 4.Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact added!")
    elif choice == "2":
        print("All Contacts:", contacts)
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice")