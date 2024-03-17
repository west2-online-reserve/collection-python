from fastapi import Depends,APIRouter,Request
from ..auth import get_current_user
from ..crud import *
from ..database import get_db
from ..models import *

router = APIRouter()

@router.post("/relation/action")
async def upload_image(request:Request, db: Session = Depends(get_db),current_user: dict = Depends(get_current_user)):
    from_user = db.query(User).filter_by(username=current_user.username).first()
    if not from_user:
        return {"base": {"code": -1, "msg": "当前用户不存在"}}
    
    from_user_id = from_user.id
    data = await request.json()
    to_user_id = data["to_user_id"]
    action_type = data["action_type"]
    # 检查是否已关注
    existing_follower = db.query(Follower).filter_by(follower_id=from_user_id, following_id=to_user_id).first()

    if action_type == 0 and not existing_follower:  # 关注操作
        new_follower = Follower(follower_id=from_user_id, following_id=to_user_id)
        db.add(new_follower)
        db.commit()
        return {"base": {"code": 10000, "msg": "关注成功"}}

    elif action_type == 1 and existing_follower:  # 取关操作
        db.delete(existing_follower)
        db.commit()
        return {"base": {"code": 10000, "msg": "取消关注成功"}}

    else:
        return {"base": {"code": -1, "msg": "操作无效"}}
