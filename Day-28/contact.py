# Program to Create Contact Management System

contacts = {}

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Display All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        phone = input("Enter Phone Number: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")

        contacts[phone] = {
            "NAME": name,
            "EMAIL": email
        }

        print("Contact added successfully!")

    elif choice == 2:
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for phone, details in contacts.items():
                print("Phone Number:", phone)
                print("Name:", details["NAME"])
                print("Email:", details["EMAIL"])
                print("------------------------")

    elif choice == 3:
        phone = input("Enter Phone Number to search: ")

        if phone in contacts:
            print("Contact Found!")
            print("Name:", contacts[phone]["NAME"])
            print("Email:", contacts[phone]["EMAIL"])
        else:
            print("Contact not found.")

    elif choice == 4:
        print("Thank you for using the Contact Management System.")
        break

    else:
        print("Invalid choice! Please try again.")