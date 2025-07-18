from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from abstracts.parking_spot import ParkingSpot
from abstracts.vehicle import Vehicle


class ParkingTicket:
    def __init__(self, vehicle: Vehicle, parking_spot: ParkingSpot):
        self.ticket_id: UUID = uuid4()
        self.__entry_timestamp: datetime = datetime.now()
        self.exit_timestamp: Optional[datetime] = None
        self.vehicle: Vehicle = vehicle
        self.parking_spot: ParkingSpot = parking_spot

    def get_ticket_id(self) -> UUID:
        return self.ticket_id

    def get_vehicle(self) -> Vehicle:
        return self.vehicle

    def get_spot(self) -> ParkingSpot:
        return self.parking_spot

    def get_entry_timestamp(self) -> datetime:
        return self.__entry_timestamp

    def get_exit_timestamp(self) -> Optional[datetime]:
        return self.exit_timestamp

    def set_exit_timestamp(self, timestamp: Optional[datetime] = None):
        self.exit_timestamp = timestamp or datetime.now()
