# Factory Pattern

from uuid import uuid4

from enums import ParkingSpotType
from models import BikeSpot, CompactSpot, LargeSpot


class ParkingSpotFactory:
    @classmethod
    def create_parking_spot(
        self,
        parking_spot_type: ParkingSpotType,
    ):
        spot_id = uuid4()
        if parking_spot_type == ParkingSpotType.BIKE:
            return BikeSpot(spot_id)

        if parking_spot_type == ParkingSpotType.COMPACT:
            return CompactSpot(spot_id)

        if parking_spot_type == ParkingSpotType.LARGE:
            return LargeSpot(spot_id)

        raise Exception("Invalid parking spot type.")
