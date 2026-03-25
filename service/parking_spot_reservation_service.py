from typing import Any
from fastapi import status
from fastapi.responses import JSONResponse
from datetime import time
from dto.parking_reservation_request import ParkingReservationRequest
from dto.parking_reservation_response import ParkingReservationResponse
from model.parking_reservation import ParkingReservation
from repository.parking_reservation_repository import ParkingReservationRepository
from repository.parking_spot_repository import ParkingSpotRepository

class ParkingSpotReservationService:
    OPENING_TIME = time(6, 0) # 6:00 AM
    CLOSING_TIME = time(22, 0) # 10:00 PM

    def __init__(self, 
                 parking_reservation_repository: ParkingReservationRepository,
                 parking_spot_repository: ParkingSpotRepository):
        self.parking_reservation_repository = parking_reservation_repository
        self.parking_spot_repository = parking_spot_repository

    def reserve_parking_spot(self, request: ParkingReservationRequest) -> Any:
        # Validate reservation duration
        duration = request.end_time - request.start_time
        if duration.total_seconds() / 60 >= 30:
            # Ensure the end time is after the start time
            if request.end_time > request.start_time:
                # Ensure reservation is within operating hours
                if request.start_time.time() >= self.OPENING_TIME and request.end_time.time() <= self.CLOSING_TIME:
                    # Check if the user already has an active reservation
                    has_active_reservation = self.parking_reservation_repository.has_active_reservation(
                        request.reserved_by, request.start_time, request.end_time
                    )

                    if not has_active_reservation:
                        # Find any available spot
                        spot = self.parking_spot_repository.find_any_available_spot()

                        if spot is not None:
                            # Create and save the reservation
                            reservation = ParkingReservation(
                                reserved_by=request.reserved_by,
                                spot_id=spot.id,
                                start_time=request.start_time,
                                end_time=request.end_time
                            )
                            self.parking_reservation_repository.save(reservation)

                            # Mark the parking spot as unavailable
                            spot.is_available = False
                            self.parking_spot_repository.save(spot)

                            # Build and return the response
                            response = ParkingReservationResponse(
                                reservation_id=reservation.id,
                                reserved_by=request.reserved_by,
                                start_time=request.start_time,
                                end_time=request.end_time,
                                spot_id=spot.id
                            )

                            return JSONResponse(status_code=status.HTTP_201_CREATED, content=response.model_dump(mode='json'))
                        else:
                            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content="No available spot left.")

                    else:
                        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content="You already have an active reservation.")

                else:
                    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Reservations can only be made between 6:00 AM and 10:00 PM.")

            else:
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="End time must be after start time.")

        else:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Reservation must be at least 30 minutes long.")
