# expense_tracker.py
expenses = []

while True:
    print("\n1.Add Expense 2.View Total 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Item: ")
        amount = float(input("Amount: "))
        expenses.append(amount)
        print(f"{item} - Rs.{amount} added")
    elif choice == "2":
        print(f"Total Spent: Rs.{sum(expenses)}")
    elif choice == "3":
        break