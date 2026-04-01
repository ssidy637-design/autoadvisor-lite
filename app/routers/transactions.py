from fastapi import APIRouter

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/")
def create_transaction(transaction: dict):
    return {"message": "Transaction created", "data": transaction}

@router.get("/")
def get_transactions():
    return {"transactions": []}
