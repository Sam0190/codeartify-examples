from sqlmodel import Session, select
from typing import Optional
from model.parking_spot import ParkingSpot
from sqlalchemy.sql.expression import func

class ParkingSpotRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_any_available_spot(self) -> Optional[ParkingSpot]:
        statement = select(ParkingSpot).where(ParkingSpot.is_available == True).order_by(func.random()).limit(1)
        return self.session.exec(statement).first()

    def save(self, spot: ParkingSpot) -> ParkingSpot:
        self.session.add(spot)
        self.session.commit()
        self.session.refresh(spot)
        return spot
