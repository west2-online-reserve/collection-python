from fastapi import APIRouter
from fastapi.params import Query
from ..auth import *
from ..crud import *

router = APIRouter()


@router.get("/video/visit")
async def delete_video(id: int = Query(..., ge=1),
                       db: Session = Depends(get_db)):
    return await visit_video_by_id(db, id)
