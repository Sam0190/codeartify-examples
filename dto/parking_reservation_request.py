from datetime import datetime
from pydantic import BaseModel

class ParkingReservationRequest(BaseModel):
    reserved_by: str
    start_time: datetime
    end_time: datetime
