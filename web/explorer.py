from fastapi import APIRouter

router = APIRouter(prefix="/explorer")

@router.get("/")
def top():
    return "top exploerer endpont"