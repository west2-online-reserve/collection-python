from sqlalchemy.orm import joinedload
from ..database import *
from ..models import *
from ..crud import *
from ..auth import *
from fastapi import Depends, HTTPException,APIRouter,Request
from fastapi.params import Query
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func

router = APIRouter()
@router.get("/friends/list")
async def get_user_friends(page_num: int = Query(1, ge=1), 
                                         page_size: int = Query(20, le=100),
                                         db: Session = Depends(get_db),
                                         current_user: dict = Depends(get_current_user)):
    if find_username(db, current_user['username']) == False:
        return {
                "base": {
                    "code": -1,
                    "msg": "token无效"
                }
            }

    # 获取当前登录用户信息
    user = await db.query(User).filter_by(username=current_user['username']).first()

    if not user:
        return {"base": {"code": -1, "msg": "用户不存在"}}

    # 计算总记录数
    total_count = await db.query(func.count(Friendship.friend_id)).filter_by(user_id=user.id).scalar()

    # 计算偏移量（OFFSET）
    offset = (page_num - 1) * page_size

    # 分页查询朋友列表
    friends_query = (
        db.query(User)
        .join(Friendship, User.id == Friendship.friend_id)
        .filter(Friendship.user_id == user.id)
        .offset(offset)
        .limit(page_size)
    )

    friends = await friends_query.all()
    res_item = []
    for item in friends:
        res_item.append({
            "id": item.id,
            "username": item.username,
            "avatar_url": item.avatar_url
        })

    response_data = {
        "base": {"code": 10000, "msg": "success"},
        "data": {
            "items": res_item,
            "total": total_count
        },
    }

    return response_data