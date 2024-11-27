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


 Features:
Vehicle Parking:
Simulates parking vehicles of different types (two-wheelers and four-wheelers).
Assigns a unique identifier (vehicle number) to each vehicle.
Records the entry time of each vehicle.
Charge Calculation:
Calculates parking charges based on the vehicle type and parking duration.
Rounds up the parking duration to the nearest hour.
Multithreading:
Employs multiple threads to simulate concurrent vehicle entry and exit operations.
Improves efficiency by allowing multiple operations to occur simultaneously.
Error Handling:
Implements error handling to gracefully handle invalid inputs and unexpected scenarios.
Raises ValueError for invalid vehicle types or duplicate parking attempts.
Raises KeyError for attempting to calculate charges for a non-existent vehicle.

