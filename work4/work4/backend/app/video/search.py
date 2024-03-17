from fastapi import Depends, APIRouter, Request
from fastapi import Form
from ..auth import get_current_user
from ..crud import *

router = APIRouter()


@router.post("/video/search")
async def search_video_post(keywords: str = Form(...), page_size: int = Form(...),
                            page_num: int = Form(...),
                            db: Session = Depends(get_db)):
    video = await search_videos(db, keywords, page_size, page_num)
    items = []
    if video:
        for item in video:
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
            }}
    else:
        return {
            "base": {
                "code": -1,
                "msg": "密码错误"
            }
        }
