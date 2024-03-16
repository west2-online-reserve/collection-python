from fastapi import APIRouter
from fastapi.params import Query
from ..auth import *
from ..crud import *
from ..database import get_db

router = APIRouter()


@router.delete("/comment/delete")
async def delete_comment(comment_id: int = Query(..., ge=1),
                         db: Session = Depends(get_db)):
    return await delete_comment_by_id(db, comment_id)
