from fastapi import APIRouter

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.post("/")
def create_vehicle(vehicle: dict):
    return {"message": "Vehicle created", "data": vehicle}

@router.get("/")
def get_vehicles():
    return {"vehicles": []}
