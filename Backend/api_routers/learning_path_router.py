from fastapi import APIRouter, Query, BackgroundTasks
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from orm_dto.db_connection import get_db
from orm_dto.models import LearningPath

router = APIRouter()


@router.get("/welcome")
async def welcome():
    return {"message": "Welcome to LearnForU!"}

@router.post("/create")
async def create_learning_path(title: str,
                               description: str, db: Session = Depends(get_db)):
    new_learning_path = LearningPath(title=title, description=description)
    db.add(new_learning_path)
    db.commit()
    db.refresh(new_learning_path)
    return {"message": "Learning path created successfully", "learning_path": new_learning_path}

@router.get("/list")
async def list_learning_paths(title: str = Query(None), db: Session = Depends(get_db)):
    if title:
        learning_paths = db.query(LearningPath).filter(LearningPath.title==title).all()
    else:
        learning_paths = db.query(LearningPath).all()
    return {"learning_paths": learning_paths}

