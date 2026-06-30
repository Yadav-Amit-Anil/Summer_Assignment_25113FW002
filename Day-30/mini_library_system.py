# Program to Create Mini Library System

library = {}

while True:
    print("\n===== Mini Library System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        library[book_id] = {
            "TITLE": title,
            "AUTHOR": author,
            "STATUS": "Available"
        }

        print("Book added successfully!")

    elif choice == 2:
        if len(library) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books")
            for book_id, details in library.items():
                print("Book ID :", book_id)
                print("Title   :", details["TITLE"])
                print("Author  :", details["AUTHOR"])
                print("Status  :", details["STATUS"])
                print("--------------------------")

    elif choice == 3:
        book_id = input("Enter Book ID to search: ")

        if book_id in library:
            print("Book Found!")
            print("Title  :", library[book_id]["TITLE"])
            print("Author :", library[book_id]["AUTHOR"])
            print("Status :", library[book_id]["STATUS"])
        else:
            print("Book not found.")

    elif choice == 4:
        book_id = input("Enter Book ID to issue: ")

        if book_id in library:
            if library[book_id]["STATUS"] == "Available":
                library[book_id]["STATUS"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")