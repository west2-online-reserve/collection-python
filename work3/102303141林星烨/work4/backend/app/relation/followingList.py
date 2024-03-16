from sqlalchemy.orm import joinedload
from ..database import *
from ..models import *
from ..crud import *
from ..auth import *
from fastapi import Depends, HTTPException, APIRouter, Request
from fastapi.params import Query
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func

router = APIRouter()


@router.get("/following/list")
async def get_user_following(user_id: int = Query(..., ge=1),
                             page_num: int = Query(1, ge=1),
                             page_size: int = Query(20, le=100),
                             db: Session = Depends(get_db),
                             current_user: dict = Depends(get_current_user)):
    if find_username(db, current_user.username) == False:
        return {
            "base": {
                "code": -1,
                "msg": "token无效"
            }
        }

    async def find1(user_id):
        res = db.query(User).filter_by(id=user_id).first()
        return res

    user = await find1(user_id)

    if not user:
        return {"base": {"code": -1, "msg": "用户不存在"}}

    # 计算总记录数
    async def find2():
        res = db.query(func.count(Follower.following_id)).filter(Follower.follower_id == user_id).scalar()
        return res

    total_count = await find2()

    # 计算偏移量（OFFSET）
    offset = (page_num - 1) * page_size

    # 分页查询following列表
    following_users_query = (
        db.query(User)
        .join(Follower, User.id == Follower.following_id)
        .filter(Follower.follower_id == user_id)
        .offset(offset)
        .limit(page_size)
    )

    async def find3():
        res = following_users_query.all()
        return res

    following_users = await find3()
    res_item = []
    for item in following_users:
        res_item.append({
            "id": item.id,
            "username": item.username,
            "avatar_url": item.avatar_url
        })
    response_data = {
        "base": {"code": 10000, "msg": "success"},
        "data": {
            "item": res_item,
            "total": total_count
        },
    }

    return response_data
