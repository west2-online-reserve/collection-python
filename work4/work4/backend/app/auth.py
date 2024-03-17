# auth.py
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from pydantic import BaseModel
import jwt
from datetime import datetime

SECRET_KEY = "this-is-a-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="newToken/")


class TokenData(BaseModel):
    username: str


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        """ print('token start...', token)"""
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
            options={"verify_exp": True},
        )
        print('payload', payload["sub"])
        return TokenData(username=payload["sub"])
    except (jwt.PyJWTError, KeyError):
        return None

# res = get_current_user('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0MTIzIiwiZXhwIjoxNzA4OTU3MjY1Ljk5MjIzNX0.-y_cdRZbCn52H6x-GtDQsTlJPpRiVreJZe4gR36lIn')
# print(res)
