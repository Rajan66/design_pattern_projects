import time

from enums import ParkingSpotType, VehicleType
from factory import ParkingSpotFactory, VehicleFactory
from models import ParkingFloor, ParkingLot, VehicleBasedFeeStrategy

# --- Setup Phase ---

# Create vehicles
bike = VehicleFactory.create_vehicle("BIKE123", VehicleType.BIKE)

car = VehicleFactory.create_vehicle("CAR456", VehicleType.CAR)

truck = VehicleFactory.create_vehicle("TRUCK789", VehicleType.TRUCK)

# Create parking spots (unique for each floor)
floor_1_spots = [
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
]

floor_2_spots = [
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
]

floor_3_spots = [
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.BIKE),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.COMPACT),
    ParkingSpotFactory.create_parking_spot(ParkingSpotType.LARGE),
]

# Create parking floors
floor_1 = ParkingFloor(1, floor_1_spots)
floor_2 = ParkingFloor(2, floor_2_spots)
floor_3 = ParkingFloor(3, floor_3_spots)

# Get the singleton parking lot instance and configure it
parking_lot = ParkingLot.get_instance()
parking_lot.set_fee_strategy(VehicleBasedFeeStrategy())
parking_lot.add_floor(floor_1)
parking_lot.add_floor(floor_2)
parking_lot.add_floor(floor_3)

# --- Simulation Phase ---

print("\n=== Vehicle Entry ===")
bike_ticket = parking_lot.park_vehicle(bike)
print(f"Bike parked at spot {bike_ticket.get_spot().get_spot_id()}")

car_ticket = parking_lot.park_vehicle(car)
print(f"Car parked at spot {car_ticket.get_spot().get_spot_id()}")

truck_ticket = parking_lot.park_vehicle(truck)
print(f"Truck parked at spot {truck_ticket.get_spot().get_spot_id()}")

# Simulate parking time
print("\n[Waiting 5 seconds to simulate time spent parked...]\n")
time.sleep(5)

# --- Exit Phase ---

print("=== Vehicle Exit ===")

bike_fee = parking_lot.unpark_vehicle("BIKE123")
print(f"Bike exited. Total fee: {bike_fee} units")

car_fee = parking_lot.unpark_vehicle("CAR456")
print(f"Car exited. Total fee: {car_fee} units")

truck_fee = parking_lot.unpark_vehicle("TRUCK789")
print(f"Truck exited. Total fee: {truck_fee} units")
