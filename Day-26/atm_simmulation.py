#program to create ATM simulation
balance = 10000
pin = 1234
print ("==== ATM simulation ====")
entered_pin = int(input("Enter your PIN:"))
if entered_pin == pin:
    while True:
        print("1. Check balance.")
        print("2. Deposit money.")
        print("3. Withdraw money.")
        print("4. exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            print("Your total available balance:",balance)

        elif choice == 2:
            amount = int(input("Enter the amount you want to deposit:"))
            if amount > 0:
                balance += amount
                print(amount,"deposited successfully")
                print("New balance:",balance)
            else:
                print("Invalid amount")

        elif choice == 3:
            amount = int(input("Enter the amount you want to deposit:"))
            if amount > 0:
                balance -= amount
                print("Please collect your cash.")
                print("New balance:",balance)
            else:
                print("Insufficient balance.")

        elif choice == 4:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice, please try again.")
else:
    print("Incorrect PIN. Access denied.")