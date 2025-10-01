from sqlalchemy import Column, Integer, String, Text
from orm_dto.db_connection import Base

class LearningPath(Base):
    __tablename__ = "LEARNING_PATHS"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    tags = Column(String)