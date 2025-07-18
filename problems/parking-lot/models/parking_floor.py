from typing import List

from abstracts import ParkingSpot, Vehicle


class ParkingFloor:
    def __init__(self, floor_number: int, parking_spots: List[ParkingSpot]):
        self.floor_number = floor_number
        self.parking_spots = parking_spots

    def get_available_spot(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if spot.is_available() and spot.can_fit_vehicle(vehicle):
                return spot

        return None

    def get_floor_number(self):
        return self.floor_number
