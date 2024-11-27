import threading
import time

# Parking charges
CHARGES = {
    "two_wheeler": 10,   # ₹10 per hour for two-wheelers
    "four_wheeler": 20  # ₹20 per hour for four-wheelers
}


class ParkingLot:
    
    """
    Represents a parking lot with methods to park vehicles, calculate charges, and manage vehicle data.
    """

    def __init__(self):
        self.parking_data = {}  # Store vehicle details: {vehicle_number: (vehicle_type, entry_time)}

    def park_vehicle(self, vehicle_number, vehicle_type):
        """
        Parks a vehicle in the parking lot.

        Args:
            vehicle_number (str): The vehicle's registration number.
            vehicle_type (str): The type of vehicle (e.g., 'two_wheeler', 'four_wheeler').

        Raises:
            ValueError: If the vehicle is already parked or the vehicle type is invalid.
        """


        try:
            if vehicle_number in self.parking_data:
                raise ValueError(f"Vehicle {vehicle_number} is already parked!")
            elif vehicle_type not in CHARGES:
                raise ValueError(f"Invalid vehicle type: {vehicle_type}. Allowed types: two_wheeler, four_wheeler.")
            else:
                self.parking_data[vehicle_number] = (vehicle_type, time.time())
                print(f"{vehicle_type.capitalize()} {vehicle_number} parked successfully!")
        except ValueError as e:
            print(e)

    def calculate_charges(self, vehicle_number):
        """
        Calculates and prints the parking charges for a vehicle.

        Args:
            vehicle_number (str): The vehicle's registration number.

        Raises:
            KeyError: If the vehicle is not found in the parking lot.
        """
        try:
            if vehicle_number not in self.parking_data:
                raise KeyError(f"Vehicle {vehicle_number} is not found!")

            vehicle_type, entry_time = self.parking_data[vehicle_number]
            total_time = time.time() - entry_time
            hours_parked = int(total_time // 3600) + 5  # Round up to the next hour

            charges = hours_parked * CHARGES[vehicle_type]
            print(f"{vehicle_type.capitalize()} {vehicle_number} parked for {hours_parked} hour(s). Total charges: ₹{charges}")
            del self.parking_data[vehicle_number]
        except KeyError as e:
            print(e)

def handle_vehicle(parking_lot, vehicle_number, vehicle_type, action):
    """
    Handles parking and exiting actions for a vehicle.

    Args:
        parking_lot (ParkingLot): The parking lot object.
        vehicle_number (str): The vehicle's registration number.
        vehicle_type (str): The type of vehicle.
        action (str): The action to perform ('park' or 'exit').
    """
    if action == "park":
        parking_lot.park_vehicle(vehicle_number, vehicle_type)
    elif action == "exit":
        parking_lot.calculate_charges(vehicle_number)
    else:
        print(f"Invalid action for vehicle {vehicle_number}.")

if __name__ == "__main__":
    parking_lot = ParkingLot()
    threads = []

    # Simulate actions for two-wheelers and four-wheelers
    actions = [
        ("KA-01-HH-1234", "two_wheeler", "park"),
        ("KA-01-HH-5678", "four_wheeler", "park"),
        ("KA-01-HH-1234", "two_wheeler", "exit"),
        ("KA-01-HH-5678", "four_wheeler", "exit"),
    ]

    for vehicle_number, vehicle_type, action in actions:
        thread = threading.Thread(target=handle_vehicle, args=(parking_lot, vehicle_number, vehicle_type, action))
        threads.append(thread)
        thread.start()
        time.sleep(1)  # Simulate time delay between actions

    for thread in threads:
        thread.join()