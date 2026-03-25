from typing import Optional
from sqlmodel import SQLModel, Field

class ParkingSpot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_available: bool = True
