#program to create student record management system
students = {}
while True:
    print("===== student rcord management system =====")
    print("1. Add student.")
    print("2. Display All students.")
    print("3. Search student.")
    print("4. Exit.")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        roll = input("Enter Roll Number:")
        name = input("Enter name:")
        marks = int(input("Enter marks:"))
        students[roll] = {
            "NAME":name,
            "MARKS":marks
        }
        print("student record added successfully!")
    
    elif choice == 2:
        if len(students) == 0:
            print("NO students record:")
        else:
            print("Student Record:")
            for roll , details in students.items():
                print("Roll no=",roll)
                print("Name=",details["NAME"])
                print("Marks",details["MARKS"])
                print("-------------------------------")

    elif choice == 3:
        roll = input("Enter the roll number you want to search:")
        if roll in students :
            print("Student Found!")
            print("Name:",students[roll]["NAME"])
            print("Marks:",students[roll]["MARKS"])
        else:
            print("Student record not found.")
    
    elif choice == 4:
        print("Thank you! for exicuting the program.")
        break
    else:
        print("invalid choice! try again")