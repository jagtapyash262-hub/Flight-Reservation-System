# MINI PROJECT: FLIGHT RESERVATION SYSTEM
# Concepts: Linear Search, Binary Search, Bubble Sort, Selection Sort
# Storage: In-memory lists and dictionaries

flights = [
    {"flight_no": 105, "airline": "Air India", "source": "Pune", "destination": "Delhi", "departure": "08:30", "price": 4500, "available_seats": 5},
    {"flight_no": 102, "airline": "IndiGo", "source": "Pune", "destination": "Mumbai", "departure": "10:15", "price": 2500, "available_seats": 6},
    {"flight_no": 108, "airline": "Akasa Air", "source": "Pune", "destination": "Bengaluru", "departure": "13:45", "price": 5200, "available_seats": 4},
    {"flight_no": 101, "airline": "SpiceJet", "source": "Pune", "destination": "Goa", "departure": "06:20", "price": 3200, "available_seats": 3},
    {"flight_no": 104, "airline": "IndiGo", "source": "Pune", "destination": "Hyderabad", "departure": "17:10", "price": 3800, "available_seats": 5},
]
reservations = []


def display_flights(flight_list):
    if not flight_list:
        print("\nNo flights found.")
        return
    print("\n" + "-" * 91)
    print(f"{'Flight No.':<12}{'Airline':<15}{'From':<12}{'Destination':<16}{'Departure':<12}{'Price (Rs.)':<15}{'Seats':<8}")
    print("-" * 91)
    for flight in flight_list:
        print(f"{flight['flight_no']:<12}{flight['airline']:<15}{flight['source']:<12}{flight['destination']:<16}{flight['departure']:<12}{flight['price']:<15}{flight['available_seats']:<8}")
    print("-" * 91)


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


# LINEAR SEARCH: find all flights for a destination.
def linear_search_by_destination(flight_list, destination):
    matches = []
    destination = destination.strip().lower()
    for flight in flight_list:
        if flight["destination"].lower() == destination:
            matches.append(flight)
    return matches


# BINARY SEARCH: search a sorted copy by flight number.
def binary_search_by_flight_number(flight_list, flight_number):
    sorted_list = sorted(flight_list, key=lambda flight: flight["flight_no"])
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        current_number = sorted_list[mid]["flight_no"]
        if current_number == flight_number:
            return sorted_list[mid]
        if current_number < flight_number:
            low = mid + 1
        else:
            high = mid - 1
    return None


# BUBBLE SORT: sort by price from lowest to highest.
def bubble_sort_by_price(flight_list):
    result = flight_list.copy()
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j]["price"] > result[j + 1]["price"]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


# SELECTION SORT: sort by departure time, earliest first.
def selection_sort_by_departure(flight_list):
    result = flight_list.copy()
    n = len(result)
    for i in range(n - 1):
        earliest_index = i
        for j in range(i + 1, n):
            if result[j]["departure"] < result[earliest_index]["departure"]:
                earliest_index = j
        result[i], result[earliest_index] = result[earliest_index], result[i]
    return result


def book_flight(flight, passenger_name, seats):
    if seats < 1:
        print("Please book at least one seat.")
        return
    if seats > flight["available_seats"]:
        print("Not enough seats are available for this flight.")
        return

    booking_id = f"B{len(reservations) + 1:03d}"
    total_price = flight["price"] * seats
    booking = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "flight_no": flight["flight_no"],
        "airline": flight["airline"],
        "source": flight["source"],
        "destination": flight["destination"],
        "departure": flight["departure"],
        "seats": seats,
        "total_price": total_price,
    }
    reservations.append(booking)
    flight["available_seats"] -= seats
    print("\nBooking successful!")
    print(f"Booking ID   : {booking_id}")
    print(f"Passenger    : {passenger_name}")
    print(f"Flight       : {flight['flight_no']} - {flight['airline']}")
    print(f"Route        : {flight['source']} to {flight['destination']}")
    print(f"Departure    : {flight['departure']}")
    print(f"Seats        : {seats}")
    print(f"Total amount : Rs. {total_price}")


def make_reservation():
    display_flights(flights)
    number = get_integer("\nEnter the flight number you want to book: ")
    flight = binary_search_by_flight_number(flights, number)
    if flight is None:
        print("Flight number not found.")
        return
    if flight["available_seats"] == 0:
        print("Sorry, this flight is fully booked.")
        return
    print(f"Selected: {flight['airline']} to {flight['destination']} at Rs. {flight['price']} per seat.")
    passenger_name = input("Enter passenger name: ").strip()
    if not passenger_name:
        print("Passenger name cannot be empty.")
        return
    seats = get_integer("Enter number of seats: ")
    book_flight(flight, passenger_name, seats)


def view_reservations():
    if not reservations:
        print("\nNo reservations have been made in this session.")
        return
    print("\nYOUR RESERVATIONS")
    for booking in reservations:
        print("-" * 40)
        print(f"Booking ID: {booking['booking_id']}")
        print(f"Passenger: {booking['passenger_name']}")
        print(f"Flight: {booking['flight_no']} - {booking['airline']}")
        print(f"Route: {booking['source']} to {booking['destination']}")
        print(f"Departure: {booking['departure']}")
        print(f"Seats: {booking['seats']}")
        print(f"Total: Rs. {booking['total_price']}")
    print("-" * 40)


def main():
    while True:
        print("\n======================================")
        print("       FLIGHT RESERVATION SYSTEM")
        print("======================================")
        print("1. View all flights")
        print("2. Search flight by flight number (Binary Search)")
        print("3. Search flights by destination (Linear Search)")
        print("4. Sort flights by ticket price (Bubble Sort)")
        print("5. Sort flights by departure time (Selection Sort)")
        print("6. Book a flight")
        print("7. View reservations")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            display_flights(flights)
        elif choice == "2":
            number = get_integer("Enter flight number: ")
            result = binary_search_by_flight_number(flights, number)
            if result:
                print("\nFlight found:")
                display_flights([result])
            else:
                print("\nSorry, no flight with that number was found.")
        elif choice == "3":
            destination = input("Enter destination: ")
            display_flights(linear_search_by_destination(flights, destination))
        elif choice == "4":
            display_flights(bubble_sort_by_price(flights))
        elif choice == "5":
            display_flights(selection_sort_by_departure(flights))
        elif choice == "6":
            make_reservation()
        elif choice == "7":
            view_reservations()
        elif choice == "8":
            print("Thank you for using the Flight Reservation System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
