import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import FileResponse
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# 引入各个模块中的路由器
from app.user.info import router as user_info_router
from app.user.login import router as user_login_router
from app.user.register import router as user_register_router
from app.relation.follow import router as relation_follow_router
from app.relation.followingList import router as relation_following_list_router
from app.relation.followerList import router as relation_follower_list_router
from app.action.like import router as action_like_router
from app.action.list import router as action_list_router
from app.action.comment import router as action_comment_router
from app.action.commentList import router as action_commentList_router
from app.action.deleteComment import router as action_deleteComment_router
from app.video.popular import router as video_popular_router
from app.video.visit import router as video_visit_router
from app.video.search import router as video_search_router
from app.video.delete import router as video_delete_router

app = FastAPI()

# 注册所有路由器到FastAPI应用
app.include_router(user_info_router)
app.include_router(user_login_router)
app.include_router(user_register_router)
app.include_router(relation_follow_router)
app.include_router(relation_following_list_router)
app.include_router(relation_follower_list_router)
app.include_router(video_delete_router)
app.include_router(action_like_router)
app.include_router(action_list_router)
app.include_router(action_comment_router)
app.include_router(action_commentList_router)
app.include_router(action_deleteComment_router)
app.include_router(video_popular_router)
app.include_router(video_visit_router)
app.include_router(video_search_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=10001)
