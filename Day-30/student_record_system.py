# Program to Create Student Record System Using Arrays and Strings

roll = []
name = []
course = []

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll.append(input("Enter Roll Number: "))
        name.append(input("Enter Student Name: "))
        course.append(input("Enter Course: "))
        print("Student record added successfully!")

    elif choice == 2:
        if len(roll) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("-------------------------------")
            for i in range(len(roll)):
                print("Roll Number :", roll[i])
                print("Name        :", name[i])
                print("Course      :", course[i])
                print("-------------------------------")

    elif choice == 3:
        r = input("Enter Roll Number to search: ")

        if r in roll:
            index = roll.index(r)
            print("\nStudent Found!")
            print("Roll Number :", roll[index])
            print("Name        :", name[index])
            print("Course      :", course[index])
        else:
            print("Student record not found.")

    elif choice == 4:
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")