from sqlmodel import Session, select
from model.parking_reservation import ParkingReservation
from datetime import datetime

class ParkingReservationRepository:
    def __init__(self, session: Session):
        self.session = session

    def has_active_reservation(self, reserved_by: str, start_time: datetime, end_time: datetime) -> bool:
        statement = select(ParkingReservation).where(
            ParkingReservation.reserved_by == reserved_by,
            ParkingReservation.start_time < end_time,
            ParkingReservation.end_time > start_time
        )
        result = self.session.exec(statement).first()
        return result is not None
        
    def save(self, reservation: ParkingReservation) -> ParkingReservation:
        self.session.add(reservation)
        self.session.commit()
        self.session.refresh(reservation)
        return reservation
