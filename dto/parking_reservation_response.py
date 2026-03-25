from datetime import datetime
from pydantic import BaseModel

class ParkingReservationResponse(BaseModel):
    reservation_id: int
    spot_id: int
    reserved_by: str
    start_time: datetime
    end_time: datetime
