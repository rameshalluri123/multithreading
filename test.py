import time
import unittest
from parkinglotlog import ParkingLot, CHARGES, handle_vehicle

class TestParkingLot(unittest.TestCase):
    """
    Unit tests for the ParkingLot class and handle_vehicle function.
    """

    def setUp(self):
        """
        Sets up a new ParkingLot instance for each test.
        """
        self.parking_lot = ParkingLot()

    # Positive Test Cases
    def test_park_vehicle_success(self):
        """
        Tests successful parking of a vehicle.
        """
        self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        self.assertIn("KA-01-HH-1234", self.parking_lot.parking_data)
        self.assertEqual(self.parking_lot.parking_data["KA-01-HH-1234"][0], "two_wheeler")

    def test_calculate_charges_success(self):
        """
        Tests successful calculation of parking charges.
        """
        self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        time.sleep(2)  # Simulate 2 seconds of parking
        with self.assertLogs(level="INFO") as cm:
            self.parking_lot.calculate_charges("KA-01-HH-1234")
        self.assertIn("Total charges", cm.output[0])

    def test_handle_vehicle_park(self):
        """
        Tests the handle_vehicle function for parking.
        """
        handle_vehicle(self.parking_lot, "KA-01-HH-5678", "four_wheeler", "park")
        self.assertIn("KA-01-HH-5678", self.parking_lot.parking_data)

    def test_handle_vehicle_exit(self):
        """
        Tests the handle_vehicle function for exiting.
        """
        self.parking_lot.park_vehicle("KA-01-HH-5678", "four_wheeler")
        handle_vehicle(self.parking_lot, "KA-01-HH-5678", "four_wheeler", "exit")
        self.assertNotIn("KA-01-HH-5678", self.parking_lot.parking_data)

    # Negative Test Cases
    def test_park_vehicle_already_parked(self):
        """
        Tests parking a vehicle that is already parked.
        """
        self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        with self.assertLogs(level="ERROR") as cm:
            self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        self.assertIn("Vehicle KA-01-HH-1234 is already parked!", cm.output[0])

    def test_park_vehicle_invalid_type(self):
        """
        Tests parking a vehicle with an invalid type.
        """
        with self.assertLogs(level="ERROR") as cm:
            self.parking_lot.park_vehicle("KA-01-HH-5678", "truck")
        self.assertIn("Invalid vehicle type: truck.", cm.output[0])

    def test_calculate_charges_vehicle_not_found(self):
        """
        Tests calculating charges for a non-existent vehicle.
        """
        with self.assertLogs(level="ERROR") as cm:
            self.parking_lot.calculate_charges("KA-01-HH-9999")
        self.assertIn("Vehicle KA-01-HH-9999 is not found!", cm.output[0])

    def test_exit_vehicle_without_parking(self):
        """
        Tests exiting a vehicle that was not parked.
        """
        with self.assertLogs(level="ERROR") as cm:
            handle_vehicle(self.parking_lot, "KA-01-HH-1234", "two_wheeler", "exit")
        self.assertIn("Vehicle KA-01-HH-1234 is not found!", cm.output[0])

    def test_calculate_charges_correct_amount(self):
        """
        Tests if the correct parking charges are calculated.
        """
        self.parking_lot.park_vehicle("KA-01-HH-5678", "four_wheeler")
        time.sleep(2)  # Simulate 2 seconds of parking
        vehicle_type, entry_time = self.parking_lot.parking_data["KA-01-HH-5678"]
        total_time = time.time() - entry_time
        hours_parked = int(total_time // 3600) + 5
        expected_charges = hours_parked * CHARGES[vehicle_type]

        with self.assertLogs(level="INFO") as cm:
            self.parking_lot.calculate_charges("KA-01-HH-5678")
        self.assertIn(f"Total charges: ₹{expected_charges}", cm.output[0])

if __name__ == "__main__":
    unittest.main()
