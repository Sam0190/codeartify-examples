from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Any

from database import get_session
from dto.parking_reservation_request import ParkingReservationRequest
from repository.parking_reservation_repository import ParkingReservationRepository
from repository.parking_spot_repository import ParkingSpotRepository
from service.parking_spot_reservation_service import ParkingSpotReservationService

def get_parking_spot_repository(session: Session = Depends(get_session)) -> ParkingSpotRepository:
    return ParkingSpotRepository(session)

def get_parking_reservation_repository(session: Session = Depends(get_session)) -> ParkingReservationRepository:
    return ParkingReservationRepository(session)

def get_parking_spot_reservation_service(
    parking_reservation_repo: ParkingReservationRepository = Depends(get_parking_reservation_repository),
    parking_spot_repo: ParkingSpotRepository = Depends(get_parking_spot_repository)
) -> ParkingSpotReservationService:
    return ParkingSpotReservationService(parking_reservation_repo, parking_spot_repo)

router = APIRouter()

@router.post("/reserveSpot")
def reserve_parking_spot(
    request: ParkingReservationRequest,
    service: ParkingSpotReservationService = Depends(get_parking_spot_reservation_service)
) -> Any:
    return service.reserve_parking_spot(request)
