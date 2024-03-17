from fastapi import Depends, HTTPException, APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import timedelta
import jwt
from ..database import *
from ..models import *
from ..crud import *
import time

# 假设已经定义了User模型和验证用户名密码的函数authenticate_user
router = APIRouter()

SECRET_KEY = "this-is-a-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Access Token的有效期为30分钟
REFRESH_TOKEN_EXPIRE_HOURS = 24 * 7  # Refresh Token的有效期为7天


class TokenData(BaseModel):
    username: str


async def create_tokens(user: User) -> dict:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(hours=REFRESH_TOKEN_EXPIRE_HOURS)

    access_token = jwt.encode(
        {"sub": user.username, "exp": time.time() + access_token_expires.seconds},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    refresh_token = jwt.encode(
        {"sub": user.username, "exp": time.time() + refresh_token_expires.seconds},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return {
        "res": True,
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": int(access_token_expires.total_seconds()),
        "refresh_token": refresh_token,
    }


@router.post("/user/login")
async def login(request: Request, db: Session = Depends(get_db)):
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


