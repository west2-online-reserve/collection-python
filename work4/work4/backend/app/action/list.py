from sqlalchemy.orm import joinedload
from ..database import *
from ..models import *
from ..crud import *
from ..auth import *
from fastapi import Depends, HTTPException, APIRouter, Request
from fastapi.params import Query
from sqlalchemy.sql import func

router = APIRouter()


@router.get("/like/list")
async def get_user_likes(user_id: int = Query(..., ge=1),
                         page_num: int = Query(1, ge=1),
                         page_size: int = Query(20, le=100),
                         db: Session = Depends(get_db),
                         current_user: dict = Depends(get_current_user)):
    if not find_username(db, current_user.username):
        return {
            "base": {
                "code": -1,
                "msg": "token无效"
            }
        }

    user = find_user_id(db, user_id)
    if not user:
        return {"base": {"code": -1, "msg": "用户不存在"}}
    else:
        # 计算偏移量（OFFSET）
        offset = (page_num - 1) * page_size

        likes_list = db.query(Likes).filter(Likes.user_id == user_id).offset(offset).limit(page_size).all()

        res_item = []
        for like in likes_list:
            video = db.query(Video).filter(Video.id == like.video_id).first()
            like_amount = db.query(func.count(Likes.id)).filter(Likes.video_id == video.id).scalar()
            if video:
                res_item.append({
                    "id": like.id,
                    "user_id": like.user_id,
                    "video_url": video.video_url,
                    "title": video.title,
                    "description": video.description,
                    "visit_count": video.views_count,
                    "like_count": like_amount,
                    # "comment_count": 0,
                    "created_at": video.created_at,
                    "updated_at": video.updated_at
                })

        response_data = {
            "base": {
                "code": 10000,
                "msg": "success"
            },
            "data": {
                "items": res_item
            },
        }
    return response_data
