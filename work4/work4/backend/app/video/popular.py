from typing import List
from fastapi import Depends, APIRouter, Request
from sqlalchemy.orm import joinedload
from ..crud import *
from ..auth import *
from fastapi.params import Query

router = APIRouter()


@router.get("/video/popular")
async def popular_video(page_size: int = Query(10, ge=1),
                        page_num: int = Query(1, ge=1),
                        db: Session = Depends(get_db)):
    res = find_top_videos(db, page_size, page_num)
    items = []
    for item in res:
        user = find_username(db, item.username)
        items.append({
            "id": item.id,
            "user_id": user.id,
            "video_url": item.video_url,
            "views_count": item.views_count,
            "title": item.title,
            "description": item.description,
            "created_at": item.created_at,
            "updated_at": item.updated_at
        })
    return {
        "base": {
            "code": 10000,
            "msg": "success"
        },
        "data": {
            "items": items
        }
    }
