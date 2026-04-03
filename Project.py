#ME
class Hotel:
    def __init__(self):
        self.rooms = {
            101: {"type": "Single", "price": 1000, "booked": False},
            102: {"type": "Single", "price": 1000, "booked": False},
            201: {"type": "Double", "price": 2000, "booked": False},
            202: {"type": "Double", "price": 2000, "booked": False},
            301: {"type": "Suite", "price": 4000, "booked": False}
        }
        self.customers = {}
#Show Rooms
    def show_rooms(self):
        print("\nAvailable Rooms:")
        for room, details in self.rooms.items():
            status = "Booked" if details["booked"] else "Available"
            print(f"Room {room} - {details['type']} - ₹{details['price']} - {status}")
#Book Rooms
    def book_room(self, name, room_no):
        if room_no in self.rooms:
            if not self.rooms[room_no]["booked"]:
                self.rooms[room_no]["booked"] = True
                self.customers[room_no] = {"name": name, "days": 0}
                print(f"Room {room_no} successfully booked for {name}")
            else:
                print("Room already booked!")
        else:
            print("Invalid room number!")
#Check In
    def check_in(self, room_no, days):
        if room_no in self.customers:
            self.customers[room_no]["days"] = days
            print(f"Customer checked into Room {room_no} for {days} days")
        else:
            print("Room not booked!")
#Check Out
    def check_out(self, room_no):
        if room_no in self.customers:
            days = self.customers[room_no]["days"]
            price = self.rooms[room_no]["price"]
            total = days * price

            print("\n--- Bill Summary ---")
            print(f"Customer: {self.customers[room_no]['name']}")
            print(f"Room: {room_no}")
            print(f"Days: {days}")
            print(f"Total Amount: ₹{total}")

# Payment
            paid = float(input("Enter payment amount: ₹"))
            if paid >= total:
                print("Payment successful. Thank you!")
                self.rooms[room_no]["booked"] = False
                del self.customers[room_no]
            else:
                print("Insufficient payment!")
        else:
            print("Invalid check-out!")

#Main Program
hotel = Hotel()

while True:
    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Show Rooms")
    print("2. Book Room")
    print("3. Check-In")
    print("4. Check-Out")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hotel.show_rooms()

    elif choice == "2":
        name = input("Enter customer name: ")
        room_no = int(input("Enter room number: "))
        hotel.book_room(name, room_no)

    elif choice == "3":
        room_no = int(input("Enter room number: "))
        days = int(input("Enter number of days: "))
        hotel.check_in(room_no, days)

    elif choice == "4":
        room_no = int(input("Enter room number: "))
        hotel.check_out(room_no)

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")  