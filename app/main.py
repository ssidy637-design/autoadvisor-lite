from fastapi import FastAPI
from app.database import Base, engine
from app.routers import vehicles, transactions, users

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoAdvisor Lite")

# Include routes
app.include_router(users.router)
app.include_router(vehicles.router)
app.include_router(transactions.router)

@app.get("/")
def root():
    return {"message": "AutoAdvisor Lite API Running"}
