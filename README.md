
Flight Reservation System
A simple console-based Flight Reservation System developed in Python as a Data Structures mini project. It demonstrates searching and sorting algorithms through a basic flight booking workflow.

Features
Display all available flights.
Search for flights by destination using Linear Search.
Search for a flight by flight number using Binary Search.
Sort flights by ticket price using Bubble Sort.
Sort flights by departure time using Selection Sort.
Book seats on a flight and update the available seat count.
Generate a booking ID and display reservations during the current run.
Data Structures and Algorithms
Feature	Algorithm / Concept	Purpose
Search by destination	Linear Search	Checks flights one by one for a matching destination.
Search by flight number	Binary Search	Searches a list sorted by flight number.
Sort by ticket price	Bubble Sort	Arranges flights by increasing ticket price.
Sort by departure time	Selection Sort	Arranges flights by departure time.
Flight and reservation records	Lists and dictionaries	Store flight details and booking information.
Requirements
Python 3.8 or later
No external Python packages are required.
How to Run
Download or clone this repository.

Open a terminal or Command Prompt in the project folder.

Run:

python main.py
If your system uses the py launcher, you can run:

py main.py
Follow the menu shown in the terminal and enter the number for the operation you want.

Project Structure
Flight-Reservation-System/
├── main.py
├── README.md
└── sample_output.txt
main.py — complete Python program.
README.md — project description and run instructions.
sample_output.txt — example of the program's console output.
Sample Workflow
Choose View All Flights to see available flights.
Search for a destination or flight number.
Sort flights by ticket price or departure time.
Choose Book a Flight, enter the requested flight details, passenger name, and number of seats.
Choose View Reservations to see bookings made during the current run.
The exact menu wording and output depend on the version of main.py in the repository.

Important Notes
This is a beginner-level educational project, not a real airline booking service.
Flight and reservation data are stored in memory. Reservations are not saved permanently and will be cleared when the program exits.
Sample flights and seat availability are predefined in the program.
Binary Search requires the flights to be ordered by flight number; the program should sort a copy of the flight list before searching.
Future Improvements
Save flight and booking records in a database or file.
Add passenger login and registration.
Add cancellation and booking history.
Provide a graphical user interface.
Connect to a real flight-data service.
Author
Created as a Data Structures mini project using Python.

⋮⋮⋮⋮
