from uuid import UUID

from abstracts import ParkingSpot, Vehicle
from enums import VehicleType


class CompactSpot(ParkingSpot):
    def __init__(self, spot_id: UUID):
        super().__init__(spot_id)

    def can_fit_vehicle(self, vehicle: Vehicle):
        if vehicle.get_type() == VehicleType.CAR:
            return True
        return False
