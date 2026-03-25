from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class ParkingReservation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reserved_by: str
    spot_id: int
    start_time: datetime
    end_time: datetime
