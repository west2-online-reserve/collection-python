from fastapi import APIRouter, Depends, Request
from ..auth import get_current_user
from ..crud import *
from ..database import get_db
from ..models import *

router = APIRouter()


@router.post("/like/action")
async def like_video(request: Request, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    data = await request.json()
    video_id = data.get('video_id')
    action_type = data.get('action_type')
    print('like')
    from_user = db.query(User).filter_by(username=current_user.username).first()
    if not from_user:
        return {"base": {"code": -1, "msg": "当前用户不存在"}}

    from_user_id = from_user.id

    existing_like = db.query(Likes).filter(Likes.user_id == from_user_id, Likes.video_id == video_id).first()

    if action_type == 1 and not existing_like:  # 点赞操作
        new_like = Likes(user_id=from_user_id, video_id=video_id)
        db.add(new_like)
        db.commit()
        return {"base": {"code": 10000, "msg": "点赞成功"}}

    elif action_type == 2 and existing_like:  # 取消点赞操作
        db.delete(existing_like)
        db.commit()
        return {"base": {"code": 10000, "msg": "取消点赞成功"}}

    else:
        return {"base": {"code": -1, "msg": "操作无效"}}
