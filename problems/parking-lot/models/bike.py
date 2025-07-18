from abstracts import Vehicle
from enums import VehicleType


class Bike(Vehicle):
    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.vehicle_type = VehicleType.BIKE

    def get_type(self):
        return self.vehicle_type

    def get_license_number(self):
        return self.license_plate
