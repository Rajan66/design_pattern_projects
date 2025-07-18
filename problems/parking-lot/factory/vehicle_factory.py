# Factory Pattern


from enums import VehicleType
from models import Bike, Car, Truck


class VehicleFactory:
    @classmethod
    def create_vehicle(self, license: str, vehicle_type: VehicleType):
        if vehicle_type == VehicleType.CAR:
            return Car(license)

        if vehicle_type == VehicleType.BIKE:
            return Bike(license)

        if vehicle_type == VehicleType.TRUCK:
            return Truck(license)

        raise Exception("Invalid vehicle type.")
