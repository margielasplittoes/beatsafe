from sqlalchemy import Column, Integer, String
from app.database import Base

class Beat(Base):
    __tablename__ = "beats"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
