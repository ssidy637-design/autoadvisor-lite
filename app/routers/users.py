from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: dict):
    return {"message": "User registered", "data": user}

@router.post("/login")
def login(user: dict):
    return {"message": "Login successful", "token": "fake-jwt-token"}
