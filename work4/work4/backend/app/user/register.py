from fastapi import APIRouter, Depends, Request
from ..database import *
from ..models import *
from ..crud import *
from passlib.context import CryptContext

router = APIRouter()


@router.post("/user/register")
async def register(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    username = data["username"]
    password = data["password"]
    # hash_pw = hash_password(password)
    if check_username_exists(db, username):
        return {
            "base": {
                "code": -1,
                "msg": "用户存在"
            }
        }
    else:
        await register_user(db, username, password)
        return {
            "base": {
                "code": 10000,
                "msg": "success"
            }
        }

# @router.get("/test")
# async def test():
#     return {"message": "Hello World"}
