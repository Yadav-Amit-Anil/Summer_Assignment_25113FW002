#program to create bank account system
accounts = {}
while True:
    print ("==== Bank Account System ====")
    print("1. Create account")
    print("2. Display account")
    print("3. Deposit money")
    print("4. withdraw money")
    print("5. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        acc_no = input("Enter account number:")
        name = input("Enter account holder name:")
        balance = int(input("Enter Initial balance:"))
        accounts[acc_no]={
            "NAME":name,
            "BALANCE":balance
        }
        print("Account created successfully!")

    elif choice == 2:
        acc_no = input("Enter account number:")
        if acc_no in accounts:
            print("Account number=",acc_no)
            print("Name=",accounts[acc_no]["NAME"])
            print("Balance=",accounts[acc_no]["BALANCE"])
        else:
            print("Account not found.")

    elif choice == 3:
        acc_no = input("Enter the account number:")
        if acc_no in accounts:
            amount = int(input("Enter deposit amount:"))
            accounts[acc_no]["BALANCE"]+=amount
            print ("Amount deposited successfully!")
            print ("Updated balance=",accounts[acc_no]["BALANCE"])
        else:
            print("Account not found.")

    elif choice == 4:
        acc_no = input("Enter the account number:")
        if acc_no in accounts:
            amount = int(input("Enter withdrawl amount:"))
            if amount<=accounts[acc_no]["BALANCE"]:
                accounts[acc_no]["BALANCE"]-=amount
                print ("please collect your cash")
                print ("Remaining balance=",accounts[acc_no]["BALANCE"])
            else:
                print("Insufficient Balance. ")
        else:
            print("Account not found.")
    elif choice == 5:
        print("Thank you for using the bank account system.")
        break
    else:
        print("invalid choice! Please try again.")