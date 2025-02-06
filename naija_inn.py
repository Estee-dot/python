import re
import random
from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = "Free"

    def book_room(self, guest, nights):
        if self.status == "Free":
            self.status = "Taken"
            booking_ref = f"RES{random.randint(1000, 9999)}"
            check_in_date = datetime.today().strftime('%d %B, %Y')
            check_out_date = (datetime.today() + timedelta(days=nights)).strftime('%d %B, %Y')
            guest.booking_reference = booking_ref
            guest.check_in_date = check_in_date
            guest.check_out_date = check_out_date
            guest.room_number = self.room_number
            guest.room_type = self.room_type
            guest.total_payment = self.price * nights
            print(f"Booking Successful!\nGuest Details:\nName: {guest.name}\nPhone: {guest.phone}\nEmail: {guest.email}\nRoom Details:\nRoom Number: {self.room_number}\nType: {self.room_type}\nPrice per Night: ₦{self.price}\nTotal Payment: ₦{guest.total_payment}\nBooking Reference Number: {booking_ref}\nYour check-in date is {check_in_date} and check-out date is {check_out_date}.")
            return booking_ref
        else:
            print(f"Room {self.room_number} is not available.")
            return None

class Guest:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.booking_reference = None
        self.room_number = None
        self.room_type = None
        self.check_in_date = None
        self.check_out_date = None
        self.total_payment = None

class HotelManagementSystem:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.guests = []

    def create_rooms(self):
        rooms = []
        for i in range(1, 5):
            rooms.append(Room(100 + i, "Single", 10000))
            rooms.append(Room(200 + i, "Double", 15000))
            rooms.append(Room(300 + i, "Suite", 25000))
        return rooms

    def input_name(self):
        while True:
            name = input("Please enter your name: ")
            if name.isalpha() and len(name) >= 3:
                return name
            else:
                print("Name must contain only letters and be at least 3 characters long.")

    def input_phone(self):
        while True:
            phone = input("Enter your phone number: ")
            if phone.isdigit() and len(phone) == 11:
                return phone
            else:
                print("Phone number must contain only numbers and be 11 digits long.")

    def input_email(self):
        while True:
            email = input("Enter your email address: ")
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                print("Please enter a valid email address.")

    def book_room(self):
        print("Welcome to Naija Comfort Inn!")
        name = self.input_name()
        phone = self.input_phone()
        email = self.input_email()
        guest = Guest(name, phone, email)
        room_type = input("Select room type (Single/Double/Suite): ").capitalize()
        nights = int(input("Enter number of nights: "))

        available_rooms = [room for room in self.rooms if room.room_type == room_type and room.status == "Free"]
        if available_rooms:
            room = available_rooms[0]
            booking_ref = room.book_room(guest, nights)
            if booking_ref:
                self.guests.append(guest)
        else:
            print(f"No {room_type} rooms available.")

    def view_rooms(self):
        print("Rooms Available: ")
        for room in sorted(self.rooms, key=lambda x: x.room_number):
            print(f"Room Number: {room.room_number} | Type: {room.room_type} | Status: {room.status}")

    def payment_status(self):
        booking_ref = input("Enter your booking reference number: ")
        guest = next((g for g in self.guests if g.booking_reference == booking_ref), None)
        if guest:
            print(f"\nPayment Status for Booking Reference: {booking_ref}")
            print(f"Total Payment: ₦{guest.total_payment}")
        else:
            print("Booking reference not found.")

    def cancel_booking(self):
        booking_ref = input("Enter your booking reference number: ")
        guest = next((g for g in self.guests if g.booking_reference == booking_ref), None)
        if guest:
            room = next((r for r in self.rooms if r.room_number == guest.room_number), None)
            if room:
                room.status = "Free"
                self.guests.remove(guest)
                print(f"Booking with reference {booking_ref} cancelled successfully. Room {guest.room_number} is now free.")
        else:
            print("Booking reference not found.")

    def manage_reservations(self):
        print("\nManage Reservations:")
        for room in self.rooms:
            print(f"Room {room.room_number} | Type: {room.room_type} | Status: {room.status}")

    def generate_reports(self):
        total_booked = sum(1 for room in self.rooms if room.status == "Taken")
        occupancy_rate = (total_booked / len(self.rooms)) * 100 if len(self.rooms) > 0 else 0
        total_revenue = sum(guest.total_payment for guest in self.guests if guest.total_payment)
        print(f"\nWeekly Report:")
        print(f"Total Rooms Booked: {total_booked}")
        print(f"Occupancy Rate: {occupancy_rate:.2f}%")
        print(f"Total Revenue: ₦{total_revenue}")

    def mark_rooms_for_maintenance(self):
        room_number = int(input("Enter room number to mark for maintenance: "))
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room:
            if room.status == "Free":
                room.status = "In maintenance"
                print(f"Room {room_number} marked as unavailable for maintenance.")
            elif room.status == "In maintenance":
                room.status = "Free"
                print(f"Room {room_number} is now available.")
        else:
            print(f"Room {room_number} not found.")

    def add_room(self):
        room_type = input("What type of room would you like to add (Single/Double/Suite)? ").capitalize()
        room_number = 0
        if room_type == "Single":
            room_number = 100 + len([r for r in self.rooms if r.room_type == "Single"]) + 1
            price = 10000
        elif room_type == "Double":
            room_number = 200 + len([r for r in self.rooms if r.room_type == "Double"]) + 1
            price = 15000
        elif room_type == "Suite":
            room_number = 300 + len([r for r in self.rooms if r.room_type == "Suite"]) + 1
            price = 25000
        else:
            print("Invalid room type.")
            return

        self.rooms.append(Room(room_number, room_type, price))
        print(f"Room {room_number} added successfully.")

    def view_guest_details(self):
        room_number = int(input("View guest details for room: "))
        room = next((room for room in self.rooms if room.room_number == room_number), None)
        if room and room.status == "Taken":
            guest = next((g for g in self.guests if g.room_number == room_number), None)
            if guest:
                print(f"\nGuest Details for Room {room_number}:")
                print(f"Name: {guest.name}")
                print(f"Phone: {guest.phone}")
                print(f"Email: {guest.email}")
                print(f"Reservation Details:")
                print(f"Room Number: {guest.room_number}")
                print(f"Check-in Date: {guest.check_in_date}")
                print(f"Check-out Date: {guest.check_out_date}")
                print(f"Booking Reference Number: {guest.booking_reference}")
        else:
            print(f"Room {room_number} is either free or not found.")

    def calculate_payment(self):
        room_type = input("Enter room type (Single/Double/Suite): ").capitalize()
        nights = int(input("Enter number of nights: "))
        festive_period = input("Is this a festive period? (Yes/No): ").lower()
        price = next((room.price for room in self.rooms if room.room_type == room_type), None)
        if price:
            total_price = price * nights
            if festive_period == "yes":
                total_price += total_price * 0.2
            print(f"Room Type: {room_type}\nPrice per Night: ₦{price}\nFestive Period Surcharge: 20%\nTotal Payment: ₦{total_price}")
        else:
            print("Invalid room type.")

    def send_notification(self):
        booking_ref = input("Enter your booking reference number: ")
        guest = next((g for g in self.guests if g.booking_reference == booking_ref), None)
        if guest:
            print(f"\nNotification sent to {guest.name}")
            print(f"Dear {guest.name}, this is a reminder for your stay at Naija Comfort Inn.\nCheck-in Date: {guest.check_in_date}\nRoom Number: {guest.room_number}\nWe look forward to hosting you!")
        else:
            print("Booking reference not found.")

    def guest_menu(self):
        while True:
            print("\nWelcome, Our Esteemed Customer!")
            print("Options:")
            print("1. Book room")
            print("2. View booking")
            print("3. Edit profile")
            print("4. Check room availability")
            print("5. Payment status")
            print("6. Cancel booking")
            print("7. View all available rooms")
            print("8. View notification")
            print("9. Logout")
            option = input("Select an option: ")

            if option == "1":
                self.book_room()
            elif option == "2":
                booking_ref = input("Enter your booking reference number: ")
                guest = next((g for g in self.guests if g.booking_reference == booking_ref), None)
                if guest:
                    print(f"\nBooking Details for Reference {booking_ref}:")
                    print(f"Name: {guest.name}")
                    print(f"Room Number: {guest.room_number}")
                    print(f"Room Type: {guest.room_type}")
                    print(f"Check-in Date: {guest.check_in_date}")
                    print(f"Check-out Date: {guest.check_out_date}")
                    print(f"Total Payment: ₦{guest.total_payment}")
                else:
                    print("Booking reference not found.")
            elif option == "3":
                self.edit_profile()
            elif option == "4":
                self.view_rooms()
            elif option == "5":
                self.payment_status()
            elif option == "6":
                self.cancel_booking()
            elif option == "7":
                self.view_rooms()
            elif option == "8":
                self.send_notification()
            elif option == "9":
                self.run()
            else:
                print("Invalid option, try again.")

    def edit_profile(self):
        print("\nEdit Profile:")
        booking_ref = input("Enter your booking reference number: ")
        guest = next((g for g in self.guests if g.booking_reference == booking_ref), None)
        if guest:
            new_name = input(f"Current Name: {guest.name} - Enter new name: ")
            new_phone = input(f"Current Phone: {guest.phone} - Enter new phone number: ")
            new_email = input(f"Current Email: {guest.email} - Enter new email: ")

            guest.name = new_name
            guest.phone = new_phone
            guest.email = new_email

            print("Profile updated successfully.")
        else:
            print("Booking reference not found.")

    def admin_menu(self):
        while True:
            print("\nWelcome Admin!")
            print("Options:")
            print("1. View rooms")
            print("2. Manage reservations")
            print("3. Generate reports")
            print("4. Mark rooms for maintenance")
            print("5. Add room")
            print("6. View guest details")
            print("7. Calculate payment")
            print("8. Send notification")
            print("9. Logout")
            option = input("Select an option: ")

            if option == "1":
                self.view_rooms()
            elif option == "2":
                self.manage_reservations()
            elif option == "3":
                self.generate_reports()
            elif option == "4":
                self.mark_rooms_for_maintenance()
            elif option == "5":
                self.add_room()
            elif option == "6":
                self.view_guest_details()
            elif option == "7":
                self.calculate_payment()
            elif option == "8":
                self.send_notification()
            elif option == "9":
                self.run()
            else:
                print("Invalid option, try again.")

    def run(self):
        print("Welcome to Naija Comfort Inn Management System!")
        user_type = input("Login as Admin or a Guest? ").lower()
        if user_type == "admin":
            self.admin_menu()
        elif user_type == "guest":
            self.guest_menu()
        else:
            print("Invalid option, please enter 'Admin' or 'Guest'.")
            
hotel_system = HotelManagementSystem()
hotel_system.run()
