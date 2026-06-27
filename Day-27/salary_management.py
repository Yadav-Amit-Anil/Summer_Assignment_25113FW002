#program to create salary management system
employee = {}
while True:
    print("===== employee salary management system =====")
    print("1. Add emloyee.")
    print("2. Display All employee.")
    print("3. Search employee.")
    print("4. Exit.")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        emp_id = input("Enter employee ID:")
        name = input("Enter name:")
        basic = int(input("Enter basic salary:"))
        hra = int(input("Enter HRA:"))
        da = int(input("Enter DA:"))
        salary = basic + hra + da
        employee[emp_id] = {
            "NAME":name,
            "BASIC":basic,
            "HRA":hra,
            "DA":da,
            "SALARY":salary
        }
        print("employee salary record added successfully!")
    
    elif choice == 2:
        if len(employee) == 0:
            print("NO employee record:")
        else:
            print("employee Record:")
            for emp_id , details in employee.items():
                print("Employee ID=",emp_id)
                print("Name=",details["NAME"])
                print("basic",details["BASIC"])
                print("hra",details["HRA"])
                print("da",details["DA"])
                print("Salary",details["SALARY"])
                print("-------------------------------")

    elif choice == 3:
        emp_id = input("Enter the Employee ID you want to search:")
        if emp_id in employee :
            print("employee Found!")
            print("Name:",employee[emp_id]["NAME"])
            print("basic:",employee[emp_id]["BASIC"])
            print("hra:",employee[emp_id]["HRA"])
            print("da:",employee[emp_id]["DA"])
            print("salary:",employee[emp_id]["SALARY"])
        else:
            print("Student record not found.")
    
    elif choice == 4:
        print("Thank you! for exicuting the program.")
        break
    else:
        print("invalid choice! try again")