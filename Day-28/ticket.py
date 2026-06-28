# Program to Create Ticket Booking System

tickets = {}

while True:
    print("\n===== Ticket Booking System =====")
    print("1. Book Ticket")
    print("2. Display All Bookings")
    print("3. Search Booking")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ticket_id = input("Enter Ticket ID: ")
        name = input("Enter Passenger Name: ")
        destination = input("Enter Destination: ")

        tickets[ticket_id] = {
            "NAME": name,
            "DESTINATION": destination
        }

        print("Ticket booked successfully!")

    elif choice == 2:
        if len(tickets) == 0:
            print("No bookings found.")
        else:
            print("\nBooked Tickets:")
            for ticket_id, details in tickets.items():
                print("Ticket ID:", ticket_id)
                print("Passenger Name:", details["NAME"])
                print("Destination:", details["DESTINATION"])
                print("------------------------")

    elif choice == 3:
        ticket_id = input("Enter Ticket ID to search: ")

        if ticket_id in tickets:
            print("Booking Found!")
            print("Passenger Name:", tickets[ticket_id]["NAME"])
            print("Destination:", tickets[ticket_id]["DESTINATION"])
        else:
            print("Booking not found.")

    elif choice == 4:
        print("Thank you for using the Ticket Booking System.")
        break

    else:
        print("Invalid choice! Please try again.")