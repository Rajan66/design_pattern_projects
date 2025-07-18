from abstracts import FeeStrategy

from models.parking_ticket import ParkingTicket


class FlatFeeStrategy(FeeStrategy):
    def __init__(self):
        self.RATE_PER_HOUR = 20  # in rupees

    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        exit_time = parking_ticket.get_exit_timestamp()
        entry_time = parking_ticket.get_entry_timestamp()

        if not exit_time or not entry_time:
            raise ValueError("Both entry and exit times must be set.")

        parking_time = exit_time - entry_time
        hours_parked = parking_time.total_seconds() / 3600

        total_fee = hours_parked * self.RATE_PER_HOUR

        return round(total_fee, 2)
