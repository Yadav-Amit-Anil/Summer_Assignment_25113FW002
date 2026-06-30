# Student Management System

roll = []
name = []
course = []

# Function to add a student
def add_student():
    r = input("Enter Roll Number: ")
    n = input("Enter Name: ")
    c = input("Enter Course: ")

    roll.append(r)
    name.append(n)
    course.append(c)

    print("Student record added successfully!")

# Function to display students
def display_students():
    if len(roll) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records")
        print("-----------------------------")
        for i in range(len(roll)):
            print("Roll No :", roll[i])
            print("Name    :", name[i])
            print("Course  :", course[i])
            print("-----------------------------")

# Function to search a student
def search_student():
    r = input("Enter Roll Number to search: ")

    if r in roll:
        index = roll.index(r)
        print("\nStudent Found!")
        print("Roll No :", roll[index])
        print("Name    :", name[index])
        print("Course  :", course[index])
    else:
        print("Student not found.")

# Function to delete a student
def delete_student():
    r = input("Enter Roll Number to delete: ")

    if r in roll:
        index = roll.index(r)
        roll.pop(index)
        name.pop(index)
        course.pop(index)
        print("Student record deleted successfully!")
    else:
        print("Student not found.")

# Main Program
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")