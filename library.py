# library.py
books = ["Python", "Java", "C++"]

while True:
    print("\n1.View Books 2.Borrow 3.Return 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print("Books:", books)
    elif choice == "2":
        book = input("Book name: ")
        if book in books:
            books.remove(book)
            print("Book Borrowed!")
    elif choice == "3":
        book = input("Book name: ")
        books.append(book)
        print("Book Returned!")
    elif choice == "4":
        break