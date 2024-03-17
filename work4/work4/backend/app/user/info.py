from fastapi import Depends, APIRouter, Request
from ..auth import get_current_user
from ..crud import *
from ..database import *

router = APIRouter()


@router.get("/user/info")
async def get_info(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    username = data["username"]
    password = data["password"]
    exists = check_password(db, username, password)
    # print(exists)
    user = find_username(db, username)
    if not exists:
        return {
            "base": {
                "code": -1,
                "msg": "密码错误"
            }
        }
    else:
        return {
            "base": {
                "code": 10000,
                "msg": "success"
            },
            "data": {
                "id": user.id,
                "username": user.username,
                "avatar_url": user.avatar_url,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "deleted_at": user.deleted_at
            }
        }
