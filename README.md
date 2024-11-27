This Python script simulates a parking lot system, demonstrating the use of multithreading and exception handling to manage vehicle entry, exit, and charge calculation.

Core Concepts
1. Object-Oriented Programming (OOP):
The ParkingLot class encapsulates the state and behavior of a parking lot.
It has attributes to store vehicle information and methods to park vehicles, calculate charges, and remove vehicles.
2. Multithreading:
The threading module is used to create multiple threads of execution, allowing for concurrent operations.
This simulates multiple vehicles entering and exiting the parking lot simultaneously.
3. Exception Handling:
try-except blocks are used to handle potential exceptions like ValueError (for invalid input) and KeyError (for vehicles not found).
This ensures the program's robustness and prevents unexpected crashes.


Key Components:

1. Parking Charges Dictionary (CHARGES):
Stores hourly parking rates for different vehicle types (two_wheeler and four_wheeler).

2. ParkingLot Class:
Manages the parking lot operations:

parking_data: A dictionary storing parked vehicle details ({vehicle_number: (vehicle_type, entry_time)}).
park_vehicle(vehicle_number, vehicle_type):
Parks a vehicle if it isn't already parked.
Records the vehicle type and entry time.

calculate_charges(vehicle_number):

Calculates the total charges for a vehicle based on the time parked.

Rounds up to the next hour and multiplies by the hourly rate.

Removes the vehicle from parking_data.

3. Multithreading:
Simulates simultaneous vehicle actions (parking and exiting) using the threading module.

4. handle_vehicle Function:

Manages vehicle actions (parking or exiting) by invoking appropriate methods in the ParkingLot class.

Execution Flow:

1. Initialize the ParkingLot:

An instance of ParkingLot is created.

2. Actions List:

A sequence of vehicle actions is defined:

park: Adds a vehicle to the parking lot.

exit: Calculates charges for a parked vehicle and removes it.


3. Threads:

For each action, a thread is created to handle the operation.

A small delay (time.sleep(1)) simulates staggered vehicle activities.



4. Processing Actions:

Each thread performs the park or exit action, ensuring that multiple vehicles can act simultaneously.

5. Join Threads:

Ensures that the main program waits for all threads to finish execution.
---

Output Behavior:

When a vehicle is parked:

Vehicle details are added to parking_data.

A confirmation message is printed.


When a vehicle exits:

The time parked is calculated, charges are displayed, and the vehicle is removed.


Handles edge cases:

Vehicle already parked, invalid vehicle type, or vehicle not found.
Purpose:
Simulates a parking system for practical use in real-world scenarios.

Demonstrates multithreading to handle concurrent operations efficiently.




