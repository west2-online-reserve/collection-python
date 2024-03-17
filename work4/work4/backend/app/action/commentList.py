from sqlalchemy.orm import joinedload
from ..database import *
from ..models import *
from ..crud import *
from ..auth import *
from fastapi import Depends, HTTPException, APIRouter, Request
from fastapi.params import Query
from sqlalchemy.sql import func

router = APIRouter()


@router.get("/comment/list")
async def get_video_comments(video_id: int = Query(..., ge=1),
                             page_num: int = Query(1, ge=1),
                             page_size: int = Query(20, le=100),
                             db: Session = Depends(get_db)):
    # 计算总记录数
    total_count = db.query(func.count(Comment.id)).filter(Comment.video_id == video_id).scalar()

    # 计算偏移量（OFFSET）
    offset = (page_num - 1) * page_size

    # 分页查询评论列表
    comments_query = (
        db.query(Comment)
        .filter(Comment.video_id == video_id)
        .order_by(Comment.created_at.desc())  # 按创建时间降序排列
        .offset(offset)
        .limit(page_size)
    )

    comments_list = comments_query.all()

    res_item = []
    for comment in comments_list:
        user = db.query(User).filter(User.id == comment.user_id).first()
        if user:
            res_item.append({
                "id": comment.id,
                "user_id": comment.user_id,
                "username": user.username,
                "content": comment.content,
                "created_at": comment.created_at,
            })

    response_data = {
        "base": {"code": 10000, "msg": "success"},
        "data": {
            "items": res_item,
            "total": total_count
        },
    }
    return response_data
