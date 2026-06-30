# Program to Create Mini Employee Management System

employees = {}

while True:
    print("\n===== Mini Employee Management System =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))

        employees[emp_id] = {
            "NAME": name,
            "SALARY": salary
        }

        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for emp_id, details in employees.items():
                print("Employee ID :", emp_id)
                print("Name        :", details["NAME"])
                print("Salary      :", details["SALARY"])
                print("---------------------------")

    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in employees:
            print("Employee Found!")
            print("Name   :", employees[emp_id]["NAME"])
            print("Salary :", employees[emp_id]["SALARY"])
        else:
            print("Employee not found.")

    elif choice == 4:
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            new_salary = float(input("Enter New Salary: "))
            employees[emp_id]["SALARY"] = new_salary
            print("Salary updated successfully!")
        else:
            print("Employee not found.")

    elif choice == 5:
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")