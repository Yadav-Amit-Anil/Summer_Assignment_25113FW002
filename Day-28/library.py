#program to create library management system
library ={}
while True:
    print("===== library management system =====")
    print("1. Add book.")
    print("2. Display All book.")
    print("3. Search book.")
    print("4. Exit.")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        Book_id = input("Enter Book ID:")
        title= input("Enter book title:")
        author = input("Enter author name:")
        library[Book_id] = {
            "TITLE":title,
            "AUTHOR":author
        }
        print("book added successfully!")
    
    elif choice == 2:
        if len(library) == 0:
            print("NO book record:")
        else:
            print("Book Record:")
            for book_id , details in library.items():
                print("Book ID=",book_id)
                print("Title=",details["TITLE"])
                print("Author=",details["AUTHOR"])
                print("-------------------------------")

    elif choice == 3:
        book_id = input("Enter the Book ID you want to search:")
        if book_id in library :
            print("book Found!")
            print("Title:",library[book_id]["TITLE"])
            print("Author:",library[book_id]["AUTHOR"])
        else:
            print("Book not found.")
    
    elif choice == 4:
        print("Thank you! for exicuting the program.")
        break
    else:
        print("invalid choice! try again")