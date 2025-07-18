# Singleton Pattern
from typing import Dict, List

from abstracts.fee_strategy import FeeStrategy
from abstracts.vehicle import Vehicle

from models.parking_floor import ParkingFloor
from models.parking_ticket import ParkingTicket


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("Only one ParkingLot instance is allowed.")

        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.fee_strategy: FeeStrategy = None
        ParkingLot._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        return cls()

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def set_fee_strategy(self, fee_strategy):
        self.fee_strategy = fee_strategy

    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        for floor in self.floors:
            spot = floor.get_available_spot(vehicle)
            if spot:
                spot.assign_vehicle(vehicle)
                ticket = ParkingTicket(vehicle, spot)
                self.active_tickets[vehicle.get_license_number()] = ticket
                return ticket
        raise Exception("No available spots.")

    def unpark_vehicle(self, license: str) -> float:
        ticket = self.active_tickets.get(license)
        if not ticket:
            raise Exception("No active ticket for license number: ", license)

        if not self.fee_strategy:
            raise Exception("Fee strategy not set.")

        ticket.set_exit_timestamp()
        ticket.get_spot().remove_vehicle
        fee = self.fee_strategy.calculate_fee(ticket)

        del self.active_tickets[license]

        return fee
