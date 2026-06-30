# Program to Create Menu-Driven Array Operations System

arr = []

while True:
    print("\n===== Menu-Driven Array Operations =====")
    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter element to insert: "))
        arr.append(num)
        print("Element inserted successfully!")

    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array Elements:", arr)

    elif choice == 3:
        num = int(input("Enter element to search: "))

        if num in arr:
            print("Element found at index", arr.index(num))
        else:
            print("Element not found.")

    elif choice == 4:
        num = int(input("Enter element to delete: "))

        if num in arr:
            arr.remove(num)
            print("Element deleted successfully!")
        else:
            print("Element not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")