from abc import ABC, abstractmethod

from enums.vehicle_type import VehicleType

from abstracts.vehicle import Vehicle


class ParkingSpot(ABC):
    def __init__(self, spot_id: int):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None
        self.vehicle_type: VehicleType = ""

    def is_available(self) -> bool:
        return not self.is_occupied

    def assign_vehicle(self, vehicle: Vehicle):
        if not self.is_available():
            return False
        self.is_occupied = True
        self.vehicle = vehicle

    def remove_vehicle(self):
        self.is_occupied = False
        self.vehicle = None

    def get_vehicle(self):
        return self.vehicle

    def get_spot_id(self):
        return self.spot_id

    @abstractmethod
    def can_fit_vehicle(self, vehicle: Vehicle):
        pass
