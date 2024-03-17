from fastapi import APIRouter, Depends, Request
from ..database import *
from ..models import *
from ..auth import get_current_user
from fastapi import Depends, APIRouter, Request
from ..crud import *

router = APIRouter()


@router.post("/comment/publish")
async def add_comment(request: Request, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    data = await request.json()
    video_id = data.get('video_id')
    content = data.get('content')
    from_user = db.query(User).filter_by(username=current_user.username).first()
    if not from_user:
        return {"base": {"code": -1, "msg": "当前用户不存在"}}

    from_user_id = from_user.id
    new_comment = Comment(user_id=from_user_id, video_id=video_id, content=content)

    db.add(new_comment)
    db.commit()

    return {"base": {"code": 10000, "msg": "评论成功"}}
