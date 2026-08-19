# atm_system.py
balance = 10000
pin = "1234"

print("--- WELCOME TO ATM ---")
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == pin:
    while True:
        print("\n1. Balance Enquiry")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            print(f"Your Balance: Rs.{balance}")
            
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print(f"Rs.{amount} Deposited Successfully!")
            print(f"New Balance: Rs.{balance}")
            
        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print(f"Rs.{amount} Withdrawn Successfully!")
                print(f"Remaining Balance: Rs.{balance}")
            else:
                print("Insufficient Balance!")
                
        elif choice == "4":
            new_pin = input("Enter new PIN: ")
            pin = new_pin
            print("PIN Changed Successfully!")
            
        elif choice == "5":
            print("Thank you! Please collect your card.")
            break
        else:
            print("Invalid choice!")
else:
    print("Wrong PIN! Card Blocked.")