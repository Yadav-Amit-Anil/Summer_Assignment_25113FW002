# Program to Create Inventory Management System

inventory = {}

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        inventory[product_id] = {
            "NAME": product_name,
            "QUANTITY": quantity,
            "PRICE": price
        }

        print("Product added successfully!")

    elif choice == 2:
        if len(inventory) == 0:
            print("No products available.")
        else:
            print("\nInventory Details:")
            for product_id, details in inventory.items():
                print("Product ID:", product_id)
                print("Product Name:", details["NAME"])
                print("Quantity:", details["QUANTITY"])
                print("Price: ₹", details["PRICE"])
                print("--------------------------")

    elif choice == 3:
        product_id = input("Enter Product ID to search: ")

        if product_id in inventory:
            print("Product Found!")
            print("Product Name:", inventory[product_id]["NAME"])
            print("Quantity:", inventory[product_id]["QUANTITY"])
            print("Price: ₹", inventory[product_id]["PRICE"])
        else:
            print("Product not found.")

    elif choice == 4:
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please try again.")