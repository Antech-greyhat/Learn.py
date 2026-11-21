# Reserve groups of seats and cancel a reservation by its booking ID.
# Practice: classes, sets, dictionaries, validation, and atomic state changes.
from itertools import count


class SeatBookingSystem:
    def __init__(self, rows=3, seats_per_row=4):
        if type(rows) is not int or not 1 <= rows <= 26:
            raise ValueError("Rows must be a whole number from 1 to 26.")
        if type(seats_per_row) is not int or not 1 <= seats_per_row <= 20:
            raise ValueError("Seats per row must be a whole number from 1 to 20.")
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = {f"{chr(65 + row)}{number}"
                      for row in range(rows) for number in range(1, seats_per_row + 1)}
        self.reservations = {}
        self.next_id = count(1)

    def available_seats(self):
        booked = set()
        for reservation in self.reservations.values():
            booked.update(reservation["seats"])
        return self.seats - booked

    def book(self, name, seat_text):
        name = name.strip()
        if not name:
            raise ValueError("Customer name cannot be empty.")
        requested = [seat.strip().upper() for seat in seat_text.split(",")]
        if any(not seat for seat in requested):
            raise ValueError("Enter seat labels separated by commas, such as A1,A2.")
        if len(set(requested)) != len(requested):
            raise ValueError("A booking cannot contain duplicate seats.")
        chosen = set(requested)
        if not chosen <= self.seats:
            raise ValueError("One or more seat labels do not exist.")
        if not chosen <= self.available_seats():
            raise ValueError("One or more seats are already booked.")
        # Reserve the entire group only after every requested seat is validated.
        booking_id = next(self.next_id)
        self.reservations[booking_id] = {"name": name, "seats": chosen}
        return booking_id

    def cancel(self, booking_id):
        if booking_id not in self.reservations:
            raise ValueError("Booking ID not found.")
        return self.reservations.pop(booking_id)

    def show_seats(self):
        available = self.available_seats()
        for row in range(self.rows):
            labels = [f"{chr(65 + row)}{number}" for number in range(1, self.seats_per_row + 1)]
            print(" ".join(seat if seat in available else "--" for seat in labels))
        print(f"Available seats: {len(available)} | -- means booked")


def main():
    system = SeatBookingSystem()
    print("Seat Booking System - reservations last for this session.")
    while True:
        print("\n1. View seats\n2. Book seats\n3. View bookings\n4. Cancel booking\n5. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                system.show_seats()
            elif choice == "2":
                name = input("Customer name: ")
                seats = input("Seat labels separated by commas: ")
                print(f"Booking confirmed: #{system.book(name, seats)}")
            elif choice == "3":
                if not system.reservations:
                    print("No bookings yet.")
                for booking_id, reservation in system.reservations.items():
                    seats = sorted(reservation["seats"], key=lambda seat: (seat[0], int(seat[1:])))
                    print(f"#{booking_id} | {reservation['name']} | {', '.join(seats)}")
            elif choice == "4":
                booking = system.cancel(int(input("Booking ID: ")))
                print(f"Cancelled booking for {booking['name']}.")
            elif choice == "5":
                break
            else:
                print("Choose an option from 1 to 5.")
        except ValueError as error:
            print(f"Bookings unchanged: {error}")


if __name__ == "__main__":
    main()
