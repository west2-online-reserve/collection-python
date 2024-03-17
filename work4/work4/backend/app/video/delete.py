from typing import List
from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import joinedload
from ..crud import *
from ..auth import *
from fastapi.params import Query

from ..database import get_db

router = APIRouter()


@router.get("/video/delete")
async def delete_video(id: int = Query(..., ge=1),
                       db: Session = Depends(get_db)):
    print(id)
    return await delete_video_by_id(db, id)
