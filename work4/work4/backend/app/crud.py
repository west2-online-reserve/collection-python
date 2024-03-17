from passlib.context import CryptContext
from sqlalchemy.orm import Session

from .models import User, Video, Comment

# 创建一个加密上下文，用于处理密码哈希与验证
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # 使用bcrypt对密码进行哈希
    hashed_password = pwd_context.hash(password)
    return hashed_password


async def register_user(db: Session, username: str, password: str):
    hashed_password = hash_password(password)
    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def check_password(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and pwd_context.verify(password, user.password):
        return True
    return False


def check_username_exists(db: Session, username: str) -> bool:
    user = db.query(User).filter(User.username == username).first()
    return user is not None


def find_username(db: Session, username: str) -> bool:
    user = db.query(User).filter(User.username == username).first()
    return user


def find_user_id(db: Session, id: str) -> bool:
    user = db.query(User).filter(User.id == id).first()
    return user


async def add_avatar(db: Session, username: str, avatar_url: str):
    # 查找指定用户名的用户记录
    user = db.query(User).filter(User.username == username).first()

    if user:
        # 如果找到用户，则更新其avatar_url字段
        user.avatar_url = avatar_url
        db.commit()
        return user
    else:
        return None


async def add_video(db: Session, username: str, title: str, description: str, video_url: str):
    # 查找指定用户名的用户记录
    new_video = Video(username=username, title=title, description=description, video_url=video_url)
    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video


async def delete_video_by_id(db: Session, video_id: int):
    video_to_delete = db.query(Video).filter(Video.id == video_id).first()
    if video_to_delete is None:
        return {"message": "视频不存在"}
    db.delete(video_to_delete)
    db.commit()
    return {"message": "视频已成功删除", "video_id": video_id}


async def visit_video_by_id(db: Session, video_id: int):
    video_to_visit = db.query(Video).filter(Video.id == video_id).first()
    if video_to_visit is not None:
        video_to_visit.views_count += 1
        db.commit()
        return {
            "base": {
                "code": 10000,
                "msg": "success to view + 1",
                "data": video_to_visit.title
            }
        }
    else:
        return {
            "base": {
                "code": -1,
                "msg": "failed"
            }
        }


def find_top_videos(db: Session, page_size: int = 10, page_num: int = 1):
    offset = (page_num - 1) * page_size
    top_videos_query = db.query(Video).order_by(desc(Video.views_count)).offset(offset).limit(page_size)
    return top_videos_query.all()


from sqlalchemy import desc


async def delete_comment_by_id(db: Session, comment_id: int):
    comment_to_delete = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment_to_delete is None:
        return {"message": "评论不存在"}
    db.delete(comment_to_delete)
    db.commit()
    return {"message": "评论已成功删除", "comment_id": comment_id}
