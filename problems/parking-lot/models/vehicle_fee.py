from typing import Dict

from abstracts import FeeStrategy
from enums import VehicleType

from models.parking_ticket import ParkingTicket


class VehicleBasedFeeStrategy(FeeStrategy):
    def __init__(self):
        self.hourly_rates: Dict[VehicleType, float] = {
            VehicleType.BIKE: 20,
            VehicleType.CAR: 40,
            VehicleType.TRUCK: 80,
        }

    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        exit_time = parking_ticket.get_exit_timestamp()
        entry_time = parking_ticket.get_entry_timestamp()

        if not exit_time or not entry_time:
            raise ValueError("Both entry and exit times must be set.")

        parking_time = exit_time - entry_time
        hours_parked = parking_time.total_seconds() / 3600

        rate = self.hourly_rates.get(parking_ticket.vehicle.get_type())
        if rate is None:
            raise ValueError("Unknown vehicle type for fee calculation.")

        total_fee = hours_parked * rate

        return round(total_fee, 2)
