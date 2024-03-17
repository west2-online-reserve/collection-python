from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
from datetime import datetime
from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(length=50), unique=True, nullable=False)
    password = Column(String(length=128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)
    avatar_url = Column(String(length=255),
                        default="https://img0.baidu.com/it/u=1429435380,946942033&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500")


class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(length=128), nullable=False)
    title = Column(String(length=128), nullable=False)
    description = Column(String(length=1024))
    video_url = Column(String(length=2048), nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    views_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    follower_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    following_id = Column(Integer, ForeignKey('users.id'), nullable=False)


class Friendship(Base):
    __tablename__ = 'friendships'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    friend_id = Column(Integer, ForeignKey('users.id'), nullable=False)


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    video_id = Column(Integer, nullable=False)
    content = Column(String(length=2048), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# 播放量排行榜表如果用redis或者模拟redis的话可以单独做一个表
# 这里直接通过/video/popular路由直接每次查询views_count来模拟类似操作
