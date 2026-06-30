# Program to Create Menu-Driven String Operations System

while True:
    print("\n===== Menu-Driven String Operations =====")
    print("1. Find Length")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Reverse String")
    print("5. Check Palindrome")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Thank you!")
        break

    string = input("Enter a string: ")

    if choice == 1:
        print("Length of string =", len(string))

    elif choice == 2:
        print("Uppercase String =", string.upper())

    elif choice == 3:
        print("Lowercase String =", string.lower())

    elif choice == 4:
        print("Reversed String =", string[::-1])

    elif choice == 5:
        if string == string[::-1]:
            print("The string is a Palindrome.")
        else:
            print("The string is not a Palindrome.")

    else:
        print("Invalid choice! Please try again.")