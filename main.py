import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from controller.parking_spot_reservation_controller import router as reservation_router

app = FastAPI(title="Parking Spot Reservation API")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(reservation_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
