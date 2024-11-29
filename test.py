import unittest
import time
from parkinglotlog import ParkingLot, CHARGES,handle_vehicle

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot()

    def test_park_vehicle_success(self):
        self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        self.assertIn("KA-01-HH-1234", self.parking_lot.parking_data)
        self.assertEqual(self.parking_lot.parking_data["KA-01-HH-1234"][0], "two_wheeler")

    def test_park_vehicle_invalid_type(self):
        with self.assertLogs(level="ERROR") as cm:
            self.parking_lot.park_vehicle("KA-01-HH-5678", "truck")
        self.assertIn("Invalid vehicle type", cm.output[0])

    def test_park_vehicle_already_parked(self):
        self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        with self.assertLogs(level="ERROR") as cm:
            self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        self.assertIn("already parked", cm.output[0])

    def test_calculate_charges_success(self):
        self.parking_lot.park_vehicle("KA-01-HH-1234", "two_wheeler")
        time.sleep(2)  # Simulate 2 seconds of parking
        with self.assertLogs(level="INFO") as cm:
            self.parking_lot.calculate_charges("KA-01-HH-1234")
        self.assertIn("Total charges", cm.output[0])

    def test_calculate_charges_vehicle_not_found(self):
        with self.assertLogs(level="ERROR") as cm:
            self.parking_lot.calculate_charges("KA-01-HH-9999")
        self.assertIn("not found", cm.output[0])

    def test_calculate_charges_correct_amount(self):
        self.parking_lot.park_vehicle("KA-01-HH-5678", "four_wheeler")
        time.sleep(2)  # Simulate 2 seconds of parking
        vehicle_type, entry_time = self.parking_lot.parking_data["KA-01-HH-5678"]
        total_time = time.time() - entry_time
        hours_parked = int(total_time // 3600) + 5
        expected_charges = hours_parked * CHARGES[vehicle_type]

        with self.assertLogs(level="INFO") as cm:
            self.parking_lot.calculate_charges("KA-01-HH-5678")
        self.assertIn(f"Total charges: ₹{expected_charges}", cm.output[0])

    def test_handle_vehicle_park(self):
        handle_vehicle(self.parking_lot, "KA-01-HH-5678", "four_wheeler", "park")
        self.assertIn("KA-01-HH-5678", self.parking_lot.parking_data)

    def test_handle_vehicle_exit(self):
        self.parking_lot.park_vehicle("KA-01-HH-5678", "four_wheeler")
        handle_vehicle(self.parking_lot, "KA-01-HH-5678", "four_wheeler", "exit")
        self.assertNotIn("KA-01-HH-5678", self.parking_lot.parking_data)

    def test_handle_vehicle_invalid_action(self):
        with self.assertLogs(level="INFO") as cm:
            handle_vehicle(self.parking_lot, "KA-01-HH-5678", "four_wheeler", "invalid")
        self.assertIn("Invalid action for vehicle KA-01-HH-5678.", cm.output[0])

if __name__ == "__main__":
    unittest.main()