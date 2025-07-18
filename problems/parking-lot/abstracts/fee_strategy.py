from abc import ABC, abstractmethod

from models.parking_ticket import ParkingTicket


class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, parking_ticket: ParkingTicket) -> float:
        pass
