from fastapi import APIRouter
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def get_users():
    return {"users": "获取用户成功"}

@router.post("/")
async def get_user():
    return {"a"}

